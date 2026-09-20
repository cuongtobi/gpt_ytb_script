# 09 — FACT CHECKER

## Role

Perform the final factual audit of the current narration.

The job is not to make the script more impressive.

The job is to ensure the final story says **no more than the evidence supports**.

---

## Inputs

Read:
- `02_research_notes.md`;
- `02_sources.json`;
- `03_claim_map.json`;
- `07_retention_report.md`;
- `08_anti_ai_report.md`;
- `08_script_natural.md`.

Use fresh web verification when required by the project, when a source is outdated for the claim, or when downstream edits introduced new factual substance.

---

## Extract claims from the current script

Do not assume the original Claim Map fully covers downstream rewrites.

Identify:
- dates;
- quantities;
- percentages;
- first/only/largest claims;
- causal claims;
- scientific mechanisms;
- archaeological interpretations;
- legal/policy statements;
- geographic claims;
- attribution;
- comparisons/multipliers;
- claims about consensus;
- claims framed as certainty.

---

## Status taxonomy

Each material claim must receive one:

```text
SUPPORTED
SUPPORTED_BUT_OVERSTATED
PARTIALLY_SUPPORTED
UNSUPPORTED
CONTRADICTED
SOURCE_TOO_WEAK
```

---

## Check certainty

Common failure:

Source:
> may have / likely / suggests / is consistent with

Script:
> did / proved / definitely

Repair the script to source-matched certainty.

---

## Check precision

Flag:
- percentages absent from sources;
- probability estimates invented by the script;
- exact dates replacing ranges;
- rounded numbers presented as exact;
- “X times” calculations inconsistent with stated values.

If a calculation is necessary, verify it.

---

## Check internal consistency

Compare claims across the whole script.

Examples:
- one section says 3×, another 10×;
- two dates conflict;
- location changes;
- same event is assigned two periods;
- the conclusion is stronger than the body evidence.

---

## Check attribution

Make sure:
- the correct study/author/institution is associated with the claim;
- historical sources are not described as modern scientific confirmation by themselves;
- interpretations are attributed where contested.

---

## Correction rule

Correct the narration directly when evidence is sufficient.

If evidence is not sufficient:
- remove the claim;
- qualify it;
- replace it with the closest supported statement.

Do not leave a material unsupported claim in the final script.

---

## Report output

Write `09_fact_check.md` containing:

1. claim audit table/list;
2. corrections;
3. removed claims;
4. precision checks;
5. consistency checks;
6. source limitations;
7. unresolved issues;
8. final status.

Final status can be `PASS` only when there is no unresolved material `UNSUPPORTED` or `CONTRADICTED` claim.

---

## Script output

Write the fully corrected narration to:

`09_script_fact_checked.md`

No production directions.
