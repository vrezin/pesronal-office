# LinkedIn Gmail Monitor Automation

- Area: personal-projects / personal-brand / automation
- Related workspace: `automation/`, `tools/linkedin-mcp/`, `personal-projects/personal-brand/workspace/job-intake/`
- Status: active

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

Hook the new monitor into cron and verify one dry run against the current LinkedIn mailbox.

## Implementation Note

- The cron entry has been added.
- The LinkedIn MCP client helper is in place.
- The remaining check is a first live dry run, which depends on the local runtime binding cleanly on the host outside this editing sandbox.
