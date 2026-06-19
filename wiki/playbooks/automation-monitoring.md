# Automation Monitoring Playbook

## Structure

- `automation/prompts/` - prompts for `codex exec`;
- `automation/scripts/` - launch wrappers;
- `automation/systemd/` - user-level timer templates;
- `automation/cron/` - crontab snippets;
- `automation/state/` - idempotency and last-run markers;
- `automation/runs/` - run logs.

## Rules

- Scheduled automation must leave a run log.
- State markers update only after successful processing.
- If a connector is unavailable, write a blocked run log and do not fake results.
- Scheduled automation must not require Git commits. Do not let `git add`, `git commit`, `.git/index.lock`, or read-only Git metadata block a successful monitor run. Run logs and state markers are the automation durability contract; commits are manual/operator work.
- Do not install OS timers without explicit user approval.

## HH Gmail

HH Gmail monitor uses:

- `automation/prompts/hh-gmail-monitor.md`;
- `automation/scripts/run-hh-gmail-monitor.sh`;
- `automation/state/hh-gmail-monitor-state.md`;
- `automation/runs/`.
