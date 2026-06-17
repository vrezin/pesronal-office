# LinkedIn Gmail Monitor Automation

- Area: personal-projects / personal-brand / automation
- Related workspace: `automation/`, `tools/linkedin-mcp/`, `personal-projects/personal-brand/workspace/job-intake/`
- Status: done

## Objective

Build an unattended 4-hour LinkedIn Gmail monitor that scans `from:linkedin.com` mail, classifies job-related messages, enriches job ids through the local LinkedIn MCP runtime when needed, and updates personal-brand job-intake artifacts.

## Scope

- Mirror the HH monitor structure for LinkedIn mail.
- Use the current LinkedIn mailbox rules already established in the workspace.
- Keep Gmail mutations conservative in unattended runs.
- Leave a durable run log and state marker for idempotency.

## Deliverables

1. `automation/prompts/linkedin-gmail-monitor.md`
2. `automation/scripts/run-linkedin-gmail-monitor.sh`
3. `automation/scripts/linkedin-mcp-client.py`
4. `automation/state/linkedin-gmail-monitor-state.md`
5. `automation/cron/linkedin-gmail-monitor.cron`
6. `automation/README.md` update

## Next Action

Implementation is complete. Scheduler / unattended commit reliability is tracked separately in `tasks/active/2026-06-15-investigate-hh-linkedin-cron-missed-runs.md`.

## Implementation Note

- The cron entry has been added.
- The LinkedIn MCP client helper is in place.
- The repo now registers a local LinkedIn MCP server named `linkedin` in `.codex/config.toml` and points it to `http://127.0.0.1:8019/mcp`; the monitor should prefer that registered server and only fall back to `tools/linkedin-mcp/scripts/start-daemon.sh` if the daemon is unavailable inside the run.
- Live manual runs succeeded on 2026-06-15 at 09:07 for both LinkedIn and HH. Gmail access worked and no new post-marker messages required routing.
- The remaining reliability issue is scheduler-level: cron fired the 00:00 jobs but did not appear to fire the expected 04:00 and 08:00 jobs on 2026-06-15.
