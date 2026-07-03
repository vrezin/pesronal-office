# Pi Job Search Gmail Monitor Run

- Timestamp: 2026-07-01 18:58:56 +0700
- Trigger: scheduled task, Pi Job Search Gmail Monitor
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: unset
- Telegram account: default
- Gmail mutation: none; read-only search only
- Git mutation: none

## Runtime

- Ran `python3 tools/job-search-runtime/job_search_runtime.py init`.
- Ran `python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state`.
- Checked every seen Gmail id with `message-status` before message-specific processing.
- SQLite was the operational dedupe source. All seen ids were already processed, so no Gmail bodies were read and no message-specific artifacts were touched.

## Gmail Queries

- HH primary: `from:(hh.ru OR notification@hh.ru OR no-reply@hh.ru OR noreply@hh.ru) newer_than:7d`
- HH fallback: `(hh.ru OR HeadHunter) newer_than:7d`
- LinkedIn: `from:linkedin.com newer_than:7d`

## Message IDs Seen

### HH

- `19f191abaf5759ab` / thread `19f191abaf5759ab`
- `19f12cd62b56bebe` / thread `19f12cd62b56bebe`
- `19f0d7d179bacbb7` / thread `19f0d7d179bacbb7`

The HH fallback query returned the same three ids.

### LinkedIn

- `19f1ccd893dd5007` / thread `19f1ccd893dd5007`
- `19f1c5f9c902533e` / thread `19f1c5f9c902533e`
- `19f19cc71bda9b7d` / thread `19f19cc71bda9b7d`
- `19f17a756395463d` / thread `19f17a756395463d`
- `19f1739460e5ee68` / thread `19f1739460e5ee68`

## Duplicate / No-op IDs

All seen ids were already present in SQLite with `processed: true`.

### HH

- `19f191abaf5759ab`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.
- `19f12cd62b56bebe`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.
- `19f0d7d179bacbb7`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.

### LinkedIn

- `19f1ccd893dd5007`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.
- `19f1c5f9c902533e`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.
- `19f19cc71bda9b7d`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.
- `19f17a756395463d`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.
- `19f1739460e5ee68`: existing status `noise`; artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`.

## Processed Items

- None. No new message ids were processed.
- No `mark-message` calls were needed because every seen id was already processed.

## Telegram

- No Telegram packet sent.
- Reason: Telegram target is `unset`.
- Intended packets: none; there were no actionable vacancies, invitations, or status updates.

## Blocked Items

- None. Pi-local `google_workspace` Gmail search succeeded.

## Artifacts

- Run log: `automation/runs/2026-07-01-1858-pi-job-search-gmail-monitor.md`
- Message-specific artifacts: none.

## Legacy State

- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.
- Updated `automation/state/linkedin-gmail-monitor-state.md` after successful scan.
