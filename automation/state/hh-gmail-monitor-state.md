# HH Gmail Monitor State

- Last successful scan: 2026-07-02 12:22:28 +07
- Last processed Gmail message id: 19f1da56fdce89b2
- Last processed Gmail internal date: 2026-07-01T15:26:48+03:00
- Last run status: success, duplicate/no-op HH scan; 3 recent HH ids already processed in SQLite

## Notes

This file is updated only after a successful scheduled or manual scan.

Latest successful Pi-primary scan used Pi-local `google_workspace` Gmail read-only access and SQLite runtime dedupe. The HH primary and fallback queries returned only already-processed overlap ids, so no HH bodies were read and no HH artifacts were changed.
