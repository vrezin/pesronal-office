# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-02 20:28:39 +07
- Last processed Gmail message id: 19f21faa18a56d48
- Last processed Gmail internal date: 2026-07-02T08:38:19Z
- Last run status: success, duplicate-only scan; 5 LinkedIn ids skipped by SQLite dedupe

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. No new LinkedIn messages were processed; all seen ids were already present in SQLite. No full JD analysis, handoff requiring user reply, or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
