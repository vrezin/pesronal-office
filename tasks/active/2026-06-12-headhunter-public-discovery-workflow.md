# Build HeadHunter Public Discovery Workflow

- Created: 2026-06-12
- Status: active
- Area: personal-projects / personal-brand / tools
- Related tool: `tools/headhunter-mcp-server/`

## Goal

Use the public HeadHunter MCP functions to remove manual vacancy copy/paste and first-pass filtering from the job-search workflow.

## Scope

- search vacancies;
- inspect vacancy details;
- inspect employer/company details;
- collect similar vacancies;
- keep only the shortlist that deserves manual review and resume adaptation.

## Current Finding

As of 2026-06-12, the local MCP server starts and can call `hh_get_dictionaries`, but `hh_get_vacancy` and `hh_search_vacancies` return `403 Forbidden` in the current session.

Code-side fixes already made:

- MCP entrypoint now uses a sync `main()` wrapper around the async server;
- Codex config gives `uv` a writable cache directory;
- HH client uses `Personal HH Applicant Assistant/0.1 (v.rezin@gmail.com)` as `HH-User-Agent`;
- HH client has explicit HTTP timeouts.

This likely still needs approved HH app credentials, OAuth, or another vacancy-detail access path before it can replace manual JD retrieval.

## Next Step

- Resolve vacancy search/detail `403`.
- After that, wire public MCP results into archive/analysis notes.
