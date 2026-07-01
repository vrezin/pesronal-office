# HH Gmail Monitor State

- Last successful scan: 2026-07-01 20:27:18 +07
- Last processed Gmail message id: 19f1da56fdce89b2
- Last processed Gmail internal date: 2026-07-01T15:26:48+03:00
- Last run status: success, processed 2 HH status updates and 1 thin HH digest; Видеоглаз closed, one HH chat needs human mapping

## Notes

This file is updated only after a successful scheduled or manual scan.

Latest successful Pi-primary scan used Pi-local `google_workspace` Gmail read-only access and SQLite runtime dedupe. The HH primary and fallback queries returned three new ids plus duplicate overlap. Видеоглаз was closed from an HH rejection. A separate HH employer chat rejection/closure message did not expose company/vacancy in Gmail, so it was written to `inbox/processed/needs-clarification-2026-07-01-hh-gmail.md` for human mapping.
