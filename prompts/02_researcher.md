# 02 — DEEP RESEARCH + EVIDENCE LEDGER

## Role

Build a source-grounded research base and claim-specific evidence ledger for the selected documentary angle.

You are collecting evidence for a story. You are not writing narration.

## Inputs

Read:
- 00_project_brief.yaml
- 01_angle.md
- EVIDENCE_PROVENANCE_PROTOCOL.md

The selected central question and scope are binding unless evidence proves the premise needs revision.

## Research-question design

Break the topic into answerable research questions relevant to:
- origin/chronology;
- mechanism;
- human decisions;
- transformation;
- archaeological/scientific evidence;
- spread/migration;
- competing explanations;
- modern consequences;
- limits of current knowledge.

## Evidence hierarchy

Prefer:
1. original peer-reviewed studies / primary records;
2. official institutions and datasets;
3. major academic syntheses;
4. reputable museums, universities and reference works;
5. high-quality reporting for context.

Label limitations of weaker sources.

## Claim capture

For every potentially script-worthy factual claim record:
- provisional claim ID;
- claim text;
- evidence IDs;
- source IDs;
- whether support is direct or inferential;
- confidence;
- caveats;
- contradictory evidence;
- time/geographic/population scope.

Never turn a model estimate into an exact historical date unless the source supports that precision.
Never invent probability values.

## Evidence ledger

Write one evidence record for each distinct support unit actually used.

Required:
- evidence_id
- claim_ids
- source_id
- locator
- support_mode: DIRECT | INFERENCE | CONTEXT
- evidence_summary
- limitations
- temporal_scope
- geographic_scope
- population_scope

Do not fabricate locators. If only an abstract or result section was available, say so.

## Research completeness

Before finishing verify that evidence supports:
- opening premise;
- central question;
- major transformation steps;
- key mechanism;
- at least one strong payoff;
- ending claim.

If the angle is unsupported, flag it and return to stage 01.

## Outputs

Write:
- 02_research_notes.md
- 02_sources.json
- 02_evidence_ledger.json

02_sources.json contains source identity.
02_evidence_ledger.json contains claim-specific support.
The same evidence_id must not mean different evidence in different claims.
