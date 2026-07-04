# Pi Job Search Handoff Async

- Started at: 2026-07-04T19:19:58+07:00
- Trigger: intake async enqueue
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md`
- Dispatcher: `/home/openclaw/personal-office-agent/personal-office/automation/scripts/dispatch-pi-job-search-handoff.sh`
- Worker: `/home/openclaw/personal-office-agent/personal-office/automation/scripts/worker-pi-job-search-handoff.sh`
- Dispatch output: `automation/runs/2026-07-04-191958-pi-job-search-handoff-async-dispatch.md`
- Systemd unit: `personal-office-job-search-handoff-2026-07-04-191958`
- Telegram account: `personal-office-intake-telegram`
- Telegram target: `113174019`
- Status: queued


## Enqueue Result


## Worker

- Queued at: 2026-07-04T19:19:59+07:00
- Systemd exit code: `0`

### Systemd Output

- Started at: 2026-07-04T19:19:59+07:00
- PID: `3630519`
- Systemd unit: `7f36872fd1f842859554d9a173bfe2f9`
    Running as unit: personal-office-job-search-handoff-2026-07-04-191958.service; invocation ID: 7f36872fd1f842859554d9a173bfe2f9
- Status: queued

## Dispatcher Result

- Finished at: 2026-07-04T19:23:16+07:00
- Exit code: `0`

## Dispatcher Output

    Initialized automation/state/job-search-runtime.sqlite
    DISPATCH_STATUS=completed
    RUN_LOG=automation/runs/2026-07-04-1919-pi-job-search-handoff-dispatch.md
    JOB_SEARCH_OUTPUT_BEGIN
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
    
    JOB_SEARCH_OUTPUT_END

## Telegram Follow-Up

- Finished at: 2026-07-04T19:23:25+07:00
- Exit code: `0`

### Message

    Готово по job-search handoff: LinkedIn job 4436302720 is already fully archived and analyzed as Techmunity / unnamed UK AI mobility startup, Head of Software Engineering / Head of Engineering route to CTO.
    
    Вердикт: maybe
    Почему:
    - Full LinkedIn JD is available and already archived/analyzed; no duplicate artifacts were created.
    - Content match is plausible for startup/product engineering and AI-assisted engineering leadership.
    - Main blocker is practical: UK-based remote with 2-4 London/Bristol team days per month, plus likely UK right-to-work/logistics and hands-on stack screens.
    
    CV: personal-projects/personal-brand/workspace/final-cv/CTO - Co-founder CTO - Head of Product Engineering.pdf
    
    Next: Clarify UK residence/right-to-work, London/Bristol team-day requirement, international B2B from Novosibirsk, and hands-on coding screen before applying.
    Artifacts:
    - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md
    - personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-techmunity-head-software-engineering.md
    - personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-techmunity-head-software-engineering-analysis.md
    - personal-projects/personal-brand/workspace/job-intake/INDEX.md
    - personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md
    Blocked:
    - Is UK residence/right-to-work mandatory, or is international B2B work from Novosibirsk possible?
    Run log: automation/runs/2026-07-04-1919-pi-job-search-handoff-dispatch.md

### Send Output

    {
      "action": "send",
      "channel": "telegram",
      "dryRun": false,
      "handledBy": "plugin",
      "messageId": "405",
      "payload": {
        "ok": true,
        "messageId": "405"
      }
    }

## Wrapper Result

- Finished at: 2026-07-04T19:23:25+07:00
- Status: completed
