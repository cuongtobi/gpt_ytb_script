# GPT YouTube Visual-Storytelling Script Pipeline

Pipeline tạo YouTube documentary narration trên ChatGPT Web + GitHub.

Mục tiêu:
- research chắc;
- visual storytelling trong lời kể;
- dễ hiểu với audience phổ thông;
- không bắt người xem học jargon không cần thiết;
- retention tốt;
- không lặp reveal;
- ngôn ngữ nghe tự nhiên;
- fact-check đúng mức chắc chắn của nguồn;
- final audit độc lập.

## Pipeline v3.1

USER INPUT
→ 00 ORCHESTRATOR
→ 01 ANGLE ENGINE
→ 02 DEEP RESEARCH
→ 03A CORE SUBJECT GROUNDING
→ 03B CLAIM MAP + AUDIENCE KNOWLEDGE GRAPH
→ 04 STORY + KNOWLEDGE ARCHITECT
→ 05 VISUAL NARRATIVE WRITER
→ 05B TWO-PASS BLIND KNOWLEDGE DISCOVERY
→ 06 AUDIENCE KNOWLEDGE CLOSURE
→ 06B TERMINOLOGY NECESSITY PRUNER
→ 07 RETENTION + REVEAL INTEGRITY
→ 08 NATURALNESS + RHYTHM + LISTENING
→ 09 FACT CHECK + CLAIM STRENGTH
→ 10A FINAL STORY EDITOR
→ 10B1 BLIND KNOWLEDGE AUDIT
→ 10B2 BLIND CLAIM AUDIT
→ 10B3 BLIND NATURALNESS AUDIT
→ 10C FINAL INTEGRITY RECONCILIATION
→ FINAL SCRIPT

## V3.1 thêm gì?

### 1. Two-pass Knowledge Discovery

PASS A scan từng câu và tạo lexical candidates.

PASS B kiểm semantic role.

Mọi candidate đều phải được reconcile.

Không còn:
concept xuất hiện → auditor không notice → false PASS.

### 2. No Silent Ignore

Mỗi candidate phải thành:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

Final:
silently_ignored_candidates = 0

### 3. Terminology Necessity Pruner

Một label được giải thích đúng vẫn có thể bị xóa nếu người xem không cần nhớ nó.

Ví dụ:
- scientific alias chỉ dùng một lần nếu đủ;
- Cannabis có thể quay về "cần sa";
- hemp có thể đổi thành "dòng lấy sợi" nếu label không phục vụ reasoning.

### 4. Alias Budget

Mỗi core entity ưu tiên một spoken label chính.

Không luân phiên quá nhiều tên chỉ vì chúng đều đúng.

### 5. Reveal Duplication Gate

Mỗi occurrence của một claim phải có story function:
- TEASE
- EXPLAIN
- EVIDENCE
- COMPLICATE
- PAYOFF
- CALLBACK

Cùng claim + cùng evidence + cùng meaning lặp lại không có chức năng mới → cắt/gộp.

### 6. Claim Strength Contract

Claim Map giờ kiểm:
- allowed certainty
- forbidden strengthening
- time scope
- geographic scope
- population scope
- temporal wording

Ví dụ:
"ít nhất khoảng 2.500 năm trước"
tốt hơn
"chắc chắn từ rất lâu"
khi nguồn chỉ trực tiếp chứng minh mốc ~2.500 năm.

### 7. Naturalness + Rhythm + Listening

Audit:
- translationese
- noun stacking
- academic compression
- repeated sentence openings
- fragment patterns
- rhetorical-question overload
- audio density

UNDERSTANDABLE không đồng nghĩa NATURAL.

### 8. Three independent final auditors

10B1:
blind knowledge extraction.

10B2:
blind claim/certainty extraction.

10B3:
blind naturalness/redundancy extraction.

Các auditor không được nhìn report tương ứng trước đó.

## Final Integrity Gate

10_final_integrity.json là source of truth.

PASS khi tất cả bằng 0:

knowledge:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved
- silently_ignored_candidates

terminology:
- unnecessary_labels
- alias_overload

narrative:
- redundant_reveals
- high_load_listening_blocks

factual:
- unsupported_claims
- certainty_overstatements
- unsupported_temporal_generalizations

naturalness:
- translationese_flags
- repeated_rhetorical_patterns
- unresolved_audio_density_flags

## Required artifacts

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
- 05_lexical_knowledge_sweep.json
- 05_blind_knowledge_inventory.json
- 06_audience_report.md
- 06_knowledge_closure.json
- 06_script_accessible.md
- 06_terminology_prune.json
- 06_script_pruned.md
- 07_retention_report.md
- 07_reveal_audit.json
- 07_knowledge_delta.json
- 07_script_retention_edit.md
- 08_anti_ai_report.md
- 08_naturalness_audit.json
- 08_knowledge_delta.json
- 08_script_natural.md
- 09_fact_check.md
- 09_claim_strength_audit.json
- 09_knowledge_delta.json
- 09_script_fact_checked.md
- 10_story_report_draft.md
- 10_final_candidate.md
- 10b1_blind_knowledge_inventory.json
- 10b2_blind_claim_inventory.json
- 10b3_blind_naturalness_audit.json
- 10_final_story_report.md
- 10_final_integrity.json
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

## Output dùng để sản xuất

projects/<project_slug>/10_final_script.md

## Shared protocols

- prompts/KNOWLEDGE_GROUNDING_PROTOCOL.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

Legacy v3 final closure:
- 10_knowledge_closure.json

v3.1 final source of truth:
- 10_final_integrity.json
