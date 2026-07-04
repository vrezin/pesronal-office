# Job Search Handoff Pipeline Repair

- Date: 2026-07-04
- Runtime: Raspberry Pi / OpenClaw primary Personal Office
- Scope: Telegram HH vacancy intake -> async handoff -> job-search agent -> HH MCP -> Telegram follow-up
- Status: repaired and smoke-tested

## Problem

Two Telegram HH vacancy intakes created handoff artifacts, but the asynchronous
job-search follow-up did not complete.

Earlier diagnosis said the JD was unavailable, but the deeper runtime issue was
that the job-search path could not actually use the HH MCP server and the async
worker was not durable.

## Findings

- `automation/runs/2026-07-04-175846-pi-job-search-handoff-async.md` and
  `automation/runs/2026-07-04-180849-pi-job-search-handoff-async.md` queued
  background workers, but their `*-async-dispatch.md` files stayed empty.
- Manual dispatch initially failed because the OpenClaw runtime did not have
  `node` on PATH.
- After the PATH fix, manual dispatch reached the job-search agent, but the
  agent reported that `headhunter_web` was unavailable.
- `openclaw mcp doctor headhunter_web` on the Pi showed the global MCP registry
  pointed at a stale deleted command under
  `/home/openclaw/personal-office-agent/job-search-contour/...`.
- `openclaw mcp probe headhunter_web --json` failed before the registry fix.

## Runtime Repair

Updated the Pi OpenClaw MCP registry for `headhunter_web` to use the shared
Personal Office runtime wrapper:

- Command:
  `/home/openclaw/personal-office-agent/personal-office/tools/job-search-runtime/run-headhunter-web-mcp.sh`
- Working directory:
  `/home/openclaw/personal-office-agent/personal-office`
- Storage:
  `/home/openclaw/personal-office-agent/personal-office/tools/headhunter-web-mcp/.local/state/hh-storage-state.json`

After `openclaw mcp reload`:

- `openclaw mcp doctor headhunter_web` returned `ok`.
- `openclaw mcp probe headhunter_web --json` exposed 11 HH tools, including
  `headhunter_web__hh_web_get_vacancy`.

## Dispatch Verification

Manual dispatch after the MCP repair completed successfully:

- Wrapper log:
  `automation/runs/2026-07-04-1823-pi-job-search-handoff-dispatch.md`
- Agent run log:
  `automation/runs/2026-07-04-182521-pi-job-search-handoff-dispatch.md`
- HH tool result: `hh_web_get_vacancy` succeeded for vacancy `134804503`.
- JD archive:
  `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-emphasoft-project-office-head.md`
- Analysis:
  `personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-emphasoft-project-office-head-analysis.md`
- Verdict: `maybe / clarify first`.

## Async Repair

Changed `automation/scripts/enqueue-pi-job-search-handoff.sh` so it no longer
uses an inline background subshell. The enqueue wrapper now starts a durable
user systemd transient unit with `systemd-run --user --collect`.

Added:

- `automation/scripts/worker-pi-job-search-handoff.sh`

The worker runs the dispatcher, parses the structured YAML result, sends the
Telegram follow-up, and appends final status to the async run log.

## Smoke Test

Smoke command on Pi:

```bash
automation/scripts/enqueue-pi-job-search-handoff.sh personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md
```

Result:

- Async run log:
  `automation/runs/2026-07-04-183052-pi-job-search-handoff-async.md`
- Dispatch output:
  `automation/runs/2026-07-04-183052-pi-job-search-handoff-async-dispatch.md`
- Systemd unit:
  `personal-office-job-search-handoff-2026-07-04-183052`
- Dispatcher status: `completed`
- Job-search verdict: `no-op`, because vacancy `134804503` was already archived
  and analyzed by the manual verification run.
- Telegram follow-up: sent successfully, message id `398`.
- Async wrapper result: `completed`.

## Current State

The job-search handoff sequence is now proven end-to-end for this HH vacancy:

1. intake handoff exists;
2. enqueue creates a durable systemd user unit;
3. worker continues after enqueue exits;
4. dispatcher invokes the OpenClaw `job-search` agent;
5. job-search can use the HH MCP tool path;
6. structured YAML is returned;
7. Telegram follow-up is sent;
8. run logs contain final status.

Remaining non-blocking improvement: tune duplicate/known-vacancy dispatch so the
agent exits even faster on already archived HH ids.
