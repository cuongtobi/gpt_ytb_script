# 00 — ORCHESTRATOR

## Role

Control the v3.1 research-driven YouTube documentary pipeline.

Read:
- AGENTS.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md
- this file

## Input

Required:
- topic
- language
- duration

Defaults:
- audience: general
- hook_mode: auto
- angle_mode: auto
- research_depth: deep
- technical_level: accessible
- tone: conversational_documentary

## Project

Create:
projects/YYYY-MM-DD_topic-slug/

Never overwrite an old project unless explicitly requested.

## Pipeline v3.1

00 Project Brief
→ 01 Angle Engine
→ 02 Deep Research
→ 03A Core Subject Grounding
→ 03B Claim Map + Audience Knowledge Graph
→ 04 Story + Knowledge Architect
→ 05 Visual Narrative Writer
→ 05B Two-Pass Blind Knowledge Discovery
→ 06 Audience Knowledge Closure
→ 06B Terminology Necessity Pruner
→ 07 Retention + Reveal Integrity + Knowledge Delta
→ 08 Naturalness + Rhythm + Listening + Knowledge Delta
→ 09 Fact Check + Claim Strength + Knowledge Delta
→ 10A Final Story Editor
→ 10B1 Blind Final Knowledge Audit
→ 10B2 Blind Final Claim/Certainty Audit
→ 10B3 Blind Final Naturalness/Redundancy Audit
→ 10C Final Integrity Reconciliation
→ FINAL SCRIPT

## Blind isolation

### 05B
Allowed only:
- 00_project_brief.yaml
- 05_script_draft.md
- shared protocols

Must not read graph/closure artifacts.

### 10B1
Allowed only:
- 00_project_brief.yaml
- 10_final_candidate.md
- shared protocols

### 10B2
Allowed only:
- 00_project_brief.yaml
- 10_final_candidate.md
- FINAL_INTEGRITY_PROTOCOL.md

Must not read Claim Map/sources before extraction.

### 10B3
Allowed only:
- 00_project_brief.yaml
- 10_final_candidate.md
- FINAL_INTEGRITY_PROTOCOL.md

Must not read retention/anti-AI/naturalness reports.

## Project brief

Write 00_project_brief.yaml with:
- topic
- language
- locale
- duration_minutes
- target_word_range
- audience
- technical_level
- tone
- hook_mode
- angle_mode
- visual_storytelling: true
- research settings
- pipeline.version: 3.1
- pipeline.status: running

## Routing

Stage 06 fails if any knowledge failure count > 0.

Stage 06B fails if:
- unnecessary_labels > 0
- alias_overload > 0

Stage 07 fails if:
- redundant_reveals > 0
- unresolved knowledge delta exists

Stage 08 fails if naturalness/listening counts remain > 0.

Stage 09 fails on unsupported/overstated claims.

If downstream edits introduce unresolved knowledge:
route back to stage 06/06B.

If final factual repair changes substance:
rerun stage 09.

After any final candidate repair:
rerun all three blind final auditors.

## Required v3.1 artifacts

00_project_brief.yaml
01_angle.md
02_research_notes.md
02_sources.json
03_core_subject.json
03_claim_map.json
03_knowledge_graph.json
04_story_architecture.md
05_script_draft.md
05_lexical_knowledge_sweep.json
05_blind_knowledge_inventory.json
06_audience_report.md
06_knowledge_closure.json
06_script_accessible.md
06_terminology_prune.json
06_script_pruned.md
07_retention_report.md
07_reveal_audit.json
07_knowledge_delta.json
07_script_retention_edit.md
08_anti_ai_report.md
08_naturalness_audit.json
08_knowledge_delta.json
08_script_natural.md
09_fact_check.md
09_claim_strength_audit.json
09_knowledge_delta.json
09_script_fact_checked.md
10_story_report_draft.md
10_final_candidate.md
10b1_blind_knowledge_inventory.json
10b2_blind_claim_inventory.json
10b3_blind_naturalness_audit.json
10_final_story_report.md
10_final_integrity.json
10_final_script.md

## Final completion

Do not mark complete until:
- all required artifacts exist;
- stage 09 factual PASS;
- 10_final_integrity.json status = PASS;
- every Final Integrity count = 0;
- central question paid off;
- Visual Storytelling Score >= 8.0;
- duration reasonably aligned;
- no production directions unless requested.
