# Pi Job Search History Backfill

- Started at: 2026-07-03T18:03:00+07:00
- Finished at: 2026-07-03T18:12:00+07:00
- Status: completed
- Mode: registry plus active
- Manifest: `automation/state/job-search-backfill-manifest.json`
- Runtime database: `automation/state/job-search-runtime.sqlite`

## Source

- Source index: `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- Backfill origin: `local-personal-office-job-intake`
- Import source prefix: `backfill:local-personal-office-job-intake`

## Manifest Counts

- Entries: 231
- Index rows parsed: 231
- Explicit active task links: 22
- Explicit waiting task links: 9
- Missing artifacts during manifest generation: 0

## Pi Dry Run

Command:

```bash
python3 tools/job-search-runtime/job_search_runtime.py import-vacancy-backfill --manifest automation/state/job-search-backfill-manifest.json --mode dry-run
```

Result:

- Would insert: 231
- Would update: 0
- Would skip existing: 0
- Conflicts: 0

## Pi Apply

Command:

```bash
python3 tools/job-search-runtime/job_search_runtime.py import-vacancy-backfill --manifest automation/state/job-search-backfill-manifest.json --mode apply
```

Result:

- Inserted vacancies: 231
- Updated vacancies: 0
- Skipped existing: 0
- Artifact links written: 262
- Conflicts: 0
- `processed_messages` was not written by this backfill.

## Runtime Status After Apply

Vacancy rows:

- `active`: 22
- `waiting`: 55
- `historical_open`: 64
- `historical_closed`: 55
- `historical_no_action`: 30
- `historical_backfill`: 5

Artifact links for `backfill:local-personal-office-job-intake`:

- `analysis`: 139
- `summary`: 66
- `task`: 31
- `search_run`: 11
- `artifact`: 15

## Post-Apply Idempotency Check

Command:

```bash
python3 tools/job-search-runtime/job_search_runtime.py import-vacancy-backfill --manifest automation/state/job-search-backfill-manifest.json --mode dry-run
```

Result after tightening no-op detection:

- Would insert: 0
- Would update: 0
- Would no-op: 231
- Conflicts: 0

## Notes

- Existing Pi state is treated as authoritative. This run inserted only new
  `backfill:*` vacancy rows because no prior Pi vacancy rows existed.
- The importer intentionally does not write `processed_messages` because the
  historical job-intake index does not prove real Gmail message ids.
- Active task promotion is conservative: a task path is attached only when the
  task filename clearly matches the vacancy company and role. Broader review
  batch tasks remain registry/history context rather than live per-vacancy tasks.
