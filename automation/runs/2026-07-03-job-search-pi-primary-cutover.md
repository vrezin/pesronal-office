# Job Search Pi Primary Cutover

- Date: 2026-07-03
- Status: applied
- Decision: Raspberry Pi is the primary runtime contour for job-search automation.

## Verified Pi Contour

- `personal-office-pi-job-search-gmail-monitor.timer` is active.
- `personal-office-pi-job-search-sync.timer` is active.
- `personal-office-pi-archivist.timer` is active.
- `linkedin-mcp.service` is running on Pi.
- `personal-office-hh-direct-route.timer` is active as a system timer.

## Local Contour

The local workstation cron entries for:

- `automation/scripts/run-hh-gmail-monitor.sh`
- `automation/scripts/run-linkedin-gmail-monitor.sh`

are disabled as scheduled jobs. The scripts remain in the repository as manual
fallback wrappers only.

## Follow-Up

- Fix Pi artifact sync allowlist so the sync wrapper can commit its own
  `automation/runs/*-pi-job-search-sync.md` run logs.
- Keep HH API out of the active contour; HH Web is the working HH path.
