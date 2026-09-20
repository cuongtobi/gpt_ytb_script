# 10A1 — CANONICAL FINAL SENTENCE INDEXER

## Role

Create a mechanical content-addressed sentence index for the exact 10_final_candidate.md.

Read only:
- 00_project_brief.yaml for locale
- 10_final_candidate.md
- CONTENT_ADDRESSING_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Do not audit meaning.

Use locale-aware canonical segmentation version 3.3.0.

## Output

Write 10_final_sentence_index.json:
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

The index is provisional until 10D recomputes segmentation and source hash from released script bytes.
