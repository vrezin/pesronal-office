# Pi Job Search Handoff Dispatch

- Started at: 2026-07-04T18:23:36+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md`
- Prompt file: `/home/openclaw/personal-office-agent/personal-office/automation/prompts/pi-job-search-handoff-dispatch.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Timeout seconds: `240`
- Thinking: `medium`
- Telegram mutation: none
- Status: running


## Lock

    {"acquired": true, "lock_name": "pi-job-search-handoff-dispatch", "owner": "2026-07-04-1823-1882289"}
- Lock exit code: `0`
- Session key: `agent:job-search:handoff-dispatch:personal-projects-personal-brand-workspace-job-intake-processed-2026-07-04-hh-vacancy-1348:hh-mcp-probe-1783164216`

## Agent Output

    Status: processed; full HH JD archived and analyzed, verdict `maybe`.
    
    Run log: `automation/runs/2026-07-04-182521-pi-job-search-handoff-dispatch.md`
    
    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: HH vacancy 134804503 is Emphasoft's Project Office Head role for IT custom-development/outstaffing portfolio governance; full JD was archived and analyzed.
    verdict: maybe
    reasons:
      - Real IT PMO/custom-development portfolio role with Business Unit / Integration and Stability & Governance overlap.
      - Technical background is a plus, which helps bridge engineering leadership into delivery-process authority.
      - Salary, Алматы/remote requirement, B2B economics and hands-on firefighting load are unclear.
    cv: personal-projects/personal-brand/workspace/final-cv/Director of Development - Business Unit Technical Leader.pdf
    cover_letter: null
    next_action: Clarify remote/B2B format, compensation range and PMO mandate before applying.
    artifacts:
      - personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-emphasoft-project-office-head.md
      - personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-emphasoft-project-office-head-analysis.md
      - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md
      - automation/runs/2026-07-04-182521-pi-job-search-handoff-dispatch.md
    blocked_on:
      - Is Novosibirsk remote B2B acceptable, or is Алматы presence required?
      - What is the compensation range?
      - How much of the role is PMO building versus personal firefighting on key projects?
    ```
    ⚠️ 🛠️ `search "Emphasoft|134804503|Руководитель Проектного офиса" in ~/personal-office-agent/personal-office/personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md (in ~/personal-office-agent/openclaw-workspaces/job-search)` failed

## Wrapper Result

- Finished at: 2026-07-04T18:27:33+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-handoff-dispatch", "released": 1}
