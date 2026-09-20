# 00 — ORCHESTRATOR

## Role

Control the v3 research-driven YouTube documentary pipeline.

Read:
- AGENTS.md
- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
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

Do not overwrite an existing project unless explicitly requested.

## Pipeline v3

00 Project Brief
→ 01 Angle Engine
→ 02 Deep Research
→ 03A Core Subject Grounding
→ 03B Claim Map + Audience Knowledge Graph
→ 04 Story + Knowledge Architect
→ 05 Visual Narrative Writer
→ 05B Blind Knowledge Discovery
→ 06 Audience Knowledge Closure
→ 07 Retention + Knowledge Delta
→ 08 Anti-AI + Knowledge Delta
→ 09 Fact Check + Knowledge Delta
→ 10A Final Story Editor
→ 10B Blind Final Knowledge Audit
→ 10C Final Temporal Knowledge Closure
→ FINAL SCRIPT

## Blind-stage isolation

05B must receive only:
- 00_project_brief.yaml
- 05_script_draft.md
- shared protocol

10B must receive only:
- 00_project_brief.yaml
- 10_final_candidate.md
- shared protocol

Do not load graph/closure artifacts into blind stages.

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
- pipeline.version: 3.0
- pipeline.status: running

## Research

Use web research when requested, current information matters, or claims require verification.

Preserve uncertainty.

## Knowledge routing

Stage 06 may PASS only when all eight knowledge failure counts are zero.

If stage 07 or 08 introduces unresolved knowledge:
- route current script back to stage 06;
- rerun downstream stages.

If stage 09 introduces unresolved knowledge:
- stage 10C must resolve it;
- if repair changes factual substance, rerun stage 09.

## Final completion gate

Do not mark complete until:
- all required v3 artifacts exist;
- stage 09 factual status = PASS;
- 10_knowledge_closure.json status = PASS;
- all eight knowledge failure counts = 0;
- central question is paid off;
- Visual Storytelling Score >= 8.0;
- duration is reasonably aligned;
- no production directions are present unless requested.

## Required v3 artifacts

00_project_brief.yaml
01_angle.md
02_research_notes.md
02_sources.json
03_core_subject.json
03_claim_map.json
03_knowledge_graph.json
04_story_architecture.md
05_script_draft.md
05_blind_knowledge_inventory.json
06_audience_report.md
06_knowledge_closure.json
06_script_accessible.md
07_retention_report.md
07_knowledge_delta.json
07_script_retention_edit.md
08_anti_ai_report.md
08_knowledge_delta.json
08_script_natural.md
09_fact_check.md
09_knowledge_delta.json
09_script_fact_checked.md
10_story_report_draft.md
10_final_candidate.md
10b_blind_knowledge_inventory.json
10_final_story_report.md
10_knowledge_closure.json
10_final_script.md
