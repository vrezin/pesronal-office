# LinkedIn Live Dispatcher Regression

- Date: 2026-07-02
- Runtime: Raspberry Pi / OpenClaw Gateway
- Channel: `personal-office-intake-telegram`
- Agent path: `intake -> job-search dispatcher`
- Related handoff: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4434956568-handoff.md`
- Related dispatcher run: `automation/runs/2026-07-02-1843-pi-job-search-handoff-dispatch.md`

## Observation

Live Telegram smoke with LinkedIn job id `4434956568` confirmed that the `intake`
agent understood the route and created a job-search handoff, but stopped with a
queue-style reply:

```text
Routed: job-search / personal-brand
Created/updated: personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4434956568-handoff.md
Next: job-search contour should fetch and analyze the vacancy only if you want a review/apply decision.
```

That is not the desired end-to-end behavior for a plain HH/LinkedIn vacancy link
sent to Telegram. In this channel, the link itself is already an implicit request
for routing/review.

## Correction

The handoff was dispatched manually through:

```bash
automation/scripts/dispatch-pi-job-search-handoff.sh personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-job-alert-4434956568-handoff.md
```

The dispatcher completed successfully and returned `wait / no-op`: LinkedIn job
`4434956568` was already captured as Dr.Head `Директор по ИТ` application
submitted on 2026-07-02, and the later alert is a duplicate/no-op. LinkedIn
exposed only thin status/posting shell details and no full JD.

## Prompt Change

`automation/prompts/pi-intake-secretary.md` was strengthened to say that a plain
HH/LinkedIn vacancy link sent to Telegram must be dispatched first, then answered
from the dispatcher/job-search result. The intake agent should not answer with
`if requested` / `if you want a review` for such messages.

## Next Validation

Send a fresh HH or LinkedIn vacancy link to `personal-office-intake-telegram` and
confirm the visible reply is produced from a dispatcher result, not from a
handoff-only queue response.
