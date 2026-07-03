# Pi Job Search Telegram Intake

- Started at: 2026-07-01T18:42:40+07:00
- Trigger: scheduled/manual wrapper
- Agent: `job-search`
- Session key: `agent:job-search:telegram-intake`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `unset`
- Telegram account: `default`
- Limit: `10`
- Timeout seconds: `1200`
- Status: running

Database: automation/state/job-search-runtime.sqlite
Schema: v1 job-search-runtime-v1 applied_at=2026-07-01T11:17:00.088Z
Processed messages:
- hh noise: 3
- hh seeded_from_markdown_state: 1
- linkedin noise: 5
- linkedin seeded_from_markdown_state: 1
Run locks: 0

## Lock

    {"acquired": true, "lock_name": "pi-job-search-telegram-intake", "owner": "2026-07-01-1842-701732"}
- Lock exit code: `0`

## Wrapper Result

- Finished at: 2026-07-01T18:42:40+07:00
- Status: blocked
- Reason: TELEGRAM_JOB_SEARCH_TARGET is not set. Telegram intake was not attempted.
{"lock_name": "pi-job-search-telegram-intake", "released": 1}
