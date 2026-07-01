# Job Search Contour Migration To Raspberry Pi

- Date: 2026-06-28
- Target host: `raspberrypi-codex`
- Target user: `openclaw`
- Target path: `/home/openclaw/personal-office-agent/job-search-contour/`
- OpenClaw target agent: `job-search`
- Status: Runtime ready for read-only job-search intake smoke - HH healthy; LinkedIn MCP service/probe/auth healthy; Gmail/GCalendar MCP installed, OAuth-enabled, and read-only smoke passed

## Goal

Move the Personal Office job-search runtime contour to the Raspberry Pi OpenClaw host:

- HH.ru authenticated applicant MCP runtime;
- LinkedIn authenticated MCP runtime;
- Gmail monitor prompts/state;
- Google Calendar routing expectations;
- dedicated OpenClaw agent for job-search intake and routing.

## Transfer Boundary

Transferred as runtime mirror, not as full Personal Office source of truth.

Included:

- `tools/headhunter-web-mcp/` source and `.local/state/hh-storage-state.json`;
- `tools/linkedin-mcp/` scripts, `cookies.json`, `source-state.json`, and browser `profile/`;
- `automation/prompts/hh-gmail-monitor.md`;
- `automation/prompts/linkedin-gmail-monitor.md`;
- `automation/state/hh-gmail-monitor-state.md`;
- `automation/state/linkedin-gmail-monitor-state.md`;
- monitor wrapper scripts and LinkedIn MCP client;
- Personal Brand routing map, operating model, job-intake `INDEX.md`, and `COMPANY_NOTES.md`;
- `personal-brand-career` and `automation-monitoring` local skills.

Excluded or not treated as authoritative:

- full Personal Office repository;
- full `finance/`, `people/`, `life/`, `companies/`, `memory/`, `calendar/`, and `tasks/`;
- x64 or workstation-specific Python virtual environments;
- workstation-specific browser binaries and trace dumps.

## Runtime Notes

- Pi has Python 3.13 and `python3-venv`.
- `uv` was not installed initially.
- `pip install --user uv` was blocked by Debian PEP 668.
- A bootstrap venv install of `uv` started but was too slow/hung on the 25 MB wheel and was stopped.
- HH runtime was installed on Pi from a workstation-downloaded arm64 wheelhouse.
- HH MCP uses Pi system Chromium through `HH_WEB_CHROMIUM_EXECUTABLE=/usr/bin/chromium` and `HH_WEB_CHROMIUM_NO_SANDBOX=1`.
- HH navigation timeout was raised through `HH_WEB_NAV_TIMEOUT_MS=60000` and `HH_WEB_TIMEOUT_MS=60000`.
- HH healthcheck passed through the `job-search` agent: storage state exists, HH is reachable, and the session appears logged in.
- LinkedIn runtime was installed on Pi from a workstation-downloaded arm64 wheelhouse with `linkedin-scraper-mcp==4.13.2`.
- LinkedIn Patchright browser bundles were downloaded on the workstation, transferred to Pi, and installed under `tools/linkedin-mcp/patchright-browsers/`.
- LinkedIn MCP is managed by the `openclaw` user systemd service `linkedin-mcp.service` on `127.0.0.1:8019`; the service is enabled and active.
- LinkedIn MCP probe passes and exposes 17 tools.
- Pre-refresh LinkedIn authenticated session check failed: `get_my_profile` detected a stale/expired session and opened a login flow. Existing copied cookies/profile were not enough on Pi.
- 2026-06-30 decision note: avoid relying on WSL-host browser display forwarding for LinkedIn re-auth. The preferred path is to expose a temporary remote UI for the Pi-side Chromium/profile and use the second laptop only as the client screen. Authenticating on the second laptop and copying auth to Pi is a fallback, not the main route.
- 2026-06-30 implementation note: use the package login flow, not raw Chromium. Running `/usr/bin/chromium --user-data-dir .../profile` can show a logged-in browser, but it does not necessarily create the MCP runtime files `cookies.json` and `source-state.json`. The successful flow was `.venv/bin/linkedin-mcp-server --login --chrome-path /usr/bin/chromium --user-data-dir .../profile` displayed on `adrelinux` through X11 forwarding.
- 2026-06-30 Gmail/GCalendar spike note: `workspace-mcp==1.22.0` was installed in an isolated venv under `tools/google-workspace-mcp-spike/`. The first `pip install workspace-mcp` failed only because the slow Pi download of `google-api-python-client` was incomplete; retrying with `pip install --resume-retries 10 workspace-mcp` completed successfully.
- 2026-06-30 OpenClaw registration note: `google_workspace` was added to `/home/openclaw/.openclaw/openclaw.json` as a disabled/no-probe stdio MCP entry using `workspace-mcp --single-user --tools gmail calendar --read-only` and `WORKSPACE_MCP_CREDENTIALS_DIR=/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/credentials`.
- 2026-06-30 Google Workspace smoke note: `openclaw mcp doctor google_workspace` passed with only the expected disabled warning. A direct stdio smoke with the intended credential directory started successfully, limited the server to Gmail/Calendar read-only mode, and disabled 11 write-capable Gmail/Calendar tools.
- 2026-07-01 Google Workspace auth note: `.env.google-workspace.local` was copied to Pi with mode `600`; CRLF line endings were normalized after the first generated OAuth URL showed `%0D` in the client ID.
- 2026-07-01 Google Workspace OAuth note: OAuth completed for `v.rezin@gmail.com` through a temporary loopback `streamable-http` server and SSH tunnel. Token files were saved under the configured credential directory with mode `600`; no token or secret values were printed.
- 2026-07-01 Google Workspace read-only smoke note: Gmail label listing returned 49 labels and Google Calendar listing returned 6 calendars. No Gmail message bodies or calendar event details were read.
- 2026-07-01 OpenClaw note: `google_workspace` is enabled as a stdio MCP server through `start-google-workspace-mcp.sh`; `openclaw mcp probe google_workspace --json` passes and exposes 11 read-oriented Gmail/Calendar tools plus auth/resource/prompt helpers.
- 2026-07-01 Pi-local Gmail routing smoke note: the `job-search` agent searched archived Gmail through `google_workspace`, read minimal content for one HH and one LinkedIn message, classified both as `new_vacancy` digests, recognized both as already-processed duplicates, and made no-op routing decisions. Run log: `automation/runs/2026-07-01-1248-pi-gmail-e2e-routing-smoke.md`.

## Pi State After This Pass

- `/home/openclaw/personal-office-agent/job-search-contour/` exists and is owned by `openclaw`.
- Contour size after runtime install: about 1.9 GB.
- HH authenticated storage state is present at `tools/headhunter-web-mcp/.local/state/hh-storage-state.json`.
- LinkedIn `cookies.json` is present.
- LinkedIn browser profile cookie DB is present at `tools/linkedin-mcp/profile/Default/Cookies`.
- OpenClaw agent `job-search` exists:
  - workspace: `/home/openclaw/personal-office-agent/openclaw-workspaces/job-search`;
  - agent state: `/home/openclaw/personal-office-agent/openclaw-agents/job-search`;
  - model: `openai/gpt-5.5`.
- OpenAI/Codex OAuth state was copied from `default` and re-owned for `job-search`; `openclaw models status --agent job-search` reports the OpenAI OAuth profile usable.
- Agent smoke test passed in session `agent:job-search:bootstrap-smoke-2026-06-28`.
- OpenClaw MCP entries are enabled:
  - `headhunter_web`;
  - `linkedin`.
- Final read-only verification on 2026-06-28:
  - `openclaw mcp probe --json` succeeds for `headhunter_web` and `linkedin`;
  - `headhunter_web` exposes 11 tools;
  - `linkedin` exposes 17 tools;
  - `linkedin-mcp.service` is enabled and active;
  - listeners are loopback-scoped on `127.0.0.1:18789` and `127.0.0.1:8019`.
- `headhunter_web` healthcheck passed.
- Pre-refresh `linkedin` runtime/probe passed, but LinkedIn auth still had to be refreshed before real use.
- LinkedIn auth refreshed on 2026-06-30:
  - `adrelinux-codex` was used as the live Linux display client;
  - `adrelinux` public SSH key was added to `openclaw@raspberrypi` for direct X11 login sessions;
  - `linkedin-mcp-server --login` completed successfully and exported 12 LinkedIn cookies plus `source-state.json`;
  - `linkedin-mcp.service` was restarted and is active;
  - non-mutating `get_my_profile` smoke passed through `job-search`, resolving `/in/me/` to `https://www.linkedin.com/in/vladimirrezin/`;
  - no cookies or tokens were printed.
- Google Workspace MCP spike installed on 2026-06-30:
  - package: `workspace-mcp==1.22.0`;
  - venv: `/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/.venv`;
  - credential directory: `/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/credentials`, owned by `openclaw`, mode `700`;
  - OpenClaw server: `google_workspace`;
  - state: enabled, OAuth-enabled for `v.rezin@gmail.com`, and read-only smoke passed.

## Gmail And Calendar

Gmail and Google Calendar are now exposed on the Pi through the read-only `google_workspace` MCP server.

The job-search agent must not fake Gmail or Calendar scans when those connectors are unavailable.

2026-06-30 review:

- OpenClaw stock plugins on Pi include `google`, but it is disabled/not allowlisted and is a Gemini/Vertex/search/media/speech provider plugin, not a Gmail/Calendar connector.
- OpenClaw stock plugins on Pi include `webhooks`, but it is disabled/not allowlisted and would require explicit route/secret configuration before it can be used as an inbound TaskFlow bridge.
- Current Codex/workstation environment has connected Gmail and Google Calendar tools.
- Existing `automation/prompts/hh-gmail-monitor.md` and `automation/prompts/linkedin-gmail-monitor.md` already express the correct Gmail scanning, state, and run-log behavior.
- Workstation/Codex handoff is useful for a concept demo or short-term home fallback, but it is not a production-like solution because the laptop/workstation is not always on.
- Production-like target: Gmail/GCalendar intake should run on an always-on node, preferably Pi-local or another server-side service, with explicit OAuth/token storage and read/write safety boundaries.
- Recommended sequencing: use workstation/Codex handoff only to prove the job-search routing shape, then choose between Pi-local Gmail/GCalendar MCP and a minimal always-on poller.
- Google Workspace MCP shortlist found on 2026-06-30:
  - `taylorwilsdon/google_workspace_mcp` / `workspace-mcp`: strongest feature candidate, Python/uv, OAuth 2.1/PKCE, service-account mode, local or GCS credential storage, tool/service selection and read-only controls. Pi spike installed successfully and is registered as enabled OpenClaw server `google_workspace` in read-only Gmail/Calendar mode.
  - `aliwatters/gsuite-mcp`: strongest Pi-operational candidate, Go single binary, `linux_arm64` releases, broad Workspace coverage, multi-account and token command hook.
  - `2389-research/gsuite-mcp`: smaller Go candidate with Gmail/Calendar/Contacts/Tasks and `linux_arm64` releases.
  - archived single-purpose Gmail/Calendar servers are not preferred for this contour.

## Next Steps

1. Adapt or mirror the existing HH/LinkedIn Gmail monitor prompts so they use Pi-local Gmail tools instead of workstation Codex connectors.
2. Add conservative polling/backoff and run-log/state rules before scheduling unattended Pi Gmail/Calendar checks.
3. Run a non-archived Inbox E2E check when the next fresh HH or LinkedIn message arrives.
4. Decide after monitor adaptation whether `workspace-mcp` is sufficient or whether to compare the Go `gsuite-mcp` binary path for operational simplicity.
