# GPT YouTube Visual-Storytelling Script Pipeline

Pipeline viết **YouTube documentary script có khả năng visual storytelling mạnh** trên **ChatGPT Web + GitHub**.

Mục tiêu của repository này là tạo ra narration mà người nghe có thể tự hình dung cảnh, hành động, vật thể, sự biến đổi và tương phản ngay từ lời kể — **không tạo storyboard, shot list, image prompt, B-roll list hay timeline dựng video**.

## Mục tiêu chất lượng

Pipeline ưu tiên 5 nguyên tắc:

1. **Story before prose** — xây câu chuyện trước khi viết câu chữ.
2. **Understanding before terminology** — khán giả hiểu ý trước khi gặp thuật ngữ.
3. **Concrete before abstract** — ưu tiên cảnh, hành động, vật thể, biến đổi và tương phản.
4. **Evidence before drama** — không làm claim mạnh hơn nguồn chỉ để câu chuyện kịch tính hơn.
5. **Visual storytelling from the start** — visual storytelling được thiết kế từ Story Architect, không thêm vào cuối.

---

## Pipeline hoạt động như thế nào?

```text
USER INPUT
   ↓
00 ORCHESTRATOR
   ↓
01 ANGLE ENGINE
   ↓
02 DEEP RESEARCH
   ↓
03 CLAIM MAP + CONCEPT MAP
   ↓
04 STORY ARCHITECT
   ↓
05 VISUAL NARRATIVE WRITER
   ↓
06 AUDIENCE & CONCEPT EDITOR
   ↓
07 RETENTION EDITOR
   ↓
08 ANTI-AI EDITOR
   ↓
09 FACT CHECKER
   ↓
10 FINAL STORY EDITOR
   ↓
FINAL SCRIPT
```

### 00 — Orchestrator

Đọc yêu cầu của người dùng, chuẩn hóa brief, tạo thư mục project, xác định độ dài, ngôn ngữ, audience, hook/angle mode và điều phối toàn pipeline.

### 01 — Angle Engine

Không viết outline ngay. Bước này xác định **câu chuyện đáng kể nhất** từ topic: central question, contradiction, transformation, stakes và payoff.

Ví dụ một topic có thể được kể theo chronology, contradiction, mystery, reverse assumption hoặc transformation. Angle Engine chọn một story spine duy nhất để tránh script bị lan man.

### 02 — Deep Research

Research theo các câu hỏi cụ thể thay vì gom thông tin chung chung. Ngoài facts, dates, studies và archaeological evidence, bước này chủ động tìm:

- visual facts;
- human actions;
- transformations;
- concrete objects;
- contrasting states;
- disputed/uncertain claims.

Researcher **không viết script**.

### 03 — Claim Map + Concept Map

#### Claim Map

Mỗi factual claim quan trọng được gắn với nguồn, confidence và safe wording.

Mục tiêu: ngăn việc biến “likely” thành “definitely”, tạo precision giả hoặc đưa số liệu không có nguồn.

#### Concept Map

Theo dõi các khái niệm mà khán giả phổ thông có thể chưa biết.

Mỗi concept được quyết định:

- có thực sự cần thuật ngữ hay không;
- mức độ quen thuộc với audience;
- lần đầu xuất hiện;
- cách giải thích;
- có thể thay thuật ngữ bằng plain language hay không.

Protocol mặc định:

```text
IDEA / MENTAL MODEL
        ↓
PLAIN-LANGUAGE EXPLANATION
        ↓
TECHNICAL TERM (chỉ khi thực sự cần)
```

Nếu khán giả có thể hiểu câu chuyện mà không cần nhớ thuật ngữ, pipeline ưu tiên **không đưa thuật ngữ vào**.

### 04 — Story Architect

Biến research thành các narrative beats.

Mỗi beat nên ưu tiên ít nhất một dạng:

```text
SCENE
ACTION
OBJECT
TRANSFORMATION
CONTRAST
MOVEMENT
SCALE
HUMAN DECISION
```

Story flow được ưu tiên:

```text
QUESTION
   ↓
EVIDENCE
   ↓
PARTIAL ANSWER
   ↓
COMPLICATION
   ↓
NEW QUESTION
   ↓
REVEAL
   ↓
TRANSFORMATION
   ↓
PAYOFF
```

Mục tiêu là tránh kiểu “fact → fact → fact → fact”.

### 05 — Visual Narrative Writer

Viết full narration dựa trên story architecture.

Writer phải làm cho kiến thức trở nên **có thể hình dung được trong đầu**, nhưng không chèn hướng dẫn dựng phim.

Ví dụ:

**Yếu:**

> Human activity created favorable ecological conditions.

**Tốt hơn:**

> Con người chặt cây, đốt bụi, nuôi gia súc và làm xáo trộn lớp đất quanh nơi ở. Những khoảng đất mới bị xới tung ấy lại chính là nơi loài cây này phát triển rất tốt.

Các rule chính:

- concrete before abstract;
- action before process name;
- concept before label;
- known before unknown;
- transformation over static description;
- contrast whenever useful;
- dates must attach to events;
- numbers should have understandable scale when useful;
- không lạm dụng “Imagine this”, “Picture this”, “Now zoom in” để giả visual storytelling.

### 06 — Audience & Concept Editor

Kiểm tra script bằng góc nhìn của người **nghe lần đầu**, không phải người đọc tài liệu.

Ba audit bắt buộc:

1. **First-use audit** — concept có được hiểu trước/khi xuất hiện lần đầu không?
2. **Concept-load audit** — có quá nhiều khái niệm mới trong một khoảng ngắn không?
3. **Explanation audit** — explanation có vừa đủ để hiểu câu tiếp theo không?

Heuristic mặc định: khoảng **1–2 important new concepts/phút**. Đây là warning threshold, không phải giới hạn tuyệt đối.

### 07 — Retention Editor

Kiểm tra toàn script theo block, tập trung vào:

- curiosity;
- change;
- conflict;
- concrete imagery;
- new information;
- payoff;
- repetition;
- scope drift;
- technical-density valleys.

Không dùng cliffhanger giả để vá retention.

### 08 — Anti-AI Editor

Không “detect AI”. Bước này tìm pattern làm narration nghe công thức:

- transition lặp;
- fragment lặp;
- fake profundity;
- documentary cliché;
- rhetorical question quá nhiều;
- translated-English phrasing;
- over-dramatization;
- các pattern như “And here's the thing…”, “But here's where…”, “Think about that…” dùng quá dày.

Editor phải đánh giá theo **cách kể tự nhiên của chính ngôn ngữ đầu ra**, không dùng tiếng Anh hay tiếng Việt làm chuẩn chung.

### 09 — Fact Checker

So sánh factual statements trong script với Claim Map và nguồn.

Status chuẩn:

- `SUPPORTED`
- `SUPPORTED_BUT_OVERSTATED`
- `PARTIALLY_SUPPORTED`
- `UNSUPPORTED`
- `CONTRADICTED`
- `SOURCE_TOO_WEAK`

Fact Checker cũng kiểm tra internal consistency của dates, percentages, multipliers và quantities.

### 10 — Final Story Editor

QC toàn bài thay vì chỉ sửa từng câu.

Kiểm tra:

- hook;
- central question;
- story progression;
- transformation;
- visual storytelling;
- concept accessibility;
- scope;
- retention;
- repetition;
- ending/payoff;
- callback;
- natural language;
- factual integrity.

Final Story Editor chấm **Visual Storytelling Score** và chỉ pass khi script đạt tiêu chuẩn quy định trong prompt.

---

## Cấu trúc repository

```text
gpt_ytb_script/
├── AGENTS.md
├── README.md
├── prompts/
│   ├── 00_orchestrator.md
│   ├── 01_angle_engine.md
│   ├── 02_researcher.md
│   ├── 03_claim_concept_mapper.md
│   ├── 04_story_architect.md
│   ├── 05_visual_narrative_writer.md
│   ├── 06_audience_concept_editor.md
│   ├── 07_retention_editor.md
│   ├── 08_anti_ai_editor.md
│   ├── 09_fact_checker.md
│   └── 10_final_story_editor.md
└── projects/
    └── <project_slug>/
        ├── 00_project_brief.yaml
        ├── 01_angle.md
        ├── 02_research_notes.md
        ├── 02_sources.json
        ├── 03_claim_map.json
        ├── 03_concept_map.json
        ├── 04_story_architecture.md
        ├── 05_script_draft.md
        ├── 06_audience_report.md
        ├── 06_script_accessible.md
        ├── 07_retention_report.md
        ├── 07_script_retention_edit.md
        ├── 08_anti_ai_report.md
        ├── 08_script_natural.md
        ├── 09_fact_check.md
        ├── 09_script_fact_checked.md
        ├── 10_final_story_report.md
        └── 10_final_script.md
```

---

# Cách sử dụng trên ChatGPT Web

## Yêu cầu tối thiểu

- ChatGPT Web có kết nối GitHub.
- Cho phép ChatGPT truy cập repository này.
- Với chủ đề cần thông tin hiện tại hoặc cần research bên ngoài, bật/nhắc ChatGPT sử dụng tìm kiếm web.

## Cách chạy tiêu chuẩn

Gửi một prompt như sau:

```text
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
Tạo một project mới trong projects/ và lưu mọi artifact của pipeline vào đó.
```

## Ví dụ tiếng Anh

```text
@GitHub work with repo cuongtobi/gpt_ytb_script
@Search the web

Create a new YouTube documentary script.

topic: How Humans Domesticated Dogs
language: English
duration: 25 minutes
audience: general
hook_mode: reverse_assumption

Read AGENTS.md and prompts/00_orchestrator.md.
Run the full pipeline and save every artifact into a new project under projects/.
```

## Input được hỗ trợ

```yaml
topic: required
language: required
duration: required

audience: general          # default
hook_mode: auto            # default
angle_mode: auto           # default
research_depth: deep       # default
technical_level: accessible
```

### `hook_mode`

Có thể dùng:

- `auto`
- `contradiction`
- `mystery`
- `reverse_assumption`
- `transformation`
- `scene`
- `question`

Nếu không chỉ định, Angle Engine tự chọn dựa trên research.

### `angle_mode`

- `auto`: pipeline tự chọn angle mạnh nhất và chạy liền mạch.
- `user_selected`: Angle Engine tạo các angle candidates và dừng để người dùng chọn trước khi tiếp tục.

Mặc định là `auto` để pipeline có thể chạy end-to-end trong một yêu cầu.

---

# Chỉ chạy một phần pipeline

Có thể yêu cầu ChatGPT chạy lại một stage cho project đã có.

Ví dụ:

```text
@GitHub làm việc với repo cuongtobi/gpt_ytb_script

Đọc project projects/<project_slug>/.
Chạy lại 07_retention_editor cho script hiện tại.
Cập nhật retention report và script retention edit.
Sau đó chạy lại các stage phụ thuộc từ 08 đến 10.
```

Hoặc:

```text
Fact-check lại project projects/<project_slug>/ bằng nguồn web mới nhất.
Không thay đổi angle hoặc story architecture nếu không bắt buộc.
```

---

# Output cuối cùng

Artifact dùng để sản xuất là:

```text
projects/<project_slug>/10_final_script.md
```

Đây là **narration script**, không phải screenplay dựng hình.

Nó không nên chứa:

- image prompts;
- camera instructions;
- shot list;
- B-roll instructions;
- storyboard;
- visual timeline.

Visual storytelling phải nằm trong **cách câu chuyện được viết**.

---

# Concept Introduction Protocol

Khi xuất hiện một khái niệm mới, pipeline dùng thứ tự ưu tiên:

```text
1. Khán giả có cần biết thuật ngữ không?
        ↓ no
   Dùng plain language, không đưa term.

        ↓ yes

2. Khán giả đã có mental model chưa?
        ↓ no
   Giải thích bằng action / analogy / contrast / mechanism.

        ↓

3. Đặt technical label sau khi ý đã dễ hiểu.

        ↓

4. Lần sau được phép dùng term mà không định nghĩa lại,
   trừ khi đã cách quá xa và cần micro-reminder.
```

Các cách giải thích được ưu tiên:

- direct definition;
- analogy;
- human action;
- contrast;
- mechanism.

Rule quan trọng:

> **A viewer should never need to know a term before the script teaches the idea behind that term.**

Và:

> **If the viewer can understand the story without knowing the technical term, do not make them learn it.**

---

# Quality gates

Pipeline chỉ hoàn thành khi:

- factual claims quan trọng có nguồn;
- unsupported claims quan trọng đã được sửa hoặc loại bỏ;
- central question được payoff;
- không có section dài bị scope drift rõ rệt;
- concept first-use audit không còn lỗi nghiêm trọng;
- anti-AI pass;
- final script phù hợp duration mục tiêu;
- Visual Storytelling Score đạt ít nhất **8.0/10**.

Score gồm:

```text
concrete scenes
human actions
transformations
contrast
abstract density
concept accessibility
mental visualization
```

Điểm số chỉ là QC nội bộ; ưu tiên judgment dựa trên script hơn việc tối ưu máy móc theo điểm.

---

# Ngôn ngữ

Pipeline hỗ trợ đa ngôn ngữ.

Các editor phải:

1. đánh giá theo cách kể tự nhiên của **ngôn ngữ đầu ra**;
2. giữ biến thể vùng miền, register và cách xưng hô phù hợp;
3. không dịch cấu trúc rhetoric tiếng Anh sang ngôn ngữ khác một cách máy móc;
4. giữ thuật ngữ chuyên ngành theo cách mà khán giả bản ngữ thực sự gặp chúng;
5. viết report bằng ngôn ngữ yêu cầu của project, trừ khi user chỉ định khác.

---

# Triết lý của pipeline

Pipeline không cố biến mọi câu thành cinematic.

Một documentary tốt cần xen kẽ:

```text
scene
→ explanation
→ evidence
→ action
→ contrast
→ reflection
→ reveal
```

Visual storytelling ở đây có nghĩa là **thông tin được tổ chức thành thứ có thể cảm nhận và hình dung**, không phải narration liên tục ra lệnh cho người xem tưởng tượng.

Research tốt nhưng không có Story Architect dễ trở thành Wikipedia đọc thành tiếng.

Writer hay nhưng thiếu Concept Map dễ làm khán giả phổ thông bị rơi khỏi câu chuyện.

Retention mạnh nhưng thiếu Fact Checker dễ biến uncertainty thành certainty.

Pipeline này được thiết kế để cả bốn lớp — **evidence, story, accessibility và natural narration** — cùng tồn tại trong final script.
