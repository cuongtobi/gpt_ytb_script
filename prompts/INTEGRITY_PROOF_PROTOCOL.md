# INTEGRITY PROOF PROTOCOL — v3.2

## Purpose

v3.2 separates creative freedom from audit proof.

Writers are NOT required to explain every detected term.
Auditors ARE required to prove coverage, accounting, ordering and isolation.

If a proof is missing, fail closed.

## A. Canonical narration sentence index

Build the index from the exact script text before lexical audit.

### Canonical segmentation algorithm

1. Ignore Markdown heading lines beginning with `#`.
2. Ignore blank lines.
3. Process each remaining line from left to right.
4. A narration unit ends at `. ? ! …` when that mark is sentence-final.
5. A period between two digits is NOT a boundary, e.g. `12.000`.
6. Closing quotes/brackets immediately after terminal punctuation stay in the same unit.
7. If a non-empty line ends without terminal punctuation, the remaining text is still one narration unit.
8. Preserve exact unit text after trimming only leading/trailing whitespace.
9. Assign S0001, S0002, S0003... in source order.

Index fields:
- source_file
- units[{sentence_id, section_heading, exact_text}]
- source_sentence_count
- indexed_sentence_count
- duplicate_sentence_ids
- missing_sentence_ids
- reconstruction_ok

The deterministic verifier MUST recompute units from the source script and compare exact unit text and order.

## B. Exhaustive lexical coverage

For EVERY canonical sentence ID, lexical discovery writes exactly one ledger row:

- sentence_id
- lexical_candidate_ids: []

Zero candidates is valid.
A missing sentence row is not.

PASS requires exact sentence-ID sequence equality between canonical index and lexical ledger.

## C. Candidate conservation

Every lexical candidate gets exactly one final disposition:

- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Required equation:

discovered_count
=
baseline_known_count
+ grounded_count
+ replaced_count
+ removed_count
+ unresolved_count

The discovered candidate IDs used by the verifier come directly from 10B1, not from 10C self-report.

PASS requires:
- discovered IDs == disposition IDs
- no duplicate disposition IDs
- unresolved_count = 0

## D. Strict BASELINE_KNOWN provenance

Every BASELINE_KNOWN disposition must contain:
- baseline_source_type: assumed_known | normal_language_primitive
- baseline_source_id_or_exact_entry
- canonical_mapping_if_any

Missing provenance = invalid disposition.

## E. Temporal first-use proof

For every retained unfamiliar candidate:
- candidate_id
- first_use_sentence_id
- grounding_mode: PRIOR | INLINE | BASELINE | REPLACED | REMOVED
- grounding_sentence_id where relevant
- baseline_provenance where relevant

PRIOR:
grounding sentence number < first-use sentence number

INLINE:
grounding sentence number == first-use sentence number

BASELINE:
strict provenance required

REPLACED/REMOVED:
original unfamiliar phrase must not remain in final script.

Missing coordinates/provenance = FAIL.

## F. Minimal intervention

Detection does NOT imply explanation.

Repair preference:
1. REMOVE
2. REPLACE
3. REORDER
4. minimal inline grounding
5. larger rewrite only if necessary

Do not turn narration into a glossary.

## G. Blind execution isolation

Prompt-level blindness is not verified isolation.

10B1, 10B2 and 10B3 must run in distinct fresh execution contexts for PASS_VERIFIED.

The runtime, not the auditor, writes 10b_isolation_manifest.json.

Manifest top-level:
- manifest_origin: runtime
- attestation_source
- isolation_status

For each audit:
- audit_id
- execution_id
- context_mode: fresh
- allowed_input_files
- observed_input_files
- forbidden_input_files
- forbidden_input_accessed: false
- runtime_attested: true

PASS_VERIFIED requires:
- manifest_origin = runtime
- attestation_source present
- three distinct execution IDs
- all fresh
- all runtime_attested
- observed inputs are a subset of allowed inputs
- no observed input intersects forbidden inputs
- forbidden_input_accessed = false

If the environment cannot genuinely attest these facts:
isolation_status = ISOLATION_NOT_VERIFIED

Do not invent attestation.

## H. Final statuses

Allowed:
- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

PASS_VERIFIED requires deterministic proof verifier PASS plus VERIFIED isolation.
