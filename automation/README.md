# Automation

Scheduled Personal Office jobs live here.

## Folders

- `prompts/` - prompts passed to `codex exec`.
- `scripts/` - local launch wrappers.
- `systemd/` - user-level systemd unit/timer templates.
- `cron/` - crontab snippets.
- `state/` - last-run markers and idempotency state.
- `runs/` - per-run logs written by scheduled agents.
- `rollups/` - review-only cleanup rollups that allow old high-volume run logs
  or receipt notes to be compacted later.

## Rule

Automation must leave a trace in `runs/` and update `state/` only after successful processing.

Scheduled automation must not require Git commits. Run logs and state markers are enough for unattended durability; committing is a manual/operator action.

## Active Monitors

- `hh-gmail-monitor` - legacy local wrapper; disabled from local cron on 2026-07-03 after Pi-primary cutover. Keep only as a manual fallback.
- `linkedin-gmail-monitor` - legacy local wrapper; disabled from local cron on 2026-07-03 after Pi-primary cutover. Keep only as a manual fallback.
- `linkedin-mcp` - Pi user service on `127.0.0.1:8019`; the service template is `automation/systemd/personal-office-linkedin-mcp.service` and it runs the shared job-search runtime from `<repo-root>/.runtime/job-search-venv`.
- `pi-job-search-gmail-monitor` - Pi-primary OpenClaw job-search monitor. It uses Pi-local `google_workspace` Gmail access, `tools/job-search-runtime/` SQLite dedupe, and writes run logs/state without requiring Git commits.
- `pi-archivist` - Pi-primary maintenance scanner and safe generated-file cleaner. It runs dry-run by default, writes cleanup candidates to `automation/runs/`, updates `automation/state/pi-archivist-state.md`, and leaves semantic Markdown as review-only until rollups/compaction preserve the useful facts.

Job-search Python dependencies should converge on the shared runtime managed by:

- `tools/job-search-runtime/setup-shared-env.sh`;
- `<repo-root>/.runtime/job-search-venv`;
- `<repo-root>/.cache/uv`.

Use apt for system packages only. Do not create new per-tool `.venv` directories
for job-search tools unless a version conflict is documented in that tool's
README and in the rollout task.

HH API is not an active contour. `tools/headhunter-mcp-server/` is retained only
as historical reference because there is no usable API key/OAuth path for the
applicant workflow. HH Web is the only active HH MCP contour.

User-facing Telegram output belongs to the Pi `intake` secretary. Job-search
monitors should write artifacts and structured handoffs, not stream logs or
direct tool output to Telegram.

Pi-primary scheduling is defined by:

- `automation/systemd/personal-office-pi-job-search-gmail-monitor.service`;
- `automation/systemd/personal-office-pi-job-search-gmail-monitor.timer`.

Pi-primary LinkedIn MCP service is defined by:

- `automation/systemd/personal-office-linkedin-mcp.service`.

Pi-primary HH direct route refresh is defined by system-level templates:

- `automation/systemd/personal-office-hh-direct-route.service`;
- `automation/systemd/personal-office-hh-direct-route.timer`.

Pi-primary archivist scheduling is defined by:

- `automation/systemd/personal-office-pi-archivist.service`;
- `automation/systemd/personal-office-pi-archivist.timer`.

Pi-primary artifact sync is defined by:

- `automation/scripts/run-pi-job-search-sync.sh`;
- `automation/systemd/personal-office-pi-job-search-sync.service`;
- `automation/systemd/personal-office-pi-job-search-sync.timer`.

The sync timer is separate from monitor execution. It may commit/push allowed runtime artifacts after monitors finish, but monitors themselves must remain useful without Git.

Local workstation cron is not an active job-search contour after the Pi-primary
cutover. Do not schedule `run-hh-gmail-monitor.sh` or
`run-linkedin-gmail-monitor.sh` locally unless the Pi contour is explicitly
down and the local run is marked as a temporary fallback.

Telegram ad-hoc job-search intake is scaffolded by:

- `automation/prompts/pi-job-search-telegram-intake.md`;
- `automation/scripts/run-pi-job-search-telegram-intake.sh`.
- `automation/scripts/setup-pi-job-search-telegram-channel.sh`.

General Pi intake secretary setup is scaffolded by:

- `automation/prompts/pi-intake-secretary.md`;
- `automation/scripts/setup-pi-intake-telegram-channel.sh`;
- `tools/raspberrypi-openclaw/pi-intake-secretary-2026-07-02.md`.

The intended Telegram front door is `personal-office-intake-telegram`, bound to
the `intake` agent. `job-search` should not have a direct Telegram binding; it
should receive handoffs from intake and write structured results back for
intake/output formatting.

The active path is OpenClaw Gateway routing, not scheduled `openclaw message read`.
Telegram account `personal-office-intake-telegram` should be bound to the
`intake` agent:

```bash
openclaw agents bind --agent intake --bind telegram:personal-office-intake-telegram
```

OpenClaw 2026.6.10 does not support Telegram via `openclaw message read`; use the wrapper only as a blocked/preflight diagnostic until it is rewritten for gateway event logs.

Disabled-until-configured systemd templates:

- `automation/systemd/personal-office-pi-job-search-telegram-intake.service`;
- `automation/systemd/personal-office-pi-job-search-telegram-intake.timer`.

## Planned Monitors

- `yc-workatastartup-monitor` - planned for the week of 2026-06-22 as a basic Playwright/MCP-assisted monitor for new Work at a Startup roles. Until it exists, use the daily manual reminder in `tasks/active/2026-06-19-daily-check-yc-work-at-a-startup.md`.
