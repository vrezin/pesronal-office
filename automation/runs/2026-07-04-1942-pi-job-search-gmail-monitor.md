# Pi Job Search Gmail Monitor

- Started at: 2026-07-04T19:42:46+07:00
- Trigger: scheduled/manual wrapper
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Session key: `agent:job-search:pi-gmail-monitor`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `113174019`
- Telegram account: `job-search-telegram`
- Timeout seconds: `3600`
- Status: running

Database: automation/state/job-search-runtime.sqlite
Schema: v1 job-search-runtime-v1 applied_at=2026-07-01T11:17:00.088Z
Processed messages:
- hh needs_human: 4
- hh noise: 5
- hh processed: 8
- hh seeded_from_markdown_state: 1
- linkedin duplicate: 1
- linkedin needs_human: 1
- linkedin noise: 8
- linkedin processed: 15
- linkedin seeded_from_markdown_state: 1
Run locks: 0
Vacancies:
- backfill:local-personal-office-job-intake active: 22
- backfill:local-personal-office-job-intake historical_backfill: 5
- backfill:local-personal-office-job-intake historical_closed: 55
- backfill:local-personal-office-job-intake historical_no_action: 30
- backfill:local-personal-office-job-intake historical_open: 64
- backfill:local-personal-office-job-intake waiting: 55

## Lock

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-04-1942-133534"}
- Lock exit code: `0`

## Agent Output

    env: ‘node’: No such file or directory

## Wrapper Result

- Finished at: 2026-07-04T19:42:46+07:00
- Exit code: `127`
- Status: blocked
- Reason: OpenClaw agent exited non-zero. Legacy monitor state was not advanced by wrapper.
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
