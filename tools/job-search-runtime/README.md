# Job Search Runtime

Local operational state tooling for the Raspberry Pi job-search business contour.

This is not the Personal Office source of truth. Canonical outcomes still belong in Markdown artifacts such as `automation/runs/`, `automation/state/`, `tasks/`, `inbox/processed/`, and `personal-projects/personal-brand/workspace/job-intake/`.

## Files

- `schema.sql` - SQLite schema for runtime dedupe, locks, cursors, runs, Telegram updates, and artifact mappings.
- `job_search_runtime.py` - standard-library CLI for initializing and inspecting the SQLite database.

## Default Database

```text
automation/state/job-search-runtime.sqlite
```

## Commands

Initialize or migrate the database:

```bash
python3 tools/job-search-runtime/job_search_runtime.py init
```

Seed processed Gmail message ids from existing Markdown monitor state:

```bash
python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state
```

Show a compact status:

```bash
python3 tools/job-search-runtime/job_search_runtime.py status
```

Use a custom database path:

```bash
python3 tools/job-search-runtime/job_search_runtime.py --db /path/to/job-search-runtime.sqlite status
```

## Rule

SQLite may drive idempotency, locks, cursors, retries, and duplicate checks. It must not become the only record of decisions, next actions, CV choices, cover letters, or user-visible outcomes.
