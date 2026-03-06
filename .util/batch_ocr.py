#!/usr/bin/env python3
"""
Batch OCR for a folder of images into a single text file.

Default backend: Tesseract via pytesseract (fully local).

Usage:
  python batch_ocr.py /path/to/images output.txt

Requirements (Python packages):
  pip install pillow pytesseract

System requirement:
  Tesseract installed locally (e.g. on macOS: brew install tesseract)
"""

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image
import pytesseract


def list_images(folder: Path, extensions=None):
    if extensions is None:
        extensions = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}
    files = [
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in extensions
    ]
    # Sort by creation time (st_birthtime on macOS, st_ctime on others) - old to new
    return sorted(files, key=lambda p: p.stat().st_birthtime if hasattr(p.stat(), 'st_birthtime') else p.stat().st_ctime)


def ocr_image(image_path: Path) -> str:
    """Run OCR on a single image and return recognized text."""
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img)
    return text.strip()


def _collapse_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def normalize_paragraph(p: str) -> str:
    """
    Normalize paragraph text for stable duplicate detection.

    Heuristics:
    - treat line breaks as spaces (OCR often wraps lines)
    - lowercase
    - collapse all whitespace
    """
    p = p.replace("\r\n", "\n").replace("\r", "\n")
    p = p.strip()
    if not p:
        return ""
    p = _collapse_whitespace(p.replace("\n", " ")).lower()
    return p


def split_paragraphs(text: str) -> list[str]:
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return []
    parts = re.split(r"\n\s*\n+", text)
    return [p.strip() for p in parts if p.strip()]


def paragraph_fingerprint(normalized_paragraph: str) -> str:
    # Stable digest for exact-duplicate detection across runs.
    return hashlib.blake2b(normalized_paragraph.encode("utf-8"), digest_size=16).hexdigest()


def simhash64(normalized_text: str) -> int:
    """
    Lightweight 64-bit SimHash for near-duplicate detection.
    Good for OCR-ish text where small differences (line breaks, minor noise) occur.
    """
    tokens = re.findall(r"[a-z0-9]+", normalized_text.lower())
    if not tokens:
        return 0

    weights = {}
    for t in tokens:
        weights[t] = weights.get(t, 0) + 1

    v = [0] * 64
    for token, w in weights.items():
        h = int.from_bytes(hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest(), "big")
        for i in range(64):
            bit = (h >> i) & 1
            v[i] += w if bit else -w

    out = 0
    for i, score in enumerate(v):
        if score >= 0:
            out |= 1 << i
    return out


def hamming_distance64(a: int, b: int) -> int:
    return (a ^ b).bit_count()

def batch_ocr(
    input_dir: Path,
    output_file: Path,
    *,
    dedupe_paragraphs: bool,
    paragraph_simhash_threshold: int,
    min_paragraph_chars: int,
):
    if not input_dir.exists() or not input_dir.is_dir():
        raise ValueError(f"Input directory does not exist or is not a directory: {input_dir}")

    images = list_images(input_dir)
    if not images:
        raise ValueError(f"No image files found in: {input_dir}")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    seen_para_exact: set[str] = set()
    seen_para_simhashes: list[int] = []

    stats = {
        "images_total": len(images),
        "images_ocrd": 0,
        "paragraphs_written": 0,
        "paragraphs_skipped_duplicate": 0,
        "empty_images": 0,
    }

    with output_file.open("w", encoding="utf-8") as out_f:
        for idx, img_path in enumerate(images, start=1):
            print(f"OCR {idx}/{len(images)}: {img_path.name}")
            text = ocr_image(img_path)

            if not text.strip():
                stats["empty_images"] += 1
                continue

            stats["images_ocrd"] += 1

            if not dedupe_paragraphs:
                out_f.write(text.strip())
                out_f.write("\n\n")
                continue

            paragraphs = split_paragraphs(text)
            wrote_any = False
            for p in paragraphs:
                norm = normalize_paragraph(p)
                if len(norm) < min_paragraph_chars:
                    # Too short to safely dedupe (often slide numbers / stray OCR noise).
                    out_f.write(p.strip())
                    out_f.write("\n\n")
                    stats["paragraphs_written"] += 1
                    wrote_any = True
                    continue

                fp = paragraph_fingerprint(norm)
                if fp in seen_para_exact:
                    stats["paragraphs_skipped_duplicate"] += 1
                    continue

                sh = simhash64(norm)
                is_near = any(
                    hamming_distance64(sh, prev) <= paragraph_simhash_threshold
                    for prev in seen_para_simhashes
                )
                if is_near:
                    stats["paragraphs_skipped_duplicate"] += 1
                    continue

                seen_para_exact.add(fp)
                seen_para_simhashes.append(sh)
                out_f.write(p.strip())
                out_f.write("\n\n")
                stats["paragraphs_written"] += 1
                wrote_any = True

            # Keep a small separator between slides when *everything* was deduped,
            # otherwise you can lose the sense of progression entirely.
            if not wrote_any:
                out_f.write("\n")

    print(
        "Done.\n"
        f"- Wrote OCR text to: {output_file}\n"
        f"- Images total: {stats['images_total']}\n"
        f"- Images OCR'd: {stats['images_ocrd']}\n"
        f"- Empty images: {stats['empty_images']}\n"
        f"- Paragraphs written: {stats['paragraphs_written']}\n"
        f"- Paragraphs skipped (dup/near-dup): {stats['paragraphs_skipped_duplicate']}"
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert a folder of images into a single text file using local OCR."
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="Folder containing PNG/JPEG/TIFF/etc images.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Path to output text file (will be created/overwritten).",
    )
    parser.add_argument(
        "--no-dedupe-paragraphs",
        action="store_true",
        help="Disable paragraph duplicate/near-duplicate removal.",
    )
    parser.add_argument(
        "--paragraph-simhash-threshold",
        type=int,
        default=3,
        help="Max Hamming distance for paragraph SimHash to be considered a near-duplicate (default: 3).",
    )
    parser.add_argument(
        "--min-paragraph-chars",
        type=int,
        default=50,
        help="Paragraphs shorter than this are always kept (default: 50).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    batch_ocr(
        args.input_dir,
        args.output_file,
        dedupe_paragraphs=not bool(args.no_dedupe_paragraphs),
        paragraph_simhash_threshold=int(args.paragraph_simhash_threshold),
        min_paragraph_chars=int(args.min_paragraph_chars),
    )

