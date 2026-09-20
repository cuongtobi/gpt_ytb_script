# GPT YouTube Visual-Storytelling Script Pipeline

Pipeline viết YouTube documentary script có visual storytelling mạnh trên ChatGPT Web + GitHub.

Mục tiêu: tạo narration mà người nghe có thể tự hình dung cảnh, hành động, vật thể, biến đổi và tương phản ngay từ lời kể. Pipeline không tự tạo storyboard, shot list, image prompt hay timeline dựng.

## Nguyên tắc

1. Story before prose.
2. Understanding before terminology.
3. Concrete before abstract.
4. Evidence before drama.
5. Visual storytelling được thiết kế từ Story Architect.
6. Concept system là dynamic graph, không phải glossary tĩnh.
7. Final script chỉ PASS khi Concept Closure đạt UNRESOLVED = 0.

## Pipeline

USER INPUT
→ 00 ORCHESTRATOR
→ 01 ANGLE ENGINE
→ 02 DEEP RESEARCH
→ 03 CLAIM MAP + INITIAL CONCEPT GRAPH
→ 04 STORY ARCHITECT
→ 05 VISUAL NARRATIVE WRITER + CONCEPT DELTA
→ 06 AUDIENCE + RECURSIVE CONCEPT CLOSURE
→ 07 RETENTION EDITOR + CONCEPT DELTA
→ 08 ANTI-AI EDITOR + CONCEPT DELTA
→ 09 FACT CHECKER + CONCEPT DELTA
→ 10 FINAL STORY EDITOR + FINAL CONCEPT CLOSURE
→ FINAL SCRIPT

## Điểm mới: Dynamic Concept Graph

Phiên bản cũ chỉ tạo Concept Map trước khi Writer viết. Điều đó có thể bỏ sót khái niệm được sinh ra trong quá trình giải thích hoặc rewrite.

Ví dụ lỗi:

Lactase là enzyme phân giải lactose.

Nếu người nghe chưa biết lactose là gì, lactase chưa thực sự được giải thích.

Hoặc:

Một số cục giàu calcium vẫn nằm trong bê tông.

Nếu calcium chỉ xuất hiện sau khi Concept Map đã được tạo, một audit dựa trên danh sách cũ có thể không nhìn thấy nó.

Phiên bản hiện tại sửa gốc vấn đề này bằng 3 lớp.

### 1. Initial Concept Dependency Graph

03_concept_graph.json lưu:
- concept
- label familiarity
- role familiarity
- dependency
- necessity
- status
- confusable concepts

Một concept chỉ được coi là EXPLAINED khi mọi dependency cần để hiểu nó đã KNOWN hoặc EXPLAINED.

### 2. Concept Delta sau mọi rewrite

Các stage 05, 07, 08 và 09 so sánh concept trước/sau rewrite.

Concept mới phải được:
- EXPLAIN
- REPLACE
- REMOVE
- hoặc route về stage 06

Không có thuật ngữ mới nào được phép trở nên “vô hình” chỉ vì nó xuất hiện sau stage 03.

### 3. Final Concept Closure

Stage 10 scan lại chính final candidate từ đầu.

Nó không tin PASS của stage 06.

Pipeline chỉ hoàn thành khi:
- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0

## No Unknowns in Definitions

Rule cứng:

Một khái niệm KHÔNG được coi là đã giải thích nếu phần giải thích của nó cần một khái niệm khác chưa được hiểu.

Ví dụ tốt hơn:

Lactose là loại đường tự nhiên có trong sữa. Ruột non tạo lactase, một chất giúp cơ thể xử lý loại đường này.

Thứ tự:
sữa + đường → lactose → lactase

Nếu video thực sự cần khái niệm “enzyme”, pipeline sẽ giới thiệu và resolve nó riêng. Nếu không cần, không bắt khán giả học thêm một label.

## Contextual Familiarity

Pipeline phân biệt:
- người xem có quen với từ này không
- người xem có hiểu vai trò của nó trong cơ chế hiện tại không

Ví dụ canxi có thể quen trong dinh dưỡng, nhưng vai trò của calcium trong quá trình hòa tan và tái kết tinh trong khe bê tông có thể vẫn là khái niệm mới.

## Necessity Test

Khi gặp khái niệm mới, pipeline hỏi:

Người xem có cần biết technical label này để hiểu phần sau không?

Nếu có:
- EXPLAIN

Nếu ý cần nhưng tên không cần:
- REPLACE bằng plain language

Nếu cả chi tiết lẫn tên không cần:
- REMOVE

Mục tiêu không phải giải thích mọi từ. Mục tiêu là không để concept quan trọng bị treo.

## Confusable Concepts

Nếu hai khái niệm dễ nhầm, pipeline bắt buộc phân biệt vai trò.

Ví dụ:
- lactose = loại đường trong sữa
- lactase = enzyme giúp phân giải lactose

Field confusable_with tạo nghĩa vụ biên tập, không chỉ là metadata.

## Các stage chính

### 00 — Orchestrator

Chuẩn hóa brief, tạo project, điều phối stage, route ngược khi QC fail.

### 01 — Angle Engine

Chọn central question, contradiction, transformation và payoff.

### 02 — Deep Research

Thu thập:
- facts
- sources
- visual facts
- human actions
- transformations
- uncertainty
- disputed claims

Không viết narration.

### 03 — Claim Map + Initial Concept Graph

Claim Map kiểm soát factual certainty.

Concept Graph tạo dependency model ban đầu.

### 04 — Story Architect

Biến research thành narrative beats.

Nếu concept A phụ thuộc B, B phải được hiểu trước hoặc A phải được rewrite.

### 05 — Visual Narrative Writer

Viết narration có khả năng hình dung.

Sau khi viết phải scan actual draft và tạo 05_concept_delta.json.

### 06 — Audience + Concept Closure Editor

Đây là closure gate chính.

Stage này scan script từ đầu, không chỉ check concept đã track.

Nó recursively resolve dependencies cho đến khi:
- unresolved = 0
- unresolved_dependencies = 0
- confusable_pairs_unresolved = 0

Output:
- 06_audience_report.md
- 06_concept_closure.json
- 06_script_accessible.md

### 07 — Retention Editor

Sửa retention nhưng không được sinh jargon mới mà không track.

Output thêm:
- 07_concept_delta.json

### 08 — Anti-AI Editor

Làm narration tự nhiên theo ngôn ngữ đầu ra.

Không được biến plain language thành technical language vô tình.

Output thêm:
- 08_concept_delta.json

### 09 — Fact Checker

Fact-check toàn factual substance.

Nếu correction sinh concept mới:
- ghi 09_concept_delta.json
- final closure phải xử lý

### 10 — Final Story Editor

QC toàn bài và scan concept từ chính final candidate.

Output:
- 10_final_story_report.md
- 10_concept_closure.json
- 10_final_script.md

## Cấu trúc project

projects/<project_slug>/

- 00_project_brief.yaml
- 01_angle.md
- 02_research_notes.md
- 02_sources.json
- 03_claim_map.json
- 03_concept_graph.json
- 04_story_architecture.md
- 05_script_draft.md
- 05_concept_delta.json
- 06_audience_report.md
- 06_concept_closure.json
- 06_script_accessible.md
- 07_retention_report.md
- 07_concept_delta.json
- 07_script_retention_edit.md
- 08_anti_ai_report.md
- 08_concept_delta.json
- 08_script_natural.md
- 09_fact_check.md
- 09_concept_delta.json
- 09_script_fact_checked.md
- 10_final_story_report.md
- 10_concept_closure.json
- 10_final_script.md

## Cách sử dụng trên ChatGPT Web

Prompt mẫu:

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

## Angle mode

auto:
Pipeline tự chọn angle và chạy end-to-end.

user_selected:
Angle Engine tạo candidates rồi dừng để người dùng chọn.

## Chạy lại một stage

Ví dụ:

Đọc projects/<project_slug>/.
Chạy lại 07_retention_editor.
Sau đó chạy Concept Delta và các stage phụ thuộc.
Nếu delta sinh UNRESOLVED concept, route lại qua stage 06 trước khi tiếp tục.

## Output dùng để sản xuất

projects/<project_slug>/10_final_script.md

Đây là narration script.

Không chứa:
- storyboard
- shot list
- image prompt
- camera instruction
- B-roll instruction
- visual timeline

## Quality gates

Pipeline chỉ hoàn thành khi:
- factual claims quan trọng có nguồn
- stage 09 fact check PASS
- final concept closure PASS
- unresolved concepts = 0
- unresolved dependencies = 0
- unresolved confusable pairs = 0
- central question được payoff
- không scope drift nghiêm trọng
- anti-AI/natural-language pass
- final duration hợp lý
- Visual Storytelling Score >= 8.0/10

## Shared protocol

Chi tiết thuật toán concept closure nằm tại:

prompts/CONCEPT_CLOSURE_PROTOCOL.md

Đây là source of truth chung cho các stage xử lý concept.

## Triết lý

Research tốt nhưng thiếu Story Architect dễ trở thành Wikipedia đọc thành tiếng.

Story hay nhưng glossary tĩnh vẫn có thể làm khán giả rơi khỏi câu chuyện khi explanation sinh ra explanation mới.

Pipeline hiện dùng dynamic discovery + dependency graph + recursive closure để đảm bảo khán giả không cần biết một concept trước khi script thực sự dạy họ đủ để hiểu nó.
