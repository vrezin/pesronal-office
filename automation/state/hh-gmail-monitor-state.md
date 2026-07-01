# HH Gmail Monitor State

- Last successful scan: 2026-07-01 18:58:56 +07
- Last processed Gmail message id: 19f191abaf5759ab
- Last processed Gmail internal date: 2026-06-30T18:16:49+03:00
- Last run status: success, duplicate/no-op scan; 3 recent HH ids already processed as noise in SQLite

## Notes

This file is updated only after a successful scheduled or manual scan.

Latest successful Pi-primary scan used Pi-local `google_workspace` Gmail read-only access and SQLite runtime dedupe. The HH primary and fallback queries both returned the same three recent similar-vacancy digests already recorded by the previous run, so no Gmail bodies were read and no job artifacts were changed.
