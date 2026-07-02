# Pi Job Search Gmail Monitor

- Started at: 2026-07-02T12:19:36+07:00
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
- linkedin processed: 2
- linkedin seeded_from_markdown_state: 1
Run locks: 0

## Lock

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-02-1219-1652304"}
- Lock exit code: `0`

## Agent Output

    Completed the Gmail monitor pass.
    
    One new LinkedIn message was processed: a thin Cyprus engineering-manager “similar jobs” digest. I captured it as raw intake, marked the Gmail id processed in SQLite, and did not send Telegram because there was no full JD or actionable decision packet.
    
    Updated:
    - [run log](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-02-1222-pi-job-search-gmail-monitor.md)
    - [raw intake](/home/openclaw/personal-office-agent/personal-office/inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md)
    - [HH state](/home/openclaw/personal-office-agent/personal-office/automation/state/hh-gmail-monitor-state.md)
    - [LinkedIn state](/home/openclaw/personal-office-agent/personal-office/automation/state/linkedin-gmail-monitor-state.md)

## Wrapper Result

- Finished at: 2026-07-02T12:23:53+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
