# Pi Job Search Gmail Monitor

- Started at: 2026-07-03T00:26:36+07:00
- Trigger: scheduled/manual wrapper
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Session key: `agent:job-search:pi-gmail-monitor`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `113174019`
- Telegram account: `job-search-telegram`
- Timeout seconds: `1200`
- Status: success

Database: automation/state/job-search-runtime.sqlite
Schema: v1 job-search-runtime-v1 applied_at=2026-07-01T11:17:00.088Z
Processed messages:
- hh needs_human: 1
- hh noise: 4
- hh processed: 2
- hh seeded_from_markdown_state: 1
- linkedin duplicate: 1
- linkedin noise: 7
- linkedin processed: 8
- linkedin seeded_from_markdown_state: 1
Run locks: 0

## Lock

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-03-0026-3699962"}
- Lock exit code: `0`

## Scan

- Completed at: 2026-07-03T00:30:31+07:00
- Gmail account: `v.rezin@gmail.com`
- Gmail access: Pi-local `google_workspace`, read-only
- Gmail mutations: none
- Git operations: none

## Gmail Queries

- HH primary: `from:(hh.ru OR notification@hh.ru OR no-reply@hh.ru OR noreply@hh.ru) newer_than:7d`
- HH fallback: `(hh.ru OR HeadHunter) newer_than:7d`
- LinkedIn: `from:linkedin.com newer_than:7d`

## Message IDs Seen

- HH primary:
  - `19f2344884afb3be`
  - `19f2342b5904a58d`
  - `19f222a760eeb4d3`
  - `19f191abaf5759ab`
  - `19f12cd62b56bebe`
- HH fallback:
  - `19f2344884afb3be`
  - `19f2342b5904a58d`
  - `19f222a760eeb4d3`
  - `19f191abaf5759ab`
  - `19f12cd62b56bebe`
- LinkedIn:
  - `19f233dc54d1f2ba`
  - `19f21faa18a56d48`
  - `19f21f3f0697f7ec`
  - `19f21e3d77f5ca26`
  - `19f21ba7638665c1`

## SQLite Runtime

Commands run:

```bash
python3 tools/job-search-runtime/job_search_runtime.py init
python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f2344884afb3be
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f2342b5904a58d
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f222a760eeb4d3
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f191abaf5759ab
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f12cd62b56bebe
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f233dc54d1f2ba
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21faa18a56d48
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21f3f0697f7ec
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21e3d77f5ca26
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21ba7638665c1
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source hh --gmail-message-id 19f2342b5904a58d --classification status_update --status needs_human --artifact-path inbox/processed/needs-clarification-2026-07-03-hh-gmail.md --notes 'HH Tensor rejection without vacancy id; multiple Tensor/Saby rows possible.'
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source hh --gmail-message-id 19f2344884afb3be --classification status_update --status needs_human --artifact-path inbox/processed/needs-clarification-2026-07-03-hh-gmail.md --notes 'HH Tensor employer chat says position closed; exact Tensor/Saby vacancy row ambiguous.'
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f233dc54d1f2ba --classification new_vacancy --status processed --artifact-path inbox/processed/2026-07-03-linkedin-thin-axway-director-engineering-alert.md --notes 'Thin LinkedIn Axway Director Engineering Dublin alert; no full JD analysis.'
```

Runtime status after scan:

- hh needs_human: 3
- hh noise: 4
- hh processed: 2
- hh seeded_from_markdown_state: 1
- linkedin duplicate: 1
- linkedin noise: 7
- linkedin processed: 9
- linkedin seeded_from_markdown_state: 1

## Duplicate / No-Op IDs

- HH:
  - `19f222a760eeb4d3` - already processed as `new_vacancy`, artifact `inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md`
  - `19f191abaf5759ab` - already processed as `noise`, artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`
  - `19f12cd62b56bebe` - already processed as `noise`, artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`
- LinkedIn:
  - `19f21faa18a56d48` - already processed as `status_update`, artifact `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
  - `19f21f3f0697f7ec` - already processed as `new_vacancy`, artifact `inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md`
  - `19f21e3d77f5ca26` - already processed as `status_update`, artifact `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
  - `19f21ba7638665c1` - already processed as `status_update`, artifact `inbox/processed/2026-07-02-linkedin-application-status-updates.md`

## Processed IDs And Artifacts

- HH `19f2342b5904a58d` - `status_update`, `needs_human`, artifact `inbox/processed/needs-clarification-2026-07-03-hh-gmail.md`.
- HH `19f2344884afb3be` - `status_update`, `needs_human`, artifact `inbox/processed/needs-clarification-2026-07-03-hh-gmail.md`.
- LinkedIn `19f233dc54d1f2ba` - `new_vacancy`, `processed`, artifact `inbox/processed/2026-07-03-linkedin-thin-axway-director-engineering-alert.md`.

## Routing Notes

- HH Tensor/Saby: HH sent a rejection/status update for `Тензор - Руководитель направления разработки`, followed by a chat note saying the position was already closed. The email did not expose a vacancy id or location. Because multiple Tensor/Saby rows exist with similar titles, the monitor did not update a specific analysis or `job-intake/INDEX.md`; it wrote a clarification artifact and marked both HH ids `needs_human`.
- LinkedIn Axway: the alert contains only title, company, Dublin location, and LinkedIn job id `4435338298`. No full JD, compensation, remote/legal setup, or requirements were available. The monitor wrote a thin intake note only; no JD archive, analysis, index row, or company note update was created.

## Handoff / Telegram

No direct Telegram message was sent. The job-search agent is not the Telegram-facing voice.

Internal handoffs were written inside the processed notes:

- `inbox/processed/needs-clarification-2026-07-03-hh-gmail.md` - `verdict: clarify`
- `inbox/processed/2026-07-03-linkedin-thin-axway-director-engineering-alert.md` - `verdict: no-op`

## Blocked Items

- HH Tensor/Saby closure is blocked on matching the email to the exact Tensor vacancy row or authenticated HH vacancy id.

## Legacy State

Updated after successful scan:

- `automation/state/hh-gmail-monitor-state.md`
- `automation/state/linkedin-gmail-monitor-state.md`

Not updated because no material vacancy analysis changed:

- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`

## Agent Output

    Completed the July 3 Gmail monitor run.

    New items handled:
    - HH Tensor/Saby rejection/closed-position pair was ambiguous, so I wrote a clarification artifact instead of closing the wrong vacancy row: [needs-clarification-2026-07-03-hh-gmail.md](/home/openclaw/personal-office-agent/personal-office/inbox/processed/needs-clarification-2026-07-03-hh-gmail.md)
    - LinkedIn Axway `Director, Engineering` alert was only a thin Dublin job alert, so I recorded it without creating a full JD analysis: [2026-07-03-linkedin-thin-axway-director-engineering-alert.md](/home/openclaw/personal-office-agent/personal-office/inbox/processed/2026-07-03-linkedin-thin-axway-director-engineering-alert.md)

    Updated:
    - [run log](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-03-0026-pi-job-search-gmail-monitor.md)
    - [HH monitor state](/home/openclaw/personal-office-agent/personal-office/automation/state/hh-gmail-monitor-state.md)
    - [LinkedIn monitor state](/home/openclaw/personal-office-agent/personal-office/automation/state/linkedin-gmail-monitor-state.md)

    No Telegram message was sent, Gmail stayed read-only, no git commands were run, and the SQLite monitor lock was released.

## Wrapper Result

- Finished at: 2026-07-03T00:32:59+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 0}
