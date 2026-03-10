#!/usr/bin/env python3
from __future__ import annotations

"""
Remove managed "See also" blocks inserted by .agent/obsidian_enricher.py
from all markdown files in this repo, respecting the same path exclusions
configured in .agent/config.json.
"""

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / ".agent" / "config.json"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def should_skip(path: Path, exclude_substrings: list[str]) -> bool:
    relative = "/" + path.relative_to(REPO_ROOT).as_posix()
    return any(fragment in relative for fragment in exclude_substrings)


def remove_see_also_block(
    path: Path,
    heading: str,
    marker: str,
) -> bool:
    text = read_text(path)
    pattern = re.compile(
        rf"{re.escape(heading)}\n<!-- {re.escape(marker)}:start -->.*?<!-- {re.escape(marker)}:end -->",
        re.DOTALL,
    )
    if not pattern.search(text):
        return False

    updated = pattern.sub("", text).rstrip() + "\n"
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    config = load_config()
    heading = config["see_also_heading"]
    marker = config["see_also_marker"]
    exclude_substrings = config.get("exclude_path_substrings", [])

    total_files = 0
    modified_files = 0

    for md_path in REPO_ROOT.rglob("*.md"):
        if should_skip(md_path, exclude_substrings):
            continue
        total_files += 1
        if remove_see_also_block(md_path, heading, marker):
            print(f"[removed] {md_path.relative_to(REPO_ROOT)}")
            modified_files += 1

    print(f"Scanned {total_files} markdown files; removed See also blocks from {modified_files} file(s).")


if __name__ == "__main__":
    main()

