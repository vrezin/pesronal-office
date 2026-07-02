# Intake Bootstrap Dispatcher Cache Regression

- Date: 2026-07-02
- Runtime: Raspberry Pi / OpenClaw Gateway
- Channel: `personal-office-intake-telegram`
- Session id: `968287ad-009a-4402-96a5-a1ca4f5606b4`
- Failed Telegram message id: `379`

## Observation

After `automation/prompts/pi-intake-secretary.md` was strengthened, a repeated
Jobgether LinkedIn link still produced a direct intake duplicate/no-op reply:

```text
Routed: job-search / personal-brand
Created/updated: none — already tracked in `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
Next: ждать ответ Jobgether; новый анализ не нужен
```

No handoff and no dispatcher run were created.

Transcript inspection showed why: the live Telegram turn used the active
OpenClaw workspace `BOOTSTRAP.md` as immediate project context. That bootstrap
only said to hand off job-search-shaped messages, but did not contain the hard
dispatcher/no-duplicate-decision rule. The model then made a local duplicate
decision using conversation history instead of reading the updated repo prompt.

## Correction

Both files were updated:

- `tools/raspberrypi-openclaw/intake-agent-workspace-BOOTSTRAP.md`
- live workspace `/home/openclaw/personal-office-agent/openclaw-workspaces/intake/BOOTSTRAP.md`

The bootstrap now states that plain HH/LinkedIn Telegram vacancy links must run:

```text
create/update handoff -> run automation/scripts/dispatch-pi-job-search-handoff.sh <handoff-path> -> reply from dispatcher result
```

It also explicitly forbids intake from deciding `already tracked`, `duplicate`,
`no-op`, `parked`, `blocked`, or `ready for CV/CL`.

## Next Validation

Repeat the same Telegram link. Passing behavior requires a new or updated
handoff plus a new dispatcher run log. A direct `already tracked` response from
intake is still a failure.
