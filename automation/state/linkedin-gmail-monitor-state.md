# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-02 17:52:59 +07
- Last processed Gmail message id: 19f2261db60003a6
- Last processed Gmail internal date: 2026-07-02T10:31:05Z
- Last run status: success, recorded 1 duplicate LinkedIn Dr.Head job alert; 4 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. One Dr.Head job alert repeated a job id already captured from the application confirmation and was recorded as duplicate/no-op in `inbox/processed/2026-07-02-linkedin-application-status-updates.md`. No full JD analysis or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
