#!/usr/bin/env python3
"""
Heuristically assign unlabeled Corporate Law readings to teaching weeks
and copy them into:

  Corporate Law/sources/Week X-Materials to LX/readings/

The script works by:
- building a simple text "profile" for each week from its Reading Guide(s)
- comparing each unlabeled reading's text to those profiles
- assigning the reading to the week with the highest token overlap

Usage (from repo root):
  python .util/organise_corp_readings.py /path/to/unlabeled_readings

Recommended workflow:
1. Use batch_ocr.py or another tool to convert PDFs/images to .md or .txt
2. Put those files into a single folder, e.g. ~/Downloads/corp-unlabeled
3. Run this script with that folder as input (start with --dry-run)

This script is now **non-destructive** with respect to its inputs:
- it always **copies** readings into the week folders (never moves them)
- it performs any OCR "fixups" in memory only and does **not** overwrite the
  original text files.
"""

import argparse
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


REPO_ROOT = Path(__file__).resolve().parents[1]
CORP_ROOT = REPO_ROOT / "Corporate Law"
SOURCES_ROOT = CORP_ROOT / "sources"

# Where to look for original PDFs if we need to re-OCR a "too short" text file.
PDF_SOURCE_DIRS = [
    REPO_ROOT / "Case Dump",
]

# Very short texts are likely failed or low-quality extractions.
MIN_CHARS_FOR_OK_TEXT = 500


TOKEN_RE = re.compile(r"[a-z0-9]{3,}")

# Regex to extract case names: Party1 v Party2, R v X, Re X, etc.
# Match up to citation markers or end of string
CASE_NAME_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9\s&',\.\(\)]+?)\s+v\.?\s+([A-Z][A-Za-z0-9\s&',\.\(\)]+?)(?=\s*[\[\(\-]|\s*\d|\s*$)",
    re.IGNORECASE
)
RE_CASE_RE = re.compile(
    r"\bRe\s+([A-Z][A-Za-z0-9\s&',\.\(\)]+?)(?=\s*[\[\(\-,]|\s*\d|\s*$)",
    re.IGNORECASE
)
R_V_CASE_RE = re.compile(
    r"\bR\s+v\.?\s+([A-Z][A-Za-z0-9\s&',\.\(\)]+?)(?=\s*[\[\(\-]|\s*\d|\s*$)",
    re.IGNORECASE
)


def normalize_text(s: str) -> str:
    """Lowercase and collapse whitespace."""
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def tokenize(s: str) -> set[str]:
    return set(TOKEN_RE.findall(s.lower()))


def normalize_case_name(name: str) -> str:
    """
    Normalize a case name for matching:
    - lowercase
    - strip common noise (Ltd, Pty, plc, & Co, citations, brackets, etc.)
    - collapse whitespace
    """
    name = name.lower()
    # Normalize & to "and" before stripping
    name = re.sub(r"\s*&\s*", " and ", name)
    # Remove common corporate suffixes and noise
    for noise in [
        "ltd", "limited", "pty", "plc", "inc", "corp", "corporation",
        "and co", "and another", "and others", "and ors",
        "in liq", "in liquidation", "reg", "t/as", "tas",
    ]:
        name = re.sub(r"\b" + re.escape(noise) + r"\b", "", name)
    # Remove citations, brackets, parentheses content
    name = re.sub(r"[\[\(].*?[\]\)]", "", name)
    # Collapse whitespace and punctuation
    name = re.sub(r"[^\w\s]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def extract_case_names_from_line(line: str) -> set[str]:
    """
    Extract and normalize case names from a single line of text.
    """
    names = set()
    
    # Party v Party
    for match in CASE_NAME_RE.finditer(line):
        party1 = match.group(1).strip()
        party2 = match.group(2).strip()
        full = f"{party1} v {party2}"
        names.add(normalize_case_name(full))
    
    # Re X
    for match in RE_CASE_RE.finditer(line):
        party = match.group(1).strip()
        full = f"re {party}"
        names.add(normalize_case_name(full))
    
    # R v X
    for match in R_V_CASE_RE.finditer(line):
        party = match.group(1).strip()
        full = f"r v {party}"
        names.add(normalize_case_name(full))
    
    return names


def extract_case_names(text: str) -> set[str]:
    """
    Extract and normalize all case names from a reading guide or filename.
    
    For multi-line text (reading guides), we process line-by-line and skip
    lines that look like section headings or table formatting.
    """
    # If it's a single line (e.g. filename), just extract directly
    if "\n" not in text:
        return extract_case_names_from_line(text)
    
    # Multi-line: process each line, skipping noise
    names = set()
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        # Skip markdown headings, table syntax, obvious section titles
        if stripped.startswith(("#", "|", "##", "###")):
            continue
        # Skip lines that are purely section headings (no citations)
        if not any(char.isdigit() or char in "[]()," for char in stripped):
            # Likely a section heading like "### Corporate Groups"
            continue
        
        names.update(extract_case_names_from_line(line))
    
    return names


@dataclass
class WeekProfile:
    label: str               # e.g. "Week 1"
    dir_path: Path           # .../Corporate Law/sources/Week 1-Materials to L1
    tokens: set[str]
    # (original_title_line, tokens) pairs extracted from that week's reading guide(s)
    title_index: list[tuple[str, set[str]]]
    # Normalized case names from this week's reading guide
    case_names: set[str]


def build_week_profiles() -> List[WeekProfile]:
    """
    Build a simple text profile for each week from its reading guide(s).

    We look under:
      Corporate Law/sources/Week X-Materials to LX/
    and combine the content of:
      - Reading Guide to *.md
      - any other .md files in that week folder (as a weak hint)
    """
    if not SOURCES_ROOT.exists():
        raise SystemExit(f"SOURCES_ROOT not found: {SOURCES_ROOT}")

    week_dirs = sorted(SOURCES_ROOT.glob("Week *-Materials to L*"))
    if not week_dirs:
        raise SystemExit(f"No week directories found under {SOURCES_ROOT}")

    profiles: List[WeekProfile] = []

    for d in week_dirs:
        # Derive human label from folder name prefix: "Week 1-Materials to L1" -> "Week 1"
        prefix = d.name.split("-", 1)[0].strip()

        text_chunks: list[str] = []
        title_index: list[tuple[str, set[str]]] = []
        case_names: set[str] = set()

        # Reading guides (strong signal, and source of canonical titles)
        for g in d.glob("Reading Guide to *.md"):
            try:
                guide_text = g.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue

            text_chunks.append(guide_text)
            case_names.update(extract_case_names(guide_text))

            # Heuristically collect candidate titles from the guide:
            # - non-empty lines
            # - skip markdown headings/table syntax
            for line in guide_text.splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith(("#", "|")):
                    continue
                # Skip obvious section headings
                if stripped.lower() in {
                    "required reading",
                    "further reading",
                    "key instruments",
                }:
                    continue
                # Very short fragments are unlikely to be useful titles
                if len(stripped) < 8:
                    continue

                title_tokens = tokenize(stripped)
                if not title_tokens:
                    continue
                title_index.append((stripped, title_tokens))

        # Any other markdown files in the week folder (weaker signal, but cheap)
        for other in d.glob("*.md"):
            if "Reading Guide to " in other.name:
                continue
            try:
                text_chunks.append(other.read_text(encoding="utf-8", errors="ignore"))
            except OSError:
                continue

        combined = normalize_text(" ".join(text_chunks))
        tokens = tokenize(combined)
        profiles.append(
            WeekProfile(
                label=prefix,
                dir_path=d,
                tokens=tokens,
                title_index=title_index,
                case_names=case_names,
            )
        )

    return profiles


def read_text_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Fallback for odd encodings
        return path.read_text(encoding="latin-1", errors="ignore")


def _try_ocr_from_pdf_for(path: Path) -> str | None:
    """
    Best-effort OCR fallback for badly extracted readings.

    Heuristic:
    - Look for a PDF with the same stem in known PDF_SOURCE_DIRS.
    - If ocrmypdf is installed, run it with a temporary sidecar text file and
      return that text, without modifying the original input file.

    This requires:
      brew install tesseract ocrmypdf
    or equivalent on your system.
    """
    stem = path.stem

    if shutil.which("ocrmypdf") is None:
        return None

    pdf_path: Path | None = None
    for base in PDF_SOURCE_DIRS:
        candidate = base / f"{stem}.pdf"
        if candidate.exists():
            pdf_path = candidate
            break

    if pdf_path is None:
        return None

    print(f"[OCR] {path.name}: attempting OCR from {pdf_path.relative_to(REPO_ROOT)}")

    # Perform OCR into a temporary sidecar so the original text file is untouched.
    with tempfile.TemporaryDirectory(prefix="organise_corp_readings_ocr_") as tmp_dir:
        tmp_dir_path = Path(tmp_dir)
        sidecar = tmp_dir_path / f"{stem}.txt"
        tmp_pdf_out = tmp_dir_path / f"{stem}.ocr.pdf"

        try:
            subprocess.run(
                [
                    "ocrmypdf",
                    "--sidecar",
                    str(sidecar),
                    str(pdf_path),
                    str(tmp_pdf_out),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            print(f"[OCR] {path.name}: ocrmypdf failed; keeping original extraction")
            return None

        if not sidecar.exists():
            return None

        return read_text_file(sidecar)


def load_reading_text(path: Path) -> str:
    """
    Load text from an unlabeled reading.

    This currently supports plain text formats (.md, .txt).
    For PDFs/images, run OCR first using .util/batch_ocr.py or another tool.

    If the extracted text is suspiciously short, we make a best-effort attempt
    to re-OCR from a matching PDF (if available) using `ocrmypdf`.
    """
    if path.suffix.lower() in {".md", ".txt"}:
        text = read_text_file(path)
        if len(normalize_text(text)) < MIN_CHARS_FOR_OK_TEXT:
            maybe_ocr = _try_ocr_from_pdf_for(path)
            if maybe_ocr is not None:
                return maybe_ocr
        return text

    raise ValueError(
        f"Unsupported file type for {path.name!r} (suffix {path.suffix}). "
        "Convert to .md or .txt first (e.g. via batch_ocr.py or pdftotext)."
    )


def score_against_weeks(
    filename: str,
    tokens: set[str],
    profiles: Iterable[WeekProfile]
) -> tuple[WeekProfile, int, str]:
    """
    Score an unlabeled reading against each week profile.
    
    Strategy:
    1. If the filename looks like a case, try to match it to a week's case list (high confidence).
    2. Otherwise, fall back to token overlap (lower confidence).
    
    Returns: (best_profile, score, match_type)
    where match_type is "case" or "token"
    """
    # Try case-name matching first
    file_case_names = extract_case_names(filename)
    
    if file_case_names:
        for profile in profiles:
            for file_case in file_case_names:
                if file_case in profile.case_names:
                    # Exact case match - very high confidence
                    return profile, 9999, "case"
    
    # Fall back to token overlap
    best_profile: WeekProfile | None = None
    best_score = -1

    for profile in profiles:
        if not profile.tokens:
            continue
        overlap = len(tokens & profile.tokens)
        if overlap > best_score:
            best_score = overlap
            best_profile = profile

    if best_profile is None:
        raise RuntimeError("No week profiles with tokens available.")

    return best_profile, best_score, "token"


def iter_candidate_files(input_dir: Path) -> Iterable[Path]:
    for p in sorted(input_dir.iterdir()):
        if not p.is_file():
            continue
        if p.name.startswith("."):
            continue
        yield p


def _make_safe_filename(title: str) -> str:
    """
    Turn a human-readable title from a reading guide into a filesystem-safe name.
    """
    base = title.strip()
    # Replace characters that are problematic on common filesystems.
    for ch in '<>:"/\\|?*':
        base = base.replace(ch, "-")
    # Collapse whitespace.
    base = re.sub(r"\s+", " ", base).strip()
    if not base:
        base = "reading"
    return f"{base}.md"


def best_title_for_file(filename_stem: str, profile: WeekProfile) -> str | None:
    """
    Try to match a file (by its stem) to a canonical title from the week's
    reading guide(s), based on token overlap.
    """
    stem_tokens = tokenize(filename_stem)
    if not stem_tokens:
        return None

    best_title: str | None = None
    best_score = 0

    for original, tokens in profile.title_index:
        score = len(stem_tokens & tokens)
        if score > best_score:
            best_score = score
            best_title = original

    # Require at least a couple of overlapping tokens to avoid nonsense matches.
    if best_title is None or best_score < 2:
        return None

    return best_title


def move_or_copy(src: Path, dst: Path, *, copy: bool) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    # This helper now always behaves non-destructively with respect to the input
    # tree: callers pass copy=True and we never move the source file.
    if copy:
        shutil.copy2(src, dst)
    else:
        shutil.copy2(src, dst)


def organise_readings(
    input_dir: Path,
    *,
    dry_run: bool,
    min_overlap: int,
) -> None:
    profiles = build_week_profiles()
    print(f"Found {len(profiles)} week profiles under {SOURCES_ROOT}")

    files = list(iter_candidate_files(input_dir))
    if not files:
        print(f"No candidate files found in {input_dir}")
        return

    print(f"Processing {len(files)} unlabeled readings from {input_dir}")
    print()

    for f in files:
        try:
            text = normalize_text(load_reading_text(f))
        except ValueError as e:
            print(f"[SKIP] {f.name}: {e}")
            continue

        tokens = tokenize(text)
        if not tokens:
            print(f"[SKIP] {f.name}: no text tokens found")
            continue

        profile, score, match_type = score_against_weeks(f.name, tokens, profiles)

        # Case matches are always confident; token matches need min_overlap
        if match_type == "token" and score < min_overlap:
            print(
                f"[UNSURE] {f.name}: best guess {profile.label} (score={score}, "
                f"min_overlap={min_overlap}) – leaving in place"
            )
            continue

        dest_dir = profile.dir_path / "readings"

        # Optionally rename to the canonical title from the week's reading guide(s).
        title_match = best_title_for_file(f.stem, profile)
        if title_match:
            dest_name = _make_safe_filename(title_match)
        else:
            dest_name = f.name

        dest = dest_dir / dest_name

        action = "COPY"
        match_info = f"[{match_type.upper()}]" if match_type == "case" else f"score={score}"
        print(
            f"[{action}] {f.name} -> {profile.label} / readings / {dest_name} "
            f"({match_info})"
        )

        if not dry_run:
            move_or_copy(f, dest, copy=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Heuristically assign unlabeled Corporate Law readings to teaching "
            "weeks based on reading guides, and copy them into the "
            "appropriate Week X-Materials to LX/readings folder (inputs are left untouched)."
        )
    )
    p.add_argument(
        "input_dir",
        type=Path,
        help="Directory containing unlabeled readings (converted to .md/.txt).",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Only show what would be done; do not write any files.",
    )
    p.add_argument(
        "--min-overlap",
        type=int,
        default=25,
        help=(
            "Minimum token-overlap score required before assigning a reading "
            "to a week (default: 25). Increase to be more conservative."
        ),
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    input_dir: Path = args.input_dir

    if not input_dir.exists() or not input_dir.is_dir():
        raise SystemExit(f"Input directory does not exist or is not a directory: {input_dir}")

    organise_readings(
        input_dir=input_dir,
        dry_run=args.dry_run,
        min_overlap=int(args.min_overlap),
    )


if __name__ == "__main__":
    main()

