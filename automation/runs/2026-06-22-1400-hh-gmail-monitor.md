# HH Gmail Monitor Run

- Run time: 2026-06-22 14:00:43 +0700
- Mode: unattended cron
- Status: success, no new HH mail

## State Read

Read `automation/state/hh-gmail-monitor-state.md`.

- Last successful scan: 2026-06-21 22:00:45 +07
- Last processed Gmail message id: `19ee9572b9b618af`
- Last processed Gmail internal date: `2026-06-21T08:41:04`
- Previous status: success with fallback

## Gmail Scan

Gmail connector was available. The monitor used a June 21 overlap and then narrowed the search to confirm no HH mail was missed after the state marker.

Searches attempted:

```text
(from:hh.ru OR from:headhunter.ru OR from:noreply@hh.ru OR from:no-reply@hh.ru OR from:notification@hh.ru OR HeadHunter OR HH.ru) after:2026/6/20 -in:spam -in:trash
from:(hh.ru) newer_than:3d -in:spam -in:trash
HH.ru newer_than:3d -in:spam -in:trash
HeadHunter newer_than:3d -in:spam -in:trash
hh newer_than:3d -in:spam -in:trash
from:noreply@hh.ru newer_than:7d -in:spam -in:trash
from:noreply@hh.ru after:2026/6/21 -in:spam -in:trash
from:noreply@hh.ru newer_than:1d -in:spam -in:trash
from:noreply@hh.ru after:2026/6/20 -in:spam -in:trash
from:noreply@hh.ru newer_than:2d -in:spam -in:trash
```

The only non-empty result set was `from:noreply@hh.ru newer_than:7d`, which returned older overlap messages from 2026-06-16 through 2026-06-18. Those messages are older than the state marker and were not reprocessed. Some old overlap reads hit Gmail rate limiting, but this did not affect the current scan because all returned readable message timestamps were before the last successful scan and the narrower June 20/21 searches returned no messages.

## Classification

No messages newer than the state marker were found.

- `status_update`: 0
- `invitation`: 0
- `new_vacancy`: 0
- `noise`: 0
- skipped old overlap: older `noreply@hh.ru` messages from 2026-06-16 to 2026-06-18

## Repository Updates

No vacancy, task, job-intake, company-note, raw inbox, processed inbox, or Gmail artifacts required updates.

Updated `automation/state/hh-gmail-monitor-state.md` after the successful no-new-mail scan.

## Gmail Actions

No Gmail labels, stars, importance markers, archive state, or trash state were mutated during this unattended run.

## Git

No commit was attempted by scheduled-monitor policy. The run log and state marker are the durability contract for unattended HH Gmail runs.

## Follow-Up

None. Continue from the new scan marker on the next scheduled run.
