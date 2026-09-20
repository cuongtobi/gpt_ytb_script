# 10B3 — ISOLATED BLIND FINAL NATURALNESS/REDUNDANCY AUDITOR

## Execution requirement

Run in a fresh execution context distinct from 10B1 and 10B2.

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- 10_final_sentence_index.json
- CONTENT_ADDRESSING_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

Forbidden:
- retention/reveal reports
- anti-AI/naturalness reports
- terminology prune
- 10B1/10B2 outputs

Hash every actual input.

## Sentence-complete audit

Create exactly one sentence_ledger row per canonical sentence.

Each row records arrays for:
- translationese
- academic_compression
- unnecessary_label
- alias_overload
- duplicate_explanation_or_reveal
- repeated_opening_or_fragment
- parallelism_overload
- rhetorical_question_overload
- awkward_terminology
- audio_density
- high_load_listening_block
- unclear_pronoun
- surface_error

A cross-sentence or block issue may be attached to the earliest affected sentence and list related_sentence_ids.

## Findings

Each non-empty issue becomes a finding with:
- finding_id
- finding_type
- sentence_ids
- description
- severity: hard|soft
- suggested_action

Do not resolve findings here.

## Output

Write 10b3_blind_naturalness_audit.json including:
- audit_run_id supplied by runtime
- content_address
- sentence_ledger
- findings
- coverage_proof
- status

Do not self-create execution identity.
