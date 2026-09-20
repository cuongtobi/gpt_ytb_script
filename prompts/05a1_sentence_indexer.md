# 05A1 — CANONICAL DRAFT SENTENCE INDEXER

## Role

Create a mechanical content-addressed sentence index for the exact 05_script_draft.md.

Read only:
- 00_project_brief.yaml for locale
- 05_script_draft.md
- CONTENT_ADDRESSING_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Do not evaluate meaning.

## Canonical segmentation

Use segmenter_version 3.3.0.

Follow the locale-aware algorithm in INTEGRITY_PROOF_PROTOCOL.md:
- ignore Markdown headings and blank lines;
- terminal punctuation ends a unit;
- ja/zh/ko support 。！？｡ in addition to .?!…;
- periods between digits do not split;
- closing quotes/brackets remain attached;
- line fragments without terminal punctuation remain units;
- preserve exact text except edge whitespace.

## Output

Write 05_draft_sentence_index.json with:
- source_file
- source_sha256
- locale
- segmenter_version
- content_address
- units[{sentence_id, section_heading, exact_text}]
- source_sentence_count
- indexed_sentence_count
- duplicate_sentence_ids
- missing_sentence_ids
- reconstruction_ok
- status

Do not claim PASS if exact reconstruction or source hash is uncertain.
