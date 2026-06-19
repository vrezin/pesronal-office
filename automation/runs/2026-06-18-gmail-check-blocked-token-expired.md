# Gmail Check Blocked - Token Expired

- Run time: 2026-06-18 18:45:39 +0700
- Trigger: manual user request
- Scope requested: fresh mail check, primarily HH / LinkedIn / career-relevant messages
- Status: blocked

## What Happened

Gmail MCP calls failed with `token_expired`:

```text
Provided authentication token is expired. Please try signing in again.
status: 401
code: token_expired
```

## Queries Attempted

- HH / HeadHunter messages after 2026-06-17.
- LinkedIn messages after 2026-06-17.
- Career/recruiter/application-related messages after 2026-06-17.
- General Inbox messages after 2026-06-17.

## Required Action

Reconnect / re-authenticate the Gmail connector, then rerun the mail check.

## Retry

- 2026-06-18: Retried with a minimal Gmail query `in:inbox -in:spam -in:trash newer_than:2d`.
- Result: same `token_expired` / `401`; this confirms the failure is connector authorization, not the specific HH/LinkedIn query.
- 2026-06-18 18:53:39 +0700: Retried after user completed re-authorization in UI.
- Result: HH, LinkedIn, career, and Inbox Gmail queries still returned the same `token_expired` / `401`. Current MCP session may still be holding stale connector auth.

## Notes

Per the current workflow, do not update HH / LinkedIn monitor state markers until a successful Gmail scan completes.

## Resolution

- 2026-06-18 19:00:09 +0700: User restarted the agent and asked to retry.
- Result: Gmail MCP calls succeeded. The earlier blocker was stale connector/session state, not a persistent Gmail authorization failure.
- Follow-up run log: `automation/runs/2026-06-18-hh-linkedin-mail-scan-after-agent-restart.md`.
