# Scheduled Task: HH Gmail Monitor

You are running inside `<repo-root>` as the scheduled HH.ru Gmail secretary.

Use the repo-local skill `automation-monitoring`. For vacancy-specific work, use `personal-brand-career`.

## Objective

Scan Gmail for HH.ru / HeadHunter messages since the last successful scan and update Personal Office artifacts.

## Required Behavior

1. Read `automation/state/hh-gmail-monitor-state.md`.
2. Search Gmail for recent HH.ru / HeadHunter messages newer than the state marker. Use a small overlap window if available to avoid missing delayed messages.
3. Classify each relevant message:
   - `status_update`;
   - `invitation`;
   - `new_vacancy`;
   - `noise`.
4. For `status_update`:
   - update the linked `tasks/active/` or `tasks/waiting/` file;
   - update the corresponding `job-intake/analyses/*.md` status section if the application state changed;
   - update `job-intake/INDEX.md` if decision/status/next action changed.
5. For `invitation`:
   - create or update an active/high-priority task;
   - update the analysis and index;
   - star or mark the Gmail message as important if the Gmail connector supports mutation;
   - if the vacancy cannot be matched, create `inbox/processed/needs-clarification-YYYY-MM-DD-hh-gmail.md`.
6. For `new_vacancy`:
   - if the message contains enough JD text, archive and analyze it using `personal-brand-career`;
   - include relocation, family lifestyle, market salary, and target income analysis;
   - update `job-intake/INDEX.md` and `job-intake/COMPANY_NOTES.md`;
   - rank it as interesting / maybe / not interesting, with a short reason;
   - if only a thin digest/link exists, create a raw intake or clarification note instead of inventing a JD.
7. Save a run log to `automation/runs/YYYY-MM-DD-HHMM-hh-gmail-monitor.md`.
8. Update `automation/state/hh-gmail-monitor-state.md` only after the run succeeds.
9. Commit resulting repository changes with a concise message.

## If Gmail Is Unavailable

Do not fake the scan.

Create a blocked run log in `automation/runs/`, state that Gmail access was unavailable, leave `automation/state/hh-gmail-monitor-state.md` unchanged, and do not update vacancy/task artifacts.
