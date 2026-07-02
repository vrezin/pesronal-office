# HH Gmail Monitor State

- Last successful scan: 2026-07-03 00:30:31 +07
- Last processed Gmail message id: 19f2344884afb3be
- Last processed Gmail internal date: 2026-07-02T17:38:41+03:00
- Last run status: success, wrote 1 HH clarification artifact for 2 ambiguous Tensor/Saby status-update messages; 3 duplicate HH ids skipped

## Notes

This file is updated only after a successful scheduled or manual scan.

Latest successful Pi-primary scan used Pi-local `google_workspace` Gmail read-only access and SQLite runtime dedupe. Two new HH messages reported a Tensor/Saby rejection/closed-position status, but the email did not expose a vacancy id or location and multiple similar Tensor rows exist. The monitor wrote `inbox/processed/needs-clarification-2026-07-03-hh-gmail.md` and left `job-intake/INDEX.md` unchanged pending exact vacancy matching.
