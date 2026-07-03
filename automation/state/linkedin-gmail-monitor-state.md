# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-03 08:28:37 +07
- Last processed Gmail message id: 19f233dc54d1f2ba
- Last processed Gmail internal date: 2026-07-02T14:31:14Z
- Last run status: success, no new LinkedIn ids; 5 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. All 5 returned LinkedIn ids were already present in SQLite and treated as duplicate/no-op. No full JD analysis, job-intake index update, or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
