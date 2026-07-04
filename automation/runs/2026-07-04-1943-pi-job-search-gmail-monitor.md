# Pi Job Search Gmail Monitor

- Started at: 2026-07-04T19:43:17+07:00
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

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-04-1943-150117"}
- Lock exit code: `0`

## Agent Output

    Run completed successfully.
    
    Scanned Pi-local Gmail via `google_workspace` with SQLite dedupe first:
    
    - HH: 5 messages seen, all duplicate/no-op.
    - LinkedIn: 5 messages seen, 2 new processed, 3 duplicate/no-op.
    - New LinkedIn items:
      - Work Channel `Head of Enterprise Architecture` repost: matched existing analysis, no new action.
      - Software Engineering Director digest: enriched via LinkedIn MCP, created a batch search-run and updated job-intake notes.
    
    Updated/wrote:
    
    - [run log](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-04-1948-pi-job-search-gmail-monitor.md)
    - [HH state](/home/openclaw/personal-office-agent/personal-office/automation/state/hh-gmail-monitor-state.md)
    - [LinkedIn state](/home/openclaw/personal-office-agent/personal-office/automation/state/linkedin-gmail-monitor-state.md)
    - [digest search-run](/home/openclaw/personal-office-agent/personal-office/personal-projects/personal-brand/workspace/job-intake/search-runs/2026-07-04-linkedin-software-engineering-director-digest.md)
    
    No Telegram message was sent, Gmail stayed read-only, no CV/cover letter/application was created, and no git commands were run.

## Wrapper Result

- Finished at: 2026-07-04T19:53:14+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
