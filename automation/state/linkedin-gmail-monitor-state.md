# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-02 12:22:28 +07
- Last processed Gmail message id: 19f21181ab1eddb0
- Last processed Gmail internal date: 2026-07-02T04:30:55Z
- Last run status: success, processed 1 thin LinkedIn similar-jobs digest into raw intake; 4 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. One new LinkedIn similar-jobs digest exposed only thin Cyprus engineering-manager job cards and was captured in `inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md`; no full JD analysis or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
