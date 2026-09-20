# 05A1 — CANONICAL DRAFT SENTENCE INDEXER

## Role

Create a mechanical sentence index for the exact 05_script_draft.md.

Read only:
- 05_script_draft.md
- prompts/INTEGRITY_PROOF_PROTOCOL.md

Do not evaluate meaning.

## Canonical segmentation

Use the exact algorithm in INTEGRITY_PROOF_PROTOCOL.md:
- ignore Markdown headings and blank lines;
- sentence-final punctuation ends a unit;
- periods between digits do not split;
- closing quotes/brackets remain attached;
- a non-empty line fragment without terminal punctuation is still a unit;
- preserve exact text except leading/trailing whitespace.

## Output

Write:
- 05_draft_sentence_index.json

Fields:
- source_file
- units[{sentence_id, section_heading, exact_text}]
- source_sentence_count
- indexed_sentence_count
- duplicate_sentence_ids
- missing_sentence_ids
- reconstruction_ok
- status

Do not claim PASS if exact reconstruction is uncertain.
