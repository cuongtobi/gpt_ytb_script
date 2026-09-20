# INTEGRITY PROOF PROTOCOL — v3.3

## Purpose

v3.3 separates creative freedom from audit proof and binds every proof to exact artifact bytes.

Writers are NOT required to explain every detected term.
Auditors ARE required to prove coverage, accounting, ordering, provenance, input identity and isolation.

If proof is missing, stale, malformed or contradictory, fail closed.

## A. Content identity

SHA-256 is computed over exact UTF-8 file bytes.

Every audit artifact must contain:

{
  "content_address": {
    "inputs": [
      {"path": "...", "sha256": "<64 lowercase hex>"}
    ]
  }
}

Rules:
1. include every file actually read by that audit;
2. do not include files the audit was forbidden to read;
3. the hash must match the current file bytes;
4. final B1/B2/B3 must each include 10_final_candidate.md or 10_final_script.md and bind to the exact bytes eventually released;
5. if 10C changes final text, all final index/audits are stale and must be regenerated.

10D compares the released script hash with each final audit script hash.
Mismatch = FAIL_STALE_AUDIT.

## B. Canonical sentence index

Build from exact script text.

Canonical segmentation v3.3:
1. ignore Markdown headings and blank lines;
2. process each remaining line left-to-right;
3. use locale-aware terminal punctuation;
4. default terminals: . ? ! …
5. ja/zh/ko additionally support 。！？｡
6. a period between two digits does not split;
7. closing quotes/brackets remain attached;
8. a non-empty line fragment without terminal punctuation is still a unit;
9. trim only leading/trailing whitespace;
10. assign S0001, S0002... in source order.

Index records:
- source_file
- source_sha256
- locale
- segmenter_version
- units
- source_sentence_count
- indexed_sentence_count

10D recomputes units directly from the released script.

## C. Exhaustive lexical coverage — B1

Every canonical sentence ID has exactly one knowledge ledger row.
Each row contains forward_review and reverse_review using the complete category matrix defined by 05B/10B1.

Zero-candidate sentences still receive a row.

Candidate IDs are the union of both passes.

## D. Knowledge candidate conservation

Every B1 lexical candidate receives exactly one disposition:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Required:
discovered IDs == disposition IDs
and unresolved_count = 0.

BASELINE_KNOWN requires strict machine-readable provenance.

## E. Temporal first-use proof

For each retained unfamiliar knowledge candidate:
- candidate_id
- first_use_sentence_id
- grounding_mode: PRIOR | INLINE | BASELINE
- grounding_sentence_id where relevant
- baseline_provenance where relevant

10D independently finds the earliest sentence containing exact_phrase.

PRIOR:
grounding_sentence < first_use_sentence

INLINE:
grounding_sentence == first_use_sentence

BASELINE:
strict provenance required.

## F. Sentence-complete claim discovery — B2

B2 uses the canonical final sentence index and creates exactly one row per sentence.

Each row contains two independent reviews:
- forward_claim_review
- reverse_claim_review

Each review contains arrays for:
- empirical_fact
- dates_quantities
- causal_mechanism
- scope_population_geography
- comparison_superlative
- attribution_source
- uncertainty_model
- negative_absence_claim
- definition_classification
- historical_event

claim_candidate_ids is the union of both passes.

Each claim candidate includes:
- claim_candidate_id
- sentence_id
- exact_quote
- normalized_claim
- claim_type
- discovered_by
- risk_flags

The exact_quote must occur in that canonical sentence.

## G. Claim conservation

Every B2 claim candidate receives exactly one final disposition:
- SUPPORTED
- QUALIFIED
- NON_FACTUAL
- UNRESOLVED

Repairs happen before the final proof cycle. If wording is rewritten or removed, regenerate the index and rerun B1/B2/B3; do not carry stale pre-repair claim IDs into final proof.

For SUPPORTED or QUALIFIED:
- mapped_claim_ids must be non-empty;
- evidence_ids must be non-empty;
- evidence IDs must exist in 02_evidence_ledger.json;
- evidence entries must point to source IDs that exist in 02_sources.json;
- mapped claim IDs must exist in 03_claim_map.json;
- evidence entries must support at least one mapped claim ID.

Required:
blind claim IDs == disposition IDs
and UNRESOLVED = 0.

## H. Naturalness/redundancy coverage — B3

B3 must cover every canonical sentence exactly once in sentence_ledger.

Each sentence row records flags from:
- translationese
- academic_compression
- unnecessary_label
- duplicate_explanation_or_reveal
- repeated_opening_or_fragment
- parallelism_overload
- rhetorical_question_overload
- awkward_terminology
- audio_density
- unclear_pronoun
- surface_error

Cross-sentence/block findings receive unique finding_ids.

Every finding receives exactly one disposition:
- RESOLVED
- KEEP_WITH_REASON
- UNRESOLVED

Hard final proof requires UNRESOLVED = 0.
KEEP_WITH_REASON is allowed only for soft/editorial findings and must contain a non-empty reason.

## I. Hard-counter recomputation

10D does not trust summary zeros.

It recomputes hard counters from:
- B1 candidate/disposition/temporal proof records;
- B2 claim ledger, claim dispositions and evidence links;
- B3 sentence ledger and finding dispositions;
- isolation manifest;
- content-address hashes;
- schema validation.

10_final_integrity.json summary counts must equal recomputed counts.
Mismatch = FAIL.

## J. Evidence provenance

02_evidence_ledger.json is the bridge:
claim → evidence → source.

Each evidence record includes:
- evidence_id
- claim_ids
- source_id
- locator
- support_mode: DIRECT | INFERENCE | CONTEXT
- evidence_summary
- limitations

No factual SUPPORTED/QUALIFIED blind claim may terminate at a bare source ID without an evidence record.

## K. Artifact manifest

artifact_manifest.json contains:
- pipeline_version
- artifact_schema_version
- segmenter_version
- inputs
- outputs
- hashes

All listed hashes must match current project files.
10D verifies the manifest before semantic proof checks.

## L. Blind execution isolation

10B1, 10B2 and 10B3 must run in distinct fresh execution contexts for PASS_VERIFIED.

Runtime, not auditor, writes the isolation manifest.

If isolation cannot genuinely be attested:
isolation_status = ISOLATION_NOT_VERIFIED.

## M. Final statuses

- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL
