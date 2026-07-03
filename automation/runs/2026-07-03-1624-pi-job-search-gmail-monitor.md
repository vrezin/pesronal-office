# Pi Job Search Gmail Monitor

- Started at: 2026-07-03T16:24:36+07:00
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
- hh needs_human: 4
- hh noise: 4
- hh processed: 3
- hh seeded_from_markdown_state: 1
- linkedin duplicate: 1
- linkedin noise: 7
- linkedin processed: 9
- linkedin seeded_from_markdown_state: 1
Run locks: 0

## Lock

    {"acquired": true, "lock_name": "pi-job-search-gmail-monitor", "owner": "2026-07-03-1624-803122"}
- Lock exit code: `0`

## Agent Output

    Completed the scheduled monitor run.

    Run log: [2026-07-03-1625-pi-job-search-gmail-monitor.md](/home/openclaw/personal-office-agent/personal-office/automation/runs/2026-07-03-1625-pi-job-search-gmail-monitor.md)

    Processed 4 new ids:
    - HH resume-view notice recorded as `noise`.
    - HH thin Product Engineering digest recorded here: [2026-07-03-hh-product-engineering-thin-digest.md](/home/openclaw/personal-office-agent/personal-office/inbox/processed/2026-07-03-hh-product-engineering-thin-digest.md)
    - 2 LinkedIn alert emails enriched via registered LinkedIn MCP and recorded here: [2026-07-03-linkedin-enriched-thin-alerts.md](/home/openclaw/personal-office-agent/personal-office/inbox/processed/2026-07-03-linkedin-enriched-thin-alerts.md)

    LinkedIn enrichment returned only shell details for Revolut, Ingenio Global, and Salesforce, so I did not create full JD analyses or update `INDEX.md` / `COMPANY_NOTES.md`.

    No Telegram sent, no Gmail mutations, no git commands. State snapshots were updated.

## Wrapper Result

- Finished at: 2026-07-03T16:31:05+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-gmail-monitor", "released": 1}
