# Pi Job Search Gmail Monitor Run

- Timestamp: 2026-07-02 00:20:55 +0700
- Trigger: scheduled task, Pi Job Search Gmail Monitor
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `113174019`
- Telegram account: `job-search-telegram`
- Gmail mutation: none; read-only search/read
- Git mutation: none

## Runtime

- Ran `python3 tools/job-search-runtime/job_search_runtime.py init`.
- Ran `python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state`.
- Checked every seen Gmail id with `message-status` before message-specific processing.
- SQLite was the operational dedupe source.

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

- `19f1e8510ae13eee` / thread `19f1e8510ae13eee`
- `19f19cc71bda9b7d` / thread `19f19cc71bda9b7d`
- `19f17a756395463d` / thread `19f17a756395463d`
- `19f1739460e5ee68` / thread `19f1739460e5ee68`
- `19f1581d60e0a0a0` / thread `19f1581d60e0a0a0`

## Duplicate / No-op IDs

These ids were already present in SQLite with `processed: true` and were not read or routed again:

- HH: `19f191abaf5759ab`, `19f12cd62b56bebe`, `19f0d7d179bacbb7`
- LinkedIn: `19f19cc71bda9b7d`, `19f17a756395463d`, `19f1739460e5ee68`

## Processed Items

### LinkedIn Raw Intake

- `19f1e8510ae13eee` - LinkedIn recommended-jobs digest led by Fundraise Up `Head of Product Operations & Automation`, plus Jobgether `Deputy CTO (AI Product)`, Arnold Ash Group, MonetizeMore, RecT Solutions, and Supernal AI.
- `19f1581d60e0a0a0` - LinkedIn recommended-jobs digest led by AllView Real Estate `Director of AI & Systems Architecture`, plus FYST, Fundraise Up, MonetizeMore, W Hunt Espana, and Supernal AI.

Resulting artifact:

- `inbox/processed/2026-07-02-linkedin-thin-ai-leadership-digests.md`

No full job-intake analysis was created because Gmail exposed only thin cards: title, company, location, and LinkedIn job id. There was not enough JD text to select a CV, recommend send/maybe/skip, or create a cover letter.

## Telegram

- Telegram target was configured: `113174019`.
- No Telegram packet sent.
- Intended packets: none.
- Reason: the only new items were thin LinkedIn digests without enough JD text for an actionable vacancy decision packet.

## Blocked Items

- None. Pi-local `google_workspace` Gmail search/read succeeded.

## Artifacts

- Run log: `automation/runs/2026-07-02-0020-pi-job-search-gmail-monitor.md`
- Raw intake: `inbox/processed/2026-07-02-linkedin-thin-ai-leadership-digests.md`

## Legacy State

- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.
- Updated `automation/state/linkedin-gmail-monitor-state.md` after successful scan.
