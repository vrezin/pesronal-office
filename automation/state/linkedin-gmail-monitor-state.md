# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-01 18:58:56 +07
- Last processed Gmail message id: 19f1ccd893dd5007
- Last processed Gmail internal date: 2026-07-01T08:30:57Z
- Last run status: success, duplicate/no-op scan; 5 recent LinkedIn ids already processed as noise in SQLite

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. Five recent LinkedIn job alerts/digests were returned and were already recorded by the previous run, so no Gmail bodies were read and no job artifacts were changed. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. Telegram target was unset, and there were no actionable packets to send. No git commit was attempted by policy.
