# OpenClaw Dispatcher And Intake Model Switch

- Timestamp: 2026-07-02 18:20 +07
- Runtime: Raspberry Pi OpenClaw
- Objective: `intake handoff -> job-search run -> intake/output reply`, then
  move `intake` to a cheaper model.

## Dispatcher

Added:

- `automation/prompts/pi-job-search-handoff-dispatch.md`
- `automation/scripts/dispatch-pi-job-search-handoff.sh`

The dispatcher accepts one intake-created handoff path, acquires the
`pi-job-search-handoff-dispatch` SQLite lock, runs the `job-search` agent, writes
a run log, and prints a compact dispatcher result for the intake/output
secretary.

## Prompt Wiring

Updated `automation/prompts/pi-intake-secretary.md` so job-search-shaped inputs
should:

1. create a thin intake/handoff artifact;
2. call `automation/scripts/dispatch-pi-job-search-handoff.sh <handoff-path>`;
3. rewrite the returned structured handoff into a concise human reply;
4. avoid forwarding shell output, tool logs, or raw dispatcher chatter.

## Smoke Evidence

Direct dispatcher smoke:

- Input handoff:
  `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-hh-vacancy-134758284-handoff.md`
- Dispatcher run:
  `automation/runs/2026-07-02-1805-pi-job-search-handoff-dispatch.md`
- Result: `completed`; `job-search` returned structured handoff; no duplicate
  job-intake artifacts were created.

Integrated intake smoke:

- Input: Telegram-style HH vacancy URL for vacancy id `134758284`.
- Result: `intake` routed to `personal-brand/job-search`, called the dispatcher,
  and returned a concise intake/output reply.
- Dispatcher logs created during the integrated run:
  - `automation/runs/2026-07-02-1810-pi-job-search-handoff-dispatch.md`
  - `automation/runs/2026-07-02-1813-pi-job-search-handoff-dispatch.md`

Known degradation:

- Live HH refetch timed out again.
- This did not block the user-facing decision because durable UZUM artifacts
  already existed and were used as the evidence source.

## Model Switch

Changed OpenClaw runtime config:

| Agent | Model |
|---|---|
| `intake` | `openai/gpt-5.4-mini` |
| `job-search` | `openai/gpt-5.5` |

Backup created by runtime edit:

- `/home/openclaw/.openclaw/openclaw.json.bak-before-intake-mini-20260702-181718`

Gateway was restarted after the model change.

Verification:

- `openclaw agents list` shows `intake` on `openai/gpt-5.4-mini`.
- `openclaw agents list` shows `job-search` remains on `openai/gpt-5.5`.
- `openclaw channels status --probe` reports Telegram gateway reachable/works.
- Post-switch intake smoke returned:
  `Route decision: no intake route needed. Durable artifact needed: no.`

## Remaining Notes

- The dispatcher stdout is sanitized for intake consumption, but raw job-search
  output remains in the run log for diagnosis.
- OpenClaw gateway logs may still show tool-failure diagnostic lines after agent
  replies. Intake prompt now explicitly forbids forwarding those to users.
