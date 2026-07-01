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

Telegram ad-hoc job-search intake is scaffolded by:

- `automation/prompts/pi-job-search-telegram-intake.md`;
- `automation/scripts/run-pi-job-search-telegram-intake.sh`.
- `automation/scripts/setup-pi-job-search-telegram-channel.sh`.

It remains blocked until an OpenClaw Telegram channel is configured outside Git and `TELEGRAM_JOB_SEARCH_TARGET` is set for the wrapper.

Disabled-until-configured systemd templates:

- `automation/systemd/personal-office-pi-job-search-telegram-intake.service`;
- `automation/systemd/personal-office-pi-job-search-telegram-intake.timer`.

## Planned Monitors

- `yc-workatastartup-monitor` - planned for the week of 2026-06-22 as a basic Playwright/MCP-assisted monitor for new Work at a Startup roles. Until it exists, use the daily manual reminder in `tasks/active/2026-06-19-daily-check-yc-work-at-a-startup.md`.
