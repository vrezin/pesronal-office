# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-02 04:29:06 +07
- Last processed Gmail message id: 19f1f1efb6f351b5
- Last processed Gmail internal date: 2026-07-01T19:19:11Z
- Last run status: success, marked 1 LinkedIn Service Marketplace notification as noise; 4 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. One new LinkedIn Service Marketplace notification exposed only a generic request link and no request/JD text, so it was recorded as noise in SQLite and no job-intake artifact or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
