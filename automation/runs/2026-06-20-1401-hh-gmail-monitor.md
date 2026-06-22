# HH Gmail Monitor Run - 2026-06-20 14:01 +07

## Status

Success.

## State Read

- Previous last successful scan: 2026-06-20 10:02:16 +07
- Previous last processed Gmail message id: 19edfaa9817fd922
- Previous last processed Gmail internal date: 2026-06-19T11:35:59

## Gmail Scan

- Connector: Gmail available.
- Overlap query used: HH.ru / HeadHunter sender or subject, `after:2026/6/18`, excluding trash and spam.
- Overlap candidates found: 7 messages.
- Newer-than-state sanity query used: HH.ru / HeadHunter sender or subject, `after:2026/6/19`, excluding trash and spam.
- Newer-than-state candidates found: 0 messages.

## Classification

No messages newer than the stored internal-date marker were found.

Overlap messages were all older than `2026-06-19T11:35:59` and were not reprocessed:

| Gmail message id | Email timestamp | Classification | Action |
|---|---:|---|---|
| 19edadb4be6e80c1 | 2026-06-18T13:11:04 | new_vacancy digest / overlap | skipped as already outside scan window |
| 19eda6f65cfaeb72 | 2026-06-18T11:13:13 | status_update / overlap | skipped as already outside scan window |
| 19eda8263e4c5ac1 | 2026-06-18T11:33:58 | status_update / overlap | skipped as already outside scan window |
| 19edad0b6e235de0 | 2026-06-18T12:59:31 | status_update / overlap | skipped as already outside scan window |
| 19edacedaba76790 | 2026-06-18T12:57:29 | status_update / overlap | skipped as already outside scan window |
| 19eda6d6dbb13a35 | 2026-06-18T11:11:04 | status_update / overlap | skipped as already outside scan window |
| 19eda8084b421d86 | 2026-06-18T11:31:55 | status_update / overlap | skipped as already outside scan window |

## Artifact Updates

- No vacancy, job-intake, task, company-note, or inbox artifacts were updated because there were no new HH.ru / HeadHunter messages after the state marker.
- `automation/state/hh-gmail-monitor-state.md` was updated to record this successful scan.

## Gmail Actions

No Gmail labels, stars, importance flags, archive actions, or deletes were changed. This is intentional for unattended runs.

## Git

No Git command was attempted by policy. Scheduled automation durability is this run log plus the updated state marker.
