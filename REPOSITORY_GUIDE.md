# Repository Guide & Study Workspace Strategy

This document outlines the current audit of this repository as a law study workspace and provides a blueprint for maintaining an "elite" revision system.

## 📋 Audit Checklist

### ✅ Keep (Strengths)
- **Subject-at-Root Structure**: `Admin Law`, `Corporate Law`, etc., is simple and durable.
- **Source vs. Summary Split**: Maintaining a clear boundary between raw materials and your own synthesis is critical.
- **Revision-Oriented Writing**: Notes focusing on ratio, significance, and exam checklists (e.g., the *Meridian* summary) are high-value.
- **Assessment Tracking**: The `assessment_list.md` connects the vault to real-world deadlines.

### ⚠️ Fix (Immediate Improvements)
- **Template Contamination**: Remove mismatched metadata (e.g., Corporate Law tags in Admin Law progress notes).
- **Duplicate Filenames**: Clean up files ending in ` 1.md` or ` 2.md` to maintain backlink integrity.
- **Placeholder Notes**: Rename or delete `Untitled.md` files.
- **Staging Sprawl**: Consolidate `Batch 1`, `Batch 3`, and `File Dump` into a single `99-inbox` or process them into subjects.

### 🔭 Watch (Long-term Risks)
- **Atomization**: Ensure separate statute section notes are tied together by higher-level summaries.
- **Metadata Accuracy**: Verify that AI-generated "See Also" or metadata blocks remain accurate over time.

---

## 🏗️ Ideal Pattern: The "Elite" Law Vault

### 1. Folder Structure Logic
For each subject, aim for this functional skeleton:
- `00-admin/`: Syllabus, assessment plans, exam checklists.
- `01-sources/`: Raw lectures, readings, cases, and statutes.
- `02-notes/`: Active processing area for weekly content and readings.
- `03-summaries/`: Polished exam layer (case briefs, doctrine guides, "attack sheets").
- `04-revision/`: Confidence tracking and retrieval practice.
- `99-inbox/`: Temporary landing zone for new downloads.

### 2. Standardized Note Types
- **Case Brief**: Facts, Issue, Holding, Ratio, Significance, Exam Use.
- **Statute Note**: Provision text, Elements, Exceptions, Interpreting Cases, Exam Triggers.
- **Weekly Topic**: Concept mapping and relationship between authorities.
- **Exam Summary**: 1-page doctrine compression for rapid recall.

### 3. Recommended Metadata (YAML)
Use a consistent schema to enable powerful searching and Dataview queries:

```yaml
---
course: # e.g., LAWS3702 Corporate Law
note_type: # case-brief, statute-note, topic-summary, revision-board
topic: # e.g., attribution, duty of care
jurisdiction: # e.g., Commonwealth, Qld, NSW
cases: []
statutes: []
tags: []
assessment_relevance: # Why does this matter for the exam?
last_reviewed: 2026-03-09
status: # not-started, in-progress, reviewed, high-confidence
---
```

---

## 🚀 Migration Plan
1. **Metadata Audit**: Run a global search for "legal-personality" to find and fix contaminated Admin Law notes.
2. **File Cleanup**: Use a script or manual review to merge/rename duplicates and "Untitled" files.
3. **Inbox Consolidation**: Move contents of `Batch` folders to a single `Inbox` and process them.
4. **Template Deployment**: Create Obsidian templates for the standard note types above to ensure future consistency.

---
*Generated on 2026-03-09 to support Bachelor of Laws study workflow.*
