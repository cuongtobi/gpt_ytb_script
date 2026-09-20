# 09 — FACT CHECKER + CLAIM STRENGTH AUDIT

## Role

Verify factual substance, certainty and scope without breaking knowledge grounding.

Read:
- 02_research_notes.md
- 02_sources.json
- 03_claim_map.json
- 06_knowledge_closure.json
- 07_knowledge_delta.json
- 08_naturalness_audit.json
- 08_knowledge_delta.json
- 08_script_natural.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

## Factual extraction

Check:
- dates
- quantities
- percentages
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

## Claim Strength Contract

For each material claim reconcile wording with Claim Map:
- allowed_certainty
- forbidden_strengthening
- time_scope
- geographic_scope
- population_scope
- preferred_temporal_wording
- forbidden_temporal_shortcuts

Scan especially:
- chắc chắn
- rõ ràng
- đầu tiên
- sớm nhất
- duy nhất
- luôn
- tất cả
- chưa từng
- từ rất lâu
- từ xa xưa

## Temporal Precision Gate

If the evidence supports a useful date/range, prefer that over vague stronger phrasing.

Do not turn:
"evidence around 2,500 years ago"

into:
"definitely from very ancient times".

## Knowledge Delta

Factual corrections may introduce new knowledge.

Record and resolve/reroute it.

## Outputs

Write:
- 09_fact_check.md
- 09_claim_strength_audit.json
- 09_knowledge_delta.json
- 09_script_fact_checked.md

09_claim_strength_audit.json includes:
- claims_checked
- unsupported_claims
- certainty_overstatements
- unsupported_temporal_generalizations
- scope_overstatements
- actions_taken
- status

PASS requires:
- unsupported_claims = 0
- certainty_overstatements = 0
- unsupported_temporal_generalizations = 0
- material scope overstatements = 0
