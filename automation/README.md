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

When `/home/openclaw/.config/personal-office/job-search-telegram.env` exists, the Gmail monitor also passes Telegram target/account to the `job-search` agent so actionable Gmail findings can produce Telegram decision packets.

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

Use a separate Telegram account such as `personal-office-intake-telegram` for
the general intake secretary until the router is proven. Do not rebind the
working `job-search-telegram` account away from `job-search`.

The active path is OpenClaw Gateway routing, not scheduled `openclaw message read`.
Telegram account `job-search-telegram` should be bound to the `job-search` agent:

```bash
openclaw agents bind --agent job-search --bind telegram:job-search-telegram
```

OpenClaw 2026.6.10 does not support Telegram via `openclaw message read`; use the wrapper only as a blocked/preflight diagnostic until it is rewritten for gateway event logs.

Disabled-until-configured systemd templates:

- `automation/systemd/personal-office-pi-job-search-telegram-intake.service`;
- `automation/systemd/personal-office-pi-job-search-telegram-intake.timer`.

## Planned Monitors

- `yc-workatastartup-monitor` - planned for the week of 2026-06-22 as a basic Playwright/MCP-assisted monitor for new Work at a Startup roles. Until it exists, use the daily manual reminder in `tasks/active/2026-06-19-daily-check-yc-work-at-a-startup.md`.
