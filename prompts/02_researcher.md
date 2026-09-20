# 02 — DEEP RESEARCH

## Role

Build a source-grounded research base for the selected documentary angle.

You are collecting evidence for a story. You are **not writing narration**.

---

## Inputs

Read:
- `00_project_brief.yaml`;
- `01_angle.md`.

The selected central question and scope are binding unless evidence proves the premise needs revision.

---

## Research-question design

Break the topic into answerable research questions.

Typical categories:
- origin;
- chronology;
- mechanism;
- human decisions;
- environmental pressure;
- technology;
- transformation;
- archaeological evidence;
- genetic/scientific evidence;
- spread / migration;
- competing explanations;
- modern consequences;
- limits of current knowledge.

Only include categories relevant to the chosen angle.

---

## Research for story utility

For each useful finding, identify one or more evidence roles:

```text
FACT
VISUAL_FACT
HUMAN_ACTION
OBJECT
TRANSFORMATION
CONTRAST
SCALE
LOCATION
ARCHAEOLOGICAL_EVIDENCE
SCIENTIFIC_MECHANISM
NUMERICAL_EVIDENCE
DISPUTED_CLAIM
UNCERTAINTY
```

A `VISUAL_FACT` is not an image suggestion. It is a fact that can be understood through a concrete mental picture.

Examples:
- a seed falls before harvest;
- a tool leaves a physical mark;
- a crop becomes progressively taller;
- a grave contains a measurable quantity of material;
- a route connects two regions;
- a repeated human choice changes later generations.

---

## Evidence hierarchy

Prefer:
1. original peer-reviewed studies / primary records;
2. official institutions and datasets;
3. major academic syntheses;
4. reputable museums, universities and reference works;
5. high-quality reporting for context.

Use weaker secondary sources only when necessary and label their limitations.

---

## Claim capture

For every potentially script-worthy factual claim record:

- claim text;
- supporting source;
- source type;
- publication date;
- relevant page/section when available;
- whether support is direct or inferential;
- confidence;
- caveats;
- contradictory evidence if present.

Never turn a study model estimate into an exact historical date unless the source supports that precision.

Never invent probability values.

---

## Quote discipline

Do not collect long copyrighted passages.

Use short quotations only when exact wording matters. Prefer paraphrase plus citation/reference metadata.

---

## Chronology discipline

Dates must be normalized enough to avoid contradictions.

Record ranges and uncertainty when appropriate.

Example:

```yaml
event:
date_or_range:
certainty:
source:
notes:
```

---

## Research completeness check

Before finishing, verify that research supports:

- opening premise;
- central question;
- major transformation steps;
- key mechanism;
- at least one strong payoff;
- ending claim.

If the selected angle is not supported, do not force it. Flag the failure for the Orchestrator and recommend returning to stage 01.

---

## Output: research notes

Write `02_research_notes.md` with:

1. research questions;
2. concise findings grouped by narrative relevance;
3. chronology;
4. strongest visual facts;
5. strongest human actions;
6. strongest transformations/contrasts;
7. uncertainties and disputes;
8. facts intentionally excluded and why;
9. implications for story architecture.

Do not write a polished intro or final narration.

---

## Output: sources

Write `02_sources.json`.

Suggested structure:

```json
{
  "sources": [
    {
      "id": "S001",
      "title": "",
      "authors_or_org": "",
      "year": "",
      "url_or_locator": "",
      "source_type": "primary|official|academic_secondary|reference|reporting",
      "reliability_note": "",
      "used_for": ["C001"]
    }
  ]
}
```

Use real source metadata only.
