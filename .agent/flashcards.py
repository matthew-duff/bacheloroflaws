#!/usr/bin/env python3
from __future__ import annotations

"""
Generate flashcards from summary-style markdown notes using Ollama.

Flashcards are written under .agent/flashcards/<domain>/..., mirroring
the original note structure.
"""

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = REPO_ROOT / ".agent" / "config.json"

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", re.MULTILINE)
FENCED_JSON_RE = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def relative_to_repo(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def list_domains(config: dict[str, Any]) -> list[str]:
    include_domains = config.get("include_domains", [])
    exclude_domains = set(config.get("exclude_domains", []))

    if include_domains:
        return [d for d in include_domains if (REPO_ROOT / d).exists()]

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
        path for path in root.rglob("*") if path.is_file() and is_markdown_path(path, config)
    )


def flashcards_root(config: dict[str, Any]) -> Path:
    return REPO_ROOT / config.get("flashcards_dir", ".agent/flashcards")


def flashcards_path_for_note(relative_note_path: str, config: dict[str, Any]) -> Path:
    root = flashcards_root(config)
    parts = Path(relative_note_path).parts
    if not parts:
        return root / "flashcards.md"
    domain = parts[0]
    rest = Path(*parts[1:]) if len(parts) > 1 else Path("index.md")
    return root / domain / rest


def extract_title_from_frontmatter(text: str) -> str | None:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    lines = text.splitlines(keepends=True)
    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break
    if closing_index is None:
        return None
    frontmatter = "".join(lines[1:closing_index])
    for line in frontmatter.splitlines():
        stripped = line.strip()
        if not stripped.lower().startswith("title:"):
            continue
        _, value = stripped.split(":", 1)
        title = value.strip().strip('"').strip("'")
        if title:
            return title
    return None


def extract_title(path: Path, text: str) -> str:
    frontmatter_title = extract_title_from_frontmatter(text)
    if frontmatter_title:
        return frontmatter_title
    match = HEADING_RE.search(text)
    if match:
        return match.group(1).strip()
    return path.stem


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
        try:
            parsed, _ = decoder.raw_decode(candidate)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError as exc:
            last_error = exc
            continue

    if last_error is not None:
        raise last_error
    raise json.JSONDecodeError("No JSON object found in LLM output", raw_output, 0)


def render_flashcards_prompt(
    template: str,
    *,
    domain: str,
    note_path: str,
    note_title: str,
    note_body: str,
    note_topics: str,
    note_summary: str,
    min_cards: int,
    max_cards: int,
    config: dict[str, Any],
) -> str:
    replacements = {
        "{{DOMAIN}}": domain,
        "{{NOTE_PATH}}": note_path,
        "{{NOTE_TITLE}}": note_title,
        "{{NOTE_BODY}}": note_body[: int(config.get("max_body_chars", 14000))],
        "{{NOTE_TOPICS}}": note_topics,
        "{{NOTE_SUMMARY}}": note_summary,
        "{{MIN_CARDS}}": str(min_cards),
        "{{MAX_CARDS}}": str(max_cards),
    }
    prompt = template
    for needle, value in replacements.items():
        prompt = prompt.replace(needle, value)
    return prompt


def load_memory_for_domain(domain: str, config: dict[str, Any]) -> dict[str, Any]:
    memory_dir = REPO_ROOT / config.get("memory_dir", ".agent/memories")
    path = memory_dir / f"{domain}.json"
    if not path.exists():
        return {"files": {}}
    return load_json(path)


def resolve_single_file(path_arg: str) -> Path:
    target = (REPO_ROOT / path_arg).resolve()
    if not target.exists() or not target.is_file():
        raise SystemExit(f"File not found: {path_arg}")
    return target


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate flashcards from summary notes using Ollama."
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
        "--min-cards",
        type=int,
        default=6,
        help="Minimum number of flashcards per note (default: 6).",
    )
    parser.add_argument(
        "--max-cards",
        type=int,
        default=14,
        help="Maximum number of flashcards per note (default: 14).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be generated without writing flashcard files.",
    )
    return parser.parse_args()


def write_flashcards_file(
    output_path: Path,
    *,
    note_title: str,
    relative_note_path: str,
    cards: list[dict[str, str]],
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append(f"# Flashcards – {note_title}")
    lines.append("")
    lines.append(f"_Source note: {relative_note_path}_")
    lines.append("")
    for index, card in enumerate(cards, start=1):
        q = " ".join(str(card.get("question", "")).split())
        a = " ".join(str(card.get("answer", "")).split())
        if not q or not a:
            continue
        lines.append(f"{index}. Q: {q}")
        lines.append(f"   A: {a}")
        lines.append("")
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    config = load_json(args.config)
    model = args.model or config["model"]
    flashcards_prompt_template = read_text(
        REPO_ROOT / config.get("flashcards_prompt_path", ".agent/prompts/flashcards.txt")
    )

    if args.single_file:
        single_file = resolve_single_file(args.single_file)
        relative = relative_to_repo(single_file)
        domain = Path(relative).parts[0] if len(Path(relative).parts) > 1 else "__root__"
        domains = [domain]
        single_file_lookup = {domain: [single_file]}
    else:
        single_file_lookup: dict[str, list[Path]] = {}
        domains = [args.domain] if args.domain else list_domains(config)

    processed_count = 0
    for domain in domains:
        domain_root = REPO_ROOT / domain if domain != "__root__" else REPO_ROOT
        if domain != "__root__" and not domain_root.exists():
            print(f"[skip] domain not found: {domain}")
            continue

        files = single_file_lookup.get(domain)
        if files is None:
            files = iter_markdown_files(domain_root, config)
        if not files:
            print(f"[skip] no markdown files found in {domain}")
            continue

        memory = load_memory_for_domain(domain, config)
        memory_files = memory.get("files", {})

        print(f"[domain] {domain} ({len(files)} files)")
        for path in files:
            if args.limit and processed_count >= args.limit:
                break

            text = read_text(path)
            relative_path = relative_to_repo(path)
            title = extract_title(path, text)
            meta = memory_files.get(relative_path, {})
            note_topics = ", ".join(meta.get("topics", []))
            note_summary = str(meta.get("summary", "")).strip()

            prompt = render_flashcards_prompt(
                flashcards_prompt_template,
                domain=domain,
                note_path=relative_path,
                note_title=title,
                note_body=text,
                note_topics=note_topics,
                note_summary=note_summary,
                min_cards=args.min_cards,
                max_cards=args.max_cards,
                config=config,
            )

            response = parse_llm_json(call_ollama(model, prompt))
            cards = response.get("cards") or []
            if not isinstance(cards, list):
                cards = []

            if not cards:
                print(f"  [skip] no cards returned for {relative_path}")
                continue

            if args.dry_run:
                print(f"  [dry-run] {relative_path} -> {len(cards)} cards")
            else:
                out_path = flashcards_path_for_note(relative_path, config)
                write_flashcards_file(
                    out_path,
                    note_title=title,
                    relative_note_path=relative_path,
                    cards=cards,
                )
                print(
                    f"  [written] {relative_path} -> {out_path.relative_to(REPO_ROOT)} ({len(cards)} cards)"
                )

            processed_count += 1

        if args.limit and processed_count >= args.limit:
            break


if __name__ == "__main__":
    main()

