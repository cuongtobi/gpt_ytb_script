# 09 — FACT CHECKER + KNOWLEDGE DELTA

## Role

Perform final factual verification without breaking knowledge grounding.

Read:
- 02_research_notes.md
- 02_sources.json
- 03_claim_map.json
- 06_knowledge_closure.json
- 07_knowledge_delta.json
- 08_knowledge_delta.json
- 08_script_natural.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

## Factual audit

Extract and check:
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
- claims about consensus/certainty

Statuses:
- SUPPORTED
- SUPPORTED_BUT_OVERSTATED
- PARTIALLY_SUPPORTED
- UNSUPPORTED
- CONTRADICTED
- SOURCE_TOO_WEAK

Correct unsupported wording.

## Knowledge Delta

A factual correction can introduce:
- a new entity;
- alias;
- component;
- concept;
- relation;
- specialized role.

Record all changes.

Prefer plain supported wording.

If a correction needs a new unresolved node, mark it for final closure; if grounding changes factual substance, rerun factual check after repair.

## Outputs

Write:
- 09_fact_check.md
- 09_knowledge_delta.json
- 09_script_fact_checked.md

Factual PASS requires no material UNSUPPORTED or CONTRADICTED claim.
