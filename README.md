# GPT YouTube Documentary Script Pipeline

Current version: **v3.3 — Content-Addressed Full Integrity**

## Goal

Create documentary narration that is factual, understandable, natural, retention-aware and auditable without trusting a model's own PASS statement.

## What v3.3 adds

### 1. Content-address every audit
Every audit records SHA-256 hashes for its exact inputs. Final B1/B2/B3 must all point to the exact released script bytes. A changed final script makes older audits stale and 10D fails.

### 2. Sentence-complete blind claim audit
10B2 reviews every canonical sentence in forward and reverse order. Zero-claim sentences still receive a ledger row.

### 3. Claim conservation
Every blind factual claim receives exactly one final disposition and, when factual, maps to evidence and source provenance.

### 4. B1 + B2 + B3 deterministic coverage verification
10D validates:
- knowledge sentence ledger and candidate conservation;
- claim sentence ledger and claim conservation;
- naturalness/redundancy sentence coverage and finding conservation.

### 5. Hard counters are recomputed
10D derives hard counts from underlying proof records instead of trusting top-level zeros in 10_final_integrity.json.

### 6. JSON Schema contracts
Machine-readable v3.3 artifacts are governed by schemas under schemas/v3.3/.

### 7. Evidence provenance
Research produces:
claim → evidence → source

through 02_evidence_ledger.json.

### 8. Locale-aware segmentation
Canonical sentence segmentation carries locale and segmenter version and supports full-width East Asian sentence punctuation.

### 9. Adversarial tests
CI mutates valid proof bundles to ensure stale hashes, missing ledger rows, dropped claims, invalid evidence links, unresolved findings and false counters fail closed.

### 10. Artifact manifest
artifact_manifest.json records pipeline/schema versions, project inputs/outputs and SHA-256 hashes.

## Pipeline

00 → 01 → 02 research + evidence ledger → 03A → 03B → 04 → 05
→ 05A1 sentence index
→ 05B blind knowledge discovery
→ 06 proof-carrying knowledge closure
→ 06B terminology
→ 07 retention/reveal
→ 08 naturalness/listening
→ 09 fact/claim strength
→ 10A final candidate
→ 10A1 final sentence index
→ isolated 10B1 / 10B2 / 10B3
→ 10C reconciliation
→ artifact manifest
→ 10D deterministic full-integrity verification
→ 11 deterministic TTS export
→ final


## TTS-ready final export

After 10D passes content integrity:

~~~bash
python tools/export_tts_text.py <project>
python tools/validate_tts_export.py <project>
~~~

This creates:
- \`final.txt\` — plain UTF-8 narration ready to paste into a TTS engine;
- \`11_tts_export.json\` — hashes, locale profile, transformations and validation metadata.

Supported profiles:
- Vietnamese (vi)
- English (en)
- German (de)
- French (fr)
- Spanish (es)
- Korean (ko)
- Japanese (ja)

Stage 11 removes non-spoken Markdown/metadata and expands only safe written units such as percentages and Celsius/Fahrenheit. It does not rewrite factual prose or invent phonetic spellings.

## Final statuses

- PASS_VERIFIED
- CONTENT_PASS_ISOLATION_NOT_VERIFIED
- FAIL

## Deterministic verifier — v3.3

~~~bash
python tools/verify_integrity_proof.py \
  --script <project>/10_final_script.md \
  --index <project>/10_final_sentence_index.json \
  --blind <project>/10b1_blind_knowledge_inventory.json \
  --claims <project>/10b2_blind_claim_inventory.json \
  --naturalness <project>/10b3_blind_naturalness_audit.json \
  --integrity <project>/10_final_integrity.json \
  --isolation <project>/10b_isolation_manifest.json \
  --manifest <project>/artifact_manifest.json \
  --evidence <project>/02_evidence_ledger.json \
  --sources <project>/02_sources.json
~~~

The verifier retains a v3.2 compatibility path when the new v3.3 arguments are omitted, so historical regression fixtures remain usable.

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
Chạy pipeline v3.3.
Tạo project mới trong projects/.
Không tự báo PASS_VERIFIED nếu runtime không xác nhận blind isolation.
~~~
