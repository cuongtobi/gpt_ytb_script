# v3.2 Integrity Proof Regression

Use the three v3.1 10-minute fixtures as acceptance tests.

## Fixture A — Birds / power lines

v3.1 failure:
- final lexical audit missed "điện áp", "đường dây truyền tải", "đường phân phối".

v3.2 acceptance:
- every canonical sentence has a ledger row;
- those phrases are either candidates or explicitly ordinary with candidate-level accounting;
- no missing sentence IDs;
- conservation equation valid.

## Fixture B — Maize domestication

v3.1 failure:
- "dữ liệu di truyền" first used before grounding;
- "quần thể" omitted from final audit.

v3.2 acceptance:
- temporal proof shows first_use_sentence_id and grounding coordinate;
- if grounding is later, FAIL until repaired;
- "quần thể" cannot disappear without disposition.

## Fixture C — Seawater / rain

v3.1 failure:
- "phong hóa" and "khí quyển" were discovered but disappeared in 10C accounting.

v3.2 acceptance:
- both candidates appear in candidate conservation;
- BASELINE_KNOWN requires exact provenance;
- otherwise GROUNDED/REPLACED/REMOVED/UNRESOLVED;
- equation must balance.

## Isolation test

If all 10B audits are run in the same conversation/context:

Expected:
isolation_status = ISOLATION_NOT_VERIFIED

Even if content passes:
project_status = CONTENT_PASS_ISOLATION_NOT_VERIFIED

PASS_VERIFIED is forbidden.

## Conservation invariant

For N discovered candidate IDs:

N
=
BASELINE_KNOWN
+ GROUNDED
+ REPLACED
+ REMOVED
+ UNRESOLVED

No missing IDs.
No duplicate dispositions.

## Temporal invariant

For every retained unfamiliar candidate:

PRIOR:
grounding_sentence < first_use_sentence

INLINE:
grounding_sentence == first_use_sentence

BASELINE:
strict provenance required

REPLACED/REMOVED:
label absent from final text.

## Writer-quality invariant

Do not add definitions merely to satisfy the audit.

Repairs should prefer:
REMOVE → REPLACE → REORDER → minimal grounding.
