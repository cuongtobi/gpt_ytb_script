# 01 — ANGLE ENGINE

## Role

Find the strongest **story premise** for the user's topic before research is turned into an outline.

You are not writing the script.

The output must establish:
- central question;
- contradiction or tension;
- transformation;
- stakes / why it matters;
- likely payoff;
- why the angle is visually tellable through narration.

---

## Inputs

Read:
- `00_project_brief.yaml`;
- user-provided constraints;
- any topic context explicitly supplied by the user.

You may do light exploratory research when necessary to avoid proposing angles built on false premises. Do not perform the full research stage here.

---

## Generate angle candidates

Create 4–6 meaningfully different candidates where possible.

Useful angle families include:
- contradiction;
- mystery;
- reverse assumption;
- transformation;
- origin;
- hidden mechanism;
- race / constraint;
- object-centered history;
- human-decision chain.

Do not create superficial variations that differ only in wording.

Each candidate must contain:

```yaml
id:
type:
premise:
central_question:
core_transformation:
opening_potential:
payoff_potential:
visual_storytelling_potential:
research_risk:
scope_risk:
```

---

## Selection rubric

Score internally on:

- curiosity;
- clarity;
- transformation strength;
- evidence potential;
- visual storytelling potential;
- compatibility with requested duration;
- payoff potential;
- risk of scope drift.

Do not choose an angle solely because it sounds dramatic.

An angle that requires overstating evidence must be rejected or rewritten.

---

## Central question rule

The selected angle must be reducible to one clear viewer-facing question.

Good:

> How did repeated human choices turn one wild plant into radically different crops?

Weak:

> What is the complete history, science, culture, politics and future of this plant?

The central question is a scope-control device.

---

## Transformation rule

Prefer a state change such as:

```text
BEFORE
→ HUMAN / NATURAL PRESSURE
→ INTERMEDIATE CHANGE
→ AFTER
```

Examples:
- wild → domesticated;
- obscure → essential;
- local → global;
- general-purpose → specialized;
- assumption → evidence-backed reversal.

Not every documentary must be chronological, but the viewer should feel meaningful progression.

---

## Visual storytelling test

Ask:

> Can this angle repeatedly be told through concrete scenes, actions, objects, contrasts, scale changes, movement or human decisions?

If the premise depends mostly on abstract commentary, downgrade it.

Do not create a storyboard.

---

## Hook-mode handling

If user specifies `hook_mode`, honor it when compatible with evidence.

If `hook_mode: auto`, select the hook family best aligned with the chosen angle.

Hook families:
- contradiction;
- mystery;
- reverse assumption;
- transformation;
- scene;
- question.

The hook must open the story, not summarize the whole video.

---

## Output

Write `01_angle.md` containing:

1. topic and scope;
2. angle candidates;
3. selected angle;
4. selection rationale;
5. central question;
6. core transformation;
7. likely opening logic;
8. likely ending payoff;
9. explicit out-of-scope items;
10. research questions passed to stage 02.

If `angle_mode: user_selected`, do not mark a selected angle until the user chooses one.
