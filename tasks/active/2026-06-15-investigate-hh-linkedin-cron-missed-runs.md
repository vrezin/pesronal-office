# Investigate HH / LinkedIn cron missed runs

- Created: 2026-06-15
- Status: active
- Priority: high
- Area: automation / personal-brand / Gmail monitors

## Current State

Manual checks on 2026-06-15 showed:

- `crontab -l` contains both Personal Office monitors:
  - HH Gmail monitor: `0 */4 * * *`
  - LinkedIn Gmail monitor: `0 */4 * * *`
- `cron.service` is active and running.
- Cron journal confirms both monitors ran at `2026-06-15 00:00:01 +07`.
- Expected 04:00 and 08:00 runs did not appear in `automation/runs/` or in the cron journal.
- Manual 09:07 runs succeeded for both monitors, Gmail access worked, and no new post-marker HH/LinkedIn messages required routing.

## Evidence

- HH manual run log: `automation/runs/2026-06-15-0907-hh-gmail-monitor.md`
- LinkedIn manual run log: `automation/runs/2026-06-15-0907-linkedin-gmail-monitor.md`
- HH state: `automation/state/hh-gmail-monitor-state.md`
- LinkedIn state: `automation/state/linkedin-gmail-monitor-state.md`

## Next Step

Find why cron did not fire the 04:00 and 08:00 user jobs despite the crontab being installed and `cron.service` running. Check host sleep/suspend, cron logs around 04:00/08:00, environment assumptions, and whether a more reliable systemd timer should replace or supplement cron.

