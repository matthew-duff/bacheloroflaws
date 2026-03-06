#!/usr/bin/env python3
"""
Clean "ridiculous" newlines in Markdown files.

Common OCR/PDF-to-text failure mode: every text line is separated by a blank line,
making prose unreadable and hard to search.

This script:
1) Removes *isolated* blank lines (blank line between two non-blank lines).
   - This fixes the "blank line after every line" pattern.
   - True paragraph breaks (often multiple blank lines) remain.
2) Collapses runs of blank lines to a configurable maximum (default: 1).
3) Reflows normal prose blocks by joining wrapped lines into a single paragraph line,
   while preserving Markdown structure (headings, lists, code fences, tables, etc.).

Usage:
  python .util/clean_md_newlines.py "path/to/file.md" --in-place

Safe default:
  Without --in-place or --output, prints cleaned content to stdout.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


CODE_FENCE_RE = re.compile(r"^\s{0,3}(```|~~~)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+\S")
HR_RE = re.compile(r"^\s{0,3}([-*_])(\s*\1){2,}\s*$")
BLOCKQUOTE_RE = re.compile(r"^\s{0,3}>\s?")
LIST_RE = re.compile(r"^\s{0,3}(([*+-])|(\d+[.)])|([•‣]))\s+")
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
REF_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s+\S+")
FOOTNOTEISH_RE = re.compile(r"^\s*\d+\s+")
# OCR'd/PDF text often uses full-line bold instead of '#' headings, e.g. "**1. Introduction**"
BOLD_NUMBERED_HEADING_RE = re.compile(r"^\s*\*\*\s*\d+(?:\.\d+)*\s+[^*]+\*\*\s*$")


@dataclass(frozen=True)
class Stats:
    original_chars: int
    cleaned_chars: int
    original_lines: int
    cleaned_lines: int
    isolated_blank_lines_removed: int
    blank_runs_collapsed: int
    paragraphs_reflowed: int


def _normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _is_blank(line: str) -> bool:
    return not line.strip()


def remove_isolated_blank_lines(lines: list[str]) -> tuple[list[str], int]:
    """
    Remove blank lines that occur between two non-blank lines.

    This specifically targets the pattern:
      text
      <blank>
      text

    Paragraph breaks typically appear as *multiple* blank lines. In that case,
    none of those blank lines are "isolated" (they neighbor another blank line),
    so they are preserved for later collapsing.
    """
    if not lines:
        return lines, 0

    out: list[str] = []
    removed = 0
    n = len(lines)
    for i, line in enumerate(lines):
        if _is_blank(line):
            # If the next line starts with a lowercase letter, it's almost certainly
            # a continuation of the current paragraph that was broken by a blank line.
            next_line_is_lowercase = False
            if i + 1 < n:
                next_s = lines[i + 1].lstrip()
                # Ignore '### ' when checking for lowercase continuation
                if next_s.startswith("### "):
                    next_s = next_s[4:].lstrip()
                
                if next_s and next_s[0].islower():
                    next_line_is_lowercase = True

            prev_nonblank = i > 0 and not _is_blank(lines[i - 1])
            next_nonblank = i + 1 < n and not _is_blank(lines[i + 1])
            if (prev_nonblank and next_nonblank) or next_line_is_lowercase:
                # Preserve intentional spacing around structural Markdown lines
                # (e.g. headings, list items, code fences). Otherwise, headings
                # can get glued to the next paragraph when the file has the
                # "blank line after every line" pattern.
                if is_structural_md_line(lines[i - 1]) or is_structural_md_line(lines[i + 1]):
                    # Even if structural, if the next line is lowercase, it's likely
                    # an OCR error and should be joined.
                    if not next_line_is_lowercase:
                        out.append(line)
                        continue
                removed += 1
                continue
        out.append(line)
    return out, removed


def collapse_blank_runs(lines: list[str], *, max_blank_lines: int = 1) -> tuple[list[str], int]:
    max_blank_lines = max(0, int(max_blank_lines))
    out: list[str] = []
    blank_run = 0
    collapsed = 0

    for line in lines:
        if _is_blank(line):
            blank_run += 1
            if blank_run <= max_blank_lines:
                out.append("")
            else:
                collapsed += 1
        else:
            blank_run = 0
            out.append(line.rstrip())
    return out, collapsed


def remove_blank_lines_between_list_items(lines: list[str]) -> tuple[list[str], int]:
    """
    Remove blank lines that appear *between* two list items.

    Markdown lists do not need blank lines between each bullet, and OCR/PDF
    conversions often insert them.
    """
    if not lines:
        return lines, 0

    out: list[str] = []
    removed = 0
    n = len(lines)
    for i, line in enumerate(lines):
        if _is_blank(line):
            prev_is_list = i > 0 and bool(LIST_RE.match(lines[i - 1].rstrip("\n")))
            next_is_list = i + 1 < n and bool(LIST_RE.match(lines[i + 1].rstrip("\n")))
            if prev_is_list and next_is_list:
                removed += 1
                continue
        out.append(line)
    return out, removed


def is_structural_md_line(line: str) -> bool:
    s = line.rstrip("\n")
    if _is_blank(s):
        return True
    if CODE_FENCE_RE.match(s):
        return True
    if HEADING_RE.match(s):
        # If it's a level-3 heading starting with a lowercase letter,
        # treat it as non-structural (likely an OCR error).
        if s.startswith("### "):
            content = s[4:].lstrip()
            if content and content[0].islower():
                return False
        return True
    if BOLD_NUMBERED_HEADING_RE.match(s):
        return True
    if HR_RE.match(s):
        return True
    if BLOCKQUOTE_RE.match(s):
        return True
    if LIST_RE.match(s):
        return True
    if TABLE_ROW_RE.match(s):
        return True
    if REF_DEF_RE.match(s):
        return True
    # Treat footnote-ish lines as standalone to avoid gluing them to prose.
    # This doc often has footnotes like "1 _CaseName_ ..." mid-page.
    if FOOTNOTEISH_RE.match(s) and "_" in s:
        return True
    
    # Handle list items like "(b) text" or "### (b) text" as structural
    # to avoid merging them into the previous paragraph.
    list_item_content = s
    if s.startswith("### "):
        list_item_content = s[4:].lstrip()
    if re.match(r"^\s*\([a-z]\)\s+", list_item_content):
        return True

    # Keep page-header-ish lines like "**3**Royal Commission ..." intact.
    if s.lstrip().startswith("**") and re.match(r"^\s*\*\*\d+\*\*\S", s):
        return True
    return False


def _join_with_hyphenation(acc: list[str]) -> str:
    out = ""
    for piece in acc:
        p = piece.strip()
        if not p:
            continue
        
        # Strip '### ' if it's a lowercase continuation that was accidentally
        # tagged as a heading by OCR.
        if p.startswith("### "):
            content = p[4:].lstrip()
            if content and content[0].islower():
                p = content

        if not out:
            out = p
            continue
        if out.endswith("-") and len(out) >= 2 and out[-2].isalpha() and p and p[0].isalpha():
            out = out[:-1] + p
        else:
            out = out + " " + p
    return out.strip()


def reflow_markdown(lines: list[str]) -> tuple[list[str], int]:
    """
    Reflow prose by joining wrapped lines into paragraph lines.
    Preserves Markdown structure and code fences.
    """
    out: list[str] = []
    in_code_fence = False
    acc: list[str] = []
    paragraphs = 0

    def flush_acc():
        nonlocal paragraphs, acc
        if not acc:
            return
        joined = _join_with_hyphenation(acc)
        if joined:
            out.append(joined)
            paragraphs += 1
        acc = []

    for raw in lines:
        line = raw.rstrip("\n")

        if CODE_FENCE_RE.match(line):
            flush_acc()
            in_code_fence = not in_code_fence
            out.append(line.rstrip())
            continue

        if in_code_fence:
            out.append(line.rstrip("\n"))
            continue

        if _is_blank(line):
            flush_acc()
            out.append("")
            continue

        if is_structural_md_line(line):
            flush_acc()
            out.append(line.rstrip())
            continue

        acc.append(line)

    flush_acc()
    return out, paragraphs


def clean_markdown(text: str, *, max_blank_lines: int = 1, reflow: bool = True) -> tuple[str, Stats]:
    original = _normalize_newlines(text)
    original_lines = original.split("\n")

    lines, isolated_removed = remove_isolated_blank_lines(original_lines)
    lines, collapsed = collapse_blank_runs(lines, max_blank_lines=max_blank_lines)

    paragraphs = 0
    if reflow:
        lines, paragraphs = reflow_markdown(lines)
        lines, _list_blanks_removed = remove_blank_lines_between_list_items(lines)
        lines, collapsed2 = collapse_blank_runs(lines, max_blank_lines=max_blank_lines)
        collapsed += collapsed2

    # Trim excessive blank lines at start/end.
    while lines and _is_blank(lines[0]):
        lines.pop(0)
    while lines and _is_blank(lines[-1]):
        lines.pop()

    cleaned = "\n".join(lines).rstrip() + "\n"
    stats = Stats(
        original_chars=len(original),
        cleaned_chars=len(cleaned),
        original_lines=len(original_lines),
        cleaned_lines=len(cleaned.split("\n")),
        isolated_blank_lines_removed=isolated_removed,
        blank_runs_collapsed=collapsed,
        paragraphs_reflowed=paragraphs,
    )
    return cleaned, stats


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Clean excessive newlines and reflow Markdown prose.")
    p.add_argument("path", nargs="+", type=Path, help="Markdown file(s) to clean.")
    p.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite file(s) in place (recommended).",
    )
    p.add_argument(
        "--output",
        type=Path,
        help="Write output to this file (single input only).",
    )
    p.add_argument(
        "--no-backup",
        action="store_true",
        help="With --in-place, do not create a .bak backup file first.",
    )
    p.add_argument(
        "--max-blank-lines",
        type=int,
        default=1,
        help="Maximum consecutive blank lines to keep (default: 1).",
    )
    p.add_argument(
        "--no-reflow",
        action="store_true",
        help="Only remove/collapse blank lines; do not reflow paragraphs.",
    )
    p.add_argument(
        "--report",
        action="store_true",
        help="Print a short before/after stats report to stderr.",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    paths: list[Path] = [p for p in args.path]

    if args.output and len(paths) != 1:
        print("--output can only be used with a single input file.", file=sys.stderr)
        return 2
    if not args.in_place and not args.output and len(paths) != 1:
        print("For multiple input files, use --in-place.", file=sys.stderr)
        return 2

    exit_code = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        cleaned, stats = clean_markdown(
            text,
            max_blank_lines=int(args.max_blank_lines),
            reflow=not bool(args.no_reflow),
        )

        if args.report:
            print(
                f"{path}:\n"
                f"- chars: {stats.original_chars} -> {stats.cleaned_chars}\n"
                f"- lines: {stats.original_lines} -> {stats.cleaned_lines}\n"
                f"- removed isolated blank lines: {stats.isolated_blank_lines_removed}\n"
                f"- collapsed extra blank lines: {stats.blank_runs_collapsed}\n"
                f"- paragraphs reflowed: {stats.paragraphs_reflowed}",
                file=sys.stderr,
            )

        if args.in_place:
            if not args.no_backup:
                backup = path.with_suffix(path.suffix + ".bak")
                backup.write_text(text, encoding="utf-8")
            path.write_text(cleaned, encoding="utf-8")
        elif args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(cleaned, encoding="utf-8")
        else:
            sys.stdout.write(cleaned)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

