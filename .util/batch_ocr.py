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
import os
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
    # Sort for stable, human-friendly order
    return sorted(files, key=lambda p: p.name)


def ocr_image(image_path: Path) -> str:
    """Run OCR on a single image and return recognized text."""
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img)
    return text.strip()


def batch_ocr(input_dir: Path, output_file: Path):
    if not input_dir.exists() or not input_dir.is_dir():
        raise ValueError(f"Input directory does not exist or is not a directory: {input_dir}")

    images = list_images(input_dir)
    if not images:
        raise ValueError(f"No image files found in: {input_dir}")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as out_f:
        for idx, img_path in enumerate(images, start=1):
            print(f"OCR {idx}/{len(images)}: {img_path.name}")
            text = ocr_image(img_path)

            # Just write text from each image, separated by blank lines.
            out_f.write(text)
            out_f.write("\n\n")

    print(f"Done. Wrote OCR text to: {output_file}")


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
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    batch_ocr(args.input_dir, args.output_file)

