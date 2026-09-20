# INTEGRITY PROOF PROTOCOL — v3.2

## Purpose

v3.2 separates creative freedom from audit proof.

Writers are NOT required to explain every detected term.

Auditors ARE required to prove:
1. every narration sentence was covered;
2. every discovered candidate was accounted for;
3. every temporal grounding decision has an ordering proof;
4. blind final audits were run in genuinely isolated execution contexts.

If a proof is missing, fail closed.

---

## A. Canonical narration sentence index

Before lexical discovery, build a canonical sentence index from the exact script text.

Exclude Markdown headings from narration units.

Index narration sentences sequentially:
S0001, S0002, S0003...

Each record:
- sentence_id
- section_heading
- exact_text

The index must also record:
- source_file
- source_sentence_count
- indexed_sentence_count
- duplicate_sentence_ids
- missing_sentence_ids
- reconstruction_ok

PASS requires:
- source_sentence_count == indexed_sentence_count
- duplicate_sentence_ids = []
- missing_sentence_ids = []
- reconstruction_ok = true

A zero-candidate sentence is valid.
A missing sentence record is not.

---

## B. Exhaustive lexical coverage

Lexical discovery MUST produce one ledger record for EVERY canonical sentence ID.

Each sentence ledger record:
- sentence_id
- lexical_candidate_ids: []

A sentence with no candidates still appears with an empty list.

Coverage proof:
- index_sentence_ids
- ledger_sentence_ids
- missing_sentence_ids
- extra_sentence_ids
- duplicate_sentence_ids
- coverage_ok

PASS requires:
coverage_ok = true

"Read every sentence" is not proof.
Sentence-ID conservation is proof.

---

## C. Candidate conservation

Every lexical candidate must have exactly one final disposition:

- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Required proof:

discovered_count
=
baseline_known_count
+ grounded_count
+ replaced_count
+ removed_count
+ unresolved_count

Also record:
- discovered_candidate_ids
- disposition_candidate_ids
- missing_candidate_ids
- duplicate_disposition_ids
- equation_valid

PASS requires:
- missing_candidate_ids = []
- duplicate_disposition_ids = []
- equation_valid = true
- unresolved_count = 0

An aggregate "unresolved=0" is invalid without this proof.

---

## D. Strict BASELINE_KNOWN provenance

Every BASELINE_KNOWN disposition must contain:

- baseline_source_type: assumed_known | normal_language_primitive
- baseline_source_id_or_exact_entry
- canonical_mapping_if_any

Free-text justification is not sufficient.

If provenance is missing:
disposition is invalid.

---

## E. Temporal first-use proof

For every retained unfamiliar candidate record:

- candidate_id
- first_use_sentence_id
- grounding_mode:
  - PRIOR
  - INLINE
  - BASELINE
  - REPLACED
  - REMOVED
- grounding_sentence_id
- baseline_provenance, if BASELINE
- ordering_valid

Rules:

PRIOR:
grounding_sentence_number < first_use_sentence_number

INLINE:
grounding_sentence_number == first_use_sentence_number
AND the sentence supplies the needed meaning before/with reliance on the label

BASELINE:
valid strict baseline provenance required

REPLACED / REMOVED:
the unfamiliar label may not remain in final text

PASS requires every temporal record to be valid.

Missing first-use or grounding coordinates = FAIL.

---

## F. Minimal intervention

Detection does NOT imply explanation.

Repair preference:
1. REMOVE unnecessary label
2. REPLACE with already-known plain language
3. REORDER existing grounding
4. add minimal inline grounding
5. larger rewrite only if required

Do not turn narration into a glossary.

---

## G. Blind execution isolation

Prompt-level "do not read X" is not sufficient isolation.

10B1, 10B2 and 10B3 must run in separate fresh execution contexts.

A valid runtime isolation manifest must be created by the orchestration runtime, NOT by the auditor itself.

For each audit:
- audit_id
- execution_id
- context_mode: fresh
- allowed_input_files
- observed_input_files
- forbidden_input_files
- forbidden_input_accessed: false
- runtime_attested: true

Global isolation proof:
- all three execution_id values are distinct
- all context_mode = fresh
- all runtime_attested = true
- no forbidden input accessed

If the environment cannot guarantee fresh execution contexts:

isolation_status = ISOLATION_NOT_VERIFIED

The project may have:
content_integrity_status = PASS

but MUST NOT have:
project_status = PASS_VERIFIED

Same-chat sequential prompting is NOT accepted as verified isolation.

---

## H. Final statuses

Allowed:
- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

PASS_VERIFIED requires:
- all integrity counts zero
- sentence coverage proof valid
- candidate conservation proof valid
- temporal proof valid
- strict baseline provenance valid
- blind isolation VERIFIED
- deterministic proof verifier PASS

Do not collapse these statuses into a single optimistic PASS.
