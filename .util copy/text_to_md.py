#!/usr/bin/env python3
"""
Convert plain-text lecture / OCR output into a rough Markdown structure.

Heuristics:
- Delete lines that contain only a bare number (page numbers).
- Turn certain patterns into headings:
  - "Chapter 5"       -> H1  ("# Chapter 5")
  - "1.30.05 Title"   -> H2  ("## 1.30.05 Title")   (timecode-style prefix)
- Short single-line blocks surrounded by blank lines -> H3 ("### ...")
- By default, split the resulting Markdown into one file per Chapter heading.
"""

import argparse
import re
from pathlib import Path


# A "real" chapter heading must be *only* "Chapter <number>" (no trailing text).
CHAPTER_RE = re.compile(r"^\s*chapter\s+\d+\s*$", re.IGNORECASE)
TIMECODE_HEADING_RE = re.compile(r"^\s*\d{1,2}\.\d{1,2}\.\d{1,2}\b.*$")
PAGE_NUMBER_RE = re.compile(r"^\s*\d+\s*$")


def classify_line(lines: list[str], idx: int) -> str:
    """
    Classify a line and return its Markdown-transformed version.

    Returns the transformed line (without trailing newline), or an empty string
    to indicate that the line should be removed entirely.
    """
    raw = lines[idx].rstrip("\n")
    text = raw.strip()

    # Blank lines: keep as is so paragraph breaks are preserved.
    if text == "":
        return ""

    # Drop bare page numbers.
    if PAGE_NUMBER_RE.fullmatch(text):
        return ""

    # Determine context: is this line isolated between blank lines?
    prev_blank = idx == 0 or lines[idx - 1].strip() == ""
    next_blank = idx == len(lines) - 1 or lines[idx + 1].strip() == ""
    is_isolated = prev_blank and next_blank

    # Explicit heading patterns first.
    if CHAPTER_RE.match(text):
        return "# " + text

    if TIMECODE_HEADING_RE.match(text):
        return "## " + text

    # Heuristic H3: short isolated line between blank lines.
    if is_isolated and len(text) <= 80:
        return "### " + text

    # Default: keep as body text.
    return text


def _slugify(title: str) -> str:
    title = title.strip().lower()
    # Remove leading "chapter X" to avoid duplication in filenames.
    m = re.match(r"^chapter\s+\d+\s*[:-]?\s*(.*)$", title, re.IGNORECASE)
    if m:
        title = m.group(1) or title
    title = re.sub(r"[^a-z0-9]+", "-", title)
    title = re.sub(r"-{2,}", "-", title).strip("-")
    return title or "chapter"


def _extract_chapter_number(title: str, fallback_index: int) -> int:
    m = re.search(r"\b(\d+)\b", title)
    if not m:
        return fallback_index
    try:
        return int(m.group(1))
    except ValueError:
        return fallback_index


def convert_text_to_md(input_path: Path, output_path: Path, *, split_by_chapter: bool = True) -> None:
    if not input_path.exists() or not input_path.is_file():
        raise ValueError(f"Input file does not exist or is not a file: {input_path}")

    raw_lines = input_path.read_text(encoding="utf-8").splitlines(keepends=True)

    # First pass: classify each line into Markdown (single unified document).
    md_lines: list[str] = []
    for i in range(len(raw_lines)):
        transformed = classify_line(raw_lines, i)
        if transformed == "":
            # Skip this line entirely (page numbers or intentional deletes).
            # Preserve blank lines by emitting actual empty strings separately.
            if raw_lines[i].strip() == "":
                md_lines.append("")
            continue
        md_lines.append(transformed)

    # If not splitting by chapter, just write a single file.
    if not split_by_chapter:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")
        print(f"Converted {input_path} -> {output_path}")
        return

    # Second pass: split into one file per chapter heading line.
    chapter_files: list[tuple[str, list[str]]] = []
    current_title: str | None = None
    current_buffer: list[str] = []

    for line in md_lines:
        stripped = line.lstrip()
        if stripped.startswith("# "):
            heading_text = stripped[2:].strip()
            if CHAPTER_RE.match(heading_text):
                # New chapter boundary.
                if current_title is None:
                    # First chapter: just start and keep any preface in this same buffer.
                    current_title = heading_text
                    current_buffer.append(line)
                else:
                    # Flush previous chapter.
                    chapter_files.append((current_title, current_buffer))
                    current_title = heading_text
                    current_buffer = [line]
                continue

        current_buffer.append(line)

    # Flush the last accumulated block.
    if current_buffer:
        if current_title is None:
            # No chapter headings at all: treat as a single document.
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")
            print(f"Converted {input_path} -> {output_path}")
            return
        else:
            chapter_files.append((current_title, current_buffer))

    # Write each chapter to its own file in a "<base>_chapters" folder.
    base_dir = output_path.parent
    base_stem = output_path.stem
    chapters_dir = base_dir / f"{base_stem}_chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    for idx, (title, lines) in enumerate(chapter_files, start=1):
        chap_num = _extract_chapter_number(title, idx)
        slug = _slugify(title)
        filename = f"chapter-{chap_num:02d}-{slug}.md"
        chapter_path = chapters_dir / filename
        chapter_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        print(f"Converted {input_path} -> {chapter_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a plain-text lecture/ocr file into Markdown with inferred headings.",
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Input .txt file.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        nargs="?",
        help="Output .md file (default: same path but with .md extension).",
    )
    # In case you ever want to keep a single combined file.
    parser.add_argument(
        "--no-split-by-chapter",
        action="store_true",
        help="Do not split the output into separate chapter files; emit a single Markdown file.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    in_path: Path = args.input_file
    if args.output_file is not None:
        out_path: Path = args.output_file
    else:
        if in_path.suffix.lower() == ".txt":
            out_path = in_path.with_suffix(".md")
        else:
            out_path = in_path.with_suffix(in_path.suffix + ".md")

    convert_text_to_md(
        in_path,
        out_path,
        split_by_chapter=not bool(args.no_split_by_chapter),
    )

