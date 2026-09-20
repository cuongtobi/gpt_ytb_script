# 05A1 — CANONICAL DRAFT SENTENCE INDEXER

## Role

Create a mechanical sentence index for 05_script_draft.md before blind lexical discovery.

Read only:
- 05_script_draft.md
- prompts/INTEGRITY_PROOF_PROTOCOL.md

Do not evaluate meaning.

## Rules

- Exclude Markdown headings from narration sentence count.
- Preserve exact narration sentence text.
- Assign S0001, S0002, S0003...
- Do not skip short fragments if they are narration.
- Do not merge separate sentences because they express one idea.
- Record section heading separately.

## Output

Write:
- 05_draft_sentence_index.json

Fields:
- source_file
- units:
  - sentence_id
  - section_heading
  - exact_text
- source_sentence_count
- indexed_sentence_count
- duplicate_sentence_ids
- missing_sentence_ids
- reconstruction_ok
- status

FAIL if the index cannot reconstruct the narration sequence.
