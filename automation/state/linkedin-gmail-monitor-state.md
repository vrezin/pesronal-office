# LinkedIn Gmail Monitor State

- Last successful scan: 2026-07-03 16:25:50 +07
- Last processed Gmail message id: 19f271b115d348ff
- Last processed Gmail internal date: 2026-07-03T08:31:50Z
- Last run status: success, processed 2 new LinkedIn alert emails with registered LinkedIn MCP enrichment; 3 duplicate LinkedIn ids skipped

## Notes

Last successful run scanned `from:linkedin.com newer_than:7d` with a small batch cap through Pi-local `google_workspace` Gmail read-only access. Two new LinkedIn alert emails were enriched with the registered LinkedIn MCP. Revolut `4407473235`, Ingenio Global `4435558976`, and Salesforce `4435869405` returned only title/company/location/status shells, not full JD details. The monitor wrote `inbox/processed/2026-07-03-linkedin-enriched-thin-alerts.md`; no full JD analysis, job-intake index update, CV package, cover letter, or Telegram packet was created. Gmail was read-only; no labels, stars, archive state, read state, or messages were mutated. No git commit was attempted by policy.
