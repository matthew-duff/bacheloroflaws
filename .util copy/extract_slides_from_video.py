#!/usr/bin/env python3
"""
Extract "slide" images from a video that mostly contains static pages of text,
with fade/loading transitions between pages.

This script detects when the displayed image changes and exports one *sharp*
frame per detected slide into a subfolder of images.

Typical use (matches your `Recording.mov` case):
  python .util/extract_slides_from_video.py "Corporate Law/sources/textbook/Recording.mov"

Output:
  - A folder next to the video named `<video_stem>_images/`
  - PNG files like: slide_0001_00h00m12s345.png
  - `index.json` mapping each slide to timestamps + filename

Python requirements:
  pip install pillow imagehash

Notes:
  - This is designed to be robust to fades (it waits for the next image to be stable).
  - If you want OCR-based filenames afterwards, you can run `.util/batch_ocr.py`
    on the output folder, or extend this script.
"""

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

def format_timecode(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    ms_total = int(round(seconds * 1000))
    ms = ms_total % 1000
    s_total = ms_total // 1000
    s = s_total % 60
    m_total = s_total // 60
    m = m_total % 60
    h = m_total // 60
    return f"{h:02d}h{m:02d}m{s:02d}s{ms:03d}"


def sanitize_filename_fragment(text: str, max_len: int = 80) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9 _-]+", "", text)
    text = text.replace(" ", "_")
    text = re.sub(r"_+", "_", text)
    text = text.strip("_-")
    return text[:max_len] if text else ""


def ensure_ffmpeg():
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "ffmpeg is required but was not found on PATH.\n"
            "On macOS (Homebrew): brew install ffmpeg"
        )


def extract_sample_frames(video_path: Path, sample_dir: Path, sample_fps: float) -> list[Path]:
    """
    Uses ffmpeg to extract sampled frames to `sample_dir` as PNGs.

    Filenames are zero-based (000000.png, 000001.png, ...) so we can map
    index -> timestamp as index / sample_fps.
    """
    ensure_ffmpeg()
    sample_dir.mkdir(parents=True, exist_ok=True)

    # -vf fps=N gives us a simple, stable sampling approach.
    # -start_number 0 ensures consistent time mapping.
    out_pattern = str(sample_dir / "%06d.png")
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(video_path),
        "-vf",
        f"fps={sample_fps}",
        "-start_number",
        "0",
        out_pattern,
    ]
    subprocess.run(cmd, check=True)

    frames = sorted(sample_dir.glob("*.png"), key=lambda p: p.name)
    if not frames:
        raise RuntimeError("No frames were extracted. Is the video readable?")
    return frames


@dataclass
class Slide:
    index: int
    start_s: float
    end_s: float | None
    chosen_s: float
    filename: str
    sharpness: float


def extract_slides(
    video_path: Path,
    out_dir: Path,
    *,
    sample_fps: float = 4.0,
    change_thresh: int = 18,
    stable_thresh: int = 6,
    stable_needed: int = 4,
    hash_size: int = 16,
    overwrite: bool = False,
    keep_samples: bool = False,
):
    try:
        from PIL import Image, ImageFilter, ImageStat
        import imagehash
    except ModuleNotFoundError as e:
        missing = getattr(e, "name", "a dependency")
        raise RuntimeError(
            f"Missing Python dependency: {missing}\n\n"
            "Install requirements:\n"
            "  python3 -m pip install pillow imagehash"
        ) from e

    if not video_path.exists():
        raise FileNotFoundError(f"Video not found: {video_path}")

    if out_dir.exists():
        existing = [p for p in out_dir.iterdir() if p.is_file()]
        if existing and not overwrite:
            raise ValueError(
                f"Output directory already exists and is not empty: {out_dir}\n"
                f"Re-run with --overwrite or choose a different --outdir."
            )
    out_dir.mkdir(parents=True, exist_ok=True)

    slides: list[Slide] = []

    def compute_phash(img: Image.Image) -> "imagehash.ImageHash":
        if img.width > 512:
            h = int(round(img.height * (512 / img.width)))
            img = img.resize((512, max(1, h)), Image.Resampling.LANCZOS)
        return imagehash.phash(img, hash_size=hash_size)

    def compute_sharpness(img: Image.Image) -> float:
        # Edge variance is a simple, dependency-light sharpness proxy.
        g = img.convert("L")
        if g.width > 900:
            h = int(round(g.height * (900 / g.width)))
            g = g.resize((900, max(1, h)), Image.Resampling.BILINEAR)
        edges = g.filter(ImageFilter.FIND_EDGES)
        stat = ImageStat.Stat(edges)
        return float(stat.var[0])

    # Current slide tracking
    current_start_s: float | None = None
    current_rep_hash = None
    current_best_path: Path | None = None
    current_best_sharp = -1.0
    current_best_s = 0.0

    # Transition/stability tracking
    in_transition = False
    change_run = 0
    stable_run = 0
    new_slide_start_s = 0.0
    new_best_path: Path | None = None
    new_best_sharp = -1.0
    new_best_s = 0.0
    prev_hash = None

    with tempfile.TemporaryDirectory(prefix="extract_slides_") as tmp:
        sample_dir = Path(tmp) / "samples"
        frame_paths = extract_sample_frames(video_path, sample_dir, sample_fps=sample_fps)

        for idx, frame_path in enumerate(frame_paths):
            t_s = idx / float(sample_fps)
            try:
                with Image.open(frame_path) as img:
                    img.load()
                    hsh = compute_phash(img)
                    sharp = compute_sharpness(img)
            except Exception:
                continue

            if current_rep_hash is None:
                # First slide
                current_start_s = t_s
                current_rep_hash = hsh
                current_best_path = frame_path
                current_best_sharp = sharp
                current_best_s = t_s
                prev_hash = hsh
                continue

            dist_to_current = (hsh - current_rep_hash) if current_rep_hash is not None else 0
            dist_to_prev = (hsh - prev_hash) if prev_hash is not None else 0

            if not in_transition:
                # Normal stable slide: update best frame if it's sharp (but don't chase fade frames)
                if dist_to_current <= stable_thresh and sharp > current_best_sharp:
                    current_best_path = frame_path
                    current_best_sharp = sharp
                    current_best_s = t_s
                    current_rep_hash = hsh

                # Detect possible slide change (use a small run to reduce false positives)
                if dist_to_current >= change_thresh:
                    change_run += 1
                else:
                    change_run = 0

                if change_run >= 2:
                    in_transition = True
                    stable_run = 0
                    new_best_path = None
                    new_best_sharp = -1.0
                    new_best_s = 0.0
                    change_run = 0
            else:
                # During transitions, wait until the *new* content becomes stable
                if dist_to_prev <= stable_thresh:
                    if stable_run == 0:
                        new_slide_start_s = t_s
                    stable_run += 1
                    if sharp > new_best_sharp:
                        new_best_path = frame_path
                        new_best_sharp = sharp
                        new_best_s = t_s
                else:
                    stable_run = 0
                    new_best_path = None
                    new_best_sharp = -1.0
                    new_best_s = 0.0

                if stable_run >= stable_needed and new_best_path is not None and current_best_path is not None:
                    # Finalize previous slide
                    slide_idx = len(slides) + 1
                    filename = f"slide_{slide_idx:04d}_{format_timecode(current_best_s)}.png"
                    out_path = out_dir / filename
                    with Image.open(current_best_path) as best_img:
                        best_img.save(out_path, format="PNG")

                    slides.append(
                        Slide(
                            index=slide_idx,
                            start_s=float(current_start_s or 0.0),
                            end_s=float(new_slide_start_s),
                            chosen_s=float(current_best_s),
                            filename=filename,
                            sharpness=float(current_best_sharp),
                        )
                    )

                    # Start new slide from stable region
                    current_start_s = float(new_slide_start_s)
                    current_best_path = new_best_path
                    current_best_sharp = float(new_best_sharp)
                    current_best_s = float(new_best_s)
                    current_rep_hash = hsh

                    in_transition = False
                    stable_run = 0
                    new_best_path = None
                    new_best_sharp = -1.0
                    new_best_s = 0.0

            prev_hash = hsh

        if keep_samples:
            kept = out_dir / "_samples"
            kept.mkdir(parents=True, exist_ok=True)
            for p in frame_paths:
                # Avoid overwriting if user reruns with different params
                dest = kept / p.name
                if not dest.exists():
                    shutil.copy2(p, dest)

        # Finalize last slide (must happen before the temp dir is cleaned up)
        if current_rep_hash is not None and current_best_path is not None:
            last_idx = len(slides) + 1
            filename = f"slide_{last_idx:04d}_{format_timecode(current_best_s)}.png"
            out_path = out_dir / filename
            with Image.open(current_best_path) as best_img:
                best_img.save(out_path, format="PNG")
            slides.append(
                Slide(
                    index=last_idx,
                    start_s=float(current_start_s or 0.0),
                    end_s=None,
                    chosen_s=float(current_best_s),
                    filename=filename,
                    sharpness=float(current_best_sharp),
                )
            )

    index = {
        "video": str(video_path),
        "out_dir": str(out_dir),
        "params": {
            "sample_fps": sample_fps,
            "change_thresh": change_thresh,
            "stable_thresh": stable_thresh,
            "stable_needed": stable_needed,
            "hash_size": hash_size,
        },
        "slides": [
            {
                "index": s.index,
                "start_s": s.start_s,
                "end_s": s.end_s,
                "chosen_s": s.chosen_s,
                "filename": s.filename,
                "sharpness": s.sharpness,
            }
            for s in slides
        ],
    }
    (out_dir / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    return slides


def parse_args():
    p = argparse.ArgumentParser(
        description="Detect slide changes in a mostly-static video and export one image per slide."
    )
    p.add_argument("video", type=Path, help="Path to video file (e.g. Recording.mov).")
    p.add_argument(
        "--outdir",
        type=Path,
        default=None,
        help="Output directory (default: sibling folder named <video_stem>_images).",
    )
    p.add_argument("--sample-fps", type=float, default=4.0, help="Sampling rate for analysis.")
    p.add_argument("--change-thresh", type=int, default=18, help="Hash distance to enter transition.")
    p.add_argument("--stable-thresh", type=int, default=6, help="Hash distance to count as stable.")
    p.add_argument("--stable-needed", type=int, default=4, help="Stable samples required to accept new slide.")
    p.add_argument("--hash-size", type=int, default=16, help="pHash size (higher = more sensitive).")
    p.add_argument("--keep-samples", action="store_true", help="Keep sampled frames in outdir/_samples.")
    p.add_argument("--overwrite", action="store_true", help="Allow writing into a non-empty outdir.")
    return p.parse_args()


def main():
    args = parse_args()
    video_path = args.video
    out_dir = args.outdir
    if out_dir is None:
        out_dir = video_path.parent / f"{video_path.stem}_images"

    slides = extract_slides(
        video_path,
        out_dir,
        sample_fps=args.sample_fps,
        change_thresh=args.change_thresh,
        stable_thresh=args.stable_thresh,
        stable_needed=args.stable_needed,
        hash_size=args.hash_size,
        overwrite=args.overwrite,
        keep_samples=args.keep_samples,
    )
    print(f"Done. Extracted {len(slides)} slides to: {out_dir}")
    print(f"Wrote index: {out_dir / 'index.json'}")


if __name__ == "__main__":
    main()

