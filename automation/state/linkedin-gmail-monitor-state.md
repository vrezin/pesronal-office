# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-01 18:22:15 +07
- Last processed Gmail message id: 19f1ccd893dd5007
- Last processed Gmail internal date: 2026-07-01T08:30:57Z
- Last run status: success, processed 0 new LinkedIn job artifacts; marked 5 thin LinkedIn job alerts/digests as noise in SQLite

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. Five recent LinkedIn job alerts/digests were returned. They exposed titles, locations, and several LinkedIn job ids, but no full JD text, status change, invitation, or recruiter message, so they were collapsed as noise and recorded only in SQLite/run log. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
