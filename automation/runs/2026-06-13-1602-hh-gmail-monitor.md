# HH Gmail Monitor Run

- Run started: 2026-06-13 16:02:00 +0700
- Mode: unattended cron
- State before run:
  - Last successful scan: 2026-06-13 12:01:36 +07
  - Last processed Gmail message id: 19ebaf3c69f4503f
  - Last processed Gmail internal date: 2026-06-12T08:29:57
- Gmail access: available

## Search

Used a small overlap window from 2026-06-11/2026-06-12 to avoid missing delayed HH.ru / HeadHunter messages.

Queries attempted:

- `(from:(hh.ru) OR from:(headhunter) OR from:(noreply@hh.ru) OR from:(no-reply@hh.ru) OR from:(info@hh.ru) OR HeadHunter OR hh.ru) after:2026/6/12 -in:spam -in:trash`
- `(from:(hh.ru) OR from:(headhunter) OR from:(noreply@hh.ru) OR from:(no-reply@hh.ru) OR from:(info@hh.ru) OR HeadHunter OR hh.ru) after:2026/6/11 -in:spam -in:trash`
- `from:hh.ru newer_than:7d -in:spam -in:trash`
- `from:noreply@hh.ru newer_than:7d -in:spam -in:trash`
- `HeadHunter newer_than:7d -in:spam -in:trash`
- `hh.ru newer_than:7d -in:spam -in:trash`

## Results

- Relevant messages found: 0
- Classified messages:
  - `status_update`: 0
  - `invitation`: 0
  - `new_vacancy`: 0
  - `noise`: 0
- Gmail mutations: none
- Recommended Gmail actions: none

## Artifact Updates

- No vacancy, task, analysis, index, or company-note artifacts required updates because no relevant HH.ru / HeadHunter messages were found.
- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.

## Notes

- The repository had pre-existing uncommitted HH / Personal Brand changes before this run. This monitor run only changed its own run log and state marker.
- Run status: success
