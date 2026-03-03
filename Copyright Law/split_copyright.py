import argparse
import os
import re
from typing import List, Match

from pypdf import PdfReader


HEADER_FOOTER_PATTERNS = [
    re.compile(r"^-- \d+ of \d+ --$"),
    re.compile(r"^Copyright Act 1968 \d+$"),
    re.compile(r"^\d+ Copyright Act 1968$"),
    re.compile(r"^Compilation No\. \d+ Compilation date:"),
    re.compile(r"^Replaced Authorised Version registered"),
    re.compile(r"^Section \d+[A-Z]*$"),
    re.compile(r"^Part [IVXLC0-9A-Z]+\s{2,}.+$"),
    re.compile(r"^.+\s{2,}Part [IVXLC0-9A-Z]+$"),
]

# Broad section-start matcher: accepts headings that include a body sentence
# on the same line after PDF extraction.
SECTION_LINE_PATTERN = re.compile(r"^\s*(\d+[A-Z]{0,6})\s{2,}(.+?)\s*$", re.MULTILINE)


def clean_text_formatting(text: str) -> str:
    """
    Reduce hard-wrapped PDF lines while preserving structure around subsections.
    """
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


def looks_like_noise_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    return any(pattern.match(stripped) for pattern in HEADER_FOOTER_PATTERNS)


def extract_pdf_text(pdf_path: str, start_page: int) -> str:
    print(f"Reading PDF from {pdf_path}...")
    reader = PdfReader(pdf_path)
    print(f"Extracting text from {len(reader.pages)} pages...")

    lines: List[str] = []
    for page_index in range(start_page, len(reader.pages)):
        if page_index % 100 == 0:
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


def section_num_within_act_range(section_num: str) -> bool:
    numeric_match = re.match(r"^(\d+)", section_num)
    if not numeric_match:
        return False
    # Sections in this Act run from 1..249 (with letter suffixes).
    return int(numeric_match.group(1)) <= 249


def find_section_matches(text: str) -> List[Match[str]]:
    matches = list(SECTION_LINE_PATTERN.finditer(text))
    valid_matches: List[Match[str]] = []

    for match in matches:
        section_num = match.group(1)
        title = match.group(2).strip()
        full_line = match.group(0).strip()

        if not section_num_within_act_range(section_num):
            continue
        if not is_likely_section_title(title):
            continue
        if full_line.startswith(section_num + " of "):
            continue

        valid_matches.append(match)

    return valid_matches


def split_sections(text: str, output_folder: str) -> None:
    os.makedirs(output_folder, exist_ok=True)

    # Sections finish before schedules/endnotes in this compilation.
    cutoff_indexes: List[int] = []
    schedule_match = re.search(r"(?m)^\s*The Schedule\s*$", text)
    if schedule_match:
        cutoff_indexes.append(schedule_match.start())
    endnotes_match = re.search(r"(?m)^\s*Endnotes\s*$", text)
    if endnotes_match:
        cutoff_indexes.append(endnotes_match.start())
    if cutoff_indexes:
        text = text[: min(cutoff_indexes)]

    matches = find_section_matches(text)
    unique_matches: List[Match[str]] = []
    seen_section_nums = set()
    for match in matches:
        section_num = match.group(1)
        if section_num in seen_section_nums:
            continue
        seen_section_nums.add(section_num)
        unique_matches.append(match)

    print(f"Found {len(unique_matches)} unique section starts. Splitting...")

    for file_name in os.listdir(output_folder):
        path = os.path.join(output_folder, file_name)
        if os.path.isfile(path):
            os.remove(path)

    for i, match in enumerate(unique_matches):
        section_num = match.group(1)
        section_title = match.group(2).strip()
        start_pos = match.start()
        end_pos = (
            unique_matches[i + 1].start() if i + 1 < len(unique_matches) else len(text)
        )
        raw_content = text[start_pos:end_pos].strip()

        # Keep the first line when it likely includes real body text.
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
        file_name = f"Copyright Act s {section_num}.md"
        file_path = os.path.join(output_folder, file_name)

        with open(file_path, "w", encoding="utf-8") as handle:
            handle.write(final_content.strip() + "\n")

    print(f"Extracted sections to {output_folder}")


def extract_sections(
    pdf_path: str,
    output_folder: str,
    start_page: int = 32,
    extracted_text_path: str = "",
) -> None:
    text = extract_pdf_text(pdf_path, start_page=start_page)

    if extracted_text_path:
        with open(extracted_text_path, "w", encoding="utf-8") as handle:
            handle.write(text)
        print(f"Wrote extracted text to {extracted_text_path}")

    split_sections(text, output_folder)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split Copyright Act PDF into one markdown file per section."
    )
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    parser.add_argument("output_folder", help="Directory where section files are written.")
    parser.add_argument(
        "--start-page",
        type=int,
        default=32,
        help="Zero-based page index to begin parsing the body (default: 32).",
    )
    parser.add_argument(
        "--text-out",
        default="",
        help="Optional path to save extracted plain text before splitting.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    extract_sections(
        args.pdf_path,
        args.output_folder,
        start_page=args.start_page,
        extracted_text_path=args.text_out,
    )
