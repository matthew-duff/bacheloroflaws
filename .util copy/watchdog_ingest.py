#!/usr/bin/env python3
import time
import sys
import os
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
ROOT_DIR = Path("/Users/matthewduff/Documents/Bachelor of Laws")
WATCH_ROOT = ROOT_DIR / ".blackboard"
BATCH_OCR_SCRIPT = ROOT_DIR / "util" / "batch_ocr.py"

# Course Mapping: Blackboard Code -> Workspace Folder Name
COURSE_MAP = {
    "LAWS5206": "Copyright Law",
    "LAWS3701": "LAWS3701 - Admin Law",
    "LAWS3702": "Corporate Law",
    "LAWS5151": "Law & Tech"
}

# Default conversion tools (using Copyright Law's venv as the primary processor)
# If other courses need different venvs, we can move this into a per-course config
DEFAULT_BASE = ROOT_DIR / "Copyright Law"
CONVERT_SCRIPT = DEFAULT_BASE / "01-raw-imports" / "cases" / "convert_cases_to_md.py"
VENV_PYTHON = DEFAULT_BASE / "01-raw-imports" / "cases" / ".venv" / "bin" / "python"

class IngestHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        self.handle_event(file_path)

    def on_moved(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.dest_path)
        self.handle_event(file_path)

    def handle_event(self, file_path):
        suffix = file_path.suffix.lower()
        output_info = self.get_output_info(file_path)
        
        if not output_info:
            return

        output_dir, course_name = output_info
        
        if suffix in [".pdf", ".doc", ".docx", ".pptx"]:
            print(f"[{course_name}] New document: {file_path.name}")
            self.process_file(file_path, output_dir)
        elif suffix in [".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"]:
            print(f"[{course_name}] New image: {file_path.name}")
            self.process_image(file_path, output_dir)
        elif suffix == ".txt":
            print(f"[{course_name}] New text file: {file_path.name}")
            self.process_txt(file_path, output_dir)

    def get_output_info(self, file_path):
        """
        Determines the output directory and course name based on the file path.
        Returns (output_dir, course_name) or None.
        """
        try:
            relative_path = file_path.parent.relative_to(WATCH_ROOT)
            parts = list(relative_path.parts)
            
            if not parts or "downloads" not in parts[0]:
                return None

            # Find the course code in the path (e.g., [LAWS5206])
            course_code = None
            course_folder = None
            course_index = -1
            
            for i, part in enumerate(parts):
                if part.startswith("[") and "]" in part:
                    code = part[1:part.find("]")]
                    if code in COURSE_MAP:
                        course_code = code
                        course_folder = COURSE_MAP[code]
                        course_index = i
                        break
            
            if not course_folder:
                return None

            # Simplify the path: remove everything up to and including the course folder
            # e.g., ["downloads", "[LAWS5206] ...", "Course Resources", ...] -> ["Course Resources", ...]
            new_parts = parts[course_index + 1:]
            
            output_root = ROOT_DIR / course_folder / "sources"
            output_dir = output_root / Path(*new_parts)
            # print(f"DEBUG: Mapping {file_path.name} to {output_dir} (Course: {course_folder})")
            return output_dir, course_folder

        except Exception as e:
            print(f"Error determining output info: {e}")
            return None

    def process_file(self, file_path, output_dir):
        time.sleep(2)
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
            
        try:
            result = subprocess.run(
                [str(VENV_PYTHON), str(CONVERT_SCRIPT), str(file_path.parent), "-o", str(output_dir)],
                capture_output=True,
                text=True,
                check=True
            )
            if result.stdout.strip():
                print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")
            print(e.stderr)

    def process_image(self, file_path, output_dir):
        time.sleep(2)
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
            
        try:
            output_txt = output_dir / (file_path.stem + ".txt")
            result = subprocess.run(
                [str(VENV_PYTHON), str(BATCH_OCR_SCRIPT), str(file_path.parent), str(output_txt)],
                capture_output=True,
                text=True,
                check=True
            )
            if result.stdout.strip():
                print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error during OCR: {e}")
            print(e.stderr)

    def process_txt(self, file_path, output_dir):
        time.sleep(1)
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
        output_md = output_dir / (file_path.stem + ".md")
        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
            output_md.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"Error converting .txt to .md: {e}")

def process_existing_files(handler):
    print(f"Scanning for existing files in {WATCH_ROOT}...")
    supported_docs = {".pdf", ".doc", ".docx", ".pptx"}
    supported_images = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}
    supported_txt = {".txt"}

    for root, dirs, files in os.walk(WATCH_ROOT):
        if ".venv" in root or "/." in root:
            continue

        for file in files:
            file_path = Path(root) / file
            suffix = file_path.suffix.lower()

            output_info = handler.get_output_info(file_path)
            if not output_info:
                continue
            
            output_dir, _ = output_info
            
            if suffix in supported_docs:
                output_file = output_dir / (file_path.stem + ".md")
                if not output_file.exists():
                    handler.process_file(file_path, output_dir)
            elif suffix in supported_images:
                output_file = output_dir / (file_path.stem + ".txt")
                if not output_file.exists():
                    handler.process_image(file_path, output_dir)
            elif suffix in supported_txt:
                output_file = output_dir / (file_path.stem + ".md")
                if not output_file.exists():
                    handler.process_txt(file_path, output_dir)

def main():
    if not WATCH_ROOT.exists():
        print(f"Error: Watch directory {WATCH_ROOT} does not exist.")
        sys.exit(1)

    event_handler = IngestHandler()
    
    if "--bulk" in sys.argv:
        process_existing_files(event_handler)
        if "--bulk-only" in sys.argv:
            sys.exit(0)

    observer = Observer()
    observer.schedule(event_handler, str(WATCH_ROOT), recursive=True)
    
    print(f"Monitoring {WATCH_ROOT} (recursively) for all courses...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
