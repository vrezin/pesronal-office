# Pi Job Search Gmail Monitor Run

- Timestamp: 2026-07-02 16:27:11 +0700
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
- Used the wrapper-held SQLite lock `pi-job-search-gmail-monitor` owner `2026-07-02-1623-1205654`.
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
- linkedin processed: 8
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

- `19f21faa18a56d48` / thread `19f21faa18a56d48`
- `19f21f3f0697f7ec` / thread `19f21f3f0697f7ec`
- `19f21e3d77f5ca26` / thread `19f21e3d77f5ca26`
- `19f21ba7638665c1` / thread `19f21ba7638665c1`
- `19f219e32a21d867` / thread `19f219e32a21d867`

## Duplicate / No-op IDs

These ids were already present in SQLite with `processed: true` and were not read or routed again:

- HH: `19f191abaf5759ab`, `19f12cd62b56bebe`, `19f0d7d179bacbb7`
- LinkedIn: none in the first five-message LinkedIn slice

## Processed Items

### LinkedIn Application / Status Updates

Artifact: `inbox/processed/2026-07-02-linkedin-application-status-updates.md`

- `19f21faa18a56d48` - `status_update` / `processed`: Jobgether Deputy CTO (AI Product), application submitted on 2026-07-02, LinkedIn job id `4432340752`.
- `19f21e3d77f5ca26` - `status_update` / `processed`: GRS Recruitment application viewed; the email body did not expose the role or job id.
- `19f21ba7638665c1` - `status_update` / `processed`: Techyons application viewed; the email body did not expose the role or job id.
- `19f219e32a21d867` - `status_update` / `processed`: Dr.Head `Директор по ИТ`, application submitted on 2026-07-02, LinkedIn job id `4434956568`.

No matched full analysis was updated because these messages did not provide enough role/JD detail to safely link to an existing `job-intake/analyses/*.md` file.

### LinkedIn Raw Intake

Artifact: `inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md`

- `19f21f3f0697f7ec` - `new_vacancy` / `processed`: LinkedIn `Software Engineering Director` alert led by Jobgether `Deputy CTO (AI Product)` roles.
- Captured thin cards: Jobgether Deputy CTO UAE `4432340752`, Jobgether Deputy CTO Switzerland `4432336894`, JPMorganChase Generative AI Director `4338683379`, UMATR Head of Engineering `4431229028`, JPMorganChase AI/ML Director `4369095406`, Teklens Head of Engineering / Co-Founder `4435541191`.

No full JD analysis, CV selection, cover letter, `job-intake/INDEX.md`, or `COMPANY_NOTES.md` update was made for the alert because the email exposed only thin job cards.

## SQLite Commands

```bash
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f21faa18a56d48 --classification status_update --status processed --artifact-path inbox/processed/2026-07-02-linkedin-application-status-updates.md --notes "LinkedIn application confirmation: Jobgether Deputy CTO (AI Product), job id 4432340752; status recorded only."
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f21e3d77f5ca26 --classification status_update --status processed --artifact-path inbox/processed/2026-07-02-linkedin-application-status-updates.md --notes "LinkedIn application viewed notice: GRS Recruitment; role/job id not exposed in email body."
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f21ba7638665c1 --classification status_update --status processed --artifact-path inbox/processed/2026-07-02-linkedin-application-status-updates.md --notes "LinkedIn application viewed notice: Techyons; role/job id not exposed in email body."
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f219e32a21d867 --classification status_update --status processed --artifact-path inbox/processed/2026-07-02-linkedin-application-status-updates.md --notes "LinkedIn application confirmation: Dr.Head IT Director, job id 4434956568; status recorded only."
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f21f3f0697f7ec --classification new_vacancy --status processed --artifact-path inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md --notes "Thin LinkedIn Software Engineering Director alert led by Jobgether Deputy CTO; raw intake only, no full JD or Telegram packet."
```

## Telegram

- Telegram target was configured: `113174019`.
- No Telegram packet sent.
- Intended packets: none.
- Reason: the new items were status notifications or thin job-card alerts, not actionable vacancy decision packets.

## Blocked Items

- None. Pi-local `google_workspace` Gmail search/read succeeded.

## Artifacts

- Run log: `automation/runs/2026-07-02-1627-pi-job-search-gmail-monitor.md`
- Application/status note: `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
- Raw intake: `inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md`

## Legacy State

- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.
- Updated `automation/state/linkedin-gmail-monitor-state.md` after successful scan.
