# Bachelor of Laws (LLB) Study Repository

This repository serves as a centralized hub for study materials, readings, and summaries across various law subjects, primarily focusing on **Admin Law**, **Copyright Law**, and **Corporate Law**. It appears to be designed for use within a Personal Knowledge Management (PKM) system like Obsidian.

## Repository Structure Overview

The repository is organized by subject area at the root level. Each subject folder largely adheres to a separation between **raw source materials** and **student-synthesized summaries**.

---

### 1. Admin Law (`/Admin Law`)

Organized largely sequentially by teaching week.

- `**sources/`**: Contains the raw materials provided for the course.
  - Subdivided into `Introduction`, `Course Resources`, and weekly folders (e.g., `Week 2`, `Week 10`).
  - Weekly folders contain `Workshop study materials`, `Readings`, `Legislation, cases and commentary`.
  - `**statute/**`: Contains relevant legislation and acts for the course (e.g., ADJR Act, ART Act, Judiciary Act).
- `**summaries/**`: Contains student-created summaries and study notes, organized by week (e.g., `Week 2`, `Week 12`).

---

### 2. Copyright Law (`/Copyright Law`)

Follows a more structured, pipeline-driven approach for processing materials.

- `**01-raw-imports/**`: Unprocessed incoming materials, such as raw case texts and textbook excerpts.
- `**03-sources/**`: The main repository for categorized, pre-processed source materials.
  - Divided typologically by material: `articles`, `cases`, `ppts`, `statute` (e.g., Copyright Act), `textbook`.
  - `**downloads/**`: A dump of downloaded course content, assessments, additional readings, and lecture slides. *(Note: occasionally contains cross-pollination of other subjects like Law & Tech and Admin Law downloads)*.
- `**05-summaries/*`*: Synthesized notes and reading outlines, mirroring the structure of the sources directory (`articles`, `cases`, `ppts`, `textbook`).
- `**sources/**`: Contains finalized assessment instructions and high-level course resources.
- `**Assignment-Stability AI Architecture/**`: A dedicated workspace folder for an assignment relating to AI and copyright.

---

### 3. Corporate Law (`/Corporate Law`)

Organized heavily around weekly lecture content, with robust separation for reading summaries.

- `**sources/**`:
  - `**Assessment/**`: Assessment tasks and related guides (e.g., Cadmus assignments).
  - `**Textbook/**`: Primary textbook source files and extracted images/recordings.
  - `**Week X-Materials to LX/**`: Weekly folders containing lecture transcripts/materials and a nested `readings/` subfolder for that specific week's assigned reading sources.
  - `**unassigned-readings/**`: Supplementary reading materials not tied to a specific week.
- `**summaries/**`:
  - Organized sequentially by week (`Week 1`, `Week 2`, etc.).
  - Contains synthesized weekly notes, and a `readings/` subfolder containing the direct summaries of the specific readings assigned for that week.

---

### Other Root Folders & Files

- `**Law & Tech/**`: An additional law subject folder.
- `**Batch 1`, `Batch 2`, `Batch 3**`: Folders for batch-processed or uncategorized materials.
- `**Tara AI/**`: Auxiliary materials potentially related to AI legal tools.
- `**assessment_list.md**`: A master aggregate list or tracker for upcoming assignments and assessments.

## Common Organizational Conventions

Across the different subject repositories, several robust conventions emerge:

1. **Separation of Source and Synthesis**: A distinct and intentional boundary is maintained between raw materials (`sources/`, `03-sources/`) and study notes (`summaries/`, `05-summaries/`). This ensures raw texts are kept pristine while allowing for flexible summarization.
2. **Chronological vs. Typological Filing**:
  - *Admin Law* and *Corporate Law* are primarily organized **chronologically** (by Teaching Week), reflecting a lecture-driven study approach.
  - *Copyright Law* is organized **typologically** (by material type: case, article, textbook), reflecting a research-driven or literature-driven approach.
3. **Markdown-First (Obsidian Integration)**: Materials, particularly summaries, are predominantly authored in Markdown. The presence of `.obsidian` and `.obsidian-themes` at the root directory confirms this repository serves as an **Obsidian Vault**. You can expect extensive use of internal wiki-links and tags.

