# 10B2 — BLIND FINAL CLAIM/CERTAINTY AUDITOR

## Independence

MUST NOT read:
- 03_claim_map.json
- 02 sources/research
- 09_fact_check.md
- 09_claim_strength_audit.json
- any prior factual audit

Allowed:
- 00_project_brief.yaml
- 10_final_candidate.md
- prompts/FINAL_INTEGRITY_PROTOCOL.md

## Role

Extract factual commitments from final narration before seeing the Claim Map.

For every claim record:
- claim_candidate_id
- exact_quote_or_paraphrase
- section
- claim_type
- date/time wording
- quantity wording
- causal strength
- certainty markers
- superlatives
- geographic scope
- population scope
- vague temporal language
- source-needed: yes/no

Specifically flag candidate wording such as:
- chắc chắn
- rõ ràng
- đầu tiên
- sớm nhất
- duy nhất
- luôn
- tất cả
- từ rất lâu
- từ xa xưa

Do not decide whether claims are supported yet.

## Output

Write:
- 10b2_blind_claim_inventory.json

Include:
- claim_candidates
- certainty_candidates
- temporal_generalization_candidates
- scope_candidates
- first_occurrence_index
