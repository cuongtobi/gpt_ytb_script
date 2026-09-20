# v3.1 — Three 10-Minute Stress Tests

Date: 2026-09-20

Purpose:
Stress-test Final Integrity v3.1 across three different knowledge shapes instead of one cannabis-specific story.

## Projects

### A. Birds on power lines
Path:
projects/2026-09-20_test_v3_1_birds_power_lines_10min/

Final candidate:
10_final_script.md

Word count:
1472

Stress focus:
- common words used technically
- electrical mechanism
- grounding/ground confusion
- terminology pruning
- safety wording

Seeded draft defects caught:
- điện thế
- điện trở
- sụt áp
- misleading "electricity chooses easiest path" framing

Independent post-run defect:
- "điện áp" remains without grounding
- "đường dây truyền tải" and "đường phân phối" were not extracted by 10B1

Final integrity:
FAIL

Primary root cause:
Blind lexical discovery completeness.

---

### B. Maize domestication
Path:
projects/2026-09-20_test_v3_1_maize_domestication_10min/

Final candidate:
10_final_script.md

Word count:
1573

Stress focus:
- unfamiliar ancestor entity
- scientific aliases
- genetics labels
- domestication chronology
- claim-strength calibration

Seeded draft defects caught:
- Zea mays ssp. parviglumis overload
- tb1 / tga1 gene-name detour
- "few genes created maize" overclaim
- over-clean "single event" wording

Independent post-run defects:
- "dữ liệu di truyền" first appears in the opening before plain grounding
- "quần thể" is omitted from final lexical inventory

Final integrity:
FAIL

Primary root causes:
Temporal first-use validation + specialized common-word discovery.

---

### C. Seawater vs rain
Path:
projects/2026-09-20_test_v3_1_seawater_rain_10min/

Final candidate:
10_final_script.md

Word count:
1500

Stress focus:
- causal chain
- chemistry terminology
- absolute-vs-relative factual wording
- phase-change terminology
- repeated AI rhythm

Seeded draft defects caught:
- ion / natri / chloride overload
- ngưng tụ / kết tủa labels
- "mưa là nước tinh khiết" overclaim
- repeated fragment rhythm

Independent post-run defects:
- "phong hóa" was extracted but never grounded/replaced
- "khí quyển" was extracted but no strict BASELINE_KNOWN provenance/disposition was recorded

Final integrity:
FAIL

Primary root cause:
10C reconciliation completeness.

---

## Aggregate result

| Project | Words | Seeded defects caught | Independent false-PASS found | Final status |
|---|---:|---:|---:|---|
| Birds / power lines | 1472 | YES | YES | FAIL |
| Maize domestication | 1573 | YES | YES | FAIL |
| Seawater / rain | 1500 | YES | YES | FAIL |

## What v3.1 is doing well

- terminology pruning is much better than v3;
- scientific aliases can be removed without breaking story;
- claim-strength repair works on intentionally overstated wording;
- naturalness pass catches obvious repeated fragment patterns;
- core-subject grounding is substantially stronger than v2/v3.

## Remaining architecture failures

### 1. Lexical sweep can still be selective

A prompt that says "scan every sentence" does not guarantee exhaustive candidate extraction.

Need a sentence-indexed audit table where every sentence is represented, including a zero-candidate record.

### 2. Final temporal closure is not proven mechanically

A candidate can be extracted but final status can still claim zero first-use violations without showing:
- sentence_id of first use
- sentence_id of grounding
- comparison result

Require machine-checkable:
grounded_sentence <= first_use_sentence

### 3. Reconciliation lacks candidate-level conservation

10C must prove:
number of lexical candidates
=
BASELINE_KNOWN
+ GROUNDED
+ REPLACED
+ REMOVED
+ UNRESOLVED

No aggregate zero may be accepted without this conservation equation.

### 4. BASELINE_KNOWN provenance is still too loose

Each BASELINE_KNOWN result must include:
- exact baseline entry or primitive ID
- canonical mapping, if any

No free-text justification.

### 5. Final blind auditors need true execution isolation

These stress tests show that schema-level "blind" instructions alone are insufficient when audits are composed in the same orchestration context.

Recommended next architecture:
- separate model/tool call per blind auditor;
- persist output;
- only then run reconciliation.

## Acceptance criteria for next revision

All three fixtures should be rerun after the next pipeline change.

A true PASS requires:
- no independently discoverable missing lexical candidates;
- explicit candidate conservation;
- explicit first-use ordering proof;
- strict KNOWN provenance;
- independent final auditors run in isolated calls;
- all final integrity counts zero only after those proofs.
