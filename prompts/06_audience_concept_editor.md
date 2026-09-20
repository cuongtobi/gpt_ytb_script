# 06 — AUDIENCE KNOWLEDGE CLOSURE WITH PROOFS

## Role

Reconcile draft knowledge with candidate-level accounting and temporal proof.

Read:
- project brief
- core subject
- claim map
- knowledge graph
- story architecture
- 05_script_draft.md
- 05_draft_sentence_index.json
- 05_lexical_knowledge_sweep.json
- 05_blind_knowledge_inventory.json
- shared protocols
- prompts/CONTENT_ADDRESSING_PROTOCOL.md

## 1. Validate discovery coverage

Require:
05 lexical coverage_ok = true.
The 05 script/index hashes declared by discovery artifacts must also match the current input bytes.

Otherwise FAIL.

## 2. Candidate disposition

Every discovered candidate receives exactly one:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Each BASELINE_KNOWN needs strict provenance.

## 3. Candidate conservation

Compute:
discovered_count
=
baseline_known_count
+ grounded_count
+ replaced_count
+ removed_count
+ unresolved_count

Record missing and duplicate IDs.

If equation invalid:
FAIL.

## 4. Temporal proof

For every retained unfamiliar candidate record:
- candidate_id
- first_use_sentence_id
- grounding_mode
- grounding_sentence_id
- baseline_provenance if needed
- ordering_valid

No free-text temporal PASS.

If first-use/grounding coordinate missing:
FAIL.

## 5. Repair preference

REMOVE → REPLACE → REORDER → minimal grounding.

Do not over-explain.

## Outputs

Write:
- 06_audience_report.md
- 06_knowledge_closure.json
- 06_script_accessible.md

06_knowledge_closure.json must include:
- content_address for every actual input;
- input_script_sha256;
- output_script_sha256;
- normal knowledge counters
- invalid_baseline_provenance
- discovery_coverage_proof
- candidate_disposition_crosswalk
- candidate_conservation_proof
- temporal_proofs
- status

PASS only if all hard proofs are valid and unresolved_count = 0.
