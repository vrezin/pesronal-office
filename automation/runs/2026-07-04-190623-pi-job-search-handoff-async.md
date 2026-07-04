# Pi Job Search Handoff Async

- Started at: 2026-07-04T19:06:23+07:00
- Trigger: intake async enqueue
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md`
- Dispatcher: `/home/openclaw/personal-office-agent/personal-office/automation/scripts/dispatch-pi-job-search-handoff.sh`
- Worker: `/home/openclaw/personal-office-agent/personal-office/automation/scripts/worker-pi-job-search-handoff.sh`
- Dispatch output: `automation/runs/2026-07-04-190623-pi-job-search-handoff-async-dispatch.md`
- Systemd unit: `personal-office-job-search-handoff-2026-07-04-190623`
- Telegram account: `personal-office-intake-telegram`
- Telegram target: `113174019`
- Status: queued


## Enqueue Result

- Queued at: 2026-07-04T19:06:23+07:00
- Systemd exit code: `0`

### Systemd Output

    Running as unit: personal-office-job-search-handoff-2026-07-04-190623.service; invocation ID: b414ef2adae74979a84957dfee70f347
- Status: queued

## Worker

- Started at: 2026-07-04T19:06:23+07:00
- PID: `3211746`
- Systemd unit: `b414ef2adae74979a84957dfee70f347`

## Dispatcher Result

- Finished at: 2026-07-04T19:08:27+07:00
- Exit code: `0`

## Dispatcher Output

    Initialized automation/state/job-search-runtime.sqlite
    DISPATCH_STATUS=completed
    RUN_LOG=automation/runs/2026-07-04-1906-pi-job-search-handoff-dispatch.md
    JOB_SEARCH_OUTPUT_BEGIN
    Status: no-op, already recorded; LinkedIn still exposes only a posting shell.
    
    Run log: `automation/runs/2026-07-04-190737-pi-job-search-handoff-dispatch.md`
    
    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: "LinkedIn job 4436302720 is already recorded as Techmunity | AI Startup Recruitment, Head of Software Engineering, UK remote full-time; the live LinkedIn source still exposes only a posting shell."
    verdict: no-op
    reasons:
      - "Exact-id search found prior durable dispatch/run logs for this same LinkedIn job."
      - "Live LinkedIn lookup exposed header/status fields only, with no About this job section or substantive JD paragraphs."
      - "No new job evidence was available, so creating duplicate JD/archive/analysis artifacts would be noise."
    cv: null
    cover_letter: null
    next_action: "Wait for a full JD, recruiter message, or changed LinkedIn posting body before preparing CV or reply."
    artifacts:
      - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md"
      - "automation/runs/2026-07-04-1858-pi-job-search-handoff-dispatch.md"
      - "automation/runs/2026-07-04-190737-pi-job-search-handoff-dispatch.md"
    blocked_on:
      - "Full job description is not available from the current LinkedIn source."
    ```
    
    JOB_SEARCH_OUTPUT_END

## Telegram Follow-Up

- Finished at: 2026-07-04T19:08:36+07:00
- Exit code: `0`

### Message

    Готово по job-search handoff: LinkedIn job 4436302720 is already recorded as Techmunity | AI Startup Recruitment, Head of Software Engineering, UK remote full-time; the live LinkedIn source still exposes only a posting shell.
    
    Вердикт: no-op
    Почему:
    - Exact-id search found prior durable dispatch/run logs for this same LinkedIn job.
    - Live LinkedIn lookup exposed header/status fields only, with no About this job section or substantive JD paragraphs.
    - No new job evidence was available, so creating duplicate JD/archive/analysis artifacts would be noise.
    
    Next: Wait for a full JD, recruiter message, or changed LinkedIn posting body before preparing CV or reply.
    Artifacts:
    - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md
    - automation/runs/2026-07-04-1858-pi-job-search-handoff-dispatch.md
    - automation/runs/2026-07-04-190737-pi-job-search-handoff-dispatch.md
    Blocked:
    - Full job description is not available from the current LinkedIn source.
    Run log: automation/runs/2026-07-04-1906-pi-job-search-handoff-dispatch.md

### Send Output

    {
      "action": "send",
      "channel": "telegram",
      "dryRun": false,
      "handledBy": "plugin",
      "messageId": "403",
      "payload": {
        "ok": true,
        "messageId": "403"
      }
    }

## Wrapper Result

- Finished at: 2026-07-04T19:08:36+07:00
- Status: completed
