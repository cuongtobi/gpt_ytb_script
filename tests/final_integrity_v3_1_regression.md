# Final Integrity v3.1 — Regression Tests

These acceptance cases come from real failures found while reviewing the v3 cannabis project.

## Test 1 — Blind discovery misses "di truyền"

Input:
"Người trồng không cần biết gì về di truyền."

Expected:
- lexical sweep creates candidate for "di truyền";
- candidate appears in semantic crosswalk;
- stage 06 assigns disposition;
- silently_ignored_candidates remains 0.

FAIL if "di truyền" disappears from audit.

## Test 2 — Explained but unnecessary alias

Input repeatedly alternates:
- cần sa
- Cannabis sativa
- Cannabis

Expected:
- terminology gate identifies primary spoken label;
- scientific name may be retained once if useful;
- unnecessary repeated "Cannabis" alias is REPLACED/REMOVED unless later reasoning requires it.

PASS:
unnecessary_labels = 0
alias_overload = 0

## Test 3 — Unnecessary "hemp" label

If the story only needs:
"dòng cần sa thiên về thân/sợi"

and never needs the English label later:

Expected:
hemp → REPLACE/REMOVE.

If retained because cited studies use the category:
definition_scope must state the research context.

## Test 4 — Duplicate ~12,000-year reveal

Opening:
fully explains the 2021 genomic ~12,000-year estimate.

Later genome section:
repeats same study, number and meaning.

Expected:
07_reveal_audit flags REDUNDANT_REVEAL unless occurrences have distinct TEASE vs EXPLAIN/EVIDENCE functions.

A teaser cannot fully consume the later reveal.

## Test 5 — Certainty drift

Input:
"THC chắc chắn đã được con người khai thác từ rất lâu."

Evidence:
direct chemical evidence around 2,500 years ago.

Expected:
claim-strength audit flags:
- certainty_overstatement
- unsupported_temporal_generalization

Preferred repair:
"Ít nhất khoảng 2.500 năm trước, chúng ta có bằng chứng trực tiếp..."

## Test 6 — Context-scoped hemp definition

Bad:
"hemp nghĩa là cần sa lấy sợi..."

Expected:
flag universalized definition.

Preferred:
"Trong các nghiên cứu về lịch sử thuần hóa này, những dòng thiên về thân, sợi hoặc hạt thường được xếp vào nhóm hemp."

## Test 7 — Translationese

Input:
"được sử dụng như một phần của nền kinh tế cây trồng"

Expected:
naturalness audit flags academic/translated phrasing.

Possible repair:
"đã trở thành một phần của hệ thống trồng trọt của cộng đồng"

## Test 8 — Repeated AI rhythm

Input block:
"Trở thành thời điểm ra hoa.
Trở thành lượng sợi trong thân.
Trở thành thành phần hóa học.
Và cuối cùng..."

Expected:
repeated_rhetorical_pattern candidate.

Repair by merging into a natural sentence unless repetition has a strong intentional function.

## Test 9 — Blind claim auditor independence

10B2 must extract claims/certainty before seeing Claim Map.

FAIL if 10B2 reads or quotes Claim Map during extraction.

## Test 10 — Blind naturalness auditor independence

10B3 must not read stage 07/08 reports.

Expected:
it can independently rediscover:
- duplicate reveals;
- unnecessary aliases;
- translationese;
- repeated rhythm.

## Final acceptance

10_final_integrity.json PASS only when:

knowledge:
- all 9 counts = 0

terminology:
- unnecessary_labels = 0
- alias_overload = 0

narrative:
- redundant_reveals = 0
- high_load_listening_blocks = 0

factual:
- unsupported_claims = 0
- certainty_overstatements = 0
- unsupported_temporal_generalizations = 0

naturalness:
- translationese_flags = 0
- repeated_rhetorical_patterns = 0
- unresolved_audio_density_flags = 0
