# GPT YouTube Documentary Script Pipeline

Current version: **v3.2 — Proof-Carrying Integrity**

## Goal

Create documentary narration that is factual, understandable, natural, retention-aware and auditable without trusting the model's own PASS statement.

## Four v3.1 false-PASS fixes

### 1. Exhaustive lexical coverage
A canonical sentence index is built first.
Every sentence ID must have exactly one lexical-ledger row, including zero-candidate sentences.
10D recomputes sentence units directly from the final script.

### 2. Hard temporal proof
Every retained unfamiliar candidate records first-use and grounding sentence IDs/mode.
Ordering is checked numerically.

### 3. Candidate conservation
Discovered candidate IDs come directly from 10B1.
Every ID must have exactly one disposition:
BASELINE_KNOWN / GROUNDED / REPLACED / REMOVED / UNRESOLVED.

### 4. Verified blind isolation
10B1/10B2/10B3 require distinct fresh execution contexts for PASS_VERIFIED.
If the runtime cannot attest that:
CONTENT_PASS_ISOLATION_NOT_VERIFIED

not PASS_VERIFIED.

## Creative freedom

Detection does not mean definition.

Prefer:
REMOVE → REPLACE → REORDER → minimal grounding.

The writer remains creative; auditors are constrained.

## Pipeline

00 → 01 → 02 → 03A → 03B → 04 → 05
→ 05A1 sentence index
→ 05B blind discovery
→ 06 proof-carrying closure
→ 06B terminology
→ 07 retention/reveal
→ 08 naturalness/listening
→ 09 fact/claim strength
→ 10A final candidate
→ 10A1 final sentence index
→ isolated 10B1 / 10B2 / 10B3
→ 10C reconciliation
→ 10D deterministic proof verification
→ final

## Final statuses

- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

## Deterministic verifier

```
python tools/verify_integrity_proof.py \
  --script <project>/10_final_script.md \
  --index <project>/10_final_sentence_index.json \
  --blind <project>/10b1_blind_knowledge_inventory.json \
  --integrity <project>/10_final_integrity.json \
  --isolation <project>/10b_isolation_manifest.json
```

## ChatGPT Web usage

```text
@GitHub làm việc với repo cuongtobi/gpt_ytb_script
@Tìm kiếm trên mạng

Viết một YouTube documentary script mới.

topic: ...
language: ...
duration: ...
audience: general

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy pipeline v3.2.
Tạo project mới trong projects/.
Không tự báo PASS_VERIFIED nếu runtime không xác nhận blind isolation.
```
