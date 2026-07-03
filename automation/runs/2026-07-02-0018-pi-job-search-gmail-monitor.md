# Pi Job Search Gmail Monitor

- Started at: 2026-07-02T00:18:36+07:00
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
- linkedin seeded_from_markdown_state: 1
Run locks: 0

## Lock

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-02-0018-3249473"}
- Lock exit code: `0`

## Agent Output

    Completed the July 2 scheduled Gmail monitor run.

    Run log: [2026-07-02-0020-pi-job-search-gmail-monitor.md](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-02-0020-pi-job-search-gmail-monitor.md)

    Result:
    - HH: only duplicate/no-op ids, no HH bodies read, no HH artifacts changed.
    - LinkedIn: two unprocessed thin recommended-job digests captured as raw intake: [2026-07-02-linkedin-thin-ai-leadership-digests.md](/home/openclaw/personal-office-agent/personal-office/inbox/processed/2026-07-02-linkedin-thin-ai-leadership-digests.md)
    - SQLite now marks both new LinkedIn Gmail ids as `processed`.
    - State snapshots updated for HH and LinkedIn.

    Telegram was configured, but no packet was sent because the new items had only thin LinkedIn cards and no JD text, so there was no actionable send/maybe/skip decision. Gmail stayed read-only, and I did not run Git commands.

## Wrapper Result

- Finished at: 2026-07-02T00:23:08+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
