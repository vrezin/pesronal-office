# HH Gmail Monitor Run - 2026-06-14 20:00 +07

## Status

success

## State Before Run

- Last successful scan: 2026-06-14 16:00:00 +07
- Last processed Gmail message id: 19ec53a066478a26
- Last processed Gmail internal date: 2026-06-14T08:22:53

## Gmail Search

- Query: `(from:(hh.ru) OR from:(headhunter) OR from:(noreply@hh.ru) OR from:(hh@hh.ru) OR from:(no-reply@hh.ru) OR subject:(hh.ru) OR subject:(HeadHunter)) after:2026/6/13 -in:trash -in:spam`
- Result count: 2
- Message ids: 19ec53a066478a26, 19ec0d3d9c40220d

## Classification

| Gmail message id | Internal date | Classification | Action |
|---|---:|---|---|
| 19ec53a066478a26 | 2026-06-14T08:22:53 | overlap / already processed new_vacancy digest | No repo artifact changes; matches existing state marker. |
| 19ec0d3d9c40220d | 2026-06-13T11:52:49 | overlap / older new_vacancy digest | No repo artifact changes; older than state marker. |

## Artifact Updates

- No `tasks/active/`, `tasks/waiting/`, `job-intake/`, or `inbox/processed/` artifacts were changed because no new messages were found after the state marker.
- Gmail labels, stars, and importance were not mutated during this unattended run.

## State After Run

- Last successful scan should advance to: 2026-06-14 20:00:00 +07
- Last processed Gmail message id remains: 19ec53a066478a26
- Last processed Gmail internal date remains: 2026-06-14T08:22:53

## Notes

- Gmail connector access was available.
- The search used an overlap window beginning 2026-06-13 to avoid missing delayed messages.
