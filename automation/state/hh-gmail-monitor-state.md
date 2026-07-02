# HH Gmail Monitor State

- Last successful scan: 2026-07-03 04:22:18 +07
- Last processed Gmail message id: 19f248268018bf80
- Last processed Gmail internal date: 2026-07-02T23:25:50+03:00
- Last run status: success, processed 1 UZUM rejection/status update and updated 1 HH clarification artifact for an ambiguous same-thread chat rejection; 3 duplicate HH ids skipped

## Notes

This file is updated only after a successful scheduled or manual scan.

Latest successful Pi-primary scan used Pi-local `google_workspace` Gmail read-only access and SQLite runtime dedupe. HH message `19f24808a3ca3ecc` explicitly reported rejection for UZUM TECHNOLOGIES. IT / `Team Lead команды разработки (Payment Mechanics)`, so the monitor updated the existing analysis, `job-intake/INDEX.md`, and `COMPANY_NOTES.md` to closed. HH message `19f248268018bf80` was another same-thread chat rejection without company, vacancy id, location, or role title; the monitor updated `inbox/processed/needs-clarification-2026-07-03-hh-gmail.md` and left the ambiguous Tensor/Saby rows unchanged pending exact vacancy matching.
