#!/usr/bin/env python3
"""
Tag and cross-reference Obsidian markdown notes with Ollama, while keeping
memory isolated to each top-level folder in the vault.

Usage examples:
  python .agent/obsidian_enricher.py --dry-run
  python .agent/obsidian_enricher.py --domain "Corporate Law"
  python .agent/obsidian_enricher.py --domain "Admin Law" --limit 20
  python .agent/obsidian_enricher.py --file "Corporate Law/summaries/Week 2/readings/Dodd, ‘For Whom are Corporate Managers Trustees?’ (1932).md"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = REPO_ROOT / ".agent" / "config.json"

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", re.MULTILINE)
FENCED_JSON_RE = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
WORD_RE = re.compile(r"[a-z0-9][a-z0-9'\-]{1,}", re.IGNORECASE)
SKIP_TOKENS = {
    "summary",
    "week",
    "materials",
    "reading",
    "readings",
    "sources",
    "source",
    "summaries",
    "notes",
    "law",
    "laws",
    "chapter",
    "lecture",
    "tutorial",
    "course",
}


@dataclass
class NoteRecord:
    path: str
    domain: str
    title: str
    wikilink: str
    tags: list[str]
    summary: str
    see_also: list[dict[str, str]]
    topics: list[str]
    figures: list[str]
    cases: list[str]
    statutes: list[str]
    period: str
    jurisdiction: str
    assessment_relevance: str
    last_hash: str
    updated_at: str


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def relative_to_repo(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def note_wikilink_target(relative_path: str) -> str:
    return Path(relative_path).with_suffix("").as_posix()


def slugify_domain(domain: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", domain.strip()).strip("-")
    return slug or "__root__"


def extract_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text

    lines = text.splitlines(keepends=True)
    if not lines:
        return None, text

    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return None, text

    frontmatter = "".join(lines[1:closing_index])
    body = "".join(lines[closing_index + 1 :])
    return frontmatter, body


def extract_title(path: Path, text: str) -> str:
    frontmatter, body = extract_frontmatter(text)
    if frontmatter:
        for line in frontmatter.splitlines():
            stripped = line.strip()
            if not stripped.lower().startswith("title:"):
                continue
            _, value = stripped.split(":", 1)
            title = value.strip().strip('"').strip("'")
            if title:
                return title

    match = HEADING_RE.search(body)
    if match:
        return match.group(1).strip()

    return path.stem


def tokenize(value: str) -> set[str]:
    tokens = {
        token.lower()
        for token in WORD_RE.findall(value.lower())
        if token.lower() not in SKIP_TOKENS and len(token) > 2
    }
    return tokens


def build_note_stub(path: Path) -> dict[str, str]:
    text = read_text(path)
    relative_path = relative_to_repo(path)
    title = extract_title(path, text)
    return {
        "path": relative_path,
        "title": title,
        "wikilink": note_wikilink_target(relative_path),
    }


def list_domains(config: dict[str, Any]) -> list[str]:
    include_domains = config.get("include_domains", [])
    exclude_domains = set(config.get("exclude_domains", []))

    if include_domains:
        return [domain for domain in include_domains if (REPO_ROOT / domain).exists()]

    domains: list[str] = []
    for child in sorted(REPO_ROOT.iterdir()):
        if child.name in exclude_domains:
            continue
        if child.is_dir():
            domains.append(child.name)

    return domains


def is_markdown_path(path: Path, config: dict[str, Any]) -> bool:
    if path.suffix.lower() not in set(config.get("markdown_extensions", [".md"])):
        return False
    relative = relative_to_repo(path)
    include_substrings = config.get("include_path_substrings", [])
    if include_substrings:
        if not any(fragment in f"/{relative}" for fragment in include_substrings):
            return False
    for fragment in config.get("exclude_path_substrings", []):
        if fragment in f"/{relative}":
            return False
    return True


def iter_markdown_files(root: Path, config: dict[str, Any]) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and is_markdown_path(path, config)
    )


def memory_path_for_domain(domain: str, config: dict[str, Any]) -> Path:
    memory_dir = REPO_ROOT / config["memory_dir"]
    return memory_dir / f"{slugify_domain(domain)}.json"


def load_memory(domain: str, config: dict[str, Any]) -> dict[str, Any]:
    path = memory_path_for_domain(domain, config)
    if not path.exists():
        return {"domain": domain, "schema_version": 1, "files": {}}
    data = load_json(path)
    if "schema_version" not in data:
        data["schema_version"] = 1
    if "files" not in data:
        data["files"] = {}
    return data


def save_memory(domain: str, config: dict[str, Any], memory: dict[str, Any]) -> None:
    path = memory_path_for_domain(domain, config)
    save_json(path, memory)


def candidate_score(current_path: str, current_title: str, other: dict[str, Any]) -> int:
    if current_path == other["path"]:
        return -1

    current_parts = set(Path(current_path).parts[:-1])
    other_parts = set(Path(other["path"]).parts[:-1])
    path_overlap = len(current_parts & other_parts) * 4

    current_tokens = tokenize(current_title + " " + current_path)
    other_tokens = tokenize(other.get("title", "") + " " + other["path"])
    token_overlap = len(current_tokens & other_tokens) * 3

    other_tag_tokens: set[str] = set()
    for tag in other.get("tags", []):
        other_tag_tokens.update(tokenize(tag))
    tag_overlap = len(other_tag_tokens & current_tokens) * 2

    # Topic/entity overlap from memory
    topic_overlap = len(set(other.get("topics", [])) & current_tokens) * 3
    figure_overlap = len({f.lower() for f in other.get("figures", [])} & current_tokens) * 2
    case_overlap = len({c.lower() for c in other.get("cases", [])} & current_tokens) * 4
    statute_overlap = len({s.lower() for s in other.get("statutes", [])} & current_tokens) * 4

    return path_overlap + token_overlap + tag_overlap + topic_overlap + figure_overlap + case_overlap + statute_overlap


def select_candidates(
    current_path: str,
    current_title: str,
    note_index: dict[str, dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    scored = []
    for candidate in note_index.values():
        score = candidate_score(current_path, current_title, candidate)
        if score <= 0:
            continue
        scored.append((score, candidate["path"], candidate))

    scored.sort(key=lambda item: (-item[0], item[1]))
    limit = int(config["max_candidates"])
    return [item[2] for item in scored[:limit]]


def render_candidates(candidates: list[dict[str, Any]]) -> str:
    if not candidates:
        return "- No candidate notes were available.\n"

    blocks = []
    for candidate in candidates:
        tags = ", ".join(candidate.get("tags", [])) or "(none yet)"
        summary = candidate.get("summary", "").strip() or "(no summary yet)"
        blocks.append(
            "\n".join(
                [
                    f"- path: {candidate['path']}",
                    f"  title: {candidate.get('title', '')}",
                    f"  wikilink: [[{candidate.get('wikilink', '')}]]",
                    f"  tags: {tags}",
                    f"  summary: {summary}",
                ]
            )
        )
    return "\n".join(blocks)


def render_extract_prompt(
    template: str,
    *,
    domain: str,
    note_path: str,
    note_title: str,
    note_body: str,
    config: dict[str, Any],
) -> str:
    replacements = {
        "{{DOMAIN}}": domain,
        "{{NOTE_PATH}}": note_path,
        "{{NOTE_TITLE}}": note_title,
        "{{NOTE_BODY}}": note_body[: int(config["max_body_chars"])],
    }

    prompt = template
    for needle, value in replacements.items():
        prompt = prompt.replace(needle, value)
    return prompt


def render_related_prompt(
    template: str,
    *,
    domain: str,
    note_path: str,
    note_title: str,
    current_metadata: dict[str, Any],
    candidates: list[dict[str, Any]],
    config: dict[str, Any],
) -> str:
    def _to_json(obj: Any) -> str:
        return json.dumps(obj, ensure_ascii=False, indent=2)

    replacements = {
        "{{DOMAIN}}": domain,
        "{{NOTE_PATH}}": note_path,
        "{{NOTE_TITLE}}": note_title,
        "{{CURRENT_NOTE_METADATA}}": _to_json(current_metadata),
        "{{CANDIDATE_METADATA}}": _to_json(candidates),
        "{{MAX_LINKS}}": str(config["max_links_per_note"]),
    }

    prompt = template
    for needle, value in replacements.items():
        prompt = prompt.replace(needle, value)
    return prompt


def call_ollama(model: str, prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True,
            check=True,
        )
    except FileNotFoundError as exc:
        raise SystemExit(
            "Could not find `ollama` on PATH. Install it or run the script in an environment where Ollama is available."
        ) from exc
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip()
        raise RuntimeError(f"Ollama failed for model {model!r}: {stderr}") from exc

    return result.stdout.strip()


def parse_llm_json(raw_output: str) -> dict[str, Any]:
    decoder = json.JSONDecoder()
    cleaned = raw_output.strip()
    candidates = [match.group(1).strip() for match in FENCED_JSON_RE.finditer(raw_output)]
    if cleaned:
        candidates.append(cleaned)

    last_error: json.JSONDecodeError | None = None
    for candidate in candidates:
        if not candidate:
            continue

        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError as exc:
            last_error = exc

        for start_match in re.finditer(r"[\{\[]", candidate):
            try:
                parsed, _ = decoder.raw_decode(candidate, idx=start_match.start())
            except json.JSONDecodeError as exc:
                last_error = exc
                continue
            if isinstance(parsed, dict):
                return parsed

    print(f"DEBUG: Failed to parse JSON. Raw output length: {len(raw_output)}")
    print(f"DEBUG: Raw output start: {raw_output[:200]}")
    print(f"DEBUG: Raw output end: {raw_output[-200:]}")
    if last_error is not None:
        raise last_error
    raise json.JSONDecodeError("No JSON object found in LLM output", raw_output, 0)


def normalize_tag_text(value: str) -> str:
    text = " ".join(value.split()).strip()
    text = text.lstrip("#")
    text = text.replace("_", " ")
    text = re.sub(r"(?<=\w)-(?=\w)", " ", text)
    text = re.sub(r"\s*/\s*", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -_,.;:")
    return text


def normalize_tags(values: Any, config: dict[str, Any]) -> list[str]:
    if not isinstance(values, list):
        return []

    seen: set[str] = set()
    normalized: list[str] = []
    for item in values:
        if not isinstance(item, str):
            continue
        tag = normalize_tag_text(item)
        key = tag.casefold()
        if not tag or key in seen:
            continue
        seen.add(key)
        normalized.append(tag)

    max_tags = int(config["max_tags"])
    return normalized[:max_tags]


def fallback_tags(path: str, title: str, config: dict[str, Any]) -> list[str]:
    candidates = []
    for token in tokenize(title):
        candidates.append(token.replace("-", " "))

    for part in Path(path).parts[:-1]:
        lowered = part.lower()
        if lowered.startswith("week "):
            candidates.append(lowered)

    tags: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        value = candidate.strip()
        if not value or value in seen:
            continue
        seen.add(value)
        tags.append(value)
        if len(tags) >= int(config["min_tags"]):
            break

    return tags


def normalize_topics(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []

    topics: list[str] = []
    seen: set[str] = set()

    for item in values:
        if not isinstance(item, str):
            continue
        raw = normalize_tag_text(item)
        if not raw:
            continue
        # Strip obvious subject prefixes
        raw = re.sub(
            r"^(corporate[-\s]+law|administrative[-\s]+law|admin[-\s]+law)\s*[-:]?\s*",
            "",
            raw,
            flags=re.IGNORECASE,
        )
        if not raw:
            continue
        if len(raw.split()) > 6:
            continue
        key = raw.casefold()
        if key in seen:
            continue
        seen.add(key)
        topics.append(raw)

    return topics


def normalize_see_also(
    values: Any,
    *,
    domain: str,
    current_path: str,
    note_index: dict[str, dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, str]]:
    if not isinstance(values, list):
        return []

    results: list[dict[str, str]] = []
    seen_paths: set[str] = set()

    for item in values:
        if not isinstance(item, dict):
            continue

        raw_path = item.get("path")
        raw_reason = item.get("reason", "")
        if not isinstance(raw_path, str):
            continue

        candidate = note_index.get(raw_path)
        if candidate is None:
            continue

        if candidate["domain"] != domain or raw_path == current_path or raw_path in seen_paths:
            continue

        reason = " ".join(str(raw_reason).split()).strip()
        results.append({"path": raw_path, "reason": reason})
        seen_paths.add(raw_path)

        if len(results) >= int(config["max_links_per_note"]):
            break

    return results


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def upsert_frontmatter_tags(text: str, tags: list[str]) -> str:
    frontmatter, body = extract_frontmatter(text)
    tag_block = ["tags:"] + [f"  - {yaml_quote(tag)}" for tag in tags]

    if frontmatter is None:
        rendered = ["---", *tag_block, "---", ""]
        rendered_text = "\n".join(rendered)
        return rendered_text + body.lstrip("\n")

    lines = frontmatter.splitlines()
    output: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        if re.match(r"^tags\s*:", line):
            index += 1
            while index < len(lines):
                next_line = lines[index]
                if re.match(r"^\s*-\s+", next_line) or re.match(r"^\s{2,}\S", next_line):
                    index += 1
                    continue
                break
            continue
        output.append(line)
        index += 1

    if output and output[-1].strip():
        output.append("")
    output.extend(tag_block)

    rendered_frontmatter = "\n".join(output).rstrip() + "\n"
    return f"---\n{rendered_frontmatter}---\n{body.lstrip(chr(10))}"


def build_see_also_block(
    links: list[dict[str, str]],
    *,
    note_index: dict[str, dict[str, Any]],
    heading: str,
    marker: str,
) -> str:
    lines = [heading, f"<!-- {marker}:start -->"]
    for link in links:
        candidate = note_index[link["path"]]
        line = f"- [[{candidate['wikilink']}]]"
        if link["reason"]:
            line += f" - {link['reason']}"
        lines.append(line)
    lines.append(f"<!-- {marker}:end -->")
    return "\n".join(lines)


def upsert_see_also_block(
    text: str,
    links: list[dict[str, str]],
    *,
    note_index: dict[str, dict[str, Any]],
    config: dict[str, Any],
) -> str:
    marker = config["see_also_marker"]
    heading = config["see_also_heading"]
    pattern = re.compile(
        rf"{re.escape(heading)}\n<!-- {re.escape(marker)}:start -->.*?<!-- {re.escape(marker)}:end -->",
        re.DOTALL,
    )

    if not links:
        if pattern.search(text):
            return pattern.sub("", text).rstrip() + "\n"
        return text

    block = build_see_also_block(links, note_index=note_index, heading=heading, marker=marker)
    if pattern.search(text):
        return pattern.sub(block, text).rstrip() + "\n"

    stripped = text.rstrip()
    if not stripped:
        return block + "\n"
    return stripped + "\n\n---\n\n" + block + "\n"


def should_process_note(
    path: Path,
    *,
    memory: dict[str, Any],
    force: bool,
) -> bool:
    relative_path = relative_to_repo(path)
    text = read_text(path)
    content_hash = compute_hash(text)
    existing = memory["files"].get(relative_path)
    if force or existing is None:
        return True
    return existing.get("last_hash") != content_hash


def build_note_index(
    domain: str,
    files: list[Path],
    memory: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    memory_files = memory.get("files", {})

    for file_path in files:
        stub = build_note_stub(file_path)
        existing = memory_files.get(stub["path"], {})
        index[stub["path"]] = {
            "path": stub["path"],
            "domain": domain,
            "title": existing.get("title", stub["title"]),
            "wikilink": stub["wikilink"],
            "tags": existing.get("tags", []),
            "summary": existing.get("summary", ""),
            "topics": existing.get("topics", []),
            "figures": existing.get("figures", []),
            "cases": existing.get("cases", []),
            "statutes": existing.get("statutes", []),
        }

    return index


def extract_metadata_pass(
    *,
    path: Path,
    domain: str,
    config: dict[str, Any],
    extract_prompt_template: str,
    model: str,
) -> dict[str, Any]:
    text = read_text(path)
    relative_path = relative_to_repo(path)
    current_title = extract_title(path, text)
    prompt = render_extract_prompt(
        extract_prompt_template,
        domain=domain,
        note_path=relative_path,
        note_title=current_title,
        note_body=text,
        config=config,
    )
    response = parse_llm_json(call_ollama(model, prompt))

    # Normalized metadata with sensible defaults
    topics = normalize_topics(response.get("topics", []))
    summary = " ".join(str(response.get("summary", "")).split()).strip()
    figures = [str(v).strip() for v in (response.get("figures") or []) if str(v).strip()]
    cases = [str(v).strip() for v in (response.get("cases") or []) if str(v).strip()]
    statutes = [str(v).strip() for v in (response.get("statutes") or []) if str(v).strip()]
    period = " ".join(str(response.get("period", "")).split()).strip()
    jurisdiction = " ".join(str(response.get("jurisdiction", "")).split()).strip()
    assessment_relevance = " ".join(str(response.get("assessment_relevance", "")).split()).strip()

    return {
        "topics": topics,
        "summary": summary,
        "figures": figures,
        "cases": cases,
        "statutes": statutes,
        "period": period,
        "jurisdiction": jurisdiction,
        "assessment_relevance": assessment_relevance,
    }


def slugify_tag(value: str) -> str:
    """Convert a tag string to Obsidian-compatible form (no spaces)."""
    s = " ".join(value.split()).strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)  # drop punctuation except hyphens
    s = re.sub(r"\s+", "-", s).strip("-")
    return s


def normalize_topics_to_tags(
    *,
    topics: list[str],
    fallback_path: str,
    fallback_title: str,
    config: dict[str, Any],
) -> list[str]:
    tags: list[str] = []
    seen: set[str] = set()

    for topic in topics:
        if not topic:
            continue
        tag = slugify_tag(topic)
        if not tag or tag in seen:
            continue
        seen.add(tag)
        tags.append(tag)
        if len(tags) >= int(config["max_tags"]):
            break

    if len(tags) < int(config["min_tags"]):
        extra = fallback_tags(fallback_path, fallback_title, config)
        for tag in extra:
            slug = slugify_tag(tag)
            if slug in seen:
                continue
            seen.add(slug)
            tags.append(slug)
            if len(tags) >= int(config["max_tags"]):
                break

    return tags


def select_related_notes_pass(
    *,
    path: Path,
    domain: str,
    current_metadata: dict[str, Any],
    note_index: dict[str, dict[str, Any]],
    config: dict[str, Any],
    related_prompt_template: str,
    model: str,
) -> list[dict[str, str]]:
    relative_path = relative_to_repo(path)
    current_title = current_metadata.get("title") or Path(relative_path).stem
    candidates = select_candidates(relative_path, current_title, note_index, config)
    if not candidates or int(config.get("max_links_per_note", 0)) <= 0:
        return []

    prompt = render_related_prompt(
        related_prompt_template,
        domain=domain,
        note_path=relative_path,
        note_title=current_title,
        current_metadata=current_metadata,
        candidates=candidates,
        config=config,
    )
    response = parse_llm_json(call_ollama(model, prompt))
    return normalize_see_also(
        response.get("see_also", []),
        domain=domain,
        current_path=relative_path,
        note_index=note_index,
        config=config,
    )


def update_memory_record(
    *,
    path: Path,
    domain: str,
    tags: list[str],
    summary: str,
    see_also: list[dict[str, str]],
    extracted: dict[str, Any],
    memory: dict[str, Any],
    note_index: dict[str, dict[str, Any]],
) -> NoteRecord:
    text = read_text(path)
    relative_path = relative_to_repo(path)
    current_title = extract_title(path, text)
    content_hash = compute_hash(text)
    now = datetime.now(UTC).isoformat()

    record = NoteRecord(
        path=relative_path,
        domain=domain,
        title=current_title,
        wikilink=note_wikilink_target(relative_path),
        tags=tags,
        summary=summary,
        see_also=see_also,
        topics=extracted.get("topics", []),
        figures=extracted.get("figures", []),
        cases=extracted.get("cases", []),
        statutes=extracted.get("statutes", []),
        period=extracted.get("period", ""),
        jurisdiction=extracted.get("jurisdiction", ""),
        assessment_relevance=extracted.get("assessment_relevance", ""),
        last_hash=content_hash,
        updated_at=now,
    )

    memory.setdefault("files", {})
    memory["files"][relative_path] = {
        "path": record.path,
        "domain": record.domain,
        "title": record.title,
        "wikilink": record.wikilink,
        "tags": record.tags,
        "summary": record.summary,
        "see_also": record.see_also,
        "topics": record.topics,
        "figures": record.figures,
        "cases": record.cases,
        "statutes": record.statutes,
        "period": record.period,
        "jurisdiction": record.jurisdiction,
        "assessment_relevance": record.assessment_relevance,
        "last_hash": record.last_hash,
        "updated_at": record.updated_at,
    }

    note_index[relative_path] = {
        "path": record.path,
        "domain": record.domain,
        "title": record.title,
        "wikilink": record.wikilink,
        "tags": record.tags,
        "summary": record.summary,
        "topics": record.topics,
        "figures": record.figures,
        "cases": record.cases,
        "statutes": record.statutes,
    }

    return record


def project_note_updates(
    *,
    path: Path,
    tags: list[str],
    see_also: list[dict[str, str]],
    note_index: dict[str, dict[str, Any]],
    config: dict[str, Any],
) -> None:
    text = read_text(path)
    updated_text = upsert_frontmatter_tags(text, tags)
    updated_text = upsert_see_also_block(
        updated_text,
        see_also,
        note_index=note_index,
        config=config,
    )
    path.write_text(updated_text, encoding="utf-8")


def process_note(
    path: Path,
    *,
    domain: str,
    note_index: dict[str, dict[str, Any]],
    memory: dict[str, Any],
    config: dict[str, Any],
    extract_prompt_template: str,
    related_prompt_template: str,
    model: str,
    dry_run: bool,
    memory_only: bool,
) -> NoteRecord:
    text = read_text(path)
    relative_path = relative_to_repo(path)
    current_title = extract_title(path, text)

    # Pass 1: extraction
    extracted = extract_metadata_pass(
        path=path,
        domain=domain,
        config=config,
        extract_prompt_template=extract_prompt_template,
        model=model,
    )

    # Pass 2: topics -> tags
    tags = normalize_topics_to_tags(
        topics=extracted.get("topics", []),
        fallback_path=relative_path,
        fallback_title=current_title,
        config=config,
    )

    # Pass 3: related notes
    # Build a shallow metadata view for the linking prompt
    current_metadata = {
        "path": relative_path,
        "title": current_title,
        "topics": extracted.get("topics", []),
        "figures": extracted.get("figures", []),
        "cases": extracted.get("cases", []),
        "statutes": extracted.get("statutes", []),
    }
    see_also = select_related_notes_pass(
        path=path,
        domain=domain,
        current_metadata=current_metadata,
        note_index=note_index,
        config=config,
        related_prompt_template=related_prompt_template,
        model=model,
    )

    # Persist to memory and index (single source of truth)
    record = update_memory_record(
        path=path,
        domain=domain,
        tags=tags,
        summary=extracted.get("summary", ""),
        see_also=see_also,
        extracted=extracted,
        memory=memory,
        note_index=note_index,
    )

    # Pass 4: projection into the note
    if not dry_run and not memory_only:
        project_note_updates(
            path=path,
            tags=tags,
            see_also=see_also,
            note_index=note_index,
            config=config,
        )

    return record


def resolve_single_file(path_arg: str) -> Path:
    target = (REPO_ROOT / path_arg).resolve()
    if not target.exists() or not target.is_file():
        raise SystemExit(f"File not found: {path_arg}")
    return target


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Use Ollama to add Obsidian-compatible YAML tags and managed "
            "cross-reference blocks to markdown notes, with one memory file per top-level folder."
        )
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the JSON config file (default: .agent/config.json).",
    )
    parser.add_argument(
        "--domain",
        help="Only process one top-level folder, e.g. 'Admin Law'.",
    )
    parser.add_argument(
        "--file",
        dest="single_file",
        help="Only process one markdown file, relative to the repo root.",
    )
    parser.add_argument(
        "--model",
        help="Override the Ollama model from config.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Maximum number of notes to process in this run (default: unlimited).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Call Ollama and update in-memory results, but do not write notes or memory files.",
    )
    parser.add_argument(
        "--memory-only",
        action="store_true",
        help="Write memory files but leave the notes themselves unchanged.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess notes even if the file hash matches memory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_json(args.config)
    model = args.model or config["model"]
    extract_prompt_template = read_text(REPO_ROOT / config["extract_prompt_path"])
    related_prompt_template = read_text(REPO_ROOT / config["related_prompt_path"])

    if args.single_file:
        single_file = resolve_single_file(args.single_file)
        relative = relative_to_repo(single_file)
        domain = Path(relative).parts[0] if len(Path(relative).parts) > 1 else "__root__"
        domains = [domain]
        single_file_lookup = {domain: [single_file]}
    else:
        single_file_lookup = {}
        domains = [args.domain] if args.domain else list_domains(config)

    processed_count = 0
    for domain in domains:
        domain_root = REPO_ROOT / domain if domain != "__root__" else REPO_ROOT
        if domain != "__root__" and not domain_root.exists():
            print(f"[skip] domain not found: {domain}", file=sys.stderr)
            continue

        files = single_file_lookup.get(domain)
        if files is None:
            files = iter_markdown_files(domain_root, config)

        if not files:
            print(f"[skip] no markdown files found in {domain}")
            continue

        memory = load_memory(domain, config)
        note_index = build_note_index(domain, files, memory)

        print(f"[domain] {domain} ({len(files)} files)")
        for path in files:
            if args.limit and processed_count >= args.limit:
                break

            if not should_process_note(path, memory=memory, force=args.force):
                print(f"  [cached] {relative_to_repo(path)}")
                continue

            record = process_note(
                path,
                domain=domain,
                note_index=note_index,
                memory=memory,
                config=config,
                extract_prompt_template=extract_prompt_template,
                related_prompt_template=related_prompt_template,
                model=model,
                dry_run=args.dry_run,
                memory_only=args.memory_only,
            )
            processed_count += 1
            print(
                f"  [updated] {record.path} | tags={len(record.tags)} | links={len(record.see_also)}"
            )

        if not args.dry_run:
            save_memory(domain, config, memory)

        if args.limit and processed_count >= args.limit:
            break


if __name__ == "__main__":
    main()
