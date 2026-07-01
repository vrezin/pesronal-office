# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-01 20:27:18 +07
- Last processed Gmail message id: 19f1da96e6f81e5a
- Last processed Gmail internal date: 2026-07-01T12:31:11Z
- Last run status: success, processed 1 thin LinkedIn job-alert digest as noise; 4 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. One new LinkedIn digest exposed only thin job cards for DAMAC, JPMorganChase, Xapo Bank, Salt, and Arnold Ash Group, with no full JD text or direct recruiter/status signal; it was recorded as noise only. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. Telegram target was unset, and there were no actionable packets to send. No git commit was attempted by policy.
