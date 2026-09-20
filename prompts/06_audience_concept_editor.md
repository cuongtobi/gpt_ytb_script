# 06 — AUDIENCE KNOWLEDGE CLOSURE WITH PROOFS

## Role

Reconcile draft knowledge with candidate accounting and temporal proof.

Read normal stage inputs plus:
- CONTENT_ADDRESSING_PROTOCOL.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Hash every actual input.

## Validate discovery coverage

Require lexical coverage and source hashes to match current draft/index bytes.
Otherwise FAIL.

## Candidate disposition

Every discovered candidate receives exactly one:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

BASELINE_KNOWN needs strict provenance.

## Candidate conservation

Record discovered IDs, dispositions, counts, missing/duplicate IDs and equation_valid.
UNRESOLVED must be zero for PASS.

## Temporal proof

For every retained unfamiliar candidate record exact first-use/grounding coordinates and grounding mode.

## Repair preference

REMOVE → REPLACE → REORDER → minimal grounding.

## Outputs

Write:
- 06_audience_report.md
- 06_knowledge_closure.json
- 06_script_accessible.md

06_knowledge_closure.json includes content_address plus discovery coverage, disposition crosswalk, conservation proof, temporal proofs and counters.

If output script changes, record both input_script_sha256 and output_script_sha256.
