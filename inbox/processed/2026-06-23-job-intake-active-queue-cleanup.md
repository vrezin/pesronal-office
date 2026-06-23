# Job Intake Active Queue Cleanup

Date processed: 2026-06-23
Status: processed

## Decision

Do not delete reviewed vacancies or JD analyses. Archive the operational task state instead.

Reason:

- `job-intake/jd-archive/` and `job-intake/analyses/` are evidence and market memory;
- `job-intake/INDEX.md` remains the source of truth for historical vacancy decisions;
- `tasks/active/` should contain only live next actions;
- parked, skipped, closed, stale digest, and long-tail market-signal items belong in `tasks/done/` unless they are waiting for a real employer response.

## Cleanup Performed

Moved obvious long-tail vacancy tasks out of `tasks/active/`:

- old HH digest / suitable-vacancy review queues;
- old LinkedIn digest review queues;
- explicit `C-class / parked` tasks;
- older "apply/decide/respond" tasks that `job-intake/TODAY.md` already classified as parked or not worth active attention.

Waiting tasks were not mass-closed in this pass.

## Rule Going Forward

- Keep `waiting` if an application was sent and there is no rejection/closure evidence yet.
- Close to `done` immediately when there is a rejection, vacancy archived/closed evidence, or explicit user decision to stop.
- Park to `done` when a task is only C-class / market signal / location-gated and no active next action exists.
- Do not reopen parked tasks unless the user explicitly asks or a new employer/recruiter message appears.
