# HeadHunter Public API Discovery Workflow Closed

- Created: 2026-06-17
- Status: Done
- Outcome: Closed as not viable
- Area: personal-projects / personal-brand / tools
- Related tool: `tools/headhunter-mcp-server/`

## Outcome

The public/API HeadHunter MCP path is no longer the active discovery route.

## Reason

- Local API calls for vacancy detail/search returned `403 Forbidden`.
- Negotiations required unavailable OAuth access.
- HH rejected app registration `#23262` for the intended applicant workflow.

## Decision

Use `tools/headhunter-web-mcp/` and the registered `headhunter_web` MCP server as the only real HH automation route.

## Historical Note

`tools/headhunter-mcp-server/` can remain in the repository as historical/reference code, but should not be registered or used in normal job-search workflows.
