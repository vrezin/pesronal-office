# Pi Job Search Handoff Dispatch

- Started at: 2026-07-04T18:15:08+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md`
- Prompt file: `/home/openclaw/personal-office-agent/personal-office/automation/prompts/pi-job-search-handoff-dispatch.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Timeout seconds: `420`
- Thinking: `medium`
- Telegram mutation: none
- Status: running


## Lock

    {"acquired": true, "lock_name": "pi-job-search-handoff-dispatch", "owner": "2026-07-04-1815-1634659"}
- Lock exit code: `0`
- Session key: `agent:job-search:handoff-dispatch:personal-projects-personal-brand-workspace-job-intake-processed-2026-07-04-hh-vacancy-1348:2026-07-04-1815`

## Agent Output

    Status: blocked/clarify - HH vacancy id found, but `headhunter_web` is unavailable and no full JD artifact exists.
    
    Run log: `automation/runs/2026-07-04-181624-pi-job-search-handoff-dispatch.md`
    
    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: HH vacancy 134804503 from Telegram was identified, but authenticated HH enrichment is unavailable and no durable full JD artifact exists.
    verdict: clarify
    reasons:
      - The handoff contains a stable HH vacancy id and URL, but no full JD text.
      - Exact artifact search found only the intake handoff, an earlier thin Emphasoft digest mention, and prior blocked HH-enrichment logs.
      - The required headhunter_web connector is unavailable in this runtime, so the vacancy cannot be verified or evaluated.
    cv: null
    cover_letter: null
    next_action: rerun with headhunter_web available or provide the full HH vacancy text.
    artifacts:
      - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md
      - inbox/processed/2026-07-04-hh-ai-solution-architect-thin-digest.md
      - automation/runs/2026-07-04-180555-pi-job-search-handoff-dispatch.md
      - automation/runs/2026-07-04-181624-pi-job-search-handoff-dispatch.md
    blocked_on:
      - Authenticated headhunter_web access or pasted full HH vacancy text is needed to fetch and verify the JD.
    ```

## Wrapper Result

- Finished at: 2026-07-04T18:17:14+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-handoff-dispatch", "released": 1}
