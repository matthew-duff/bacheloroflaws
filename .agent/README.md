# Obsidian Enricher

This `.agent` scaffold uses Ollama to enrich markdown notes in this vault with:

- Obsidian-compatible YAML `tags`
- A managed `## See also` block using Obsidian `[[wikilinks]]`
- Per-domain memory files so each top-level folder keeps its own context

## How it works

The runner treats each top-level folder as its own domain:

- `Admin Law/` gets its own memory file
- `Corporate Law/` gets its own memory file
- `Copyright Law/` gets its own memory file

Memory is stored in `.agent/memories/<domain>.json`. The script only passes notes from the current domain into the prompt, so cross-references and note memory do not bleed across top-level folders.

By default it only processes **summary-style** folders:

- includes paths containing `/summaries/` or `/05-summaries/`
- excludes anything under `/sources/` or `/03-sources/`

## Files

- `.agent/obsidian_enricher.py`: main runner
- `.agent/config.json`: config knobs
- `.agent/prompts/pass1_extract.txt`: metadata extraction prompt
- `.agent/prompts/pass3_related.txt`: related-note selection prompt
- `.agent/prompts/universal_prompt.txt`: legacy all-in-one prompt template
- `.agent/memories/`: generated per-domain memory JSON files

## Note edits

The runner only manages two note surfaces:

1. The YAML `tags:` field in frontmatter
2. A managed `## See also` block wrapped in markers:

```md
## See also
<!-- agent:see-also:start -->
- [[Corporate Law/summaries/Week 2/readings/A Friedman doctrine‐- The Social Responsibility of Business Is to Increase Its Profits - The New York Times]]
<!-- agent:see-also:end -->
```

That makes the links readable in Obsidian while also giving the script a stable block it can safely replace on later runs.

## Usage

From the repo root:

```bash
python3 .agent/obsidian_enricher.py --dry-run --domain "Corporate Law" --limit 3
```

Then, when the output looks right:

```bash
python3 .agent/obsidian_enricher.py --domain "Corporate Law"
```

Useful options:

- `--domain "Admin Law"`: only process one top-level folder
- `--file "Corporate Law/summaries/Week 2/readings/Dodd, ‘For Whom are Corporate Managers Trustees?’ (1932).md"`: process one file
- `--limit 10`: process only a small batch
- `--memory-only`: update memory JSON without changing notes
- `--force`: reprocess even if the note hash matches memory
- `--model llama3.1`: override the configured Ollama model

## Recommended workflow

Start conservatively:

1. Run `--dry-run` on one domain with a small `--limit`
2. Run `--memory-only` if you want to inspect the generated memory first
3. Run against a single file or a single week before scaling up
4. Tune `.agent/config.json` and the prompt files in `.agent/prompts/`

## Notes

- The default model in config is `ministral-3:14b`, because it is already installed locally here. You can switch it to any model returned by `ollama list`.
- Generated memory JSON is ignored by `.agent/.gitignore`.
- The script only processes `.md` files.
