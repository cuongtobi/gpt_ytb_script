# AGENTS.md

## Repository purpose

Prompt-native pipeline for research-driven YouTube documentary narration with:
- strong visual storytelling;
- audience knowledge grounding;
- terminology pruning;
- retention/reveal integrity;
- natural spoken language;
- claim-strength control;
- independent final audits.

Runs on ChatGPT Web + GitHub.

## Source of truth

For new projects:
1. Read AGENTS.md.
2. Read prompts/00_orchestrator.md.
3. Read prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md.
4. Read prompts/FINAL_INTEGRITY_PROTOCOL.md.
5. Follow stage prompts in order.
6. Persist all required artifacts.
7. Final production artifact is 10_final_script.md.

## Pipeline v3.1

00 Orchestrator
→ 01 Angle
→ 02 Research
→ 03A Core Subject
→ 03B Claim Map + Knowledge Graph
→ 04 Story + Knowledge Architect
→ 05 Writer
→ 05B Two-Pass Blind Knowledge Discovery
→ 06 Knowledge Closure
→ 06B Terminology Necessity Pruner
→ 07 Retention + Reveal Audit
→ 08 Naturalness + Rhythm + Listening
→ 09 Fact Check + Claim Strength
→ 10A Final Story Editor
→ 10B1 Blind Knowledge Audit
→ 10B2 Blind Claim Audit
→ 10B3 Blind Naturalness Audit
→ 10C Final Integrity Reconciliation

## Non-goals

Unless explicitly requested, do not create:
- storyboard
- shot list
- image prompts
- B-roll plan
- camera directions
- visual/editing timeline
- video-generation prompts

Visual storytelling belongs inside narration.

## Core rules

### Story before prose
Architecture first.

### Core subject before specialized claims
Familiar label != subject understanding.

### Strict KNOWN
No inferred BASELINE_KNOWN.

### No Unknowns in Explanations
Definitions cannot depend on unresolved knowledge.

### Temporal closure
Ground before/at first use.

### No Silent Ignore
Every lexical knowledge candidate receives a disposition.

### Terminology must earn its place
A label that can be replaced and is not needed later should be removed.

### Alias budget
Prefer one primary spoken label per core entity.

### Reveal integrity
Do not fully explain the same claim/evidence twice without distinct story function.

### Claim strength
Do not exceed source certainty, time, geography or population scope.

### Natural spoken language
Understandable is not enough; narration must sound natural when heard once.

### Independent blind final audits
Knowledge, claims and naturalness are extracted independently before reconciliation.

## Blind-stage isolation

05B cannot read the Knowledge Graph.

10B1 cannot read the Knowledge Graph or prior closure.

10B2 cannot read Claim Map/sources before extraction.

10B3 cannot read retention/anti-AI/naturalness reports.

## Completion

Final source of truth for v3.1:
- 10_final_integrity.json

Do not claim complete unless:
- stage 09 PASS;
- final integrity PASS;
- all integrity counts = 0;
- story QC PASS;
- duration reasonable;
- final script exists.

## Legacy

v3 projects may use:
- 10_knowledge_closure.json

v3.1 replaces final source of truth with:
- 10_final_integrity.json

v1/v2 schemas are legacy regression fixtures.
