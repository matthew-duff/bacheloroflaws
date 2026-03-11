#!/usr/bin/env python3
"""
Attach relevant Pixabay images to case-summary Markdown files.

What it does:
- Recursively scans an --input folder for .md files
- Treats files as "case summaries" when the title contains " v "
- Skips any file that already contains an image reference
- For remaining files:
  - Uses an LLM to generate *facts-first* creative search terms (optional; falls back if not configured)
  - Searches Pixabay for a suitable image
  - Downloads the image locally (Pixabay disallows permanent hotlinking)
  - Inserts a Markdown image + attribution under the title

Safe default:
- Without --apply, prints what it would do (no downloads, no edits)

Pixabay API:
- Docs: https://pixabay.com/api/docs/
- Rate limit: 100 req / 60s by default
- Requests should be cached for 24h
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Optional


IMAGE_MARKDOWN_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
IMAGE_WIKILINK_RE = re.compile(r"!\[\[[^\]]+\]\]")
IMAGE_HTML_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
TITLE_HEADING_RE = re.compile(r"^\s{0,3}#\s+(.+?)\s*$")


@dataclasses.dataclass(frozen=True)
class PixabayHit:
    id: int
    pageURL: str
    tags: str
    user: str
    user_id: int
    previewURL: str
    webformatURL: str
    largeImageURL: str
    imageWidth: int
    imageHeight: int


def _utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _has_image_reference(md: str) -> bool:
    return bool(
        IMAGE_MARKDOWN_RE.search(md)
        or IMAGE_WIKILINK_RE.search(md)
        or IMAGE_HTML_RE.search(md)
    )


def _extract_title(md: str, fallback_filename: str) -> str:
    lines = md.splitlines()
    # Obsidian-style YAML frontmatter is common in this repo.
    # If present, prefer `title:` inside it.
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        i += 1
        fm: list[str] = []
        while i < len(lines) and lines[i].strip() != "---":
            fm.append(lines[i])
            i += 1
        for l in fm:
            if l.lstrip().startswith("title:"):
                val = l.split(":", 1)[1].strip()
                # Handle simple quoting styles.
                if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
                    val = val[1:-1].strip()
                if val:
                    return val

    for line in lines:
        s = line.strip()
        if not s or s == "---":
            continue
        m = TITLE_HEADING_RE.match(line)
        if m:
            return m.group(1).strip()
        return s.strip("# ").strip() or fallback_filename

    return fallback_filename


def _is_case_summary_title(title: str) -> bool:
    # Your convention: case summaries have " v " in the title.
    return " v " in title


def _slugify(s: str, max_len: int = 80) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9 _-]+", "", s)
    s = s.replace(" ", "_")
    s = re.sub(r"_+", "_", s)
    s = s.strip("_-")
    if not s:
        return "case"
    return s[:max_len]


def _http_get_json(url: str, *, timeout_s: int = 30, headers: Optional[dict[str, str]] = None) -> Any:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8"))


def _http_download(url: str, dest: Path, *, timeout_s: int = 60) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "pixabay_case_images/1.0"})
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        data = resp.read()
    dest.write_bytes(data)


def _load_cache(cache_path: Path) -> dict[str, Any]:
    if not cache_path.exists():
        return {"version": 1, "entries": {}}
    try:
        return json.loads(_read_text(cache_path))
    except Exception:
        return {"version": 1, "entries": {}}


def _save_cache(cache_path: Path, cache: dict[str, Any]) -> None:
    _write_text(cache_path, json.dumps(cache, indent=2, ensure_ascii=False) + "\n")


def _cache_key_for_query(params: dict[str, Any]) -> str:
    stable = json.dumps(params, sort_keys=True, ensure_ascii=False)
    return hashlib.blake2b(stable.encode("utf-8"), digest_size=16).hexdigest()


def _cache_get_24h(cache: dict[str, Any], key: str) -> Optional[Any]:
    entry = (cache.get("entries") or {}).get(key)
    if not entry:
        return None
    try:
        ts = dt.datetime.fromisoformat(entry["ts"])
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=dt.timezone.utc)
    except Exception:
        return None
    if _utc_now() - ts > dt.timedelta(hours=24):
        return None
    return entry.get("value")


def _cache_put(cache: dict[str, Any], key: str, value: Any) -> None:
    cache.setdefault("entries", {})[key] = {"ts": _utc_now().isoformat(), "value": value}


def pixabay_search_image(
    *,
    api_key: str,
    query: str,
    cache: dict[str, Any],
    cache_path: Path,
    per_page: int = 30,
    safesearch: bool = True,
    image_type: str = "photo",
    orientation: str = "horizontal",
) -> list[PixabayHit]:
    base = "https://pixabay.com/api/"
    params: dict[str, Any] = {
        "key": api_key,
        "q": query,
        "image_type": image_type,
        "per_page": int(per_page),
        "safesearch": "true" if safesearch else "false",
        "orientation": orientation,
    }
    cache_key = _cache_key_for_query({"endpoint": base, **params})
    cached = _cache_get_24h(cache, cache_key)
    if cached is None:
        url = base + "?" + urllib.parse.urlencode(params, safe=":+")
        data = _http_get_json(url, timeout_s=30)
        _cache_put(cache, cache_key, data)
        _save_cache(cache_path, cache)
    else:
        data = cached

    hits = data.get("hits") or []
    out: list[PixabayHit] = []
    for h in hits:
        try:
            out.append(
                PixabayHit(
                    id=int(h["id"]),
                    pageURL=str(h["pageURL"]),
                    tags=str(h.get("tags", "")),
                    user=str(h.get("user", "")),
                    user_id=int(h.get("user_id", 0)),
                    previewURL=str(h.get("previewURL", "")),
                    webformatURL=str(h.get("webformatURL", "")),
                    largeImageURL=str(h.get("largeImageURL", "")),
                    imageWidth=int(h.get("imageWidth", 0)),
                    imageHeight=int(h.get("imageHeight", 0)),
                )
            )
        except Exception:
            continue
    return out


def _profile_url(user: str, user_id: int) -> str:
    user = (user or "").strip()
    if not user or not user_id:
        return "https://pixabay.com/users/"
    return f"https://pixabay.com/users/{urllib.parse.quote(user)}-{int(user_id)}/"


def _choose_best_hit(hits: list[PixabayHit]) -> Optional[PixabayHit]:
    if not hits:
        return None
    # Simple heuristic: prefer larger landscape-ish images; otherwise first.
    def score(h: PixabayHit) -> tuple[int, int, int]:
        return (
            1 if h.imageWidth >= h.imageHeight else 0,
            h.imageWidth * h.imageHeight,
            -h.id,
        )
    return sorted(hits, key=score, reverse=True)[0]


def llm_generate_queries_ollama(
    *,
    model: str,
    host: str,
    title: str,
    md_excerpt: str,
    timeout_s: int = 60,
) -> list[str]:
    """
    Uses a local Ollama server to generate creative search queries.

    Expects an Ollama-compatible endpoint at:
    - POST {host}/api/chat

    This is optional; if it fails, the caller should fall back to heuristics.
    """
    system = (
        "You generate short, highly visual search queries for stock photography (Pixabay). "
        "The input is a law case, but your job is NOT to describe legal doctrine. "
        "Pick the most distinctive *fact pattern* and turn it into an imageable scene.\n\n"
        "Hard rules:\n"
        "- Output ONLY JSON: {\"queries\": [\"...\", ...]} with 5-8 strings.\n"
        "- Each query must be 2-6 words, photo-realistic, and depict objects/people/places.\n"
        "- Avoid legal concepts/terms (court, tribunal, judge, standing, judicial review, ADJR, constitution, statute, section, plaintiff/defendant, etc.).\n"
        "- Prefer specific nouns from the facts (vehicle, building type, setting, profession, weather, time of day).\n"
        "- If there are multiple similar cases, focus on what makes THIS one visually unique.\n\n"
        "Few-shot examples:\n"
        "Example A (constitutional/immigration at sea):\n"
        "Facts: asylum seekers intercepted at sea, held on a government vessel, attempted return to another country.\n"
        "Good queries: [\"asylum seeker boat\", \"navy patrol boat at sea\", \"migrant boat night\", \"people on crowded boat\", \"ocean patrol ship\"]\n"
        "Bad queries: [\"constitutional law\", \"executive power\", \"high court\"]\n\n"
        "Example B (planning approval affecting supermarkets):\n"
        "Facts: minister approved new commercial development; nearby supermarket operators fear loss of turnover.\n"
        "Good queries: [\"new supermarket construction\", \"shopping centre construction site\", \"suburban supermarket exterior\", \"retail development site\", \"supermarket parking lot\"]\n"
        "Bad queries: [\"competitor standing\", \"person aggrieved\", \"administrative decision\"]\n\n"
        "Example C (procedural fairness / visa cancellation interview):\n"
        "Facts: immigration interview, documents, anxious person, airport or office setting.\n"
        "Good queries: [\"immigration interview office\", \"passport and documents desk\", \"airport immigration counter\", \"person holding passport\", \"waiting room immigration\"]\n"
        "Bad queries: [\"procedural fairness\", \"jurisdictional error\"]\n"
    )
    user = (
        f"Case title: {title}\n\n"
        "Markdown excerpt:\n"
        f"{md_excerpt}\n\n"
        "Generate creative Pixabay search queries that depict the core facts/scene."
    )
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "options": {"temperature": 0.9},
        "format": "json",
    }
    body = json.dumps(payload).encode("utf-8")

    url = host.rstrip("/") + "/api/chat"
    req = urllib.request.Request(
        url,
        method="POST",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)

    content = (((data.get("message") or {}).get("content")) or "").strip()
    parsed = json.loads(content) if content else {}
    queries = parsed.get("queries") or []
    out = []
    for q in queries:
        q = str(q).strip()
        if q:
            out.append(q)
    return out[:10]


def heuristic_queries(title: str, md_excerpt: str) -> list[str]:
    anchors = extract_concrete_keywords(md_excerpt, max_keywords=10)
    out: list[str] = []

    # Prefer facts-derived, imageable phrases over the case title.
    if anchors:
        # A few short combinations to try against Pixabay.
        out.extend(
            [
                " ".join(anchors[:1]),
                " ".join(anchors[:2]),
                " ".join(anchors[:3]),
                " ".join(anchors[:4]),
            ]
        )

        # If we have a known visual noun, add a couple themed expansions.
        a = set(anchors)
        if "supermarket" in a:
            out.append("supermarket exterior")
            out.append("new supermarket construction")
            out.append("suburban supermarket parking lot")
        if "construction" in a or "development" in a:
            out.append("commercial construction site")
            out.append("new retail development")
        if "landlord" in a or "tenant" in a or "lease" in a:
            out.append("shop lease sign")
            out.append("commercial landlord building")

    # Keep title as a last-ditch option (sometimes it contains a place/person).
    out.append(title)
    out.append(title.replace(" v ", " versus "))

    # Filter/dedupe; require anchors when available.
    return filter_queries([q for q in out if str(q).strip()], anchor_keywords=anchors)


def strip_yaml_frontmatter(md: str) -> str:
    lines = md.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        i += 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines) and lines[i].strip() == "---":
            i += 1
        return "\n".join(lines[i:]).lstrip("\n")
    return md


HEADING_ANY_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")


def extract_section_by_heading(md_body: str, heading_text: str) -> str:
    """
    Extract the markdown section under a heading matching `heading_text` (case-insensitive).
    Stops at the next heading of the same or higher level.
    """
    lines = md_body.splitlines()
    target = heading_text.strip().lower()
    start_idx: Optional[int] = None
    level: Optional[int] = None

    for i, line in enumerate(lines):
        m = HEADING_ANY_RE.match(line)
        if not m:
            continue
        lvl = len(m.group(1))
        txt = m.group(2).strip().lower()
        if txt == target:
            start_idx = i + 1
            level = lvl
            break

    if start_idx is None or level is None:
        return ""

    out: list[str] = []
    for j in range(start_idx, len(lines)):
        m = HEADING_ANY_RE.match(lines[j])
        if m:
            next_lvl = len(m.group(1))
            if next_lvl <= level:
                break
        out.append(lines[j])

    return "\n".join(out).strip()


def build_excerpt(md: str, *, max_lines: int = 120) -> str:
    body = strip_yaml_frontmatter(md)
    lines = body.splitlines()
    return "\n".join(lines[: max(1, int(max_lines))]).strip()


LEGALISH_QUERY_STOPWORDS = {
    "act",
    "adjr",
    "aggrieved",
    "appeal",
    "assessment",
    "authority",
    "case",
    "commonwealth",
    "constitution",
    "constitutional",
    "court",
    "decision",
    "defendant",
    "evidence",
    "held",
    "judge",
    "judicial",
    "law",
    "legal",
    "locus",
    "minister",
    "plaintiff",
    "ratio",
    "review",
    "section",
    "ss",
    "standing",
    "statute",
    "tribunal",
}


def _tokenize_words(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z0-9'-]{2,}", text.lower())


def extract_concrete_keywords(text: str, *, max_keywords: int = 12) -> list[str]:
    """
    Pull a small set of non-legal-ish keywords to anchor image queries.
    """
    words = _tokenize_words(text)
    if not words:
        return []

    nonvisual = {
        "this",
        "that",
        "their",
        "under",
        "also",
        "argued",
        "issue",
        "whether",
        "because",
        "would",
        "might",
        "approved",
        "approval",
        "claimed",
        "claim",
        "argue",
        "decision",
        "power",
        "scheme",
        "test",
        "majority",
        "dissent",
    }

    visual_priority = {
        "supermarket",
        "store",
        "shop",
        "shopping",
        "construction",
        "development",
        "building",
        "landlord",
        "tenant",
        "lease",
        "turnover",
        "profitability",
        "vessel",
        "boat",
        "ship",
        "airport",
        "border",
        "detention",
        "police",
        "prison",
        "hospital",
        "fire",
        "flood",
        "factory",
        "mine",
        "farm",
        "suburb",
        "street",
    }

    counts: dict[str, int] = {}
    first_pos: dict[str, int] = {}
    for i, w in enumerate(words):
        if w in LEGALISH_QUERY_STOPWORDS or w in nonvisual or len(w) < 4:
            continue
        counts[w] = counts.get(w, 0) + 1
        first_pos.setdefault(w, i)

    def key(w: str) -> tuple[int, int, int]:
        return (
            1 if w in visual_priority else 0,
            counts.get(w, 0),
            -first_pos.get(w, 10**9),
        )

    ranked = sorted(counts.keys(), key=key, reverse=True)
    return ranked[: max(1, int(max_keywords))]


def filter_queries(queries: list[str], *, anchor_keywords: list[str]) -> list[str]:
    """
    Drop legalese and keep queries grounded in concrete anchors from the facts.
    """
    anchors = set(anchor_keywords)
    cleaned: list[str] = []

    for q in queries:
        q = re.sub(r"\s+", " ", str(q).strip())
        if not q:
            continue
        words = _tokenize_words(q)
        if not words:
            continue
        if any(w in LEGALISH_QUERY_STOPWORDS for w in words):
            continue
        if anchors and not any(w in anchors for w in words):
            continue
        if len(q) > 80:
            continue
        cleaned.append(q)

    out: list[str] = []
    seen2: set[str] = set()
    for q in cleaned:
        k = q.lower()
        if k in seen2:
            continue
        seen2.add(k)
        out.append(q)
    return out[:10]


def _insert_image_block(md: str, *, image_rel_path: str, attribution_line: str) -> str:
    lines = md.splitlines()
    insert_at = 0

    # If YAML frontmatter exists, never insert inside it.
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        i += 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines) and lines[i].strip() == "---":
            i += 1
        insert_at = i

    # Prefer inserting right after the first H1 after frontmatter.
    for j in range(insert_at, len(lines)):
        if TITLE_HEADING_RE.match(lines[j]) or lines[j].lstrip().startswith("# "):
            insert_at = j + 1
            break

    block = [
        "",
        f"![Case image]({image_rel_path})",
        "",
        attribution_line,
        "",
    ]
    new_lines = lines[:insert_at] + block + lines[insert_at:]
    return "\n".join(new_lines).rstrip() + "\n"


def _relpath_posix(path: Path, start: Path) -> str:
    rel = path.relative_to(start)
    return rel.as_posix()


def relpath_posix_between(target: Path, start_dir: Path) -> str:
    """
    Relative path from start_dir -> target, as POSIX (for Markdown).
    """
    rel = os.path.relpath(str(target), start=str(start_dir))
    return Path(rel).as_posix()


def main() -> int:
    p = argparse.ArgumentParser(description="Attach Pixabay images to case-summary Markdown files.")
    p.add_argument("--input", required=True, type=Path, help="Folder to recursively scan for .md files.")
    p.add_argument("--apply", action="store_true", help="Actually download images and edit files.")
    p.add_argument("--pixabay-key", default=os.environ.get("PIXABAY_API_KEY", ""), help="Pixabay API key (or set PIXABAY_API_KEY).")
    p.add_argument("--download-dir", type=Path, default=Path("assets/pixabay"), help="Where to save downloaded images (relative to repo root by default).")
    p.add_argument("--cache", type=Path, default=Path(".util/.cache/pixabay_search_cache.json"), help="Cache path for Pixabay searches (24h).")
    p.add_argument("--max-files", type=int, default=0, help="Process at most N files (0 = no limit).")
    p.add_argument("--sleep-ms", type=int, default=350, help="Delay between Pixabay queries (rate limit friendliness).")
    p.add_argument("--llm", choices=["none", "ollama"], default="ollama", help="How to generate creative search terms.")
    p.add_argument("--ollama-host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"), help="Ollama host (or set OLLAMA_HOST).")
    p.add_argument("--ollama-model", default=os.environ.get("OLLAMA_MODEL", "llama3.1"), help="Ollama model (or set OLLAMA_MODEL).")
    args = p.parse_args()

    input_dir: Path = args.input
    if not input_dir.exists() or not input_dir.is_dir():
        print(f"Input directory not found or not a directory: {input_dir}", file=sys.stderr)
        return 2

    repo_root = Path.cwd()
    download_dir = (repo_root / args.download_dir).resolve()
    cache_path = (repo_root / args.cache).resolve()
    cache = _load_cache(cache_path)

    md_files = sorted(input_dir.rglob("*.md"))
    if not md_files:
        print(f"No .md files found under: {input_dir}")
        return 0

    to_process: list[Path] = []
    for f in md_files:
        try:
            md = _read_text(f)
        except Exception:
            continue
        title = _extract_title(md, f.stem)
        if not _is_case_summary_title(title):
            continue
        if _has_image_reference(md):
            continue
        to_process.append(f)

    if args.max_files and args.max_files > 0:
        to_process = to_process[: int(args.max_files)]

    print(f"Found {len(md_files)} markdown files under {input_dir}")
    print(f"Case summaries missing images: {len(to_process)}")

    if not to_process:
        return 0

    if args.apply and not args.pixabay_key:
        print("Missing Pixabay API key. Provide --pixabay-key or set PIXABAY_API_KEY.", file=sys.stderr)
        return 2

    for idx, path in enumerate(to_process, start=1):
        md = _read_text(path)
        title = _extract_title(md, path.stem)
        body = strip_yaml_frontmatter(md)
        facts = extract_section_by_heading(body, "Facts")
        excerpt = facts or build_excerpt(md, max_lines=140)
        anchors = extract_concrete_keywords(facts or excerpt, max_keywords=12)

        if args.llm == "ollama":
            try:
                queries = llm_generate_queries_ollama(
                    host=args.ollama_host,
                    model=args.ollama_model,
                    title=title,
                    md_excerpt=excerpt,
                )
            except Exception as e:
                print(f"[{idx}/{len(to_process)}] Ollama failed for {path}: {e}")
                queries = heuristic_queries(title, excerpt)
        else:
            queries = heuristic_queries(title, excerpt)

        queries = filter_queries([q for q in queries if str(q).strip()], anchor_keywords=anchors)
        if not queries and anchors:
            # Deterministic fallback when the LLM produces legalese.
            seed = anchors[:6]
            combos = [
                " ".join(seed[:2]),
                " ".join(seed[:3]),
                " ".join(seed[:4]),
            ]
            queries = filter_queries(combos, anchor_keywords=anchors) or combos
        if not queries:
            print(f"[{idx}/{len(to_process)}] No queries produced for: {path}")
            continue

        chosen_hit: Optional[PixabayHit] = None
        chosen_query: Optional[str] = None

        if args.apply:
            for q_i, q in enumerate(queries, start=1):
                # Be gentle to the API even with caching.
                if args.sleep_ms and args.sleep_ms > 0:
                    time.sleep(args.sleep_ms / 1000.0)
                try:
                    hits = pixabay_search_image(
                        api_key=args.pixabay_key,
                        query=q,
                        cache=cache,
                        cache_path=cache_path,
                        per_page=30,
                        safesearch=True,
                        image_type="photo",
                        orientation="horizontal",
                    )
                except urllib.error.HTTPError as e:
                    msg = e.read().decode("utf-8", errors="ignore") if hasattr(e, "read") else str(e)
                    print(f"[{idx}/{len(to_process)}] Pixabay HTTP error for query {q!r}: {e.code} {msg}")
                    continue
                except Exception as e:
                    print(f"[{idx}/{len(to_process)}] Pixabay error for query {q!r}: {e}")
                    continue

                best = _choose_best_hit(hits)
                if best is not None:
                    chosen_hit = best
                    chosen_query = q
                    break
                if q_i == len(queries):
                    chosen_hit = None

        if not args.apply:
            print(f"[DRY RUN {idx}/{len(to_process)}] Would process: {path}")
            print(f"  - title: {title}")
            print(f"  - queries: {queries[:5]}{' ...' if len(queries) > 5 else ''}")
            continue

        if chosen_hit is None:
            print(f"[{idx}/{len(to_process)}] No Pixabay results for: {path}")
            continue

        img_url = chosen_hit.largeImageURL or chosen_hit.webformatURL or chosen_hit.previewURL
        if not img_url:
            print(f"[{idx}/{len(to_process)}] Chosen hit had no usable URL: {path}")
            continue

        ext = Path(urllib.parse.urlparse(img_url).path).suffix.lower()
        if ext not in {".jpg", ".jpeg", ".png", ".webp"}:
            ext = ".jpg"

        slug = _slugify(title)
        filename = f"{slug}_pixabay_{chosen_hit.id}{ext}"
        dest = download_dir / filename

        if not dest.exists():
            try:
                _http_download(img_url, dest)
            except Exception as e:
                print(f"[{idx}/{len(to_process)}] Download failed: {e}")
                continue

        # Obsidian resolves `/...` as vault-root paths and avoids `../` traversal.
        image_rel = "/" + _relpath_posix(dest, start=repo_root).lstrip("/")
        attribution = (
            f"*Image credit: [Pixabay]({chosen_hit.pageURL}) by "
            f"[{chosen_hit.user}]({_profile_url(chosen_hit.user, chosen_hit.user_id)}). "
            f"Query: `{chosen_query}`*"
        )

        new_md = _insert_image_block(md, image_rel_path=image_rel, attribution_line=attribution)
        _write_text(path, new_md)
        print(f"[{idx}/{len(to_process)}] Updated: {path} (downloaded: {image_rel})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

