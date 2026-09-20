# v3.2 Fixture Rerun Result

## Status

**CONTENT_PASS_ISOLATION_NOT_VERIFIED**

- Content proof: PASS
- Targeted regression assertions: PASS
- Deterministic verifier: PASS
- Blind isolation verified: NO

## Execution evidence

GitHub Actions run: 35516259457
Head SHA: 0d56f108246c30c2d67997a152210318f0f520fa
Workflow conclusion: success

- recomputed_sentence_count: 90
- discovered_candidate_count: 4
- verifier errors: 0

## Regression targets

- dữ liệu di truyền
- quần thể
- phát tán
- khảo cổ

v3.1 first-use/discovery failures were caught; early genetics wording and omitted academic labels were removed or rewritten.

## Isolation

The current ChatGPT orchestration did not provide runtime-attested fresh model contexts for 10B1/10B2/10B3.

Therefore v3.2 correctly refused `PASS_VERIFIED` and returned:

`CONTENT_PASS_ISOLATION_NOT_VERIFIED`
