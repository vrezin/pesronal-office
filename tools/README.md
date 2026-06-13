# Tools

Local tools, MCP servers, helper services, and automation that belong to the personal operating system.

## Rule

All personal-office tools should live under this directory.

Do not put personal finance, calendar, inbox, or life-management tools into company repositories such as `aistudio`, `fincom`, or `setronica`.

## Current Tools

- `zenmoney-mcp/` - MCP server for ZenMoney, the source of personal finance transaction history, accounts, categories, and budgets.
- `linkedin-mcp/` - local LinkedIn MCP runtime with copied authenticated browser profile and helper scripts for job/profile lookup; registered in `.codex/config.toml` as the `linkedin` MCP server.
- `headhunter-mcp-server/` - applicant-first HeadHunter MCP fork for vacancy search, resume lookup, applications, and negotiation history.
- `headhunter-web-mcp/` - browser/session-based HeadHunter applicant MCP for reading HH vacancy pages through the logged-in web UI; registered in `.codex/config.toml` as `headhunter_web`.
- `../wiki/playbooks/headhunter-web-mcp-implementation-brief.md` - implementation brief for a browser/session-based HeadHunter applicant MCP fallback.

## Safety

- Treat tools that can change external systems as sensitive.
- Prefer read-only mode for finance tools unless the user explicitly asks for writes.
- Do not commit credentials, tokens, or local auth files.
- Tool outputs that become decisions, tasks, or records should be captured in the relevant repository artifact, not only in chat.
