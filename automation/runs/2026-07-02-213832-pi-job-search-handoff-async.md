# Pi Job Search Handoff Async

- Started at: 2026-07-02T21:38:32+07:00
- Trigger: intake async enqueue
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4431600451-handoff.md`
- Dispatcher: `/home/openclaw/personal-office-agent/personal-office/automation/scripts/dispatch-pi-job-search-handoff.sh`
- Dispatch output: `automation/runs/2026-07-02-213832-pi-job-search-handoff-async-dispatch.out`
- Telegram account: `personal-office-intake-telegram`
- Telegram target: `113174019`
- Status: queued



## Worker
## Enqueue Result


- Queued at: 2026-07-02T21:38:32+07:00
- Started at: 2026-07-02T21:38:32+07:00
- PID: `2486601`
- Worker PID: `2486663`
- Status: queued

## Dispatcher Result

- Finished at: 2026-07-02T21:40:54+07:00
- Exit code: `0`

## Dispatcher Output

    Initialized automation/state/job-search-runtime.sqlite
    DISPATCH_STATUS=completed
    RUN_LOG=automation/runs/2026-07-02-2138-pi-job-search-handoff-dispatch.md
    JOB_SEARCH_OUTPUT_BEGIN
    Status: completed; verdict `wait` for thin duplicate LinkedIn shell.

    Run log: `automation/runs/2026-07-02-214008-linkedin-4431600451-handoff-complete.md`

    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: "LinkedIn job 4431600451 for Viaquant Partners Engineering Manager in Limassol is still only a thin posting shell and was already captured as a digest signal."
    verdict: wait
    reasons:
      - "LinkedIn exposes only company, title, location, full-time status, outside-LinkedIn apply flow, and 12 applicant clicks."
      - "No full JD, requirements, compensation, remote/legal setup, or relocation/family logistics are available."
      - "Exact job id already exists in the thin Cyprus Engineering Manager digest and Gmail monitor run."
    cv: null
    cover_letter: null
    next_action: "Reopen only if a full JD or recruiter/human reply appears."
    artifacts:
      - "automation/runs/2026-07-02-214008-linkedin-4431600451-handoff-complete.md"
      - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4431600451-handoff.md"
      - "inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md"
      - "automation/runs/2026-07-02-1222-pi-job-search-gmail-monitor.md"
      - "automation/runs/2026-07-02-2033-linkedin-4431600451-dispatch-interrupted.md"
    blocked_on: []
    ```

    JOB_SEARCH_OUTPUT_END

## Telegram Follow-Up

- Finished at: 2026-07-02T21:41:03+07:00
- Exit code: `0`

### Message

    Готово по job-search handoff: LinkedIn job 4431600451 for Viaquant Partners Engineering Manager in Limassol is still only a thin posting shell and was already captured as a digest signal.

    Вердикт: wait
    Почему:
    - LinkedIn exposes only company, title, location, full-time status, outside-LinkedIn apply flow, and 12 applicant clicks.
    - No full JD, requirements, compensation, remote/legal setup, or relocation/family logistics are available.
    - Exact job id already exists in the thin Cyprus Engineering Manager digest and Gmail monitor run.

    Next: Reopen only if a full JD or recruiter/human reply appears.
    Artifacts:
    - automation/runs/2026-07-02-214008-linkedin-4431600451-handoff-complete.md
    - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4431600451-handoff.md
    - inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md
    - automation/runs/2026-07-02-1222-pi-job-search-gmail-monitor.md
    - automation/runs/2026-07-02-2033-linkedin-4431600451-dispatch-interrupted.md
    Blocked:
    - []
    Run log: automation/runs/2026-07-02-213832-pi-job-search-handoff-async-dispatch.out

### Send Output

    {
      "action": "send",
      "channel": "telegram",
      "dryRun": false,
      "handledBy": "plugin",
      "messageId": "388",
      "payload": {
        "ok": true,
        "messageId": "388"
      }
    }

## Wrapper Result

- Finished at: 2026-07-02T21:41:03+07:00
- Status: completed
