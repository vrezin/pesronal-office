# Pi Job Search Gmail Monitor

- Started at: 2026-07-02T04:24:54+07:00
- Trigger: scheduled/manual wrapper
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Session key: `agent:job-search:pi-gmail-monitor`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `113174019`
- Telegram account: `job-search-telegram`
- Timeout seconds: `1200`
- Status: running

Database: automation/state/job-search-runtime.sqlite
Schema: v1 job-search-runtime-v1 applied_at=2026-07-01T11:17:00.088Z
Processed messages:
- hh needs_human: 1
- hh noise: 4
- hh processed: 1
- hh seeded_from_markdown_state: 1
- linkedin noise: 6
- linkedin processed: 2
- linkedin seeded_from_markdown_state: 1
Run locks: 0

## Lock

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-02-0424-2936001"}
- Lock exit code: `0`

## Agent Output

    Completed the Pi job-search Gmail monitor run.

    Scanned HH and LinkedIn via Pi-local `google_workspace`, checked SQLite dedupe before processing, and found one new LinkedIn message. It was a generic LinkedIn Service Marketplace notification with no request/JD text, so I marked it as `noise`. No Gmail mutations, Telegram sends, job-intake artifacts, or git commands.

    Artifacts updated:
    - [run log](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-02-0426-pi-job-search-gmail-monitor.md)
    - [HH state](/home/openclaw/personal-office-agent/personal-office/automation/state/hh-gmail-monitor-state.md)
    - [LinkedIn state](/home/openclaw/personal-office-agent/personal-office/automation/state/linkedin-gmail-monitor-state.md)

    SQLite now records `linkedin:19f1f1efb6f351b5` as processed noise.
    ⚠️ 🛠️ `run pwd → search "SKILL.md" in ~/personal-office-agent/personal-office (in ~/personal-office-agent/personal-office)` failed

## Wrapper Result

- Finished at: 2026-07-02T04:30:24+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
