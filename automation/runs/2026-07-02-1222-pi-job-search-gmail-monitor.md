# Pi Job Search Gmail Monitor Run

- Timestamp: 2026-07-02 12:22:28 +0700
- Trigger: scheduled task, Pi Job Search Gmail Monitor
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `113174019`
- Telegram account: `job-search-telegram`
- Gmail account: `v.rezin@gmail.com`
- Gmail mutation: none; read-only search/read
- Git mutation: none

## Runtime

- Ran `python3 tools/job-search-runtime/job_search_runtime.py init`.
- Ran `python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state`.
- Used the wrapper-held SQLite lock `pi-job-search-gmail-monitor` owner `2026-07-02-1219-1652304`.
- Checked every seen Gmail id with `message-status` before message-specific processing.
- SQLite was the operational dedupe source.

Runtime status after marking:

```text
Processed messages:
- hh needs_human: 1
- hh noise: 4
- hh processed: 1
- hh seeded_from_markdown_state: 1
- linkedin noise: 7
- linkedin processed: 3
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

- `19f21181ab1eddb0` / thread `19f21181ab1eddb0`
- `19f1e8510ae13eee` / thread `19f1e8510ae13eee`
- `19f19cc71bda9b7d` / thread `19f19cc71bda9b7d`
- `19f17a756395463d` / thread `19f17a756395463d`
- `19f1739460e5ee68` / thread `19f1739460e5ee68`

## Duplicate / No-op IDs

These ids were already present in SQLite with `processed: true` and were not read or routed again:

- HH: `19f191abaf5759ab`, `19f12cd62b56bebe`, `19f0d7d179bacbb7`
- LinkedIn: `19f1e8510ae13eee`, `19f19cc71bda9b7d`, `19f17a756395463d`, `19f1739460e5ee68`

## Processed Items

### LinkedIn Raw Intake

- Gmail message id: `19f21181ab1eddb0`
- Subject: `Новые вакансии, похожие на вакансию «Engineering Manager (Localization)» в компании Scorewarrior`
- Sender: `LinkedIn <jobs-noreply@linkedin.com>`
- Date: `Thu, 2 Jul 2026 04:30:55 +0000 (UTC)`
- Classification: `new_vacancy`
- Status: `processed`
- Artifact: `inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md`

The message was a LinkedIn similar-jobs digest with thin job cards only. Captured cards:

- Viaquant Partners - Engineering Manager - Limassol - `4431600451`
- TradingView - Engineering Manager - Limassol - `4321499520`
- Scorewarrior - Engineering Manager - Limassol - `4433864043`
- TradingView - Engineering Manager - Paphos - `4402795044`
- eToro - BizOps Squad Lead (Agentic AI) - Limassol - `4408677331`
- Kraken - Data Platform Engineering Manager - Cyprus - `4405362009`
- Pepperstone - Engineering Manager - Trading Platforms - Limassol - `4414605769`
- Wheely - Tech Lead Manager - Nicosia - `4361543848`
- Azul - Software Engineering Manager for Optimizer Hub - Limassol - `4429831647`
- XM - Platform Engineer Team Lead - Limassol - `4422705511`

No full JD analysis, CV selection, cover letter, `job-intake/INDEX.md`, or `COMPANY_NOTES.md` update was made because the email did not include responsibilities, requirements, compensation, remote/legal setup, or enough JD text.

SQLite command run:

```bash
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f21181ab1eddb0 --classification new_vacancy --status processed --artifact-path inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md --notes "Thin LinkedIn similar-jobs digest for Cyprus engineering-manager roles; raw intake only, no full JD or actionable Telegram packet."
```

## Telegram

- Telegram target was configured: `113174019`.
- No Telegram packet sent.
- Intended packets: none.
- Reason: the only new item was a thin LinkedIn digest without enough JD text for an actionable vacancy decision packet.

## Blocked Items

- None. Pi-local `google_workspace` Gmail search/read succeeded.

## Artifacts

- Run log: `automation/runs/2026-07-02-1222-pi-job-search-gmail-monitor.md`
- Raw intake: `inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md`

## Legacy State

- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.
- Updated `automation/state/linkedin-gmail-monitor-state.md` after successful scan.
