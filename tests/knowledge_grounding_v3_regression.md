# Knowledge Grounding v3 — Regression Acceptance Cases

## Case 1 — Core subject familiarity trap

Input:
"Ngày nay, chỉ cần nghe hai chữ cần sa..."

Failure:
Topic label appears but viewer is never told what kind of thing cannabis is.

Expected:
Core entity requires minimum grounding before scientific name/component/mechanism claims.

## Case 2 — Scientific name alias

Input:
"Cannabis sativa đã được thuần hóa..."

Failure:
Viewer may know "cần sa" but not that Cannabis sativa is the scientific label used for the subject.

Expected:
Cannabis sativa cannot be freely used until alias/canonical relation is grounded.

## Case 3 — THC component relation

Input:
"nghĩ ngay đến THC..."

Failure:
THC is not grounded as a compound made by cannabis and associated with intoxicating effects.

Expected:
Blind discovery extracts THC as COMPONENT; closure grounds relation before/at first use.

## Case 4 — Marijuana related label

Input:
"tranh cãi pháp lý quanh marijuana"

Failure:
marijuana is neither mapped nor explained.

Expected:
Map relation or REMOVE if unnecessary.

## Case 5 — Temporal genome failure

Input:
"một nghiên cứu genome lớn..."
Definition appears minutes later.

Expected:
temporal_first_use_failures > 0 until grounding is moved to/before first use.

## Case 6 — Dependency self-declared KNOWN

Input:
"phytolith là hạt silica cực nhỏ"

If silica is absent from audience baseline and has no grounded node:
silica cannot be BASELINE_KNOWN.

Expected:
ground, replace with "hạt khoáng", or remove.

## Case 7 — Blind discovery catches graph omissions

Final script contains:
- enzyme
- áp lực chọn lọc
- con đường sinh học

Graph lacks them.

Expected:
10B blind auditor extracts them.
10C sets missing_discovered_nodes > 0 until reconciled.

## Case 8 — Rewrite creates new alias

Anti-AI editor changes "cần sa" to "marijuana".

Expected:
08_knowledge_delta identifies new_aliases and cannot PASS unresolved.

## Global PASS

All final values must equal zero:
- core_entities_ungrounded
- unmapped_aliases
- missing_discovered_nodes
- unresolved_concepts
- unresolved_dependencies
- unresolved_relations
- temporal_first_use_failures
- confusable_pairs_unresolved
