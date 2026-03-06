import re
import sys
from pathlib import Path

def remove_mid_sentence_hashes(path: Path):
    content = path.read_text(encoding="utf-8")
    
    # Regex explanation:
    # (?<=\S)      : Lookbehind for a non-whitespace character (meaning ### is preceded by text)
    # \s*###\s*    : Match "###" with optional surrounding whitespace
    # (?=\S)       : Lookahead for a non-whitespace character (meaning ### is followed by text)
    # OR
    # \s+###\s+    : Match "###" surrounded by at least one space on both sides
    
    # We want to be careful not to hit actual headers at the start of lines.
    # This pattern targets " ### " or "word###word" or "word ### word"
    pattern = re.compile(r"(?<=\S)\s*###\s*(?=\S)|(?<=\s)###\s+(?=[a-z])")
    
    new_content = pattern.sub(" ", content)
    
    # Also clean up any double spaces we might have introduced
    new_content = re.compile(r"  +").sub(" ", new_content)
    
    if content != new_content:
        path.write_text(new_content, encoding="utf-8")
        return True
    return False

if __name__ == "__main__":
    directory = Path("Corporate Law/sources/Textbook")
    count = 0
    for md_file in directory.glob("*.md"):
        if remove_mid_sentence_hashes(md_file):
            print(f"Cleaned mid-sentence hashes in: {md_file.name}")
            count += 1
    print(f"Total files updated: {count}")
