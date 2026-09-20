# v3.3 Adversarial / Mutation Regression

v3.3 adds fail-closed tests for proof integrity, not only known vocabulary misses.

The automated test suite mutates a valid minimal project and requires 10D to reject:

1. stale B1/B2/B3 script hashes;
2. missing B2 sentence-ledger rows;
3. dropped blind claim dispositions;
4. invalid claim → evidence → source links;
5. unresolved B3 findings;
6. false top-level hard-counter summaries;
7. stale artifact-manifest hashes;
8. incorrect locale segmentation assumptions.

The base fixture itself must return:
- proof_verifier_status = PASS
- project_status = CONTENT_PASS_ISOLATION_NOT_VERIFIED

because its isolation manifest intentionally does not claim runtime-attested fresh contexts.

This keeps the same fail-closed isolation behavior as v3.2 while extending deterministic proof coverage to claim and naturalness lanes.
