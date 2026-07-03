# Pi Job Search Gmail Monitor

- Started at: 2026-07-01T18:46:35+07:00
- Trigger: scheduled/manual wrapper
- Agent: `job-search`
- Session key: `agent:job-search:pi-gmail-monitor`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `unset`
- Telegram account: `default`
- Timeout seconds: `5`
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

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-01-1846-830546"}
- Lock exit code: `0`

## Agent Output

    <no output>

## Wrapper Result

- Finished at: 2026-07-01T18:46:40+07:00
- Exit code: `124`
- Status: blocked
- Reason: OpenClaw agent did not return before wrapper timeout. Legacy monitor state was not advanced by wrapper.
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
