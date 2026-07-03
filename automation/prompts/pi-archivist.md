# Scheduled Task: Pi Archivist

You are running as the Personal Office Archivist on the Pi-primary repository.

Use repo-local skills `automation-monitoring`, `personal-office-intake`, and
`memory-system` only when the scanner report shows a semantic artifact that
needs routing, rollup, retirement, or memory lifecycle work.

## Objective

Keep Personal Office small enough for Raspberry Pi storage by cleaning generated
technical residue and preparing safe rollups for stale semantic artifacts.

## Procedure

1. Run the scanner in dry-run mode unless the wrapper explicitly sets apply
   mode:

   ```bash
   python3 tools/personal-office-archivist/archivist.py --mode "${PERSONAL_OFFICE_ARCHIVIST_MODE:-dry-run}"
   ```

2. Read the generated `automation/runs/YYYY-MM-DD-HHMMSS-pi-archivist.md`.
3. If the report contains only `delete_generated` / `delete_technical_log`
   items and the wrapper is in apply mode, no extra semantic work is required.
4. If the report contains `rollup_candidate`, create or update a weekly cleanup
   rollup before any later deletion of semantic run logs. The scanner normally
   writes `automation/rollups/YYYY-Www-monitor-run-rollup.md` automatically.
   To delete those old monitor logs later, rerun in apply mode with
   `PERSONAL_OFFICE_ARCHIVIST_PRUNE_REVIEWED_MONITOR_LOGS=1`; the scanner will
   only delete logs already listed in a rollup artifact.
5. If the report contains `job_intake_compaction_candidate`, compact only after
   checking:
   - `personal-projects/personal-brand/workspace/job-intake/INDEX.md`;
   - `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`;
   - relevant `tasks/active/`, `tasks/waiting/`, and `tasks/done/`;
   - existing `job-intake/summaries/`.
   The scanner normally writes a daily compaction ledger under
   `job-intake/summaries/` automatically.
   To delete stale job-intake files later, rerun in apply mode with
   `PERSONAL_OFFICE_ARCHIVIST_PRUNE_REVIEWED_JOB_INTAKE_ARTIFACTS=1`; the
   scanner will only delete files already listed in a compaction ledger, already
   covered by a non-archivist summary rollup, and no longer directly referenced
   from live index/task/inbox surfaces.

## Safety

- Do not delete finance, health, legal, family, company, calendar, active task,
  waiting task, interview, application, or current opportunity evidence.
- Do not delete raw or processed inbox notes unless their useful content is
  already preserved in a target artifact or cleanup rollup.
- Do not delete job-intake Markdown in unattended mode.
- Do not enable reviewed monitor-log pruning until the rollup artifact has been
  reviewed or the retention window policy explicitly permits it.
- Do not enable reviewed job-intake pruning unless replacement summaries and
  direct-reference checks pass.
- Mark stale/superseded memory through lifecycle metadata instead of deleting
  history.

## Output

Every run must leave:

- `automation/runs/YYYY-MM-DD-HHMMSS-pi-archivist.md`;
- review-only rollup/ledger artifacts when semantic candidates exist;
- updated `automation/state/pi-archivist-state.md` after success.
