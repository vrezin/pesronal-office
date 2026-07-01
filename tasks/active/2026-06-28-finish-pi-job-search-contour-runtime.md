# Finish Pi Job Search Contour Runtime

- Created: 2026-06-28
- Status: Active
- Area: tools / personal-brand / automation
- Related migration note: `tools/raspberrypi-openclaw/job-search-contour-migration-2026-06-28.md`
- Related OAuth bootstrap runbook: `tools/raspberrypi-openclaw/google-workspace-oauth-bootstrap-2026-06-30.md`
- Related target process: `tools/raspberrypi-openclaw/job-search-business-contour-target-2026-07-01.md`
- Related storage decision: `tools/raspberrypi-openclaw/personal-office-shared-storage-decision-2026-07-01.md`
- Related OpenClaw task: `tasks/active/2026-06-25-try-personal-office-on-raspberry-pi-openclaw.md`

## Goal

Finish the Raspberry Pi job-search contour so the dedicated OpenClaw `job-search` agent can use HH, LinkedIn, Gmail, and Google Calendar inputs without losing existing auth/cookie state.

## Current State

- Pi-side contour path exists: `/home/openclaw/personal-office-agent/job-search-contour/`.
- OpenClaw agent `job-search` exists and passed a bootstrap smoke test.
- HH storage state was copied.
- LinkedIn cookies and browser profile were copied.
- Earlier state: OpenClaw MCP entries `headhunter_web` and `linkedin` were declared but disabled until Pi-side runtimes were installed.
- Update 2026-06-28: OpenClaw MCP entries `headhunter_web` and `linkedin` are enabled.
- Update 2026-06-28: HH runtime is installed and HH healthcheck passed through the `job-search` agent.
- Update 2026-06-28: LinkedIn runtime is installed, Patchright browser bundles are present, `linkedin-mcp.service` is enabled/active, and OpenClaw MCP probe passes.
- Update 2026-06-28: Pre-refresh LinkedIn authenticated session was not usable yet; `get_my_profile` detected a stale/expired session and opened login flow.
- Update 2026-06-28: Final read-only verification passed for OpenClaw MCP discovery: `headhunter_web` exposes 11 tools, `linkedin` exposes 17 tools, and listeners are loopback-scoped on ports `18789` and `8019`.
- Update 2026-06-28: Pi contour size is about 1.9 GB after Patchright browser bundles.
- Update 2026-06-30: Local laptop Playwright/Patchright UI auth is unreliable because browser display forwarding from WSL to the host can fail.
- Update 2026-06-30: Preferred LinkedIn re-auth route is to use a second laptop as the screen/client for a remote Pi browser session, so the login is completed in the actual Pi-side Chromium/profile. Copying fresh auth from the second laptop to Pi is a fallback only, because LinkedIn may bind or score the session by device/browser/IP/fingerprint and invalidate it again.
- Update 2026-06-30: `adrelinux-codex` was used as the live Linux display client. Its public SSH key was authorized for `openclaw@raspberrypi` so it can open Pi-side X11 sessions directly.
- Update 2026-06-30: Raw `/usr/bin/chromium --user-data-dir .../profile` login was not sufficient for the MCP runtime, because it did not write `cookies.json` and `source-state.json`.
- Update 2026-06-30: Correct flow succeeded: stopped `linkedin-mcp.service`, ran `.venv/bin/linkedin-mcp-server --login --chrome-path /usr/bin/chromium --user-data-dir .../profile` on Pi through X11 forwarding to `adrelinux`, completed manual LinkedIn login, and the package exported 12 LinkedIn cookies plus `source-state.json`.
- Update 2026-06-30: After restarting `linkedin-mcp.service`, the non-mutating `get_my_profile` smoke passed through `job-search`: `/in/me/` resolved to `https://www.linkedin.com/in/vladimirrezin/`, with no messages sent and no LinkedIn mutation.
- Update 2026-06-30: OpenClaw out-of-box review found no active Pi-local Gmail or Google Calendar connector. The stock `google` plugin exists but is disabled/not allowlisted and is for Gemini/Vertex/search/media/speech, not Gmail/Calendar. The stock `webhooks` plugin exists but is also disabled/not allowlisted and would require explicit allowlist/config/secret before using it as an inbound handoff bridge.
- Update 2026-06-30: Current Codex/workstation environment has connected Gmail and Google Calendar tools, and existing `hh-gmail-monitor` / `linkedin-gmail-monitor` prompts already implement the correct Gmail scanning behavior. This is a useful demo/home fallback path, but not the target always-on architecture because the workstation/laptop is not guaranteed to be powered on.
- Update 2026-06-30: Architecture decision: workstation/Codex handoff is acceptable for concept demonstration and short-term home experimentation only. For a production-like Personal Office contour, Gmail/GCalendar intake must run on an always-on node, preferably Pi-local or another server-side service, with explicit OAuth/token storage and read/write safety boundaries.
- Update 2026-06-30: `workspace-mcp==1.22.0` was installed on Pi in an isolated spike venv at `/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/.venv`.
- Update 2026-06-30: OpenClaw MCP entry `google_workspace` was registered disabled/no-probe with command `workspace-mcp`, args `--single-user --tools gmail calendar --read-only`, and credential directory `/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/credentials` (`700`, owned by `openclaw`).
- Update 2026-06-30: `openclaw mcp doctor google_workspace` passed with only the expected disabled warning; `openclaw mcp status` shows `google_workspace: disabled`, `headhunter_web: stdio`, and `linkedin: streamable-http`.
- Update 2026-06-30: Manual runtime smoke with the same credential-dir env started `workspace-mcp` successfully in stdio mode, limited to Gmail/Calendar read-only mode, and the server disabled 11 write-capable Gmail/Calendar tools.
- Update 2026-07-01: Google Workspace OAuth environment file was copied to Pi at `/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike/.env.google-workspace.local`, owned by `openclaw:openclaw`, mode `600`. Secret values were not printed or committed.
- Update 2026-07-01: Google OAuth completed for `v.rezin@gmail.com` through a temporary loopback HTTP server and SSH tunnel. Token files now exist under the configured credential directory with mode `600`; no token or secret values were printed.
- Update 2026-07-01: Pi-local read-only smoke passed: Gmail label listing returned 49 labels and Google Calendar listing returned 6 calendars. No message bodies or event details were read during this smoke.
- Update 2026-07-01: `google_workspace` is enabled in OpenClaw as a stdio MCP server through `start-google-workspace-mcp.sh`; `openclaw mcp probe google_workspace --json` passes and exposes 11 read-oriented Gmail/Calendar tools plus auth/resource/prompt helpers.
- Update 2026-07-01: Pi-local Gmail E2E routing smoke passed using archived mail because the active Inbox had been cleaned. The `job-search` agent searched Gmail through `google_workspace`, read minimal content for one HH and one LinkedIn message, classified both as `new_vacancy` digests, recognized both as already-processed duplicates (`19f191abaf5759ab`, `19f19cc71bda9b7d`), and made no-op routing decisions. Run log: `automation/runs/2026-07-01-1248-pi-gmail-e2e-routing-smoke.md`.
- Update 2026-07-01: Target process clarified as a standalone job-search business contour with two entrypoints: scheduled Pi-side Gmail intake and Telegram ad-hoc vacancy intake. The contour must output actionable Telegram packets with verdict, selected CV, cover letter draft, and next action. See `tools/raspberrypi-openclaw/job-search-business-contour-target-2026-07-01.md`.
- Update 2026-07-01: Shared storage decision accepted: Git + Markdown as canonical artifact layer, SQLite as operational runtime state layer, private Git remote as workstation/Pi sync layer. See `tools/raspberrypi-openclaw/personal-office-shared-storage-decision-2026-07-01.md`.
- Update 2026-07-01: Shared storage and Memory OS rules were copied to the Pi `job-search-contour` bundle. The sync included Memory OS protocol/templates/retrieval entrypoints, `memory-system` skill, Memory OS CLI, owner/operator pack, shared storage decision, job-search target process, and only the narrow source_refs needed for validation. Pi-side checks passed: `memory_os.py validate`, `graph-check`, and `stale`.
- Update 2026-07-01: Architecture correction: shared `wiki/`, Memory OS protocol, Memory OS validator, and owner/operator pack belong in the Pi shared Personal Office cookbook layer, not only in `job-search-contour`. The same rules were synced to `/home/openclaw/personal-office-agent/cookbooks/personal-office/`; Memory OS checks pass there. The `job-search-contour` copy is now compatibility/local-domain context, not the architectural owner.
- Update 2026-07-01: Runtime storage foundation created. Added `tools/job-search-runtime/` SQLite schema/CLI and `automation/scripts/run-pi-job-search-sync.sh`. Copied them to Pi, initialized `automation/state/job-search-runtime.sqlite`, and seeded baseline duplicate ids from current Markdown monitor state: 5 HH ids and 2 LinkedIn ids. Pi dry-run wrapper passed and correctly skipped Git sync because `job-search-contour` is not yet a Git worktree. Run log: `automation/runs/2026-07-01-1456-pi-job-search-runtime-storage-foundation.md`.
- Update 2026-07-01: Architecture correction: Personal Office should be Pi-primary, not split between workstation and Pi. The full canonical Personal Office working tree and always-on automations should live on Raspberry Pi; the workstation is an operator/client surface that can initiate requests, review changes, and sync. Private Git remote is backup/history/sync, not a separate owner of state.
- Update 2026-07-01: Pi-primary Personal Office working tree created at `/home/openclaw/personal-office-agent/personal-office`. The Pi `openclaw` user pushed branch `main` to `git@github.com:vrezin/pesronal-office.git` using the Pi-side GitHub SSH key. Current pushed commit: `f7f447d` (`Add Pi Personal Office storage foundation`). Note: the GitHub repository name is currently spelled `pesronal-office`.
- Update 2026-07-01: First Pi-primary scheduled Gmail monitor skeleton added: `automation/prompts/pi-job-search-gmail-monitor.md` and `automation/scripts/run-pi-job-search-gmail-monitor.sh`. The runtime CLI now supports `message-status` and `mark-message`, so every Pi Gmail message can be deduped through SQLite before artifact routing. Local CLI smoke passed with a temporary SQLite DB.
- Update 2026-07-01: First Pi-primary Gmail monitor smoke succeeded through OpenClaw `job-search` and Pi-local `google_workspace`. It scanned recent HH and LinkedIn Gmail messages, checked every Gmail id through SQLite first, marked 3 HH thin digests and 5 LinkedIn thin alerts/digests as `noise`, wrote `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`, and advanced legacy HH/LinkedIn state files. A separate 5-second watchdog smoke wrote `automation/runs/2026-07-01-1829-pi-job-search-gmail-monitor.md` with `Status: blocked`, proving the wrapper leaves evidence when OpenClaw does not return before timeout.
- Update 2026-07-01: Added Pi-primary systemd user timer templates for the monitor: `automation/systemd/personal-office-pi-job-search-gmail-monitor.service` and `automation/systemd/personal-office-pi-job-search-gmail-monitor.timer`.
- Update 2026-07-01: Installed and enabled the Pi user timer under `openclaw`. `personal-office-pi-job-search-gmail-monitor.timer` is active/waiting and triggers `personal-office-pi-job-search-gmail-monitor.service`; first observed next trigger was `2026-07-01 20:20:40 +07`.
- Update 2026-07-01: Telegram ad-hoc vacancy intake boundary scaffolded with `automation/prompts/pi-job-search-telegram-intake.md`, `automation/scripts/run-pi-job-search-telegram-intake.sh`, and runtime CLI commands `telegram-update-status` / `mark-telegram-update`. Pi currently has no configured OpenClaw chat channels, so the Telegram wrapper is expected to write a blocked run log until Telegram is configured outside Git.
- Update 2026-07-01: Telegram wrapper blocked preflight verified on Pi. With no `TELEGRAM_JOB_SEARCH_TARGET`, it wrote `automation/runs/2026-07-01-1835-pi-job-search-telegram-intake.md` and exited before attempting Telegram reads.

## Gmail/GCalendar Integration Options

### Option A - Workstation/Codex connector plus Pi handoff

Use the existing Codex Gmail and Google Calendar connectors from the workstation-side scheduled monitors. The monitor writes repo artifacts/run logs as today and, when Pi enrichment/routing is useful, sends a narrow handoff to `job-search`.

Status: demo/home fallback, not production target.

Pros:

- uses already-working Gmail/GCalendar auth;
- avoids copying Google OAuth tokens to Pi;
- matches existing monitor prompts and state files;
- keeps Gmail mutation policy under the current unattended-run guardrails.

Cons:

- Pi is not fully standalone for email/calendar intake;
- depends on a laptop/workstation being online;
- weak fit for always-on Personal Office operation;
- requires a handoff mechanism from workstation to Pi.

### Option B - Pi-local external Gmail/GCalendar MCP

Install or build explicit Gmail and Google Calendar MCP servers on Pi and register them with `openclaw mcp add` / `openclaw mcp login`.

Status: preferred production-like direction if security and token handling are acceptable.

Pros:

- makes `job-search` more standalone;
- gives the Pi agent direct tool access.
- fits the always-on reason for using Raspberry Pi.

Cons:

- requires Google OAuth app/scopes/token storage on Pi;
- higher security and maintenance surface;
- must implement strict read/write separation and unattended mutation policy.

#### 2026-06-30 MCP Server Shortlist

Candidate 1: `taylorwilsdon/google_workspace_mcp`

- URL: `https://github.com/taylorwilsdon/google_workspace_mcp`
- Package: `workspace-mcp` on PyPI.
- Language/runtime: Python 3.10+; `uvx workspace-mcp` is the documented path.
- Coverage: broad Google Workspace coverage including Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Chat, Apps Script, Tasks, Contacts, and Search.
- Auth/storage: Google OAuth client, OAuth 2.1 / PKCE mode, optional service-account / domain-wide delegation mode, local credential store or GCS credential store.
- Useful controls: `WORKSPACE_MCP_TOOLS`, `WORKSPACE_MCP_TOOL_TIER`, `WORKSPACE_MCP_READ_ONLY`, and `WORKSPACE_MCP_PERMISSIONS`.
- Fit: strongest functional candidate for a real Google Workspace contour.
- Spike result 2026-06-30: installed successfully on Pi without `uv`, using a dedicated Python venv and `pip install --resume-retries 10 workspace-mcp`; first install attempt failed only because of an incomplete slow download.
- OpenClaw registration: saved as enabled server `google_workspace` with `--single-user --tools gmail calendar --read-only`.
- Runtime smoke: starts cleanly in stdio and read-only mode with the intended credential directory.
- OAuth/read-only smoke: passed on 2026-07-01 for `v.rezin@gmail.com`.
- Risk: heavy Python dependency footprint and slow Pi downloads; future broadening beyond read-only Gmail/Calendar must be reviewed before enabling write scopes.

Candidate 2: `aliwatters/gsuite-mcp`

- URL: `https://github.com/aliwatters/gsuite-mcp`
- Language/runtime: Go single binary.
- Pi fit: release assets include `linux_arm64` tarballs.
- Coverage: broad Google Workspace coverage, including Gmail, Calendar, Drive, Docs, Tasks, Sheets, Slides, Forms, Contacts, Meet, Drive Activity, and Chat.
- Auth/storage: OAuth credentials under `~/.config/gsuite-mcp/`; supports multi-account and an external token command hook.
- Fit: strongest Pi-operational candidate because it can run as a single binary without Python/Node dependency churn.
- Risk: much smaller adoption signal than `workspace-mcp`; must inspect tool schemas and read-only controls before trusting unattended runs.

Candidate 3: `2389-research/gsuite-mcp`

- URL: `https://github.com/2389-research/gsuite-mcp`
- Language/runtime: Go.
- Pi fit: release assets include `linux_arm64` tarballs.
- Coverage: narrower but relevant: Gmail, Calendar, Contacts, and Tasks.
- Auth/storage: Desktop OAuth credentials and local token storage.
- Fit: plausible smaller-surface candidate if the goal is only mail/calendar/tasks.
- Risk: fewer services and smaller ecosystem; still needs read-only and mutation-safety review.

Not preferred for this contour:

- archived single-purpose Gmail/Calendar servers such as `GongRzhe/Gmail-MCP-Server` and `GongRzhe/Calendar-Autoauth-MCP-Server`;
- npm packages with unclear token bootstrap or broad destructive tools as default, unless we wrap/filter them heavily.

### Option C - OpenClaw webhooks handoff bridge

Enable/configure the stock OpenClaw `webhooks` plugin and have workstation monitors push small classified intake payloads into a `job-search` TaskFlow.

Pros:

- clean inbound bridge concept;
- avoids giving Pi full Gmail access.

Cons:

- currently disabled and not allowlisted on Pi;
- requires plugin allowlist/config/secret setup;
- adds TaskFlow/webhook operational complexity before the first E2E test.

### Option D - IMAP/CalDAV minimal poller

Use read-only IMAP for Gmail and CalDAV/Google Calendar API polling with local scripts, then hand off normalized facts to `job-search`.

Status: possible middle path for production-like always-on intake when full MCP is too heavy.

Pros:

- simple protocol shape;
- can be tightly scoped.

Cons:

- Gmail IMAP/app-password/OAuth details can be fiddly;
- Calendar write operations still need API/OAuth;
- duplicates capabilities already present in Codex connectors.

## Next Actions

1. Done 2026-07-01: create full Personal Office working tree on Pi as the primary repo.
2. Done 2026-07-01: configure private Git remote and push from Pi.
3. Done 2026-07-01: verify Pi-side GitHub SSH key for push.
4. Done 2026-07-01 for first monitor slice: adapt/mirror HH and LinkedIn Gmail monitoring into a Pi-local OpenClaw prompt using `google_workspace` and SQLite dedupe.
5. In progress 2026-07-01: harden conservative polling/backoff and timeout/watchdog behavior while installing unattended systemd timer.
6. In progress 2026-07-01: implement Telegram inbound routing for ad-hoc vacancy intake; wrapper/prompt/SQLite boundary exists, channel configuration remains external.
7. In progress 2026-07-01: implement Telegram outbound decision packets with verdict, selected CV, cover letter draft, and next action; output contract exists in prompt, live send awaits channel configuration.
8. Run a non-archived Inbox E2E check when the next fresh HH or LinkedIn message arrives.
9. Keep Option A only as a proof-of-concept fallback; do not treat workstation/Codex handoff as solved production architecture.
