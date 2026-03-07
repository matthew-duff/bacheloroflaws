import argparse
import os
import re
from pathlib import Path
from typing import Iterable, List


JSTOR_SUBSTRING_PATTERNS: List[re.Pattern] = [
    re.compile(r"JSTOR is a not-for-profit service", re.IGNORECASE),
    re.compile(r"This content downloaded from", re.IGNORECASE),
    re.compile(r"All use subject to https://about\.jstor\.org/terms", re.IGNORECASE),
    re.compile(r"Your use of the JSTOR archive indicates your acceptance of the Terms", re.IGNORECASE),
    re.compile(r"is collaborating with JSTOR", re.IGNORECASE),
]


RUNNING_HEADER_PATTERNS: List[re.Pattern] = [
    # Typical journal running heads with page numbers, e.g.
    # "FOR WHOM CORPORATE MANAGERS ARE TRUSTEES 1365"
    # or "1370 HARVARD LAW REVIEW"
    re.compile(r"^[A-Z0-9 ,;:'\"().\-]{10,}\s+\d{1,4}\s*$"),
    re.compile(r"^\s*\d{1,4}\s+HARVARD LAW REVIEW", re.IGNORECASE),
]


def looks_like_junk(line: str) -> bool:
    """Return True if the line looks like an OCR header/footer we want to drop."""
    stripped = line.strip()
    if not stripped:
        return False

    # Explicit JSTOR-style boilerplate
    for pat in JSTOR_SUBSTRING_PATTERNS:
        if pat.search(stripped):
            return True

    # Generic running headers with page numbers in all caps
    for pat in RUNNING_HEADER_PATTERNS:
        if pat.match(stripped):
            return True

    return False


def clean_lines(lines: Iterable[str]) -> List[str]:
    """Remove header/footer noise and normalise blank lines."""
    cleaned: List[str] = []
    blank_streak = 0

    for line in lines:
        if looks_like_junk(line):
            continue

        if line.strip() == "":
            blank_streak += 1
            # Collapse long runs of blank lines down to a maximum of two
            if blank_streak > 2:
                continue
        else:
            blank_streak = 0

        cleaned.append(line)

    # Trim leading/trailing blank lines
    while cleaned and cleaned[0].strip() == "":
        cleaned.pop(0)
    while cleaned and cleaned[-1].strip() == "":
        cleaned.pop()

    # Re-add a single trailing newline for text files
    if cleaned and not cleaned[-1].endswith("\n"):
        cleaned[-1] = cleaned[-1] + "\n"

    return cleaned


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".md"):
                yield Path(dirpath) / name


def process_file(path: Path, dry_run: bool, backup: bool) -> bool:
    with path.open("r", encoding="utf-8") as f:
        original_lines = f.readlines()

    new_lines = clean_lines(original_lines)

    if new_lines == original_lines:
        return False

    print(f"Cleaned: {path}")

    if dry_run:
        return True

    if backup:
        backup_path = path.with_suffix(path.suffix + ".bak")
        if not backup_path.exists():
            backup_path.write_text("".join(original_lines), encoding="utf-8")

    path.write_text("".join(new_lines), encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Remove common OCR headers/footers (e.g. JSTOR boilerplate, running "
            "page headers) from markdown reading files."
        )
    )
    parser.add_argument(
        "root",
        nargs="?",
        default="Corporate Law/sources",
        help="Root directory to scan for .md files (default: Corporate Law/sources)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write changes, just report which files would be modified.",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Do not create .bak backups of modified files.",
    )

    args = parser.parse_args()
    root = Path(args.root)

    if not root.exists():
        raise SystemExit(f"Root path does not exist: {root}")

    changed_any = False
    for md_path in iter_markdown_files(root):
        changed = process_file(md_path, dry_run=args.dry_run, backup=not args.no_backup)
        changed_any = changed_any or changed

    if not changed_any:
        print("No changes needed.")


if __name__ == "__main__":
    main()

