# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-02 08:23:44 +07
- Last processed Gmail message id: 19f1f1efb6f351b5
- Last processed Gmail internal date: 2026-07-01T19:19:11Z
- Last run status: success, duplicate/no-op LinkedIn scan; 5 recent LinkedIn ids already processed in SQLite

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. The query returned only already-processed overlap ids, so no LinkedIn bodies were read and no LinkedIn artifacts or Telegram packets were created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
