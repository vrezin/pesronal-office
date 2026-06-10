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

## Active Monitors

- `hh-gmail-monitor`
- `linkedin-gmail-monitor`
