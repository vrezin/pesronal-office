# HH Gmail Monitor Run

Run started: 2026-06-23 14:00:38 +07
Run finished: 2026-06-23 14:02:01 +07
Mode: unattended scheduled run

## State Before Run

- Last successful scan: 2026-06-23 09:55:11 +07
- Last processed Gmail message id: `19ef02ca444bdd43`
- Last processed Gmail internal date: 2026-06-22T16:31:57
- Last run status: success, processed 0 new HH messages; checked 8 overlap messages

## Gmail Search

Primary overlap/new-message queries:

- `(from:noreply@hh.ru OR from:hh.ru OR from:headhunter OR "HeadHunter" OR "hh.ru") after:2026/6/22 -in:spam -in:trash`
- `from:noreply@hh.ru after:2026/6/22 -in:spam -in:trash`
- `from:hh.ru after:2026/6/22 -in:spam -in:trash`
- `HeadHunter after:2026/6/22 -in:spam -in:trash`
- `hh.ru after:2026/6/22 -in:spam -in:trash`
- `from:noreply@hh.ru newer:2026/6/22 -in:spam -in:trash`
- `from:noreply@hh.ru after:2026/6/21 -in:spam -in:trash`
- `from:noreply@hh.ru newer_than:2d -in:spam -in:trash`

Result: 0 current non-trash HH-like messages found after the saved state marker.

Sanity queries:

- `from:noreply@hh.ru newer_than:7d -in:spam -in:trash`
- `hh newer_than:7d -in:spam -in:trash`
- `HeadHunter newer_than:7d -in:spam -in:trash`

Result: recent HH-like matches existed in the mailbox, but the newest non-trash HH results returned by the broad sender/text sanity checks were from 2026-06-18. They are older than the saved state marker and were treated as historical overlap/noise for this run.

The saved last-processed Gmail id `19ef02ca444bdd43` was read directly. It is a 2026-06-22 HH status-update message with labels `UNREAD`, `IMPORTANT`, `TRASH`, and `CATEGORY_UPDATES`. Because it is currently in Trash, the normal `-in:trash` monitor searches correctly omit it. No Gmail labels, stars, importance flags, archive state, or trash state were changed during this unattended run.

## Classification

| Gmail id | Timestamp | Classification | Action |
|---|---:|---|---|
| `19ef02ca444bdd43` | 2026-06-22T16:31:57 | `status_update` | State-marker verification only. Already handled by earlier monitor runs; currently in Gmail Trash. No repo change. |
| Recent HH sender/text matches | 2026-06-18 and older | historical overlap | Older than state marker. No repo change. |

## Repository Writes

- Created this run log.
- Updated `automation/state/hh-gmail-monitor-state.md` with the successful scan timestamp.

No vacancy, task, analysis, index, company-notes, or inbox artifact was changed because the scan found no new current HH messages after the prior successful state marker.

## Gmail Actions

No Gmail labels, stars, importance markers, archives, or deletes were changed. This is intentional for unattended runs.

Recommended Gmail action: none for this run.

## Git

No Git commit was attempted by policy. Scheduled automation durability is this run log plus the updated state marker.

## Outcome

Success. Processed 0 new HH messages and checked recent HH overlap/sanity results.
