# Pi Job Search Runtime Storage Foundation

- Run time: 2026-07-01 14:56 +07
- Target host: `raspberrypi-codex`
- Target path: `/home/openclaw/personal-office-agent/job-search-contour/`
- Mode: storage/sync foundation setup

## Objective

Create the first operational storage layer for the standalone Pi job-search business contour:

- SQLite schema and CLI for runtime state;
- baseline duplicate-state seed from Markdown monitor state;
- sync wrapper skeleton for future private Git remote pull/run/commit/push flow.

## Implemented Locally

Created:

- `tools/job-search-runtime/README.md`;
- `tools/job-search-runtime/schema.sql`;
- `tools/job-search-runtime/job_search_runtime.py`;
- `automation/scripts/run-pi-job-search-sync.sh`.

Updated:

- `.gitignore` to exclude `automation/state/job-search-runtime.sqlite`, `-wal`, and `-shm`;
- `tools/raspberrypi-openclaw/personal-office-shared-storage-decision-2026-07-01.md`;
- `tools/raspberrypi-openclaw/job-search-business-contour-target-2026-07-01.md`.

## Pi Result

Copied the runtime tooling and current monitor state files to Pi.

Initialized:

```text
automation/state/job-search-runtime.sqlite
```

Seeded duplicate baseline from Markdown monitor state:

```text
Processed messages:
- hh seeded_from_markdown_state: 5
- linkedin seeded_from_markdown_state: 2
Run locks: 0
```

Dry-run wrapper check on Pi passed:

```text
PERSONAL_OFFICE_SYNC_MODE=dry-run automation/scripts/run-pi-job-search-sync.sh
```

The wrapper correctly initialized/seeded SQLite and skipped Git sync because `job-search-contour` is not yet a Git worktree.

## Boundary

The private Git remote is not configured yet.

The SQLite database is operational runtime state and is ignored by Git. Canonical outcomes must still be written to Markdown artifacts.

## Next Steps

1. Configure the private Git remote / mirrored checkout for Pi.
2. Decide Pi git identity and deploy key.
3. Run `run-pi-job-search-sync.sh` in `apply` mode only after a clean Git worktree exists on Pi.
4. Extend monitor wrappers to write new processed Gmail ids into SQLite during scheduled runs.
