# INTEGRITY PROOF PROTOCOL — v3.2

## Purpose

v3.2 separates creative freedom from audit proof.

Writers are NOT required to explain every detected term.
Auditors ARE required to prove coverage, accounting, ordering and isolation.

If proof is missing, fail closed.

## A. Canonical sentence index

Build from exact script text.

Canonical segmentation:
1. ignore Markdown headings and blank lines;
2. process each remaining line left-to-right;
3. terminal . ? ! … ends a unit;
4. a period between two digits does not split;
5. closing quotes/brackets remain attached;
6. a non-empty line fragment without terminal punctuation is still a unit;
7. trim only leading/trailing whitespace;
8. assign S0001, S0002... in source order.

10D recomputes this index directly from the final script and exact-matches text/order.

## B. Exhaustive lexical coverage

Every canonical sentence ID must have one ledger row.

A zero-candidate sentence still has a row.

To reduce selective within-sentence misses, each row must contain TWO reviews:

- forward_review
- reverse_review

Each review must include this category matrix:
- technical_scientific
- acronyms_symbols
- abstract_processes
- classifications
- evidence_methods
- measurements_quantities
- historical_institutional
- specialized_common_words
- aliases_relations
- mechanisms

Each category value is an array of phrases considered in that sentence.
Empty arrays are allowed, missing category keys are not.

The sentence's lexical_candidate_ids are the UNION of candidates proposed by forward and reverse review.

10D can verify sentence coverage and matrix completeness.
Semantic exhaustiveness can never be mathematically guaranteed by an LLM, so v3.2 reduces false negatives through mandatory two-direction review and isolated final auditing rather than pretending perfect semantic recall.

## C. Candidate conservation

Every 10B1 lexical candidate gets exactly one final disposition:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

10D takes discovered candidate IDs directly from 10B1.

Required:
discovered IDs == disposition IDs
and unresolved_count = 0.

## D. Strict BASELINE_KNOWN provenance

Every BASELINE_KNOWN disposition requires:
- baseline_source_type: assumed_known | normal_language_primitive
- baseline_source_id_or_exact_entry
- canonical_mapping_if_any

No free-text-only justification.

## E. Temporal first-use proof

For every retained unfamiliar candidate:
- candidate_id
- first_use_sentence_id
- grounding_mode: PRIOR | INLINE | BASELINE | REPLACED | REMOVED
- grounding_sentence_id where relevant
- baseline_provenance where relevant

10D independently finds the earliest canonical sentence containing the candidate's exact_phrase and requires it to equal first_use_sentence_id.

PRIOR:
grounding_sentence < actual_first_use_sentence

INLINE:
grounding_sentence == actual_first_use_sentence

BASELINE:
strict provenance required

REPLACED/REMOVED:
original exact phrase must not remain in final script.

## F. Minimal intervention

Detection does NOT imply explanation.

Repair preference:
1. REMOVE
2. REPLACE
3. REORDER
4. minimal inline grounding
5. larger rewrite only if necessary

## G. Blind execution isolation

10B1, 10B2 and 10B3 must run in distinct fresh execution contexts for PASS_VERIFIED.

The runtime, not the auditor, writes 10b_isolation_manifest.json.

If isolation cannot genuinely be attested:
isolation_status = ISOLATION_NOT_VERIFIED

Same-context sequential audits may be advisory only.

## H. Final statuses

- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL
