# Job Search Async Dispatch Design

- Date: 2026-07-02
- Decision: Telegram intake must acknowledge quickly and use async job-search dispatch for vacancy handoffs.
- Scope: Pi-primary Personal Office intake and job-search handoff routing.

## Reason

Synchronous Telegram -> intake -> `dispatch-pi-job-search-handoff.sh` works for very short fast paths, but longer LinkedIn/HH enrichment can outlive the active Telegram turn. That produces partial run logs and user-facing blocked messages even when the job-search agent has already reached the source system.

The desired user experience is:

1. Intake receives a vacancy link, recruiter text, or actionable job-search item.
2. Intake creates/updates the handoff artifact.
3. Intake enqueues async job-search dispatch.
4. Intake immediately replies that the item was accepted for analysis.
5. The async worker runs job-search and sends a separate Telegram follow-up after the result is recorded.

The same pattern should later be reused for Gmail-derived A/B+ vacancy decisions.

## Implementation

- Added `automation/scripts/enqueue-pi-job-search-handoff.sh`.
- Updated `automation/prompts/pi-intake-secretary.md` to use async enqueue for Telegram vacancy links.
- Updated `tools/raspberrypi-openclaw/intake-agent-workspace-BOOTSTRAP.md` so the live Pi intake agent does not wait for job-search in the Telegram turn.
- Updated `automation/README.md` with the async dispatch boundary.

## Runtime Contract

`enqueue-pi-job-search-handoff.sh <handoff-path>` returns quickly with:

```text
ENQUEUE_STATUS=queued
RUN_LOG=<async-run-log>
WORKER_PID=<pid>
DISPATCH_OUTPUT=<dispatcher-output-log>
```

The background worker then:

- calls `automation/scripts/dispatch-pi-job-search-handoff.sh`;
- records dispatcher stdout/stderr in `automation/runs/`;
- extracts the structured `secretaries/handoff-contract.md` YAML from job-search output;
- sends a concise Telegram follow-up through `personal-office-intake-telegram`.

## Remaining Validation

Run one fresh Telegram vacancy-link smoke. Passing behavior:

- first Telegram reply is an acknowledgement, not a final verdict;
- async run log reaches `Status: completed` or a clear blocked state;
- final Telegram follow-up arrives after job-search finishes;
- no shell logs or tool chatter are sent to Telegram.
