# Scheduled Task: LinkedIn Gmail Monitor

You are running inside `<repo-root>` as the scheduled LinkedIn Gmail secretary.

Use the repo-local skill `automation-monitoring`. For vacancy-specific work, use `personal-brand-career`.

This is an unattended cron run. Do not request interactive approval. If a tool, shell command, Gmail operation, or repository write is unavailable without approval, record the limitation in the run log and continue with the safest read-only or repo-local fallback. Do not wait for human confirmation.

## Objective

Scan Gmail for `from:linkedin.com` messages since the last successful scan and update Personal Office artifacts using the same rules we already used manually for the fresh LinkedIn vacancy batch:

- MineHub Technologies `VP of Engineering`
- Pepperstone `Head of Product Engineering`
- Selby Jennings `Head of Engineering`
- RedHolt `Vice President, Technology & Analytics`

The monitor must also remain useful for future LinkedIn vacancy mail, connection requests, recruiter follow-ups, and job-status updates.

## Required Behavior

1. Read `automation/state/linkedin-gmail-monitor-state.md`.
2. Search Gmail for recent `from:linkedin.com` messages newer than the state marker. Use a small overlap window if available to avoid missing delayed messages.
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
   - create or update an active/high-priority task when it matters;
   - update the analysis and index if the invitation maps to an existing vacancy;
   - if the vacancy cannot be matched, create `inbox/processed/needs-clarification-YYYY-MM-DD-linkedin.md`.
6. For `new_vacancy`:
   - if the message contains enough JD text, archive and analyze it using `personal-brand-career`;
   - include relocation, family lifestyle, market salary, and target income analysis;
   - update `job-intake/INDEX.md` and `job-intake/COMPANY_NOTES.md`;
   - rank it as interesting / maybe / not interesting, with a short reason;
   - if only a thin digest/link exists, create a raw intake or clarification note instead of inventing a JD;
   - if the email includes a LinkedIn job id or job URL, use the local LinkedIn MCP runtime via `LINKEDIN_MCP_PORT=8019 tools/linkedin-mcp/scripts/with-server.sh -- tools/linkedin-mcp/.venv/bin/python automation/scripts/linkedin-mcp-client.py job-details <JOB_ID>` to enrich the analysis before writing it.
7. Save a run log to `automation/runs/YYYY-MM-DD-HHMM-linkedin-gmail-monitor.md`.
8. Update `automation/state/linkedin-gmail-monitor-state.md` only after the run succeeds.
9. Commit resulting repository changes with a concise message.

If the commit fails in cron, leave the repository changes in place, record the failure in the run log, and do not update the successful scan marker.

## Gmail Cleanup Policy

Do not mutate Gmail labels, stars, importance, or archive state during unattended runs. Record any recommended Gmail action in the run log instead.

## If Gmail Is Unavailable

Do not fake the scan.

Create a blocked run log in `automation/runs/`, state that Gmail access was unavailable, leave `automation/state/linkedin-gmail-monitor-state.md` unchanged, and do not update vacancy/task artifacts.
