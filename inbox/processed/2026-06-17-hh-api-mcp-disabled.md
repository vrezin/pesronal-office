# HH API MCP Disabled

- Created: 2026-06-17
- Source: user confirmation + HH email about application `#23262`
- Area: tools / automation / personal-brand-career

## Decision

Disable the official/API HeadHunter MCP server and use only the browser/session-based `headhunter_web` MCP for HH workflows.

## Reason

HH rejected the app registration for `Personal HH Applicant Assistant` and stated that the described capabilities are not realizable through the HH API. Earlier local checks also showed that the API path was not reliable for this applicant workflow: vacancy detail/search returned `403 Forbidden`, and negotiation history required unavailable OAuth access.

## Actions

- Removed `[mcp_servers.headhunter]` from `.codex/config.toml`.
- Removed approval entries for `hh_get_vacancy`, `hh_search_vacancies`, and `hh_get_negotiations`.
- Kept `[mcp_servers.headhunter_web]` as the only active HH MCP server.
- Marked the HH app-registration and public API workflow tasks as closed.
- Updated tool documentation and the web-MCP implementation brief to reflect that the API path is historical only.

## Operating Rule

For HH from now on:

- use `headhunter_web` for vacancy details, suitable vacancies, application statuses and chat/status checks;
- do not use or revive the `headhunter` API MCP unless HH policy/access materially changes.
