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

The actual OS timer is not installed yet because that writes outside the repository and should be confirmed separately.
