# Job Search Dispatch Timeout Postmortem

- Date: 2026-07-02
- Runtime: Raspberry Pi / OpenClaw Gateway
- Handoff: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4432340752-handoff.md`
- Run log: `automation/runs/2026-07-02-1909-pi-job-search-handoff-dispatch.md`
- Job-search session: `98f8eae6-4c62-4f2c-87cd-8d254fa868f9`

## Observation

The intake boundary finally behaved correctly: it created a handoff and attempted
to run the job-search dispatcher. The visible Telegram response was:

```text
Routed: job-search / personal-brand
Created/updated: personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4432340752-handoff.md
Next: dispatcher was blocked before job-search returned a verdict
Blocked: automation/scripts/dispatch-pi-job-search-handoff.sh hung on this handoff path
```

The wrapper run log remained in `running` state because the parent intake turn
interrupted the job-search session before the wrapper captured stdout and wrote a
normal `Wrapper Result`.

## Actual Job-Search Evidence

The job-search trajectory shows that the agent did not hang on LinkedIn:

- exact-id searches found the prior Jobgether application/status artifacts;
- LinkedIn `get_job_details` completed for job id `4432340752`;
- live LinkedIn exposed only thin/status shell content: Jobgether `Deputy CTO
  (AI Product)`, United Arab Emirates, remote, full-time, application submitted;
- no full JD body/responsibilities/requirements/salary were exposed.

## Root Cause

The dispatch prompt allowed broad exploration of `COMPANY_NOTES.md` and other
job-intake context before returning. For thin/status duplicate cases this is too
slow for an intake-triggered Telegram turn. The wrapper also reused a stable
session key per handoff path, so retrying the same handoff could resume the
heavy interrupted session.

## Correction

- `automation/prompts/pi-job-search-handoff-dispatch.md` now defines a fast path
  for exact LinkedIn job id status/thin cases and forbids broad index/company
  reads unless a full JD is available.
- `automation/scripts/dispatch-pi-job-search-handoff.sh` now appends the run
  stamp to the session key by default so each dispatch starts fresh.

## Decision For This Handoff

Verdict: `wait / no-op`.

No JD archive, analysis, CV, or CL should be created from this thin/status source
alone. Wait for Jobgether reply or fetch/request a full JD if the conversation
reopens.
