# Pi Job Search Gmail Monitor

- Started at: 2026-07-02T16:23:36+07:00
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
- linkedin noise: 7
- linkedin processed: 3
- linkedin seeded_from_markdown_state: 1
Run locks: 0

## Lock

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-02-1623-1205654"}
- Lock exit code: `0`

## Agent Output

    Completed the monitor pass.
    
    Processed 5 new LinkedIn messages: 4 application/status updates and 1 thin Jobgether-led job alert. HH was duplicate/no-op. No Telegram packet was sent because nothing had enough JD detail for an actionable decision.
    
    Updated:
    - [run log](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-02-1627-pi-job-search-gmail-monitor.md)
    - [application/status note](/home/openclaw/personal-office-agent/personal-office/inbox/processed/2026-07-02-linkedin-application-status-updates.md)
    - [thin Jobgether alert](/home/openclaw/personal-office-agent/personal-office/inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md)
    - [HH state](/home/openclaw/personal-office-agent/personal-office/automation/state/hh-gmail-monitor-state.md)
    - [LinkedIn state](/home/openclaw/personal-office-agent/personal-office/automation/state/linkedin-gmail-monitor-state.md)

## Wrapper Result

- Finished at: 2026-07-02T16:28:46+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
