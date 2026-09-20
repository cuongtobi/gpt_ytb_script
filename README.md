# GPT YouTube Visual-Storytelling Script Pipeline

Pipeline viết YouTube documentary script trên ChatGPT Web + GitHub, tập trung vào:
- research chắc;
- visual storytelling ngay trong narration;
- dễ hiểu với khán giả phổ thông;
- retention;
- ngôn ngữ tự nhiên;
- fact-check;
- knowledge grounding theo đúng thứ tự người xem nghe.

## Pipeline v3

USER INPUT
→ 00 ORCHESTRATOR
→ 01 ANGLE ENGINE
→ 02 DEEP RESEARCH
→ 03A CORE SUBJECT GROUNDING
→ 03B CLAIM MAP + AUDIENCE KNOWLEDGE GRAPH
→ 04 STORY + KNOWLEDGE ARCHITECT
→ 05 VISUAL NARRATIVE WRITER
→ 05B BLIND KNOWLEDGE DISCOVERY
→ 06 AUDIENCE KNOWLEDGE CLOSURE
→ 07 RETENTION + KNOWLEDGE DELTA
→ 08 ANTI-AI + KNOWLEDGE DELTA
→ 09 FACT CHECK + KNOWLEDGE DELTA
→ 10A FINAL STORY EDITOR
→ 10B BLIND FINAL KNOWLEDGE AUDIT
→ 10C FINAL TEMPORAL KNOWLEDGE CLOSURE
→ FINAL SCRIPT

## V3 giải quyết vấn đề gì?

Pipeline cũ có thể giải thích thuật ngữ nhưng vẫn bỏ sót:
- chủ đề trung tâm chưa được giải thích;
- tên khoa học/alias chưa map;
- component như THC xuất hiện trước khi biết nó là gì;
- definition sinh dependency mới;
- concept được giải thích quá muộn;
- final script có jargon mà graph cũ không phát hiện.

V3 chuyển từ Concept Graph sang Audience Knowledge Graph.

Nó quản lý:
- CORE_ENTITY
- ENTITY
- ALIAS
- COMPONENT
- PROPERTY
- PROCESS
- MECHANISM
- CONCEPT
- EVIDENCE_TYPE
- CLASSIFICATION
- RELATIONSHIPS

## Core Subject Grounding

Biết tên chủ đề không có nghĩa là hiểu chủ đề.

Ví dụ với "cần sa", pipeline phải xác định tối thiểu:
- đây là loại thứ gì;
- bộ phận/tính chất nào quan trọng với câu chuyện;
- Cannabis / Cannabis sativa liên hệ với "cần sa" thế nào;
- marijuana có phải alias chính xác hay chỉ là label liên quan;
- THC nằm ở đâu trong mental model.

## Alias Resolution

Không tự coi các tên khác nhau là đồng nghĩa.

Các relation có thể gồm:
- ALIAS_OF
- SHORT_FORM_OF
- RELATED_TO
- SUBTYPE_OF

Label chỉ được dùng tự do sau khi relation được grounding.

## Strict KNOWN rule

Một concept không được tự động đánh KNOWN chỉ vì nghe quen.

BASELINE_KNOWN chỉ hợp lệ nếu:
- nằm trong audience baseline; hoặc
- là normal-language primitive theo baseline.

Scientific name, acronym, biochemical term và specialist term không được auto-known.

## Temporal Knowledge Closure

Một concept phải được grounding trước hoặc ngay lúc first use.

Sai:
genome xuất hiện ở hook → 3 phút sau mới định nghĩa.

Đúng:
toàn bộ thông tin di truyền của cây — tức genome → sau đó dùng genome.

## Blind Knowledge Discovery

Đây là lớp chống false PASS.

05B và 10B chỉ đọc:
- audience profile;
- current script;
- shared protocol.

Chúng KHÔNG đọc Knowledge Graph trước.

Sau đó stage closure mới reconcile blind inventory với graph.

Nhờ vậy nếu final script có:
- enzyme;
- áp lực chọn lọc;
- silica;
- marijuana;

mà graph cũ quên, blind auditor vẫn phải phát hiện.

## Final Knowledge Gate

Pipeline chỉ PASS khi tất cả bằng 0:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved

## Artifact chính

projects/<project_slug>/

- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 02_sources.json
- 03_core_subject.json
- 03_claim_map.json
- 03_knowledge_graph.json
- 04_story_architecture.md
- 05_script_draft.md
- 05_blind_knowledge_inventory.json
- 06_audience_report.md
- 06_knowledge_closure.json
- 06_script_accessible.md
- 07_retention_report.md
- 07_knowledge_delta.json
- 07_script_retention_edit.md
- 08_anti_ai_report.md
- 08_knowledge_delta.json
- 08_script_natural.md
- 09_fact_check.md
- 09_knowledge_delta.json
- 09_script_fact_checked.md
- 10_story_report_draft.md
- 10_final_candidate.md
- 10b_blind_knowledge_inventory.json
- 10_final_story_report.md
- 10_knowledge_closure.json
- 10_final_script.md

## Cách sử dụng trên ChatGPT Web

### Prompt mẫu — copy toàn bộ block

~~~text
@GitHub làm việc với repo cuongtobi/gpt_ytb_script
@Tìm kiếm trên mạng

Viết một YouTube documentary script mới.

topic: cách con người thuần hóa cần sa
language: tiếng Việt
duration: 25 minutes
audience: general
hook_mode: contradiction

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy toàn bộ pipeline.
Tạo một project mới trong projects/ và lưu mọi artifact vào đó.
~~~

## Input

Bắt buộc:
- topic
- language
- duration

Tùy chọn:
- audience: general
- hook_mode: auto
- angle_mode: auto
- research_depth: deep
- technical_level: accessible
- tone: conversational_documentary

## Output dùng để sản xuất

projects/<project_slug>/10_final_script.md

Không chứa storyboard, shot list, image prompt, B-roll direction, camera direction hoặc visual timeline.

## Shared protocol

Source of truth cho knowledge grounding:

prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md

Legacy:
prompts/CONCEPT_CLOSURE_PROTOCOL.md chỉ dành cho project v2 cũ.
