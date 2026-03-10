import pathlib


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]


def fix_file(path: pathlib.Path, old_prefix: str) -> bool:
    """
    Replace occurrences of the absolute prefix with a repo-relative path.

    Returns True if the file was modified.
    """
    original = path.read_text(encoding="utf-8")
    relative_prefix = ""

    updated = original.replace(old_prefix, relative_prefix)

    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    # Absolute path prefix we want to strip out.
    # Keep this conservative to avoid unintended edits.
    old_prefixes = [
        "/Users/matthewduff/Documents/bacheloroflaws/",
        "/Users/matthewduff/Documents/Bachelor of Laws/",
    ]

    md_files = REPO_ROOT.rglob("*.md")
    changed_files = []

    for md_path in md_files:
        if ".git" in md_path.parts:
            continue

        text = md_path.read_text(encoding="utf-8")
        updated = text
        for prefix in old_prefixes:
            updated = updated.replace(prefix, "")

        if updated != text:
            md_path.write_text(updated, encoding="utf-8")
            changed_files.append(md_path)

    if changed_files:
        print("Updated the following markdown files:")
        for p in changed_files:
            print(f"- {p.relative_to(REPO_ROOT)}")
    else:
        print("No markdown files required changes.")


if __name__ == "__main__":
    main()

