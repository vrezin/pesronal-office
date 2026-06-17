# HeadHunter Web-Based Applicant MCP - Implementation Brief

- Date: 2026-06-12
- Owner: personal-office
- Target runtime: Python 3.13 + uv
- Goal: build a web-based MCP server for working with hh.ru as an applicant, not as an employer/recruiter.
- Intended implementation path: `tools/headhunter-web-mcp/`
- Related API fork: `tools/headhunter-mcp-server/`

## Problem

The official HeadHunter API route is not a viable applicant-workflow path for this workspace:

- developer app registration is employer-oriented;
- applicant API support appears constrained/deprecated;
- public API reference endpoints work, but vacancy search/detail calls can return `403 Forbidden`;
- HH rejected application `#23262` on 2026-06-17, stating that the described capabilities are not realizable through the HH API.

We need a web-based MCP server that uses the normal hh.ru applicant web UI through an authenticated browser session and exposes a stable MCP interface for discovery, JD extraction, status checks, and controlled apply workflows.

## Non-Goals

- Do not build an HR/recruiter/employer tool.
- Do not scrape employer candidate databases.
- Do not bypass captcha, 2FA, access control, paywalls, or anti-abuse systems.
- Do not store hh.ru password in the repository.
- Do not auto-apply blindly.
- Do not make destructive actions without explicit confirmation.
- Do not replace the existing Gmail HH monitor; integrate with it later.

## Runtime And Tooling

Use:

- Python `3.13`;
- `uv` for dependency and script management;
- `mcp` Python SDK;
- Playwright async Python for browser automation;
- Pydantic for typed tool inputs/outputs;
- Ruff/pytest if tests are added.

Expected project path:

```text
tools/headhunter-web-mcp/
```

Expected basic files:

```text
tools/headhunter-web-mcp/
  pyproject.toml
  README.md
  server.py
  hh_web/
    __init__.py
    browser.py
    models.py
    pages.py
    parser.py
    tools.py
  scripts/
    auth.sh
    smoke.sh
  tests/
```

## Auth Model

Use browser session auth, not stored credentials.

Requirements:

- provide a headed login/bootstrap script;
- user logs into hh.ru manually in a browser window;
- persist Playwright `storage_state` locally;
- default state path:

```text
tools/headhunter-web-mcp/.local/state/hh-storage-state.json
```

- `.local/` must be gitignored;
- never print cookies, auth headers, phone, email, or tokens;
- if session expires, return a clear `AUTH_REQUIRED` tool error with instructions to rerun `scripts/auth.sh`.

## MCP Transport

Primary transport: stdio MCP, compatible with Codex config.

Entrypoint:

```toml
[project.scripts]
headhunter-web-mcp = "server:main"
```

Server must not print normal logs to stdout. Logs go to stderr or a local log file.

## Core Design

Phase 1 must be read-only and stable:

- search vacancies;
- open vacancy by HH id or URL;
- extract normalized JD;
- get visible application status from vacancy/search/application pages;
- list sent applications if accessible through the web UI;
- extract screening questions from a vacancy page;
- produce a compact JSON payload suitable for job-intake.

Phase 2 can add controlled writes:

- submit an application with a chosen resume and optional cover letter;
- answer screening questions;
- add vacancy to favorites;
- archive/hide vacancy.

All write tools must require an explicit `confirm=true` input and return a dry-run preview when `confirm=false`.

## Tools To Implement

### `hh_web_healthcheck`

Purpose: verify browser/session health.

Returns:

- whether storage state exists;
- whether hh.ru is reachable;
- whether the session appears logged in;
- current applicant identity if visible, redacted if needed;
- current limitations.

### `hh_web_get_vacancy`

Input:

- `vacancy_id_or_url: str`

Output:

- vacancy id;
- title;
- company;
- salary;
- location;
- work format;
- schedule;
- experience;
- publication date if visible;
- already applied flag if visible;
- full raw description as markdown/plain text;
- screening questions if visible;
- canonical HH URL;
- extraction confidence.

### `hh_web_search_vacancies`

Input:

- `text: str | None`;
- `area: str | None`;
- `remote: bool | None`;
- `experience: str | None`;
- `salary_from: int | None`;
- `page: int = 0`;
- `limit: int = 20`.

Output:

- list of normalized vacancy cards;
- total visible count if available;
- search URL used;
- warnings if filters could not be applied.

### `hh_web_get_applications`

Purpose: read sent applications/statuses from applicant UI.

Output per application:

- status: viewed / not viewed / rejected / invitation / interview / unknown;
- title;
- company;
- vacancy id or URL;
- date;
- last message snippet if visible;
- next action classification.

### `hh_web_extract_from_digest_urls`

Input:

- `urls: list[str]`

Purpose: batch-open HH vacancy URLs from Gmail digests and return normalized JDs/cards.

Must:

- avoid loading more than `limit` pages per call;
- add delay/jitter between pages;
- return per-URL errors instead of failing the whole batch.

### `hh_web_apply_to_vacancy`

Phase 2 only.

Input:

- `vacancy_id_or_url: str`;
- `resume_hint: str | None`;
- `cover_letter: str | None`;
- `screening_answers: dict[str, str] | None`;
- `confirm: bool = false`.

Behavior:

- if `confirm=false`, return a preview of detected resume options, screening questions, and proposed submission;
- if `confirm=true`, submit only after all required questions are answered;
- never guess answers to employer questions.

## Parsing Requirements

Prefer robust extraction over brittle CSS selectors:

- use accessible text/roles where possible;
- keep selector logic centralized in `hh_web/pages.py`;
- normalize text into markdown/plain text;
- preserve the original visible JD text enough for job-intake;
- strip repeated HH boilerplate where safe;
- keep salary, format, schedule, experience as structured fields.

Each parser should return:

- `data`;
- `warnings`;
- `confidence`.

## Browser Requirements

Default:

- Chromium;
- headless for MCP calls;
- headed for auth/bootstrap and debug.

Environment variables:

```text
HH_WEB_STORAGE_STATE=tools/headhunter-web-mcp/.local/state/hh-storage-state.json
HH_WEB_HEADLESS=1
HH_WEB_SLOWMO_MS=0
HH_WEB_TIMEOUT_MS=15000
HH_WEB_USER_AGENT=
```

Do not hardcode personal credentials.

## Reliability Rules

- Every web action must have bounded timeout.
- Tool calls must return structured errors.
- A single failed vacancy must not fail a batch.
- Detect login-required pages and return `AUTH_REQUIRED`.
- Detect captcha/challenge pages and return `CHALLENGE_REQUIRED`; do not bypass.
- Use small concurrency; default sequential browsing is acceptable.
- Add polite delays for batch digest processing.

## Output Shape For Job Intake

Each full vacancy extraction should be convertible into:

```json
{
  "source": "hh-web",
  "vacancy_id": "134077560",
  "url": "https://hh.ru/vacancy/134077560",
  "company": "...",
  "role_title": "...",
  "location_format": "...",
  "salary": "...",
  "experience": "...",
  "schedule": "...",
  "raw_jd_markdown": "...",
  "screening_questions": [],
  "application_status": "not_applied|applied|viewed|rejected|invitation|unknown",
  "extraction_warnings": []
}
```

## Codex Registration

After implementation, register as a separate MCP server, not replacing the API fork:

```toml
[mcp_servers.headhunter_web]
command = "/home/adre/.local/bin/uv"
args = ["run", "--directory", "/home/adre/personal-office/tools/headhunter-web-mcp", "headhunter-web-mcp"]

[mcp_servers.headhunter_web.env]
UV_CACHE_DIR = "/home/adre/personal-office/.cache/uv"
HH_WEB_STORAGE_STATE = "/home/adre/personal-office/tools/headhunter-web-mcp/.local/state/hh-storage-state.json"
```

## Tests / Smoke Checks

Minimum checks:

- `uv run python -m py_compile server.py hh_web/*.py`;
- `uv run pytest` if tests exist;
- `uv run headhunter-web-mcp` stays alive under stdio until killed;
- `scripts/auth.sh` creates storage state after manual login;
- `hh_web_healthcheck` reports logged-in state;
- `hh_web_get_vacancy` works on a pasted HH vacancy URL;
- batch digest extraction handles at least 3 URLs and returns per-item results.

## Acceptance Criteria

The first usable version is done when:

- Codex can start the MCP server without handshake failure;
- user can authenticate manually once through a headed browser;
- the server can read a vacancy page from HH UI and return normalized JD text;
- the server can process a list of HH vacancy links from a Gmail digest;
- failures are explicit and bounded, not hangs;
- no credentials/session files are committed;
- write/apply tools are either absent or dry-run by default with explicit confirmation.

## First Implementation Slice

Build only this first:

1. Project skeleton with Python 3.13 + uv.
2. `scripts/auth.sh` headed login and storage-state save.
3. `hh_web_healthcheck`.
4. `hh_web_get_vacancy`.
5. `hh_web_extract_from_digest_urls`.
6. Codex config snippet in README, but do not auto-edit `.codex/config.toml` until smoke test passes.

This slice is enough to remove manual JD copy/paste from HH digest processing.
