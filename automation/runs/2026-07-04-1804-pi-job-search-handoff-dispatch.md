# Pi Job Search Handoff Dispatch

- Started at: 2026-07-04T18:04:25+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-rukovoditel-proektnogo-ofisa-emphasoft-handoff.md`
- Prompt file: `/home/openclaw/personal-office-agent/personal-office/automation/prompts/pi-job-search-handoff-dispatch.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Timeout seconds: `420`
- Thinking: `medium`
- Telegram mutation: none
- Status: running


## Lock

    {"acquired": true, "lock_name": "pi-job-search-handoff-dispatch", "owner": "2026-07-04-1804-1309804"}
- Lock exit code: `0`
- Session key: `agent:job-search:handoff-dispatch:personal-projects-personal-brand-workspace-job-intake-processed-2026-07-04-hh-rukovoditel-:2026-07-04-1804`

## Agent Output

    Status: blocked/clarify - HH enrichment connector unavailable; no JD artifacts created.
    
    Run log: `automation/runs/2026-07-04-180555-pi-job-search-handoff-dispatch.md`
    
    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: HH Telegram handoff contains an Emphasoft Project Office Head short link, but authenticated HH enrichment is unavailable and existing artifacts only contain a thin digest mention.
    verdict: clarify
    reasons:
      - The handoff has company, role, and HH short link, but no stable HH vacancy id or full JD text.
      - Existing durable artifacts only record a thin HH digest card for this Emphasoft role.
      - The required headhunter_web connector is unavailable in this runtime, so JD details cannot be verified.
    cv: null
    cover_letter: null
    next_action: rerun with headhunter_web available or provide the full HH JD text.
    artifacts:
      - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-rukovoditel-proektnogo-ofisa-emphasoft-handoff.md
      - inbox/processed/2026-07-04-hh-ai-solution-architect-thin-digest.md
      - automation/runs/2026-07-04-180555-pi-job-search-handoff-dispatch.md
    blocked_on:
      - Authenticated headhunter_web access or pasted full HH vacancy text is needed to fetch and verify the JD.
    ```

## Wrapper Result

- Finished at: 2026-07-04T18:06:38+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-handoff-dispatch", "released": 1}
