# HH Gmail Monitor Run

- Run time: 2026-06-22 08:05:09 +0700
- Mode: unattended cron
- Status: blocked

## State Read

Read `automation/state/hh-gmail-monitor-state.md`.

- Last successful scan: 2026-06-21 22:00:45 +07
- Last processed Gmail message id: 19ee9572b9b618af
- Last processed Gmail internal date: 2026-06-21T08:41:04
- Previous status: success with fallback

## Gmail Scan

Attempted Gmail connector search with a June 21 overlap:

```text
{from:hh.ru from:headhunter.ru from:headhunter subject:hh.ru subject:HeadHunter "hh.ru" "HeadHunter" "Хедхантер"} after:2026/6/21 -in:spam -in:trash
```

The Gmail connector was unavailable. The MCP server failed during startup with HTTP 403 while initializing the Gmail client.

## Classification

No messages were scanned or classified because Gmail access was unavailable.

- `status_update`: not processed
- `invitation`: not processed
- `new_vacancy`: not processed
- `noise`: not processed

## Repository Updates

No vacancy, task, job-intake, company-note, or Gmail artifacts were updated.

`automation/state/hh-gmail-monitor-state.md` was intentionally left unchanged because the scan did not succeed.

## Git

No commit was attempted by scheduled-monitor policy.

## Follow-Up

Reconnect or unblock Gmail connector access, then rerun the monitor from the unchanged state marker.
