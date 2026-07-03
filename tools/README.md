# Tools

Local tools, MCP servers, helper services, and automation that belong to the personal operating system.

## Rule

All personal-office tools should live under this directory.

Do not put personal finance, calendar, inbox, or life-management tools into company repositories such as `aistudio`, `fincom`, or `setronica`.

## Current Tools

- `zenmoney-mcp/` - MCP server for ZenMoney, the source of personal finance transaction history, accounts, categories, and budgets.
- `linkedin-mcp/` - local LinkedIn MCP runtime with copied authenticated browser profile and helper scripts for job/profile lookup; registered in `.codex/config.toml` as the `linkedin` MCP server.
- `profi-ru-mcp/` - read-only Profi.ru specialist MCP runtime with repo-owned Playwright profile under `.local/`; use it to check session state, list orders, and read order pages before routing useful leads into Personal Office artifacts.
- `headhunter-mcp-server/` - disabled HeadHunter API MCP experiment. HH rejected the app registration for this workflow on 2026-06-17, so this is kept only as historical reference and is not registered in `.codex/config.toml`.
- `headhunter-web-mcp/` - browser/session-based HeadHunter applicant MCP for reading HH vacancy pages, applications and statuses through the logged-in web UI; registered in `.codex/config.toml` as the only active HH MCP server, `headhunter_web`.
- `project-bootstrapper/` - planned Personal Office tooling prototype for turning intake/context into generated project spaces using Setronica-style operating standards.
- `memory-os/` - local standard-library validator and inspector for protocol-managed Personal Office memory.
- `personal-office-owner-operator-pack/` - OKF-like workflow pack for owner/operator commands, connector boundaries, and approval rules.
- `personal-office-archivist/` - Pi-friendly maintenance scanner for generated technical residue, stale monitor logs, and job-intake compaction candidates. It is dry-run by default and writes run/state artifacts through `automation/`.
- `../wiki/playbooks/headhunter-web-mcp-implementation-brief.md` - implementation brief for a browser/session-based HeadHunter applicant MCP fallback.

## Safety

- Treat tools that can change external systems as sensitive.
- Prefer read-only mode for finance tools unless the user explicitly asks for writes.
- Do not commit credentials, tokens, or local auth files.
- Tool outputs that become decisions, tasks, or records should be captured in the relevant repository artifact, not only in chat.
