# LinkedIn Gmail Monitor Run - 2026-06-23 09:56 +07

## Status

Success.

## State Read

- Previous last successful scan: `2026-06-23 08:02:00 +07`
- Previous last processed Gmail message id: `19ef04e89880c7d6`
- Previous last processed Gmail internal date: `2026-06-22T17:08:58`

## Gmail Search

- Query: `from:linkedin.com after:2026/6/22 -in:spam -in:trash`
- Results returned: 4
- New messages newer than stored internal-date marker: 0
- Gmail was read-only. No labels, stars, importance, archive state, or messages were mutated.

## Classification

| Gmail id | Internal date | Subject | Classification | Action |
|---|---:|---|---|---|
| `19ef04e89880c7d6` | `2026-06-22T17:08:58+00:00` | `Компания login.works ищет специалистов: Director of AI Product Management` | overlap / already processed | Exact stored last-processed message; already handled in the 2026-06-23 08:02 run. |
| `19eee7455ec9eab1` | `2026-06-22T08:30:59+00:00` | `Director, Impact Engineering в компании ServiceNow` | overlap / already processed | Older than stored marker; already represented in job-intake. |
| `19eee066f3ec2898` | `2026-06-22T06:30:57+00:00` | `Senior Director, Engineering в компании Relativity` | overlap / already processed | Older than stored marker; already represented in job-intake. |
| `19eed83e76c11897` | `2026-06-22T04:08:22+00:00` | `Kirill только что отправил(а) вам сообщение` | overlap / noise | Older than stored marker; already captured as cold outreach/noise. |

## Artifact Actions

- No vacancy, task, analysis, company-note, or processed-inbox artifacts were updated because there were no new LinkedIn messages beyond the overlap window.
- LinkedIn MCP enrichment was not needed; no new job ids were present.
- No Gmail cleanup was performed by policy.
- No git commit was attempted by policy.

## State Update

- Advanced `automation/state/linkedin-gmail-monitor-state.md` successful scan timestamp to `2026-06-23 09:56:58 +07`.
- Kept last processed Gmail message id and internal date unchanged because the newest returned message was the previous marker.

## Recommended Follow-Up

- None from this run.
