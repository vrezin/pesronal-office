# LinkedIn Duplicate Decision Leak Regression

- Date: 2026-07-02
- Runtime: Raspberry Pi / OpenClaw Gateway
- Channel: `personal-office-intake-telegram`
- Agent path expected: `intake -> job-search dispatcher`
- Agent path observed: `intake -> local duplicate/no-op reply`

## Observation

A second live Telegram smoke with a LinkedIn vacancy link produced a concise
route reply, but no new handoff and no dispatcher run:

```text
Routed: job-search / personal-brand
Created/updated: none — already tracked in inbox/processed/2026-07-02-linkedin-application-status-updates.md and inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md
Next: ждать ответ Jobgether; новая analysis не нужна
```

This is still not the intended boundary. The intake agent may recognize the
domain, but it must not close HH/LinkedIn Telegram vacancy links as duplicate or
no-op by reading old artifacts. Duplicate/no-op is a job-search contour decision
because it may require live HH/LinkedIn source checks, Gmail status context, and
job-intake state.

## Correction

`automation/prompts/pi-intake-secretary.md` was strengthened again:

- Telegram HH/LinkedIn vacancy links must create/update a handoff.
- The dispatcher must run even if existing artifacts mention the same company,
  role, or job id.
- Only the job-search contour may decide `already tracked`, `duplicate`,
  `parked`, `blocked`, or `ready for CV/CL`.

## Next Validation

Run one more live Telegram smoke. Passing behavior:

1. `intake` writes or updates a handoff under `personal-projects/personal-brand/workspace/job-intake/processed/`.
2. `automation/scripts/dispatch-pi-job-search-handoff.sh` creates a new run log under `automation/runs/`.
3. The Telegram reply is rewritten from the dispatcher handoff, not from the intake agent's direct duplicate/no-op inference.
