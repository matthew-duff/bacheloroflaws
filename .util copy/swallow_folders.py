#!/usr/bin/env python3
"""
Folder swallowing: move single-child content up and remove empty folders.

Rules:
- If a folder has exactly 1 child (file or folder), "swallow" it:
  - Move the child into the parent's parent
  - Name: join parent + child names, unless child is "ultraDocumentBody" → use parent name only
  - Delete the now-empty folder
- If a folder is empty, delete it
- If a file is empty (0 bytes), delete it

Applies to both files and folders as children.

Usage:
  python swallow_folders.py [root_dir]  # defaults to current directory
  python swallow_folders.py --dry-run [root_dir]  # preview without changing

Excluded by default: .git, .cursor, .util, node_modules, __pycache__, .venv.
.json files are ignored (not counted as children; folders with only .json are removed).
"""

import argparse
import os
import sys
from pathlib import Path

# Names that trigger "use parent name only" instead of joining
SWALLOW_AS_PARENT = frozenset({"ultraDocumentBody"})

# Path segments to never descend into or modify
SKIP_DIRS = frozenset({".git", ".cursor", ".util", "node_modules", "__pycache__", ".venv"})


def should_skip(path: Path, root: Path) -> bool:
    """Return True if path or any ancestor should be skipped."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        return True
    for part in rel.parts:
        if part in SKIP_DIRS:
            return True
    return False


def get_swallowed_name(parent_name: str, child_path: Path) -> str:
    """
    Determine the new name when swallowing parent into child.
    Join names unless child is ultraDocumentBody, then use parent name only.
    """
    if child_path.is_dir():
        child_name = child_path.name
    else:
        child_name = child_path.name  # include extension for files

    child_stem = child_path.stem if child_path.is_file() else child_path.name
    if child_stem in SWALLOW_AS_PARENT:
        if child_path.is_file():
            return parent_name + child_path.suffix  # e.g. Parent.md
        return parent_name
    # Join: Parent-Child or Parent-Child.md
    return f"{parent_name}-{child_name}"


def swallow_folder(parent: Path, dry_run: bool) -> list[str]:
    """
    If parent has exactly one child, move it up and rename per rules.
    Returns list of log messages.
    """
    entries = [
        p for p in parent.iterdir()
        if not should_skip(p, parent) and p.suffix.lower() != ".json"
    ]
    if len(entries) != 1:
        return []

    child = entries[0]
    grandparent = parent.parent
    new_name = get_swallowed_name(parent.name, child)
    dest = grandparent / new_name

    if dest.exists():
        return [f"SKIP: destination exists: {dest}"]

    msgs = []
    if dry_run:
        msgs.append(f"[DRY-RUN] Would: {child} -> {dest}")
    else:
        child.rename(dest)
        msgs.append(f"Swallowed: {child.name} -> {dest}")
        if not any(parent.iterdir()):
            parent.rmdir()
            msgs.append(f"Removed empty: {parent}")
    return msgs


def remove_empty_folder(path: Path, dry_run: bool) -> bool:
    """Remove path if it's empty (no files, or only .json). Returns True if removed."""
    if not path.is_dir():
        return False
    entries = list(path.iterdir())
    non_json = [p for p in entries if p.suffix.lower() != ".json"]
    if non_json:
        return False
    if dry_run:
        print(f"[DRY-RUN] Would remove empty: {path}")
    else:
        for p in entries:
            p.unlink()  # remove .json files if any
        path.rmdir()
        print(f"Removed empty: {path}")
    return True


def remove_empty_file(path: Path, root: Path, dry_run: bool) -> bool:
    """Remove path if it's an empty (0-byte) file. Returns True if removed."""
    if not path.is_file():
        return False
    if path.stat().st_size != 0:
        return False
    if should_skip(path, root):
        return False
    if dry_run:
        print(f"[DRY-RUN] Would remove empty file: {path}")
    else:
        path.unlink()
        print(f"Removed empty file: {path}")
    return True


def run_swallow(root: Path, dry_run: bool) -> int:
    """
    Bottom-up pass: swallow single-child folders, then remove empties.
    May need multiple passes if swallowing creates new single-child cases.
    """
    root = root.resolve()
    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        return 1

    total_ops = 0
    max_passes = 50  # prevent infinite loops
    for _ in range(max_passes):
        changed = False

        # Bottom-up: deepest dirs first
        dirs_to_check = []
        for dirpath, dirnames, _ in os.walk(root, topdown=True):
            # Prune SKIP_DIRS from descent
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            p = Path(dirpath)
            if should_skip(p, root):
                continue
            dirs_to_check.append(p)

        # Remove empty files (may create single-child situations)
        for parent in dirs_to_check:
            if not parent.exists():
                continue
            for entry in list(parent.iterdir()):
                if entry.is_file() and remove_empty_file(entry, root, dry_run):
                    total_ops += 1
                    changed = True

        # Process deepest first (swallow single-child)
        for parent in reversed(dirs_to_check):
            if not parent.exists():
                continue
            msgs = swallow_folder(parent, dry_run)
            for m in msgs:
                print(m)
                total_ops += 1
                changed = True

        # Remove empty folders (bottom-up)
        for parent in reversed(dirs_to_check):
            if not parent.exists():
                continue
            if parent == root:
                continue
            if remove_empty_folder(parent, dry_run):
                total_ops += 1
                changed = True

        if not changed:
            break

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Swallow single-child folders: move content up, join names (or use parent if child is ultraDocumentBody). Delete empty folders."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        type=Path,
        help="Root directory to process (default: current dir)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying filesystem",
    )
    args = parser.parse_args()
    sys.exit(run_swallow(args.root, args.dry_run))


if __name__ == "__main__":
    main()
