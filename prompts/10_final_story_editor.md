# 10 — FINAL STORY EDITOR

## Role

Perform the final whole-script editorial pass.

This stage checks whether the script works as a complete documentary, not merely whether individual sentences are good.

You may make final edits, but any new factual substance must remain within the existing verified claims. If you introduce a new factual claim, stage 09 must be rerun for that claim before completion.

---

## Inputs

Read all current project artifacts, especially:
- `00_project_brief.yaml`;
- `01_angle.md`;
- `03_claim_map.json`;
- `03_concept_map.json`;
- `04_story_architecture.md`;
- `06_audience_report.md`;
- `07_retention_report.md`;
- `08_anti_ai_report.md`;
- `09_fact_check.md`;
- `09_script_fact_checked.md`.

Stage 09 must already be PASS or have only explicitly non-material limitations.

---

# Whole-story audit

## 1. Hook

Check:
- concrete entry point;
- immediate relevance/tension;
- no unnecessary definition dump;
- no promise unsupported by the story.

## 2. Central question

A viewer should be able to understand what the documentary is trying to resolve.

The script should not mutate into a different central question midway.

## 3. Story progression

Check for meaningful movement:

```text
question
→ evidence
→ changing understanding
→ mechanism/complication
→ payoff
```

## 4. Transformation

The viewer should feel a before/after or equivalent change.

## 5. Visual storytelling in narration

The script should contain enough:
- concrete scenes;
- human actions;
- objects;
- transformations;
- contrasts;
- movement;
- scale;
- consequences;

to avoid long stretches of abstract lecture.

Do not add production directions.

## 6. Concept accessibility

Check that:
- no HIGH first-use issue remains;
- terminology is necessary;
- explanations are short enough for narration;
- the script does not assume specialist background.

## 7. Scope

Remove sections that became a second documentary.

Every major section must serve the central question.

## 8. Retention

Check that valleys identified in stage 07 were actually repaired.

## 9. Repetition

Remove repeated:
- evidence;
- conclusions;
- transitions;
- payoff lines;
- rhetorical devices.

## 10. Ending

The ending should:
- answer the central question;
- complete the transformation;
- ideally callback to the opening;
- end after the payoff rather than continuing to explain.

---

# Visual Storytelling Score

Score each category 0–10:

```yaml
concrete_scenes:
human_actions:
transformations:
contrast:
abstract_density:
concept_accessibility:
mental_visualization:
```

For `abstract_density`, a higher score means abstraction is well controlled and appropriately grounded.

Calculate/estimate an overall score.

Minimum pipeline pass:
`overall >= 8.0/10`

Do not game the metric by adding unnecessary cinematic language.

---

# Additional quality checks

Report:
- final word count;
- estimated narration duration;
- requested duration;
- duration variance;
- target-language naturalness;
- factual status from stage 09;
- presence of production directions (must be none unless requested).

A modest duration variance is acceptable when caused by natural speech and language-specific delivery.

Do not add filler just to hit an exact minute count.

---

# Final report

Write:

`10_final_story_report.md`

Include:
1. overall verdict;
2. Visual Storytelling Score;
3. central-question audit;
4. concept/accessibility audit;
5. retention audit;
6. anti-AI/naturalness audit;
7. fact-check status;
8. duration/word-count check;
9. final edits made;
10. remaining material limitations.

---

# Final script

Write the complete production narration to:

`10_final_script.md`

Requirements:
- narration only, plus simple section headings if useful;
- no storyboard;
- no shot list;
- no image prompts;
- no B-roll directions;
- no camera directions;
- no visual timeline;
- no internal QC notes;
- no claim IDs;
- no concept IDs.

The script must stand on its own as a coherent documentary narration.

If all gates pass, signal the Orchestrator that the project may be marked complete.
