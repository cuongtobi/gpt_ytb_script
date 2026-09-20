# v3.2 Integrity Proof Regression

Use the three v3.1 10-minute fixtures.

## A — Birds / power lines

Prior misses:
- điện áp
- đường dây truyền tải
- đường phân phối

v3.2:
- every sentence has forward + reverse category matrices;
- candidate union is reconciled;
- no missing sentence row;
- 10D validates matrix shape and candidate accounting.

## B — Maize

Prior failures:
- dữ liệu di truyền used before grounding
- quần thể omitted

v3.2:
- 10D recomputes exact first occurrence of each candidate phrase;
- declared first-use ID must equal actual first occurrence;
- temporal ordering then uses actual first occurrence.

## C — Seawater / rain

Prior reconciliation loss:
- phong hóa
- khí quyển

v3.2:
- 10D takes candidate IDs directly from 10B1;
- disposition IDs must match exactly;
- BASELINE_KNOWN requires exact provenance.

## Isolation

Same-context audits:
isolation_status = ISOLATION_NOT_VERIFIED

Even when all content proofs pass:
project_status = CONTENT_PASS_ISOLATION_NOT_VERIFIED

PASS_VERIFIED requires runtime-attested distinct fresh executions.

## Writer quality

Detection is not definition.

Prefer:
REMOVE → REPLACE → REORDER → minimal grounding.
