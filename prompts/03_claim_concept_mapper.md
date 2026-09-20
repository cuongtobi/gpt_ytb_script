# 03 — CLAIM MAP + CONCEPT MAP

## Role

Convert research into two control layers before script writing:

1. **Claim Map** — what the script may safely assert.
2. **Concept Map** — what the audience must understand and how to introduce it.

You are not writing the documentary prose.

---

# Part A — Claim Map

## Inputs

Read:
- `00_project_brief.yaml`;
- `01_angle.md`;
- `02_research_notes.md`;
- `02_sources.json`.

---

## Claim record

Each important factual claim should include:

```yaml
claim_id:
claim:
category:
importance: core|supporting|optional
confidence: high|medium|low
support_type: direct|inference|contested
source_ids: []
safe_wording:
unsafe_wording:
caveats:
visual_potential: very_high|high|medium|low
story_function:
```

### Safe wording

Safe wording must match source certainty.

Examples:

Source says:
> evidence suggests...

Allowed:
> evidence suggests...

Not allowed:
> scientists proved...

Source gives a range:
> approximately 9,000–12,000 years...

Do not silently convert to:
> exactly 12,000 years.

---

## Unsupported specificity

Flag:
- unsupported percentages;
- unsupported probabilities;
- exact dates derived from broad ranges;
- causal wording from correlational evidence;
- “first ever” / “only” / “all” claims without strong support;
- global generalizations from limited samples.

---

## Claim output

Write `03_claim_map.json`.

---

# Part B — Concept Map

## Goal

A general-audience viewer should never need to know a term before the narration teaches the idea behind that term.

If the viewer can understand the story without the technical term, do not force them to learn it.

---

## Concept discovery

Extract concepts that may be unfamiliar, abstract or cognitively expensive.

Examples:
- domain-specific terminology;
- acronyms;
- scientific mechanisms;
- historical institutions;
- technical processes;
- specialist classifications;
- unfamiliar measurement concepts.

Do not treat every proper noun as a “concept”.

---

## Concept record

For each relevant concept:

```yaml
concept_id:
name:
audience_familiarity: high|medium|low|very_low
importance: core|supporting|optional
technical_term_required: true|false
plain_language_meaning:
first_use_strategy:
best_explanation_type:
mental_model:
reuse_policy:
confusable_with:
avoid_explanation:
```

Allowed `best_explanation_type` values:

```text
direct_definition
analogy
human_action
contrast
mechanism
example
```

---

## Concept Introduction Protocol

Use this decision order:

```text
Does the viewer need the technical label?
   ↓ no
Use plain language only.

   ↓ yes

Does the viewer already have a usable mental model?
   ↓ no
Teach via action / analogy / contrast / mechanism.

   ↓

State the plain-language idea.

   ↓

Introduce the technical label.

   ↓

Later uses may use the label alone,
unless a long gap requires a micro-reminder.
```

---

## Action-before-label preference

For processes, prefer action before terminology.

Instead of:

> Artificial selection changed the population.

Prefer the underlying idea:

> People repeatedly kept seeds from individuals with the traits they wanted.

Only then, if useful:

> That process is artificial selection.

---

## Concept load planning

Estimate where concept clusters are likely to occur.

Flag any planned segment that would require the audience to hold too many unfamiliar concepts at once.

Default heuristic:
- roughly 1–2 important new concepts per minute;
- not a hard limit;
- exceeding it requires justification or simplification.

---

## Concept output

Write `03_concept_map.json`.

Include:
- all tracked concepts;
- likely high-load clusters;
- concepts intentionally removed from narration;
- concepts that must be explained before first label use.
