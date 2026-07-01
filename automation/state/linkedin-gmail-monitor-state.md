# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-02 00:20:55 +07
- Last processed Gmail message id: 19f1e8510ae13eee
- Last processed Gmail internal date: 2026-07-01T16:31:01Z
- Last run status: success, processed 2 thin LinkedIn recommended-job digests into raw intake; 3 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. Two new LinkedIn recommended-job digests exposed only thin job cards and were captured in `inbox/processed/2026-07-02-linkedin-thin-ai-leadership-digests.md`; no full JD analysis or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
