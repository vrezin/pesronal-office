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
