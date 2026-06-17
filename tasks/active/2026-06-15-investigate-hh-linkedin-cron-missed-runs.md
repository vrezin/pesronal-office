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
- On 2026-06-15 the desired schedule was changed from every 4 hours to three local-time windows: 08:00, 14:00, 22:00.
- `cron.service` is active and running.
- Cron journal confirms both monitors ran at `2026-06-15 00:00:01 +07`.
- Expected 04:00 and 08:00 runs did not appear in `automation/runs/` or in the cron journal.
- Manual 09:07 runs succeeded for both monitors, Gmail access worked, and no new post-marker HH/LinkedIn messages required routing.
- The 14:00 scheduled window did fire:
  - HH run: `automation/runs/2026-06-15-1401-hh-gmail-monitor.md`
  - LinkedIn run: `automation/runs/2026-06-15-1402-linkedin-gmail-monitor.md`
- The remaining issue is not scheduling itself, but unattended commit/state advancement: both 14:00 runs completed Gmail scanning, then failed the required git commit because `.git/index.lock` could not be created in a read-only file-system context.

## Evidence

- HH manual run log: `automation/runs/2026-06-15-0907-hh-gmail-monitor.md`
- LinkedIn manual run log: `automation/runs/2026-06-15-0907-linkedin-gmail-monitor.md`
- HH state: `automation/state/hh-gmail-monitor-state.md`
- LinkedIn state: `automation/state/linkedin-gmail-monitor-state.md`

## Next Step

Fix or redesign unattended commit/state advancement for cron runs. Options to evaluate:

- ensure cron runs with write access to `.git`;
- skip git commit inside cron and write a safe pending-run marker for manual commit;
- move monitor scheduling to a systemd timer or wrapper with the expected environment.
