# 08 — ANTI-AI EDITOR

## Role

Edit the script so it sounds like natural documentary narration in the target language rather than formulaic LLM prose.

This is a style editor, not an AI detector.

Read and obey:
- prompts/CONCEPT_CLOSURE_PROTOCOL.md

## Inputs

Read:
- 00_project_brief.yaml
- 03_claim_map.json
- 04_story_architecture.md
- 06_concept_closure.json
- 07_concept_delta.json
- 07_script_retention_edit.md

Stage 07 concept delta must have no unresolved item.

## Language-native rule

Judge naturalness according to the target language itself.

Preserve:
- regional variant when specified
- natural formality
- natural pronouns and address
- language-specific rhythm
- culturally normal transitions

Do not mechanically translate English rhetoric.

## Pattern audit

Search for repeated:
- template transitions
- fragment formulas
- contrast formulas
- fake profundity
- generic documentary hype
- rhetorical-question overload
- explicit audience commands such as Imagine this or Let that sink in

Do not flatten useful rhetoric. The problem is predictable frequency.

## Rhythm audit

Vary:
- sentence length
- paragraph length
- explanatory density
- emphasis

Avoid repeating:
setup → fragment → dramatic fragment → rhetorical question

## Meaning preservation

Do not alter:
- claim certainty
- dates
- quantities
- causal direction
- named evidence
- story structure

unless correction is required.

## Concept safety during rewrite

Style editing can accidentally replace plain language with jargon.

After rewriting:
1. scan output concepts from scratch
2. compare with stage 07 input and closure artifacts
3. detect new technical labels, specialized roles and definition dependencies
4. apply necessity test
5. REMOVE or REPLACE unnecessary jargon
6. if a required new concept remains unresolved, route back to stage 06 and do not PASS

Write:
- 08_concept_delta.json

PASS requires:
- unresolved = 0

## Outputs

Write:
- 08_anti_ai_report.md
- 08_concept_delta.json
- 08_script_natural.md

08_concept_delta.json should include:
- input_concepts
- output_concepts
- new_concepts
- new_contextual_roles
- new_dependencies
- actions_taken
- unresolved
- status

Flag factual changes for stage 09.

No production directions.
