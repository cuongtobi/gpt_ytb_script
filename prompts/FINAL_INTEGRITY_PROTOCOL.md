# FINAL INTEGRITY PROTOCOL — v3.3

## Purpose

v3.3 keeps the creative lane flexible and makes the integrity lane content-addressed, provenance-aware and machine-checkable.

Read:
- CONTENT_ADDRESSING_PROTOCOL.md
- KNOWLEDGE_GROUNDING_PROTOCOL.md
- EVIDENCE_PROVENANCE_PROTOCOL.md
- INTEGRITY_PROOF_PROTOCOL.md

## Creative-lane rule

Do not write to satisfy counters.
Write the best story first.
Audit afterward.
Repair minimally.

## Hard proof gates

Hard:
- artifact/schema validity
- current-file SHA-256 integrity
- no stale final audits
- canonical sentence coverage
- B1 lexical ledger coverage
- knowledge candidate conservation
- temporal ordering
- strict BASELINE_KNOWN provenance
- B2 claim sentence coverage
- claim conservation
- claim → evidence → source provenance
- B3 sentence coverage
- finding conservation
- factual support/scope closure
- blind execution isolation for PASS_VERIFIED

Soft/editorial:
- terminology necessity
- translationese
- rhetorical repetition
- listening density
- duplicate reveal judgment

Soft findings may remain only as KEEP_WITH_REASON. They must not be silently dropped.

## Terminology necessity

For every non-baseline label consider:
- needed_for_later_reasoning
- reuse_count
- precision_gain
- story_value
- replacement_available
- context_scope

Prefer REMOVE/REPLACE when exact label is not necessary.

## Reveal integrity

Track:
- TEASE
- EXPLAIN
- EVIDENCE
- COMPLICATE
- PAYOFF
- CALLBACK

Same claim + same evidence + same meaning with no distinct story job = redundant reveal.

## Claim strength

Do not exceed:
- certainty
- time scope
- geographic scope
- population scope
- source strength

All retained factual commitments discovered by B2 must be conserved and mapped to evidence.

## Naturalness/listening

Audit for:
- translationese
- academic compression
- noun stacking
- repeated templates
- fragment-pattern repetition
- overloaded one-listen sentences
- awkward aliases
- ambiguous pronouns

B3 must prove complete canonical-sentence coverage.

## Independent final auditors

10B1 = knowledge
10B2 = claims/certainty
10B3 = naturalness/redundancy

They must:
- run in separate fresh execution contexts for verified isolation;
- read only allowed inputs;
- hash every actual input;
- bind to the exact final candidate bytes.

If final text changes after any B audit, all three audits are stale and must be rerun.

## Final integrity counters

10D recomputes rather than trusts:

knowledge:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved
- silently_ignored_candidates
- invalid_baseline_provenance

claims:
- missing_claim_sentence_rows
- unconserved_claims
- unresolved_claims
- invalid_evidence_links

terminology:
- unnecessary_labels
- alias_overload

narrative:
- redundant_reveals
- high_load_listening_blocks

factual:
- unsupported_claims
- certainty_overstatements
- unsupported_temporal_generalizations
- scope_overstatements

naturalness:
- translationese_flags
- repeated_rhetorical_patterns
- unresolved_audio_density_flags
- unresolved_naturalness_findings

proof:
- schema_failures
- hash_failures
- stale_audit_failures
- sentence_coverage_failures
- candidate_conservation_failures
- claim_conservation_failures
- finding_conservation_failures
- temporal_proof_failures
- isolation_failures

## Final status

10_final_integrity.json must include:
- recomputable proof records;
- summary counters;
- content_integrity_status;
- isolation_status;
- proof_verifier_status;
- project_status.

PASS_VERIFIED only when every hard gate passes and isolation is VERIFIED.
