# Google Workspace OAuth Bootstrap For Pi Job Search

- Date: 2026-06-30
- Target host: `raspberrypi-codex`
- Target user: `openclaw`
- MCP server: `google_workspace`
- Package: `workspace-mcp==1.22.0`
- Goal: enable Gmail and Google Calendar read-only intake for the Pi `job-search` contour.
- Status: Completed for `v.rezin@gmail.com` on 2026-07-01.

## Safety Boundary

Do not commit or print Google OAuth client secrets, refresh tokens, token files, or exported environment files.

Keep Google Workspace access read-only for the first production-like pass:

- Gmail: read/search messages and metadata only.
- Calendar: read/list events and calendars only.
- No sending mail.
- No drafting mail.
- No label/filter changes.
- No event creation/update/deletion.

## Cost And Quota Note

The Google Cloud Free Tier page is not the same thing as Google Workspace API pricing. Gmail API and Google Calendar API are not listed there as generic Google Cloud Free Tier products, but standard Gmail/Calendar API use is currently available at no additional cost under the Workspace API daily billing thresholds.

Current practical implication for this contour:

- Personal Office job-search polling should be cost-free if it stays well below quota.
- The Pi monitor must still use conservative polling, backoff, and read-only scopes.
- Re-check Workspace API pricing before turning this into a broader multi-user or high-volume workflow.

Reference thresholds as of 2026-07-01:

- Gmail API: 80,000,000 quota units per day per project before charges apply; per-minute limits also apply.
- Google Calendar API: 1,000,000 requests per day per project before charges apply; per-minute limits also apply.

## Current Pi State

`workspace-mcp` is installed in:

`/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/.venv`

Credential directory is:

`/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/credentials`

OpenClaw MCP entry `google_workspace` is enabled:

```text
workspace-mcp --single-user --tools gmail calendar --read-only
```

## Google Cloud Console Setup

1. Create or select a Google Cloud project for Personal Office automation.
2. Enable APIs:
   - Gmail API;
   - Google Calendar API.
3. Configure OAuth consent screen:
   - app type: External is acceptable for a personal Google account;
   - publish status: Testing is acceptable for personal use;
   - add the user Google account as a test user if the app remains in Testing.
4. Create an OAuth client:
   - recommended first pass: Desktop app OAuth client;
   - keep the downloaded JSON or client id/secret outside git.
5. Use only read-only scopes during the first pass:
   - `https://www.googleapis.com/auth/gmail.readonly`;
   - `https://www.googleapis.com/auth/calendar.readonly`.

## Pi Secret Placement

Preferred runtime input for this spike is environment variables, not a repo-tracked JSON file.

Use a root-owned or `openclaw`-owned environment file outside git, for example:

`/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/.env.google-workspace.local`

Status 2026-07-01: the environment file has been copied to this Pi path and protected as `openclaw:openclaw`, mode `600`. Secret values were not printed or committed.

The file originally had CRLF line endings; those were normalized on the workstation and Pi after an OAuth URL showed `%0D` in the client ID.

Required values:

```bash
GOOGLE_OAUTH_CLIENT_ID="..."
GOOGLE_OAUTH_CLIENT_SECRET="..."
WORKSPACE_MCP_CREDENTIALS_DIR="/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/credentials"
WORKSPACE_MCP_READ_ONLY="true"
WORKSPACE_MCP_TOOLS="gmail,calendar"
OAUTHLIB_INSECURE_TRANSPORT="1"
```

The installed package prefers `WORKSPACE_MCP_CREDENTIALS_DIR`; `GOOGLE_MCP_CREDENTIALS_DIR` is only a compatibility alias.

Protect the file:

```bash
chmod 600 /home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/.env.google-workspace.local
```

## Bootstrap Smoke

Completed 2026-07-01:

- OAuth completed for `v.rezin@gmail.com` through a temporary loopback `streamable-http` server and SSH tunnel.
- Tokens exist under the configured credential directory.
- Token files are owned by `openclaw` and mode `600`.
- The temporary HTTP server was stopped after bootstrap.
- `openclaw mcp probe google_workspace --json` passes in the normal stdio configuration.
- Gmail label listing returned 49 labels.
- Google Calendar listing returned 6 calendars.
- No Gmail message bodies or calendar event details were read during the smoke.
- Write tools remain disabled by `--read-only`.

## Enable Gate

`google_workspace` was enabled after all were true:

- Gmail read-only smoke passes;
- Calendar read-only smoke passes;
- OpenClaw probe/list shows read-oriented Gmail/Calendar tools only;
- no token/client-secret file is committed to the repo;
- the task file records the auth date and verification result without secrets.
