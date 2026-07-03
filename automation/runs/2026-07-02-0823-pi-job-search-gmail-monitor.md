# Pi Job Search Gmail Monitor Run

- Timestamp: 2026-07-02 08:23:44 +0700
- Trigger: scheduled task, Pi Job Search Gmail Monitor
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `113174019`
- Telegram account: `job-search-telegram`
- Gmail account: `v.rezin@gmail.com`
- Gmail mutation: none; read-only search only
- Git mutation: none

## Runtime

- Ran `python3 tools/job-search-runtime/job_search_runtime.py init`.
- Ran `python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state`.
- Used the wrapper-held SQLite lock `pi-job-search-gmail-monitor` owner `2026-07-02-0821-2269206`.
- Checked every seen Gmail id with `message-status` before message-specific processing.
- SQLite was the operational dedupe source.

Runtime status:

```text
Processed messages:
- hh needs_human: 1
- hh noise: 4
- hh processed: 1
- hh seeded_from_markdown_state: 1
- linkedin noise: 7
- linkedin processed: 2
- linkedin seeded_from_markdown_state: 1
```

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

- `19f1f1efb6f351b5` / thread `19f1f1efb6f351b5`
- `19f1e8510ae13eee` / thread `19f1e8510ae13eee`
- `19f19cc71bda9b7d` / thread `19f19cc71bda9b7d`
- `19f17a756395463d` / thread `19f17a756395463d`
- `19f1739460e5ee68` / thread `19f1739460e5ee68`

## Duplicate / No-op IDs

All seen ids were already present in SQLite with `processed: true`:

- HH: `19f191abaf5759ab`, `19f12cd62b56bebe`, `19f0d7d179bacbb7`
- LinkedIn: `19f1f1efb6f351b5`, `19f1e8510ae13eee`, `19f19cc71bda9b7d`, `19f17a756395463d`, `19f1739460e5ee68`

No message bodies were read. No message-specific artifacts were created or updated.

## Processed Items

- None. This was a duplicate/no-op scan.

## Telegram

- Telegram target was configured: `113174019`.
- No Telegram packet sent.
- Intended packets: none.
- Reason: no new actionable vacancy, invitation, or status-changing item was found.

## Blocked Items

- None. Pi-local `google_workspace` Gmail search succeeded.

## Artifacts

- Run log: `automation/runs/2026-07-02-0823-pi-job-search-gmail-monitor.md`

## Legacy State

- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.
- Updated `automation/state/linkedin-gmail-monitor-state.md` after successful scan.
