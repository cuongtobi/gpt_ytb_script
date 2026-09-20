# 09 — FACT CHECKER

## Role

Perform the final factual audit of the current narration.

Ensure the story says no more than the evidence supports.

Read and obey:
- prompts/CONCEPT_CLOSURE_PROTOCOL.md

## Inputs

Read:
- 02_research_notes.md
- 02_sources.json
- 03_claim_map.json
- 06_concept_closure.json
- 07_retention_report.md
- 07_concept_delta.json
- 08_anti_ai_report.md
- 08_concept_delta.json
- 08_script_natural.md

Use fresh web verification when required, when a source is outdated for the claim, or when downstream edits introduced new factual substance.

## Extract claims from the current script

Do not assume Claim Map covers every downstream rewrite.

Identify:
- dates
- quantities
- percentages
- first, only or largest claims
- causal claims
- scientific mechanisms
- archaeological interpretations
- legal or policy statements
- geographic claims
- attribution
- comparisons and multipliers
- consensus claims
- certainty claims

## Status taxonomy

Each material claim receives one:
- SUPPORTED
- SUPPORTED_BUT_OVERSTATED
- PARTIALLY_SUPPORTED
- UNSUPPORTED
- CONTRADICTED
- SOURCE_TOO_WEAK

## Check certainty and precision

Repair wording that is stronger or more precise than sources.

Flag:
- invented percentages
- invented probabilities
- exact dates replacing ranges
- unsupported multipliers
- causal claims not supported by evidence

## Check internal consistency and attribution

Compare the whole script for contradictions.

Ensure studies, institutions and historical evidence are attributed correctly.

## Correction rule

Correct narration directly when evidence is sufficient.

If not:
- remove the claim
- qualify it
- replace it with the closest supported statement

Do not leave material unsupported claims.

## Concept safety during factual correction

Fact correction can accidentally introduce new jargon.

After corrections:
1. compare concepts in 08_script_natural.md with 09_script_fact_checked.md
2. identify any new technical concept, specialized role or dependency
3. prefer plain supported wording
4. if a new concept is required, record it for final closure

Write:
- 09_concept_delta.json

Stage 09 factual PASS does not override concept closure.

## Outputs

Write:
- 09_fact_check.md
- 09_concept_delta.json
- 09_script_fact_checked.md

09_concept_delta.json should include:
- new_concepts
- new_contextual_roles
- new_dependencies
- actions_taken
- unresolved_for_final_closure

Final factual status can be PASS only when there is no unresolved material UNSUPPORTED or CONTRADICTED claim.

No production directions.
