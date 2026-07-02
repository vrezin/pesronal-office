# Automation

Scheduled Personal Office jobs live here.

## Folders

- `prompts/` - prompts passed to `codex exec`.
- `scripts/` - local launch wrappers.
- `systemd/` - user-level systemd unit/timer templates.
- `cron/` - crontab snippets.
- `state/` - last-run markers and idempotency state.
- `runs/` - per-run logs written by scheduled agents.

## Rule

Automation must leave a trace in `runs/` and update `state/` only after successful processing.

Scheduled automation must not require Git commits. Run logs and state markers are enough for unattended durability; committing is a manual/operator action.

## Active Monitors

- `hh-gmail-monitor`
- `linkedin-gmail-monitor` - uses the registered local LinkedIn MCP server from `.codex/config.toml`, with a loopback wrapper fallback if needed.
- `pi-job-search-gmail-monitor` - Pi-primary OpenClaw job-search monitor. It uses Pi-local `google_workspace` Gmail access, `tools/job-search-runtime/` SQLite dedupe, and writes run logs/state without requiring Git commits.

User-facing Telegram output belongs to the Pi `intake` secretary. Job-search
monitors should write artifacts and structured handoffs, not stream logs or
direct tool output to Telegram.

Pi-primary scheduling is defined by:

- `automation/systemd/personal-office-pi-job-search-gmail-monitor.service`;
- `automation/systemd/personal-office-pi-job-search-gmail-monitor.timer`.

Pi-primary artifact sync is defined by:

- `automation/scripts/run-pi-job-search-sync.sh`;
- `automation/systemd/personal-office-pi-job-search-sync.service`;
- `automation/systemd/personal-office-pi-job-search-sync.timer`.

The sync timer is separate from monitor execution. It may commit/push allowed runtime artifacts after monitors finish, but monitors themselves must remain useful without Git.

Telegram ad-hoc job-search intake is scaffolded by:

- `automation/prompts/pi-job-search-telegram-intake.md`;
- `automation/scripts/run-pi-job-search-telegram-intake.sh`.
- `automation/scripts/setup-pi-job-search-telegram-channel.sh`.

General Pi intake secretary setup is scaffolded by:

- `automation/prompts/pi-intake-secretary.md`;
- `automation/scripts/setup-pi-intake-telegram-channel.sh`;
- `tools/raspberrypi-openclaw/pi-intake-secretary-2026-07-02.md`.

Pi intake-to-job-search dispatch is scaffolded by:

- `automation/prompts/pi-job-search-handoff-dispatch.md`;
- `automation/scripts/dispatch-pi-job-search-handoff.sh`.

The intended Telegram front door is `personal-office-intake-telegram`, bound to
the `intake` agent. `job-search` should not have a direct Telegram binding; it
should receive handoffs from intake and write structured results back for
intake/output formatting.

For ad-hoc Telegram vacancy/recruiter inputs, the intended internal flow is:

```text
Telegram -> intake -> job-search handoff artifact
         -> dispatch-pi-job-search-handoff.sh
         -> job-search structured handoff
         -> intake/output reply
```

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
