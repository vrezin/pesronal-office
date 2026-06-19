# Build YC Work at a Startup Playwright MCP Monitor

- Created: 2026-06-19
- Start no earlier than: 2026-06-22
- Status: active
- Domain: automation / personal brand career
- Source: https://www.workatastartup.com/

## Goal

Next week, create a basic local automation/MCP path for checking new Work at a Startup roles through Playwright.

## Desired Outcome

A minimal monitor that can:

- open Work at a Startup with an authenticated/local browser session if needed;
- capture visible job cards / search results;
- identify new or changed roles since last run;
- write a run log to `automation/runs/`;
- update state in `automation/state/`;
- route promising roles into the normal `job-intake` workflow.

## First Scope

Keep this intentionally basic:

- no complex ranking model;
- no mass scraping;
- no auto-apply;
- no credentials in repo;
- manual review before creating application tasks.

## Suggested Files

- `automation/prompts/yc-workatastartup-monitor.md`
- `automation/scripts/run-yc-workatastartup-monitor.sh`
- `automation/state/yc-workatastartup-monitor-state.md`
- `automation/runs/YYYY-MM-DD-HHMM-yc-workatastartup-monitor.md`

## Safety / Practical Notes

- Treat Work at a Startup as a logged-in browser workflow, not a clean public API.
- Avoid storing secrets or browser session tokens in the repo.
- Keep output bounded: only new/changed role titles, companies, locations, links, and short fit notes.
- Every selected vacancy still needs a normal JD archive and analysis before applying.
