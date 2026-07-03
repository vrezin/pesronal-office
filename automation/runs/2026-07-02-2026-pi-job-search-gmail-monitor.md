# Pi Job Search Gmail Monitor

- Started at: 2026-07-02T20:26:36+07:00
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

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-02-2026-238072"}
- Lock exit code: `0`

## Scan

- Completed at: 2026-07-02T20:28:39+07:00
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
  - `19f222a760eeb4d3`
  - `19f191abaf5759ab`
  - `19f12cd62b56bebe`
  - `19f0d7d179bacbb7`
- HH fallback:
  - `19f222a760eeb4d3`
  - `19f191abaf5759ab`
  - `19f12cd62b56bebe`
  - `19f0d7d179bacbb7`
- LinkedIn:
  - `19f21faa18a56d48`
  - `19f21f3f0697f7ec`
  - `19f21e3d77f5ca26`
  - `19f21ba7638665c1`
  - `19f219e32a21d867`

## SQLite Runtime

Commands run:

```bash
python3 tools/job-search-runtime/job_search_runtime.py init
python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f222a760eeb4d3
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f191abaf5759ab
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f12cd62b56bebe
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id 19f0d7d179bacbb7
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21faa18a56d48
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21f3f0697f7ec
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21e3d77f5ca26
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f21ba7638665c1
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id 19f219e32a21d867
```

Runtime status after scan:

- hh needs_human: 1
- hh noise: 4
- hh processed: 2
- hh seeded_from_markdown_state: 1
- linkedin duplicate: 1
- linkedin noise: 7
- linkedin processed: 8
- linkedin seeded_from_markdown_state: 1

## Duplicate / No-Op IDs

- HH:
  - `19f222a760eeb4d3` - already processed as `new_vacancy`, artifact `inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md`
  - `19f191abaf5759ab` - already processed as `noise`, artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`
  - `19f12cd62b56bebe` - already processed as `noise`, artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`
  - `19f0d7d179bacbb7` - already processed as `noise`, artifact `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`
- LinkedIn:
  - `19f21faa18a56d48` - already processed as `status_update`, artifact `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
  - `19f21f3f0697f7ec` - already processed as `new_vacancy`, artifact `inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md`
  - `19f21e3d77f5ca26` - already processed as `status_update`, artifact `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
  - `19f21ba7638665c1` - already processed as `status_update`, artifact `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
  - `19f219e32a21d867` - already processed as `status_update`, artifact `inbox/processed/2026-07-02-linkedin-application-status-updates.md`

## Processed Items

No new message-specific items were processed in this slice. No bodies were read because every seen message id was already processed in SQLite.

## Handoff / Telegram

No actionable vacancy or invitation was found. No user-reply handoff was produced, and no Telegram message was sent.

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: gmail_monitor
summary: Duplicate-only HH and LinkedIn Gmail monitor slice; no new actionable job-search messages.
verdict: no-op
reasons:
  - All seen HH and LinkedIn Gmail ids were already processed in SQLite.
  - No new vacancy, invitation, or status change required artifact routing.
cv: null
cover_letter: null
next_action: wait for next scheduled scan
artifacts:
  - automation/runs/2026-07-02-2026-pi-job-search-gmail-monitor.md
blocked_on: []
```

## Blocked Items

None. Gmail search and repository writes were available.

## Legacy State

Updated after successful scan:

- `automation/state/hh-gmail-monitor-state.md`
- `automation/state/linkedin-gmail-monitor-state.md`

## Agent Output

    Completed the scheduled Gmail monitor run.

    It was a clean duplicate-only scan: HH returned 4 already-processed ids, LinkedIn returned 5 already-processed ids, so no message bodies were read, no new job-intake artifacts were created, and no Telegram/user-facing packet was sent.

    Updated:
    - [run log](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-02-2026-pi-job-search-gmail-monitor.md)
    - [HH monitor state](/home/openclaw/personal-office-agent/personal-office/automation/state/hh-gmail-monitor-state.md)
    - [LinkedIn monitor state](/home/openclaw/personal-office-agent/personal-office/automation/state/linkedin-gmail-monitor-state.md)

    SQLite runtime was initialized/checked, all message ids were deduped before processing, Gmail was read-only, and the monitor lock was released.

## Wrapper Result

- Finished at: 2026-07-02T20:31:56+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 0}
