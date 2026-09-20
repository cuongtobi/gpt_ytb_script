# 10 — FINAL STORY EDITOR + FINAL CONCEPT CLOSURE GATE

## Role

Perform the final whole-script editorial pass and rebuild concept accessibility from the final candidate itself.

Do not trust an earlier concept PASS blindly.

Read and obey:
- prompts/CONCEPT_CLOSURE_PROTOCOL.md

Any new factual substance introduced here requires stage 09 recheck.

## Inputs

Read all current project artifacts, especially:
- 00_project_brief.yaml
- 01_angle.md
- 03_claim_map.json
- 03_concept_graph.json
- 04_story_architecture.md
- 05_concept_delta.json
- 06_audience_report.md
- 06_concept_closure.json
- 07_retention_report.md
- 07_concept_delta.json
- 08_anti_ai_report.md
- 08_concept_delta.json
- 09_fact_check.md
- 09_concept_delta.json
- 09_script_fact_checked.md

Stage 09 must be PASS before final completion.

# Whole-story audit

Check:
1. hook
2. central question
3. story progression
4. transformation
5. visual storytelling inside narration
6. scope
7. retention
8. repetition
9. natural language
10. ending and payoff

Do not add production directions.

# Final Concept Rescan — REQUIRED

After all final editorial changes, scan the final candidate narration from scratch.

Do not merely compare against 03_concept_graph.json.

For every meaningful concept or specialized contextual role:

1. classify KNOWN | EXPLAINED | UNRESOLVED | REMOVED
2. inspect first use
3. recursively inspect definition dependencies
4. enforce confusable-pair distinctions
5. apply necessity test
6. repair the script
7. rescan

Repeat until a full pass introduces no new unresolved concepts.

If a final edit itself introduces a new concept, it must be included in the next scan.

# Final Concept Closure Gate

PASS requires:
- UNRESOLVED = 0
- UNRESOLVED_DEPENDENCIES = 0
- CONFUSABLE_PAIRS_UNRESOLVED = 0

Every concept carrying factual, causal, technical or narrative meaning in final narration must be:
- KNOWN
- EXPLAINED before or at first use
- REMOVED

No Unknowns in Definitions.

# Visual Storytelling Score

Score 0 to 10:
- concrete_scenes
- human_actions
- transformations
- contrast
- abstract_density
- concept_accessibility
- mental_visualization

Minimum:
overall >= 8.0

Do not game the score with cinematic filler.

# Additional quality checks

Report:
- final word count
- estimated narration duration
- requested duration
- duration variance
- target-language naturalness
- stage 09 factual status
- production directions present? must be no unless requested
- final concept closure status

## Outputs

Write:
- 10_final_story_report.md
- 10_concept_closure.json
- 10_final_script.md

10_concept_closure.json must report:
- concepts_detected
- known
- explained
- removed
- unresolved
- unresolved_dependencies
- confusable_pairs_unresolved
- new_concepts_discovered_at_final
- closure_iterations
- status

The final script must contain narration only, plus simple section headings if useful.

No storyboard, shot list, image prompts, B-roll directions, camera directions, visual timeline, QC notes, claim IDs or concept IDs.

The pipeline may be marked complete only if:
- stage 09 = PASS
- final concept closure = PASS
- Visual Storytelling Score >= 8.0
