# HH Gmail Monitor Automation

Date: 2026-06-09

## Input

Set up a scheduled process that scans Gmail every 4 hours for HH.ru mail and:

- updates related task statuses when HH notifications arrive;
- updates related tasks and promotes importance when invitations arrive;
- analyzes and ranks new vacancies.

## Decision

Create a repo-local automation workflow driven by `codex exec`, with:

- `hh-gmail-monitor` skill;
- reusable scheduled prompt;
- launch script;
- systemd and cron templates;
- state file for idempotency;
- per-run logs.

## OS Install Status

Installed on 2026-06-09 as a user crontab entry.

Current schedule:

```cron
0 */4 * * * cd /home/adre/personal-office && /home/adre/personal-office/automation/scripts/run-hh-gmail-monitor.sh >> /home/adre/personal-office/automation/runs/hh-gmail-monitor.cron.log 2>&1
```

The crontab also sets an explicit `PATH` including the Node/Codex binary directory so the scheduled wrapper can find `codex`.
