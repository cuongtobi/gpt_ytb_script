# v3.2 — Three Fixture Rerun Results

Date: 2026-09-20

GitHub Actions run: 35516336963
Head SHA tested: c0d46cfdca7d77a624efee5bb94bfa3147880110
Workflow conclusion: **SUCCESS**

Final HEAD verification: all three matrix jobs completed with `success`.

The workflow executed:
- `tools/assert_v3_2_fixture_targets.py`
- `tools/verify_integrity_proof.py`

on all three fixture projects.

## Results

| Fixture | Targeted regression | Proof verifier | Sentence count | Final status |
|---|---|---|---:|---|
| Birds / power lines | PASS | PASS | 72 | CONTENT_PASS_ISOLATION_NOT_VERIFIED |
| Maize domestication | PASS | PASS | 90 | CONTENT_PASS_ISOLATION_NOT_VERIFIED |
| Seawater / rain | PASS | PASS | 86 | CONTENT_PASS_ISOLATION_NOT_VERIFIED |

## Hole 1 — Lexical sweep completeness

### Birds
The v3.1 misses:
- điện áp
- đường dây truyền tải
- đường phân phối

were all present in the v3.2 draft lexical candidate set and absent from final narration.

### Maize
The v3.1 targets:
- dữ liệu di truyền
- quần thể
- phát tán
- khảo cổ

were detected in the draft sweep and absent from final narration.

### Seawater / rain
The v3.1 targets:
- phong hóa
- khí quyển

were detected in the draft sweep and absent from final narration.

**Fixture result: PASS.**

Important limitation:
sentence-ledger + dual-pass review reduces false negatives and the targeted regression list proves these known misses are blocked, but no LLM lexical audit can mathematically guarantee discovery of every possible semantic concept in arbitrary future prose.

## Hole 2 — Temporal first-use proof

The deterministic verifier recomputed canonical sentences from the actual final scripts, independently found first occurrence of each final candidate's exact phrase, and compared that to the recorded first-use/grounding coordinates.

All three jobs returned:
- `proof_verifier_status = PASS`
- `errors = []`

The maize v3.1 failure where “dữ liệu di truyền” appeared before its plain mental model was removed; “thuần hóa” now has a PRIOR temporal proof.

**Fixture result: PASS.**

## Hole 3 — Candidate conservation

The verifier took discovered candidate IDs directly from 10B1 and required exact equality with 10C disposition IDs.

Results:
- Birds: 5 discovered = 3 GROUNDED + 2 BASELINE_KNOWN
- Maize: 4 discovered = 4 GROUNDED
- Rain: 6 discovered = 4 GROUNDED + 2 BASELINE_KNOWN

UNRESOLVED = 0 in all three.
No missing or duplicate disposition IDs.

**Fixture result: PASS.**

## Hole 4 — True blind execution isolation

This environment did NOT provide runtime-attested fresh model contexts for 10B1, 10B2 and 10B3.

The isolation manifests therefore report:
- `ISOLATION_NOT_VERIFIED`

The deterministic verifier returned:
- `isolation_verified = false`
- `project_status = CONTENT_PASS_ISOLATION_NOT_VERIFIED`

The CI workflow explicitly asserted this status and would fail if the projects incorrectly claimed `PASS_VERIFIED`.

**Fail-closed behavior: PASS.**
**True isolated execution itself: NOT YET VERIFIED.**

## Overall conclusion

v3.2 successfully blocks the three content/proof false-PASS mechanisms demonstrated by the v3.1 fixtures:
1. targeted lexical misses;
2. unproven first-use ordering;
3. disappearing candidates during reconciliation.

For the fourth issue, v3.2 successfully blocks the false claim of isolation, but the current ChatGPT execution environment did not demonstrate genuine isolated auditor contexts.

Therefore the correct overall status is:

**CONTENT PROOFS VERIFIED; BLIND ISOLATION NOT VERIFIED.**
