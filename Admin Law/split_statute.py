#!/usr/bin/env python3
"""
Split statute text or PDF into individual section/clause Markdown files.

Usage:
  # From plain text (e.g. AustLII or legislation.gov.au export):
  python split_statute.py input.txt output_folder --act "ADJR Act" --act-short adjr-act --max-section 30

  # From PDF:
  python split_statute.py input.pdf output_folder --act "ADJR Act" --act-short adjr-act --max-section 30 --start-page 10

Examples for Admin Law statutes:
  ADJR Act (Administrative Decisions (Judicial Review) Act 1977): --max-section 20
  AAT Act (Administrative Appeals Tribunal Act 1975): --max-section 70
  Migration Act 1958: --max-section 500 (or omit for no limit)
"""
import argparse
import os
import re
from pathlib import Path
from typing import List, Match, Optional

try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False


# Patterns that indicate header/footer noise (not section content)
DEFAULT_HEADER_FOOTER_PATTERNS = [
    re.compile(r"^-- \d+ of \d+ --$"),
    re.compile(r"^Compilation No\. \d+ Compilation date:"),
    re.compile(r"^Replaced Authorised Version registered"),
    re.compile(r"^Authorised Version [A-Z0-9]+ registered \d+/\d+/\d+$"),
    re.compile(r"^\d+\s+[\w\s(\)]+Act \d{4}\s*$"),  # "8 Administrative Decisions (Judicial Review) Act 1977"
    re.compile(r"^Section \d+[A-Z]*$"),
    re.compile(r"^Part [IVXLC0-9A-Z]+\s{2,}.+$"),
    re.compile(r"^.+\s{2,}Part [IVXLC0-9A-Z]+$"),
]

# Section start: number (optional letter suffix) + 2+ spaces + title
SECTION_LINE_PATTERN = re.compile(r"^\s*(\d+[A-Z]{0,6})\s{2,}(.+?)\s*$", re.MULTILINE)


def clean_text_formatting(text: str) -> str:
    """Reduce hard-wrapped lines while preserving structure around subsections."""
    text = text.replace("\r\n", "\n")
    lines = text.split("\n")

    new_lines: List[str] = []
    current_paragraph: List[str] = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        if not stripped:
            if current_paragraph:
                new_lines.append(" ".join(current_paragraph))
                current_paragraph = []
            new_lines.append("")
            continue

        is_list_start = re.match(r"^\s*(\(\w+\)|\d+\.)", stripped)
        is_short_heading = (
            len(stripped) < 80
            and stripped[0].isupper()
            and not stripped.endswith((".", ":", ";", ","))
        )

        if (is_list_start or is_short_heading) and current_paragraph:
            new_lines.append(" ".join(current_paragraph))
            current_paragraph = []

        current_paragraph.append(stripped)

        if stripped.endswith((".", ":", ";")):
            if i + 1 < len(lines):
                next_stripped = lines[i + 1].strip()
                if (
                    not next_stripped
                    or re.match(r"^\s*(\(\w+\)|\d+\.)", next_stripped)
                    or (
                        len(next_stripped) < 80
                        and next_stripped
                        and next_stripped[0].isupper()
                        and not next_stripped.endswith(".")
                    )
                ):
                    new_lines.append(" ".join(current_paragraph))
                    current_paragraph = []

    if current_paragraph:
        new_lines.append(" ".join(current_paragraph))

    return "\n".join(new_lines).strip()


def looks_like_noise_line(line: str, patterns: Optional[List] = None) -> bool:
    patterns = patterns or DEFAULT_HEADER_FOOTER_PATTERNS
    stripped = line.strip()
    if not stripped:
        return False
    return any(p.match(stripped) for p in patterns)


def read_text_from_file(path: str) -> str:
    """Read plain text from a file."""
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def extract_pdf_text(pdf_path: str, start_page: int = 0) -> str:
    """Extract text from PDF, skipping header pages."""
    if not HAS_PYPDF:
        raise ImportError("pypdf is required for PDF input. Run: pip install pypdf")
    print(f"Reading PDF from {pdf_path}...")
    reader = PdfReader(pdf_path)
    print(f"Extracting text from {len(reader.pages)} pages...")

    lines: List[str] = []
    for page_index in range(start_page, len(reader.pages)):
        if page_index > start_page and page_index % 100 == 0:
            print(f"Processing page {page_index}...")
        page_text = reader.pages[page_index].extract_text() or ""
        lines.extend(page_text.splitlines())

    cleaned_lines = [line for line in lines if not looks_like_noise_line(line)]
    return "\n".join(cleaned_lines)


def is_likely_section_title(title: str) -> bool:
    if not title:
        return False
    if ".." in title:
        return False
    if re.search(r"\.{3,}", title):
        return False
    if re.search(r"\s\d{1,4}\s*$", title):
        return False
    if len(title) > 260:
        return False
    if title.lower().startswith(("january", "june", "july", "jan ", "mar ")):
        return False
    return True


def find_section_matches(
    text: str,
    max_section: Optional[int] = None,
) -> List[Match[str]]:
    matches = list(SECTION_LINE_PATTERN.finditer(text))
    valid_matches: List[Match[str]] = []

    for match in matches:
        section_num = match.group(1)
        title = match.group(2).strip()
        full_line = match.group(0).strip()

        if max_section is not None:
            numeric_match = re.match(r"^(\d+)", section_num)
            if numeric_match and int(numeric_match.group(1)) > max_section:
                continue

        if not is_likely_section_title(title):
            continue
        if full_line.startswith(section_num + " of "):
            continue

        valid_matches.append(match)

    return valid_matches


def split_sections(
    text: str,
    output_folder: str,
    act_short_name: str,
    act_full_name: str,
    max_section: Optional[int] = None,
) -> None:
    os.makedirs(output_folder, exist_ok=True)

    # Cut off before schedules/endnotes
    cutoff_indexes: List[int] = []
    for pattern in [
        r"(?m)^\s*The Schedule\s*$",
        r"(?m)^\s*Schedules?\s*$",
        r"(?m)^\s*Endnotes\s*$",
        r"(?m)^\s*Schedule \d+\s*$",
    ]:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            cutoff_indexes.append(m.start())
    if cutoff_indexes:
        text = text[: min(cutoff_indexes)]

    matches = find_section_matches(text, max_section=max_section)
    unique_matches: List[Match[str]] = []
    seen_section_nums = set()
    for match in matches:
        section_num = match.group(1)
        if section_num in seen_section_nums:
            continue
        seen_section_nums.add(section_num)
        unique_matches.append(match)

    print(f"Found {len(unique_matches)} unique section starts. Splitting...")

    # Clear existing section files (but not the folder)
    act_subfolder = os.path.join(output_folder, act_short_name)
    if os.path.isdir(act_subfolder):
        for file_name in os.listdir(act_subfolder):
            path = os.path.join(act_subfolder, file_name)
            if os.path.isfile(path) and file_name.endswith(".md"):
                os.remove(path)
    os.makedirs(act_subfolder, exist_ok=True)

    for i, match in enumerate(unique_matches):
        section_num = match.group(1)
        section_title = match.group(2).strip()
        start_pos = match.start()
        end_pos = (
            unique_matches[i + 1].start() if i + 1 < len(unique_matches) else len(text)
        )
        raw_content = text[start_pos:end_pos].strip()

        header_line = match.group(0).strip()
        likely_title_only = (
            "." not in header_line
            and len(header_line) < 140
            and " For the purposes " not in header_line
            and " In this section" not in header_line
        )

        if likely_title_only and raw_content.startswith(header_line):
            content_body = raw_content[len(header_line) :].strip()
        else:
            content_body = raw_content

        formatted_content = clean_text_formatting(content_body)
        final_content = f"# {section_num} {section_title}\n\n{formatted_content}"
        file_name = f"{act_full_name} s {section_num}.md"
        file_path = os.path.join(act_subfolder, file_name)

        with open(file_path, "w", encoding="utf-8") as handle:
            handle.write(final_content.strip() + "\n")

    print(f"Extracted sections to {act_subfolder}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Split statute PDF or text into one markdown file per section."
    )
    parser.add_argument("input_path", help="Path to the PDF or .txt file.")
    parser.add_argument("output_folder", help="Directory where section files are written.")
    parser.add_argument(
        "--act",
        required=True,
        help='Full act name for file headers, e.g. "ADJR Act", "Copyright Act".',
    )
    parser.add_argument(
        "--act-short",
        required=True,
        help="Short name for output subfolder, e.g. adjr-act, aat-act, copyright-act.",
    )
    parser.add_argument(
        "--max-section",
        type=int,
        default=None,
        help="Maximum section number to include (omit for no limit).",
    )
    parser.add_argument(
        "--start-page",
        type=int,
        default=0,
        help="Zero-based page index for PDF (skip preamble). Default: 0.",
    )
    parser.add_argument(
        "--text-out",
        default="",
        help="Optional path to save extracted plain text before splitting.",
    )
    args = parser.parse_args()

    input_path = Path(args.input_path)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}")
        return

    suffix = input_path.suffix.lower()
    if suffix == ".pdf":
        if not HAS_PYPDF:
            print("Error: pypdf required for PDF. Run: pip install pypdf")
            return
        text = extract_pdf_text(str(input_path), start_page=args.start_page)
    elif suffix in (".txt", ".md"):
        print(f"Reading text from {input_path}...")
        text = read_text_from_file(str(input_path))
    else:
        print("Error: input must be .pdf, .txt, or .md")
        return

    if args.text_out:
        with open(args.text_out, "w", encoding="utf-8") as handle:
            handle.write(text)
        print(f"Wrote extracted text to {args.text_out}")

    split_sections(
        text,
        args.output_folder,
        act_short_name=args.act_short,
        act_full_name=args.act,
        max_section=args.max_section,
    )


if __name__ == "__main__":
    main()
