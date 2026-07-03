# Pi Job Search Handoff Dispatch

- Started at: 2026-07-02T18:43:09+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- OpenClaw binary: `/home/openclaw/.local/bin/openclaw`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4434956568-handoff.md`
- Prompt file: `/home/openclaw/personal-office-agent/personal-office/automation/prompts/pi-job-search-handoff-dispatch.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Timeout seconds: `900`
- Thinking: `medium`
- Telegram mutation: none
- Status: success / already processed, no duplicate artifacts


## Lock

    {"acquired": true, "lock_name": "pi-job-search-handoff-dispatch", "owner": "2026-07-02-1843-1214928"}
- Lock exit code: `0`

## Outcome

Processed the intake handoff for LinkedIn job id `4434956568`.

The opportunity was already captured in the canonical Personal Office repo as a LinkedIn application/status event for Dr.Head, `Директор по ИТ`. A later LinkedIn job alert for the same job id had already been recorded as duplicate. No duplicate JD archive, analysis, index row, company note, CV, or cover-letter artifact was created.

## Live Source Check

Attempted a fresh LinkedIn connector fetch with `get_job_details` for job id `4434956568`.

Result: LinkedIn was reachable, but the live page exposed only thin status/posting shell content:

- company: Dr.Head
- role: `Директор по ИТ`
- location: Moscow, Russia
- work format: office
- employment: full-time
- application status: application submitted
- current availability: applications no longer accepted
- visible skill match: 1 of 10

The connector did not expose a full JD body, responsibilities, requirements, salary, or enough evidence for a normal vacancy analysis. Because durable artifacts already exist, those artifacts remain the evidence source per handoff rules. Monitor state files were not changed.

## Durable Evidence

- Intake handoff: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4434956568-handoff.md`
- Status artifact: `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
- Prior Gmail monitor run: `automation/runs/2026-07-02-1627-pi-job-search-gmail-monitor.md`
- Duplicate alert monitor run: `automation/runs/2026-07-02-1752-pi-job-search-gmail-monitor.md`

## Decision

- Vacancy: Dr.Head, `Директор по ИТ`
- LinkedIn job id: `4434956568`
- Status: application submitted on 2026-07-02; later alert is duplicate/no-op
- Verdict: `wait`
- CV: no new CV artifact; the applied LinkedIn resume is referenced by LinkedIn but not durably exposed in the handoff evidence
- Cover letter / reply: no new artifact
- Next action: wait for Dr.Head reply; if they respond, fetch or request the full JD before creating a normal analysis.

## Secretary Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: "LinkedIn job 4434956568 was already captured as Dr.Head Director of IT application submitted on 2026-07-02; the later alert is duplicate/no-op. Live LinkedIn exposes only thin status details and no full JD, so no new vacancy analysis or CV/reply artifact was created."
verdict: wait
reasons:
  - "Durable repo evidence already records the Dr.Head application submission and duplicate later alert for the same LinkedIn job id."
  - "Live LinkedIn confirms the application was submitted and that applications are no longer accepted, but does not expose full JD details."
  - "There is not enough evidence to create a normal vacancy analysis without inventing responsibilities, requirements, salary, or fit."
cv: null
cover_letter: null
next_action: "Wait for Dr.Head reply; if they respond, fetch or request the full JD before preparing analysis or response text."
artifacts:
  - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4434956568-handoff.md"
  - "inbox/processed/2026-07-02-linkedin-application-status-updates.md"
  - "automation/runs/2026-07-02-1843-pi-job-search-handoff-dispatch.md"
blocked_on:
  - "Full LinkedIn JD was not exposed by the live source; only thin status/posting shell details were available."
```

## Agent Output

    Status: success / already processed; no duplicate artifacts created.

    Run log: `automation/runs/2026-07-02-1843-pi-job-search-handoff-dispatch.md`

    ```yaml
    handoff_type: user_reply
    source_agent: job-search
    domain: personal-brand/job-search
    priority: normal
    user_intent: vacancy_review
    summary: "LinkedIn job 4434956568 was already captured as Dr.Head Director of IT application submitted on 2026-07-02; the later alert is duplicate/no-op. Live LinkedIn exposes only thin status details and no full JD, so no new vacancy analysis or CV/reply artifact was created."
    verdict: wait
    reasons:
      - "Durable repo evidence already records the Dr.Head application submission and duplicate later alert for the same LinkedIn job id."
      - "Live LinkedIn confirms the application was submitted and that applications are no longer accepted, but does not expose full JD details."
      - "There is not enough evidence to create a normal vacancy analysis without inventing responsibilities, requirements, salary, or fit."
    cv: null
    cover_letter: null
    next_action: "Wait for Dr.Head reply; if they respond, fetch or request the full JD before preparing analysis or response text."
    artifacts:
      - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4434956568-handoff.md"
      - "inbox/processed/2026-07-02-linkedin-application-status-updates.md"
      - "automation/runs/2026-07-02-1843-pi-job-search-handoff-dispatch.md"
    blocked_on:
      - "Full LinkedIn JD was not exposed by the live source; only thin status/posting shell details were available."
    ```
    ⚠️ 🛠️ `search "4434956568|Dr.Head|Директор по ИТ" in ~/personal-office-agent/personal-office/automation/runs/2026-07-02-*.md (in ~/personal-office-agent/personal-office)` failed

## Wrapper Result

- Finished at: 2026-07-02T18:47:01+07:00
- Exit code: `0`
- Status: completed
{"lock_name": "pi-job-search-handoff-dispatch", "released": 1}
