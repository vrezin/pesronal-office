# HeadHunter Web-Based Applicant MCP

Web-based MCP server for working with hh.ru as an applicant, using browser session auth.

## Setup

```bash
tools/job-search-runtime/setup-shared-env.sh
playwright install chromium
```

The target runtime is the shared Personal Office job-search environment:

```text
<repo-root>/.runtime/job-search-venv
```

Tool-local `.venv` directories are migration/fallback state, not the target
steady state.

## Authentication

```bash
bash scripts/auth.sh
```

Opens a headed browser, logs in manually, saves session to `.local/state/hh-storage-state.json`.
The script uses the shared job-search runtime by default:

```text
<repo-root>/.runtime/job-search-venv
```

On the Pi, it also uses `/usr/bin/chromium` with `--no-sandbox` when available.

Pi auth refresh flow:

```bash
ssh -Y openclaw@raspberrypi-codex
cd <repo-root>
bash tools/headhunter-web-mcp/scripts/auth.sh
```

After login completes, rerun `hh_web_healthcheck` from the shared runtime before
deleting any old `.venv` fallback.

Current local setup note:

- On this workstation headed Playwright/Chromium auth is unreliable.
- The working applicant session state was copied from the working Linux host at `192.168.1.72`.
- The local MCP runtime uses that copied `.local/state/hh-storage-state.json` in headless mode.
- Do not commit `.local/` or print its contents; it contains authenticated HH cookies.
- 2026-07-03 Pi shared-runtime smoke: the only available storage state was dated
  2026-06-12 and opened an anonymous/login page. Refresh auth into the canonical
  `.local/state/hh-storage-state.json` before treating HH Web as green.

## Usage

The server runs over stdio MCP transport:

```bash
tools/job-search-runtime/run-headhunter-web-mcp.sh
```

## Codex Registration

Add to `.codex/config.toml`:

```toml
[mcp_servers.headhunter_web]
command = "<repo-root>/tools/job-search-runtime/run-headhunter-web-mcp.sh"
args = []

[mcp_servers.headhunter_web.env]
UV_CACHE_DIR = "/home/adre/personal-office/.cache/uv"
HH_WEB_STORAGE_STATE = "/home/adre/personal-office/tools/headhunter-web-mcp/.local/state/hh-storage-state.json"
```

## Tools

| Tool | Description |
|------|-------------|
| `hh_web_healthcheck` | Verify session health and login status |
| `hh_web_get_vacancy` | Get full vacancy details by ID or URL |
| `hh_web_search_vacancies` | Search vacancies with filters |
| `hh_web_list_resumes` | List applicant resumes and HH resume hashes |
| `hh_web_get_resume` | Get resume detail and management state |
| `hh_web_get_suitable_vacancies` | Search HH vacancies suitable for a selected resume |
| `hh_web_get_applications` | List sent applications and statuses from applicant negotiations |
| `hh_web_extract_from_digest_urls` | Batch-process vacancy URLs from digests |
| `hh_web_classify_email` | Classify HH email body into digest, view, rejection, chat, application status, or unknown |
| `hh_web_parse_digest_email` | Parse HH vacancy digest email, dedupe links, check job-intake index, and optionally fetch vacancy details |
| `hh_web_open_chat_by_chat_id` | Open applicant chat by HH chat id and best-effort parse vacancy/status/latest message |

### HH Email Processing

`hh_web_classify_email(body, subject="")` is a lightweight classifier for HH.ru
mail. It returns:

- `vacancy_digest` for emails with vacancy links/recommendations;
- `resume_view` for resume-view notifications;
- `explicit_rejection` for employer rejection emails;
- `chat_message` for chat notifications with `chat_id`;
- `application_status` for generic application-status messages;
- `unknown` when no supported pattern is detected.

`hh_web_parse_digest_email(...)` is the main tool for "spam from HH" processing.
It extracts `hh.ru/vacancy/<id>` links from the pasted email body, deduplicates
links by vacancy id, checks already-known vacancies against:

```text
personal-projects/personal-brand/workspace/job-intake/INDEX.md
```

and, when `fetch_details=true`, opens only new vacancy links through the
authenticated browser session.

The response separates:

- `new_successes`: fetched vacancies that are readable and not already in job-intake;
- `inaccessible`: links HH shows as unavailable to the applicant;
- `failed`: links that failed because of auth, challenge, timeout, or parsing errors;
- `duplicates`: links already present in job-intake or repeated inside the same email;
- `recommended_next_tasks`: draft task filenames for new successful vacancies.

Digest results expose both a full nested `vacancy` object, when the page was
readable, and flattened `vacancy_id`, `title`, `company`, `salary`, and `status`
fields for email triage decisions.

`hh_web_extract_from_digest_urls(...)` now uses explicit per-link statuses:

- `ok`;
- `access_denied` for `Вам недоступна эта вакансия`;
- `auth_required`;
- `challenge_required`;
- `failed`.

This is intentionally not optimistic: inaccessible vacancies are returned with
`success=false`, so the caller can delete the email without creating a fake
intake artifact.

`hh_web_open_chat_by_chat_id(chat_id)` opens:

```text
https://hh.ru/applicant/resumes?dl_command=open_chat&chat_id=<chat_id>
```

and tries to infer the vacancy, company, normalized status, and latest useful
message. HH sometimes does not render chat contents in the headless browser even
with a valid applicant session. In that case the tool returns
`status="not_resolved"` with warnings instead of guessing from page chrome.

### Resume-Based Suitable Vacancy Search

`hh_web_list_resumes()` opens `https://hh.ru/applicant/resumes` and returns the
resume cards visible in the authenticated applicant account.

Returned fields include:

- `resume_id`;
- `title`;
- `employment`;
- `salary`;
- `work_format`;
- `views`;
- `new_views`;
- `invitations`;
- `lift_status`, for example `Поднять в 02:23`;
- `suitable_vacancies_url`.

`hh_web_get_resume(resume=...)` opens one resume detail page. `resume` can be a
resume hash or title substring, for example `AI Transformation`.

Returned detail fields include:

- basic resume metadata;
- `experience_total`;
- `skills`;
- `about`;
- `completion_text`;
- `lift_details`, for example `Можно завтра в 02:23`;
- `auto_raise`;
- `visibility`;
- `suitable_vacancies_count`;
- `suitable_vacancies_url`.

Write actions such as editing, changing visibility, auto-raise, or lifting a
resume are intentionally not executed by the read tools. Add separate explicit
write tools for those actions only when the user asks for that exact action.

`hh_web_get_suitable_vacancies(...)` opens HH search with the `resume=<hash>`
parameter, which is the same "suitable vacancies for this resume" search that HH
links from the applicant resume list.

Arguments:

- `resume`: optional resume hash or title substring, for example `AI Transformation`;
- `page`: zero-based HH search page;
- `limit`: maximum returned cards from the visible page;
- `remote`: optional remote-only filter;
- `salary_from`: optional minimum salary filter;
- `text`: optional keyword filter;
- `include_applications`: when true, merge known applicant negotiation statuses into returned cards.

The suitable search response reuses the standard search result shape and adds:

- `resume_id`;
- `resume_title`;
- `search_url`.

Implementation note: search-result parsing is card-based. It anchors on
`data-qa='vacancy-serp__vacancy'` around each `serp-item__title`, so employer
and location are read from the same card and do not drift when HH injects
promotional blocks.

### Application Status Parsing

`hh_web_get_applications(max_pages=4)` opens `https://hh.ru/applicant/negotiations`
and parses applicant-side response cards across paginated pages.

Returned fields include:

- `status`: normalized enum (`not_viewed`, `viewed`, `rejected`, `invitation`, `interview`, `applied`, `unknown`);
- `status_text`: raw HH label, for example `Не просмотрен`, `Просмотрен`, `Отказ`, `Собеседование`;
- `title`, `company`, `vacancy_id`, `url`, `date`;
- `online_text` and `response_rate_text` when HH shows them;
- `status_counts` summary in the top-level response.

Implementation note: the HH applicant UI currently does not expose the old
`data-qa='negotiation-item'` selector. The parser therefore anchors on vacancy
links containing `hhtmFrom=negotiation_list` and reads the surrounding response
card. Recommendation blocks are filtered out by requiring a recognized response
status.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HH_WEB_STORAGE_STATE` | `.local/state/hh-storage-state.json` | Path to Playwright storage state |
| `HH_WEB_HEADLESS` | `1` | Run headless (0 for headed) |
| `HH_WEB_SLOWMO_MS` | `0` | Slow down actions by ms |
| `HH_WEB_TIMEOUT_MS` | `15000` | Default timeout in ms |
| `HH_WEB_USER_AGENT` | (empty) | Custom user agent |
| `HH_WEB_CHROMIUM_EXECUTABLE` | (empty) | Optional system Chromium executable path |
| `HH_WEB_CHROMIUM_NO_SANDBOX` | `0` | Pass `--no-sandbox` when launching Chromium |
| `HH_WEB_NAV_TIMEOUT_MS` | `15000` | Navigation timeout in ms |
