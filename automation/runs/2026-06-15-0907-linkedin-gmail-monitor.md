# LinkedIn Gmail Monitor Run - 2026-06-15 09:07 +07

## Status

Success. Gmail was available, the scan completed, and no new post-marker LinkedIn messages required routing.

## Scan

- State marker before run: `2026-06-15 00:01:30 +07`
- Last processed Gmail message id before run: `19ec6f8dd2354e86`
- Last processed Gmail internal date before run: `2026-06-14T16:30:55`
- Gmail query: `from:linkedin.com after:2026/6/14 -in:spam -in:trash`
- Overlap messages returned: 3
- New messages after saved marker: 0

## Classification

| Gmail id | Gmail timestamp | Subject | Classification | Action |
|---|---:|---|---|---|
| `19ec543614d183c0` | `2026-06-14T08:33:05` | `Senior Director, Data Platform and AI в компании Oyster®` | `new_vacancy` | Overlap duplicate; older than saved marker and already represented in job-intake. |
| `19ec4d37face4463` | before saved marker | `FS Technology Consulting - Engineering Lead, Features Team- Director - Dublin в компании EY` | `new_vacancy` | Overlap duplicate; older than saved marker and already represented in job-intake. |
| `19ec465a43721708` | `2026-06-14T04:30:55` | `Новые вакансии, похожие на вакансию «Director of Platform Engineering» в компании Overstory` | `new_vacancy` | Overlap duplicate; older than saved marker and already represented in earlier monitor artifacts. |

## Artifact Changes

- Updated `automation/state/linkedin-gmail-monitor-state.md` with the successful scan time.
- No job-intake, task, waiting, or processed-inbox artifacts changed because there were no new post-marker LinkedIn messages.

## Gmail Cleanup

No Gmail labels, stars, importance markers, or archive state were changed.

## Limitations

- The Gmail connector returned the EY message with a very large body; the exact timestamp was not necessary for routing because the message was still before the saved successful marker.
