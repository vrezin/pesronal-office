# HH Gmail Monitor Run

- Run started: 2026-06-13 12:01:36 +07
- Mode: unattended cron
- Previous successful scan: 2026-06-13 08:01:12 +07
- Previous last processed Gmail message id: `19ebaf3c69f4503f`
- Previous last processed Gmail internal date: 2026-06-12T08:29:57
- Gmail access: available
- Gmail mutations: not performed
- Result: success

## Search Window

Used a small overlap from 2026-06-12 to avoid missing delayed messages.

Queries attempted:

1. `{from:hh.ru from:noreply@hh.ru from:no-reply@hh.ru from:headhunter subject:(HH.ru) subject:(HeadHunter) subject:(hh.ru)} after:2026/6/12 -in:spam -in:trash`
2. `(hh OR hh.ru OR HeadHunter OR Хедхантер OR hh@) after:2026/6/12 -in:spam -in:trash`
3. `from:(hh.ru) newer_than:3d -in:spam -in:trash`

## Messages

No HH.ru / HeadHunter messages were found in Gmail for the overlap window.

## Classification

- `status_update`: 0
- `invitation`: 0
- `new_vacancy`: 0
- `noise`: 0

## Repository Updates

- Updated `automation/state/hh-gmail-monitor-state.md` with the successful scan timestamp.
- No vacancy, task, analysis, index, or company-note artifacts were changed.

## Limitations

- None. Gmail search was available and returned no matching messages.
