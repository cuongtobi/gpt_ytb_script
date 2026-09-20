# GPT YouTube Documentary Script Pipeline

Current version: **v3.2 — Proof-Carrying Integrity**

## Goal

Create documentary narration that is:
- factual
- understandable
- natural when heard once
- retention-aware
- visually tellable
- not overloaded with jargon
- auditable without trusting the model's own PASS statement

## What v3.2 fixes

### 1. Exhaustive lexical coverage

A canonical sentence index is created first.

Every sentence ID must have a lexical-ledger row, even when candidate list is empty.

### 2. Hard temporal proof

Every retained unfamiliar candidate records:
- first-use sentence ID
- grounding sentence ID/mode
- ordering validity

### 3. Candidate conservation

Every discovered candidate must end as exactly one of:
- BASELINE_KNOWN
- GROUNDED
- REPLACED
- REMOVED
- UNRESOLVED

The totals must balance exactly.

### 4. Verified blind isolation

10B1/10B2/10B3 must run in distinct fresh contexts for PASS_VERIFIED.

If fresh-context execution cannot be attested:
CONTENT_PASS_ISOLATION_NOT_VERIFIED

not PASS_VERIFIED.

## Pipeline

00 → 01 → 02 → 03A → 03B → 04 → 05
→ 05A1 sentence index
→ 05B blind discovery
→ 06 proof-carrying knowledge closure
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

## Important principle

Detection does not mean explanation.

The writer stays free.
The auditor is constrained.

## Final statuses

- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

## Deterministic verifier

When Python runtime is available:

~~~text
python tools/verify_integrity_proof.py \
  --index <project>/10_final_sentence_index.json \
  --blind <project>/10b1_blind_knowledge_inventory.json \
  --integrity <project>/10_final_integrity.json \
  --isolation <project>/10b_isolation_manifest.json
~~~

## ChatGPT Web usage

~~~text
@GitHub làm việc với repo cuongtobi/gpt_ytb_script
@Tìm kiếm trên mạng

Viết một YouTube documentary script mới.

topic: ...
language: ...
duration: ...
audience: general

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy pipeline v3.2.
Tạo project mới trong projects/ và lưu mọi artifact.
Không tự báo PASS_VERIFIED nếu blind isolation không được runtime xác nhận.
~~~
