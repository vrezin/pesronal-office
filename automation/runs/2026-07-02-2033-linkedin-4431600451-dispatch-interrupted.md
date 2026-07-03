# LinkedIn 4431600451 Dispatch Interrupted

- Date: 2026-07-02
- Handoff: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4431600451-handoff.md`
- Run log: `automation/runs/2026-07-02-2031-pi-job-search-handoff-dispatch.md`
- Job-search session: `18e618cb-9d51-4293-b825-2d6725c0fe53`
- Result: `wait / no-op`

## Evidence

- Intake routed the Telegram LinkedIn URL into a job-search handoff.
- The dispatcher acquired the `pi-job-search-handoff-dispatch` lock and started a `job-search` session.
- The `job-search` session called `linkedin.get_job_details` for job id `4431600451`.
- LinkedIn returned only thin shell details: Viaquant Partners, Engineering Manager, Limassol, Cyprus, full-time, applications outside LinkedIn, 12 applied.
- No full JD, requirements, salary, remote/legal setup, or relocation/family logistics were available.
- Existing durable context: `inbox/processed/2026-07-02-linkedin-thin-cyprus-engineering-manager-digest.md`.
- Existing monitor evidence: `automation/runs/2026-07-02-1222-pi-job-search-gmail-monitor.md`.

## Decision

No JD archive, analysis, CV, or cover letter should be created from this item.

Treat the item as a thin market signal and wait. Reopen only if a full JD appears or a recruiter/human reply creates a real opportunity.

## Runtime Note

The synchronous Telegram -> intake -> dispatcher path still interrupts before the wrapper captures final output for longer job-search calls.

Next architecture fix: make job-search dispatch asynchronous. Intake should acknowledge the request quickly, enqueue the handoff, and let a detached worker send the follow-up Telegram message after the job-search result is recorded.
