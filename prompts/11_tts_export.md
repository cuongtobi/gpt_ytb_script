# 11 — TTS EXPORT

## Role

Create the final plain-text narration artifact that can be sent directly to a TTS engine.

This stage is **post-10D** and deterministic.

Preferred execution:

```bash
python tools/export_tts_text.py <project>
```

## Inputs

Required:
- 00_project_brief.yaml
- 10_final_script.md
- 10d_proof_verification.json

10D must have:
- proof_verifier_status = PASS
- project_status = PASS_VERIFIED or CONTENT_PASS_ISOLATION_NOT_VERIFIED

Do not export a project whose content proof failed.

## Outputs

Write:
- final.txt
- 11_tts_export.json

`final.txt` is the direct TTS input.
`10_final_script.md` remains the integrity source of truth.

## Supported languages

Optimized deterministic profiles:
- Vietnamese: vi
- English: en
- German: de
- French: fr
- Spanish: es
- Korean: ko
- Japanese: ja

Regional locale tags such as `en-US`, `de-DE`, `fr-FR`, `es-ES`, `ko-KR`, `ja-JP`, `vi-VN` inherit the base-language profile.

## Transform rules

Allowed transformations are presentation-only:

1. remove Markdown headings;
2. remove horizontal rules;
3. remove bullet/number markers while keeping their spoken text;
4. remove blockquote markers while keeping their spoken text;
5. keep Markdown-link anchor text but remove the URL;
6. remove raw URLs and rich citation tokens;
7. remove inline Markdown code/emphasis markers but keep the words;
8. normalize Unicode to NFC and normalize whitespace;
9. preserve paragraph breaks as natural pauses;
10. expand only locale-safe written units currently supported by the deterministic exporter:
   - percentages;
   - degrees Celsius;
   - degrees Fahrenheit.

Do not:
- translate;
- paraphrase;
- summarize;
- add facts;
- change certainty/scope;
- add SSML;
- insert stage directions;
- invent pronunciation spellings;
- expand arbitrary acronyms;
- spell out arbitrary numbers/years.

If a scientific name, acronym or proper noun needs pronunciation help, fix the narration upstream or use an explicitly configured TTS lexicon outside this deterministic stage. Do not silently alter lexical identity here.

## Locale profiles

### Vietnamese
Prefer normal Vietnamese punctuation and spacing.
Examples:
- `25%` → `25 phần trăm`
- `20 °C` → `20 độ C`

### English
Examples:
- `25%` → `25 percent`
- `20 °C` → `20 degrees Celsius`

### German
Examples:
- `25%` → `25 Prozent`
- `20 °C` → `20 Grad Celsius`

### French
Examples:
- `25%` → `25 pour cent`
- `20 °C` → `20 degrés Celsius`

### Spanish
Examples:
- `25%` → `25 por ciento`
- `20 °C` → `20 grados Celsius`

### Korean
Keep Korean sentence punctuation and spacing.
Examples:
- `25%` → `25 퍼센트`
- `20 °C` → `섭씨 20도`

### Japanese
Preserve Japanese full-width sentence punctuation.
Examples:
- `25%` → `25パーセント`
- `20 °C` → `摂氏20度`

## Content addressing

11_tts_export.json must record SHA-256 for:
- 10_final_script.md
- 10d_proof_verification.json
- 00_project_brief.yaml
- final.txt

The exporter must verify that the current final script matches the released-script hash recorded by 10D when that hash is present.

## Pipeline placement

Stage 11 occurs after 10D.

Because `final.txt` and `11_tts_export.json` are generated after 10D, they are intentionally excluded from `artifact_manifest.json`.

This prevents a circular invalidation chain:
10M manifest → 10D → 11 export.

If 10_final_script.md changes:
rerun the normal final integrity cycle before Stage 11.
