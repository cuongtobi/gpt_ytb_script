# v3.3 Multilingual 10-Minute Regression — Results

Date: 2026-09-20

Topic held constant across all languages:
**Why Do Onions Make Us Cry?**

Languages:
- English (en)
- French (fr)
- German (de)
- Spanish (es)
- Korean (ko)
- Japanese (ja)

The same evidence/claim spine was used across all six fixtures so the main variable is language behavior.

## Final CI run

GitHub Actions run: **35521576090**

All jobs completed successfully:
- v3.3 adversarial suite — SUCCESS
- v3.2 Birds regression — SUCCESS
- v3.2 Maize regression — SUCCESS
- v3.2 Seawater regression — SUCCESS
- English multilingual fixture — SUCCESS
- French multilingual fixture — SUCCESS
- German multilingual fixture — SUCCESS
- Spanish multilingual fixture — SUCCESS
- Korean multilingual fixture — SUCCESS
- Japanese multilingual fixture — SUCCESS

Every multilingual 10D run returned:
- `proof_verifier_status = PASS`
- `project_status = CONTENT_PASS_ISOLATION_NOT_VERIFIED`
- `isolation_verified = false`
- `errors = []`

This is the correct fail-closed status because fresh-context runtime isolation was not available.

## Final fixture sizes

| Language | Locale | Canonical sentences | Whitespace tokens | Characters | B1 candidates | B2 claims | 10D |
|---|---|---:|---:|---:|---:|---:|---|
| English | en | 87 | 1213 | 7510 | 5 | 10 | PASS |
| French | fr | 92 | 1354 | 8781 | 5 | 10 | PASS |
| German | de | 92 | 1190 | 8753 | 5 | 10 | PASS |
| Spanish | es | 92 | 1363 | 8610 | 5 | 10 | PASS |
| Korean | ko | 92 | 985 | 4007 | 5 | 10 | PASS |
| Japanese | ja | 93 | 113 | 3400 | 5 | 10 | PASS |

Important: whitespace-token counts are not a valid cross-language duration metric, especially for Japanese.

## What worked

### 1. Locale-aware sentence segmentation

Japanese full-width sentence punctuation (`。！？`) was segmented correctly.
The final Japanese fixture contains 93 canonical sentences and passed exact index reconstruction.

Korean also passed with the locale-aware segmenter.

### 2. Content-addressing / stale-audit detection

During the diagnostic repair pass, only `10_final_candidate.md` was edited first.

The following CI runs failed immediately because index/audit hashes were stale:
- 35521456282
- 35521459896
- 35521463383
- 35521466901

After regenerating sentence indexes, B1/B2/B3, integrity records and manifests, run 35521576090 passed.

This is expected behavior and confirms the v3.3 stale-audit defense works.

### 3. Schema validation

All six projects passed `tools/validate_project_artifacts.py`.

The source/evidence/claim/index/audit/integrity/manifest schemas therefore work with:
- Latin-script languages;
- Korean;
- Japanese Unicode content.

### 4. Claim and knowledge conservation mechanics

Final fixtures contain:
- 5 knowledge candidates per language;
- 10 blind factual claims per language;
- exact candidate/claim disposition conservation;
- zero unresolved candidates;
- zero unresolved claims;
- valid evidence → source references.

### 5. Backward compatibility

Adding multilingual v3.3 regression did not break the three v3.2 fixtures.

## Problems found during the first pass

The first machine-verifiable run passed all six languages, but manual semantic review found important false negatives.

### Finding A — B1 can still miss a real knowledge-bearing term

Examples from the initial fixtures:
- English: `volatile`
- German: `flüchtige`
- Spanish: `volátil`
- Korean: `휘발성`
- Japanese: `揮発性`
- French also contained the ungrounded label `Allium`

These phrases occurred in the released scripts but were absent from the B1 candidate inventory.

10D still passed because it can prove candidate conservation only for candidates the semantic auditor actually discovered.

Repair:
- avoidable `volatile` labels were removed and replaced with plain descriptions such as “can readily enter the air”;
- the unnecessary French `Allium` label was removed;
- the final B1 inventories were regenerated.

### Finding B — B2 can still miss a factual commitment

The initial scripts contained the recommendation/claim that a sharp knife reduces crushing compared with a blunt knife.

That sentence had:
`claim_candidate_ids = []`

in all six initial B2 ledgers.

10D still passed because sentence coverage proves that a row exists; it cannot deterministically know that a factual statement inside a row was missed.

Repair:
- the weakly evidenced sharp-knife claim was removed rather than defended with a weak source;
- ventilation was retained as a sourced exposure-reduction claim;
- variation in onion material / human sensitivity was added to the claim/evidence map;
- final B2 inventories contain 10 conserved claims per language.

### Finding C — B3 conservation is not the same as native-language quality

Initial B3 ledgers had no findings, yet manual review found wording that was understandable but not fully native/natural, for example:
- French: `des molécules très réactives et très brèves`
- German: `scharfe Chemie`
- Spanish: `la même intensidad de compuestos picantes`
- Korean: `황 화학`, `화학 생산라인`
- Japanese: `硫黄化学`, `防御化学`, `高速の化学反応ライン`

These were repaired with language-native wording before the final run.

Conclusion:
10D can verify that B3 findings are conserved and resolved.
It cannot independently judge whether B3 failed to notice awkward language.

## Remaining design limitations

### 1. Semantic completeness remains probabilistic

Forward + reverse sentence ledgers reduce omission risk, but a semantic auditor can still put an empty array in a sentence that actually contains:
- an unfamiliar concept;
- a factual commitment;
- an unnatural phrase.

The deterministic verifier cannot infer arbitrary semantics from prose.

This remains the most important false-PASS risk after v3.3.

### 2. Duration is not locale-safe yet

The current pipeline can check a requested duration editorially, but it has no deterministic locale-aware duration proof.

A whitespace word count is useful for English/French/German/Spanish, partially useful for Korean depending on the chosen unit, and nearly meaningless for Japanese.

Recommended next change:
store a declared duration measurement method in the project brief, for example:
- words for space-delimited languages;
- eojeol or characters for Korean;
- characters/mora-aware estimate for Japanese;
- explicit project-specific delivery-rate range rather than one global WPM assumption.

### 3. Naturalness cannot be proven by counters alone

Language-native B3 is still an LLM semantic judgment.
A zero-finding ledger is evidence that the auditor reported no issue, not mathematical proof that the prose is native-quality.

Recommended next change:
add language-specific naturalness profiles for en/fr/de/es/ko/ja and retain a multilingual regression corpus with known calque/translationese failures.

### 4. Evidence semantic truth is still not independently proven by 10D

v3.3 correctly proves:
`blind claim → mapped claim → evidence ID → source ID`.

It does not independently reread the scientific paper and prove that the evidence summary semantically entails the narration.
That remains the job of research/fact-check stages.

## Overall result

### Structural / proof-engine result
**PASS for all six languages.**

### Language-quality result
After the repair pass:
- English: good
- French: good
- German: good
- Spanish: good
- Korean: good, but should keep a strong anti-calque pass
- Japanese: good, and full-width sentence segmentation works correctly

### Final assessment

v3.3 works substantially better across the six tested languages and the new content-addressing layer works as intended.

However, `PASS` should still be interpreted as:
**the recorded proofs are internally consistent and complete with respect to what the semantic auditors discovered**,

not:
**the verifier can mathematically guarantee that the semantic auditors discovered every possible term, claim or naturalness issue.**
