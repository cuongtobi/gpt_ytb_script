# 10A1 — CANONICAL FINAL SENTENCE INDEXER

## Role

Create a mechanical sentence index for the exact 10_final_candidate.md.

Read only:
- 10_final_candidate.md
- prompts/INTEGRITY_PROOF_PROTOCOL.md

Do not audit meaning.

Use the exact canonical segmentation algorithm from INTEGRITY_PROOF_PROTOCOL.md.

## Output

Write:
- 10_final_sentence_index.json

Fields:
- source_file
- units[{sentence_id, section_heading, exact_text}]
- source_sentence_count
- indexed_sentence_count
- duplicate_sentence_ids
- missing_sentence_ids
- reconstruction_ok
- status

This index is only provisional until 10D recomputes the segmentation directly from the script and verifies exact equality.
