# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-03 00:30:31 +07
- Last processed Gmail message id: 19f233dc54d1f2ba
- Last processed Gmail internal date: 2026-07-02T14:31:14Z
- Last run status: success, processed 1 thin LinkedIn Axway Director Engineering alert; 4 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. One thin Axway Director, Engineering alert for Dublin was recorded in `inbox/processed/2026-07-03-linkedin-thin-axway-director-engineering-alert.md`; no full JD analysis, job-intake index update, or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
