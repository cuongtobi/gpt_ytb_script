# EVIDENCE PROVENANCE PROTOCOL — v3.3

## Purpose

Make factual integrity auditable through an explicit chain:

claim → evidence → source

A source citation by itself is not sufficient provenance for a material factual claim.

## Source records

02_sources.json stores bibliographic/source identity:
- source_id
- title
- authors_or_org
- year
- url_or_locator
- source_type
- publication_date when known
- accessed_or_retrieved_at when relevant
- reliability_note

## Evidence records

02_evidence_ledger.json stores claim-specific support.

Each record:
- evidence_id
- claim_ids
- source_id
- locator
- support_mode: DIRECT | INFERENCE | CONTEXT
- evidence_summary
- limitations
- temporal_scope
- geographic_scope
- population_scope

locator should be the most precise available:
- page;
- section;
- figure/table;
- abstract/result subsection;
- official dataset field;
- stable fragment/record identifier.

Do not fabricate a page/locator that was not actually observed.

## Claim map integration

Every material claim in 03_claim_map.json must contain evidence_ids.

Claim strength fields:
- confidence
- allowed_certainty
- forbidden_strengthening
- time_scope
- geographic_scope
- population_scope

must be justified by the linked evidence.

## Blind claim reconciliation

10B2 discovers factual commitments without seeing the claim map or research evidence.

10C maps each retained factual blind claim to:
- mapped_claim_ids;
- evidence_ids.

If no existing claim/evidence supports the sentence:
- reroute to research/claim mapping;
- add real evidence;
- or rewrite/remove the factual commitment;
- then rerun the final index and all blind audits.

Do not silently create evidence during 10C.

## Machine checks

10D verifies referential integrity:
- mapped claim IDs exist;
- evidence IDs exist;
- evidence claim_ids intersect mapped claim IDs;
- evidence source_id exists in 02_sources.json.

10D cannot independently prove scientific truth from metadata alone.
Semantic support still comes from research/fact-check stages, but the provenance chain and conservation cannot be skipped.
