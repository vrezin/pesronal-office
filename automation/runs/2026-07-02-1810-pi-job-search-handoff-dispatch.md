# Pi Job Search Handoff Dispatch

- Started at: 2026-07-02T18:10:54+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Handoff path: `/home/openclaw/personal-office-agent/personal-office/personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-hh-vacancy-134758284-handoff.md`
- Prompt file: `/home/openclaw/personal-office-agent/personal-office/automation/prompts/pi-job-search-handoff-dispatch.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Timeout seconds: `900`
- Thinking: `medium`
- Telegram mutation: none
- Status: running


## Lock

    {"acquired": true, "lock_name": "pi-job-search-handoff-dispatch", "owner": "2026-07-02-1810-218416"}
- Lock exit code: `0`

## Agent Output

    Status: success / already processed; no duplicate artifacts created.

    Run log: `automation/runs/2026-07-02-1813-pi-job-search-handoff-dispatch.md`

    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: "HH vacancy 134758284 was already processed as UZUM TECHNOLOGIES. IT Team Lead Payment Mechanics; no duplicate artifacts created. Live HH refetch timed out, so existing durable JD archive and analysis remain the evidence source."
    verdict: maybe
    reasons:
      - "Real fintech engineering-management role with good Stability & Governance overlap: SDLC, incidents, CI/CD, technical debt, architecture decisions, and team health."
      - "Likely downleveled for the current target profile: Team Lead for a 7-person team, with hidden salary and possible Java/payments hard filters."
      - "Remote-from-anywhere plus Uzbekistan IT Park/legal setup may be practical, but compensation, legal setup, and hands-on backend depth must be clarified first."
    cv: "personal-projects/personal-brand/workspace/final-cv/CTO - Head of Engineering - Stability and Governance.pdf"
    cover_letter: null
    next_action: "Clarify compensation band, remote/legal setup, and hands-on Java/payments depth before applying."
    artifacts:
      - "personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-02-uzum-technologies-team-lead-payment-mechanics.md"
      - "personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-07-02-uzum-technologies-team-lead-payment-mechanics-analysis.md"
      - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-hh-vacancy-134758284-handoff.md"
      - "automation/runs/2026-07-02-1813-pi-job-search-handoff-dispatch.md"
    blocked_on:
      - "Live HH refetch timed out; use durable saved JD unless a fresh source check is explicitly required."
    ```
    ⚠️ 🛠️ `search "134758284|Payment Mechanics|UZUM|hh-vacancy-134758284|134758" in automation (in ~/personal-office-agent/personal-office)` failed

## Wrapper Result

- Finished at: 2026-07-02T18:14:23+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-handoff-dispatch", "released": 1}
