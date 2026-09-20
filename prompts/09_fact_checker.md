# 09 — FACT CHECKER + CLAIM STRENGTH AUDIT

## Role

Verify factual substance, certainty, scope and evidence provenance without breaking knowledge grounding.

Read:
- 02_research_notes.md
- 02_sources.json
- 02_evidence_ledger.json
- 03_claim_map.json
- 06_knowledge_closure.json
- 07_knowledge_delta.json
- 08_naturalness_audit.json
- 08_knowledge_delta.json
- 08_script_natural.md
- CONTENT_ADDRESSING_PROTOCOL.md
- EVIDENCE_PROVENANCE_PROTOCOL.md
- FINAL_INTEGRITY_PROTOCOL.md

Hash every actual input.

## Factual extraction

Check every material factual commitment:
- dates
- quantities
- causal claims
- scientific mechanisms
- archaeological interpretations
- legal/policy statements
- geographic claims
- attribution
- comparisons
- consensus/certainty
- population scope

Statuses:
- SUPPORTED
- SUPPORTED_BUT_OVERSTATED
- PARTIALLY_SUPPORTED
- UNSUPPORTED
- CONTRADICTED
- SOURCE_TOO_WEAK

Every supported result must cite evidence_ids, not only source_ids.

## Claim Strength Contract

Reconcile wording with Claim Map:
- allowed_certainty
- forbidden_strengthening
- time_scope
- geographic_scope
- population_scope
- preferred_temporal_wording
- forbidden_temporal_shortcuts

## Evidence integrity

For every factual claim checked:
- mapped claim_id must exist;
- evidence_ids must exist in 02_evidence_ledger.json;
- evidence source_id must exist in 02_sources.json.

If script introduces a new material factual commitment not represented by the evidence ledger, reroute to stage 02/03B instead of inventing evidence here.

## Knowledge Delta

Factual corrections may introduce knowledge.
Record and resolve/reroute it.

## Outputs

Write:
- 09_fact_check.md
- 09_claim_strength_audit.json
- 09_knowledge_delta.json
- 09_script_fact_checked.md

JSON artifacts include content_address and script input/output hashes.

PASS requires zero unsupported claims, certainty overstatements, unsupported temporal generalizations, scope overstatements and invalid evidence links.
