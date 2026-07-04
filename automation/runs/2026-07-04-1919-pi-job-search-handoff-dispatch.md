# Pi Job Search Handoff Dispatch

- Started at: 2026-07-04T19:19:59+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md`
- Prompt file: `/home/openclaw/personal-office-agent/personal-office/automation/prompts/pi-job-search-handoff-dispatch.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Timeout seconds: `900`
- Thinking: `medium`
- Telegram mutation: none
- Status: running


## Lock

    {"acquired": true, "lock_name": "pi-job-search-handoff-dispatch", "owner": "2026-07-04-1919-3630533"}
- Lock exit code: `0`
- Session key: `agent:job-search:handoff-dispatch:personal-projects-personal-brand-workspace-job-intake-processed-2026-07-04-linkedin-job-al:2026-07-04-191958-async`

## Agent Output

    Status: processed; full JD already archived/analyzed, no duplicate artifacts created.
    
    Run log: `automation/runs/2026-07-04-192220-pi-job-search-handoff-dispatch.md`
    
    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: "LinkedIn job 4436302720 is already fully archived and analyzed as Techmunity / unnamed UK AI mobility startup, Head of Software Engineering / Head of Engineering route to CTO."
    verdict: maybe
    reasons:
      - "Full LinkedIn JD is available and already archived/analyzed; no duplicate artifacts were created."
      - "Content match is plausible for startup/product engineering and AI-assisted engineering leadership."
      - "Main blocker is practical: UK-based remote with 2-4 London/Bristol team days per month, plus likely UK right-to-work/logistics and hands-on stack screens."
    cv: "personal-projects/personal-brand/workspace/final-cv/CTO - Co-founder CTO - Head of Product Engineering.pdf"
    cover_letter: null
    next_action: "Clarify UK residence/right-to-work, London/Bristol team-day requirement, international B2B from Novosibirsk, and hands-on coding screen before applying."
    artifacts:
      - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md"
      - "personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-techmunity-head-software-engineering.md"
      - "personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-techmunity-head-software-engineering-analysis.md"
      - "personal-projects/personal-brand/workspace/job-intake/INDEX.md"
      - "personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md"
    blocked_on:
      - "Is UK residence/right-to-work mandatory, or is international B2B work from Novosibirsk possible?"
    ```

## Wrapper Result

- Finished at: 2026-07-04T19:23:16+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-handoff-dispatch", "released": 1}
