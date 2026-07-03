# Personal Office Archivist

The archivist is the maintenance contour for keeping Personal Office usable on
small always-on hardware such as the Raspberry Pi.

## Contract

- Dry-run by default.
- Delete only generated technical residue automatically.
- Treat semantic Markdown as state: fold it into rollups or mark it stale before
  removal.
- Never delete active, waiting, interview, finance, medical, legal, family, or
  company evidence just because it is old.
- Always write a run log under `automation/runs/`.
- Update `automation/state/pi-archivist-state.md` only after a successful run.

## First Cleanup Classes

- Generated files: `__pycache__/`, `.pyc`, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`.
- Runtime noise: local `.run/*.log` and cron wrapper logs after the configured
  retention window.
- Dependency/runtime directories: large `tools/*/.venv` and
  `tools/*/node_modules` folders are reported as review-only candidates. They
  are not deleted automatically because they may be needed for quick tool
  recovery or contain local runtime/session state.
- Automation run logs: report old high-volume monitor logs as rollup candidates.
- Job-intake: report closed, parked, rejected, expired, duplicate, or no-action
  full JD/analysis files as compaction candidates once canonical indexes already
  preserve the useful state.

## Review Artifacts

The scanner writes review-only artifacts by default:

- `automation/rollups/YYYY-Www-monitor-run-rollup.md` for old high-volume
  monitor logs.
- `personal-projects/personal-brand/workspace/job-intake/summaries/YYYY-MM-DD-archivist-job-intake-compaction-ledger.md`
  for stale job-intake compaction candidates.

Set `PERSONAL_OFFICE_ARCHIVIST_WRITE_REVIEW_ARTIFACTS=0` to suppress these
artifacts during experiments.

## Usage

Preview:

```bash
python3 tools/personal-office-archivist/archivist.py --mode dry-run
```

Apply generated-file cleanup:

```bash
python3 tools/personal-office-archivist/archivist.py --mode apply
```

The `apply` mode still does not delete semantic Markdown job-intake or inbox
notes. Those are listed for rollup/compaction so a later agent pass can preserve
the useful facts first.

Prune old monitor logs only after a rollup exists:

```bash
PERSONAL_OFFICE_ARCHIVIST_PRUNE_REVIEWED_MONITOR_LOGS=1 \
python3 tools/personal-office-archivist/archivist.py --mode apply
```

This deletes only old high-volume HH/LinkedIn monitor run logs that are already
listed in an `automation/rollups/*monitor-run-rollup.md` artifact.

Prune reviewed job-intake artifacts only after a replacement summary exists:

```bash
PERSONAL_OFFICE_ARCHIVIST_PRUNE_REVIEWED_JOB_INTAKE_ARTIFACTS=1 \
python3 tools/personal-office-archivist/archivist.py --mode apply
```

This deletes only stale JD/analysis files that are listed in an archivist
compaction ledger, referenced by a non-archivist summary rollup, and no longer
referenced directly from `INDEX.md`, `COMPANY_NOTES.md`, `tasks/`, or `inbox/`.
