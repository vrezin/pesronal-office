# Job Search Runtime

Local operational state tooling for the Raspberry Pi job-search business contour.

This is not the Personal Office source of truth. Canonical outcomes still belong in Markdown artifacts such as `automation/runs/`, `automation/state/`, `tasks/`, `inbox/processed/`, and `personal-projects/personal-brand/workspace/job-intake/`.

## Files

- `schema.sql` - SQLite schema for runtime dedupe, locks, cursors, runs, Telegram updates, and artifact mappings.
- `job_search_runtime.py` - standard-library CLI for initializing and inspecting the SQLite database.
- `shared-requirements.txt` - shared Python runtime requirements for job-search MCP/tools that are not owned by a local project.
- `setup-shared-env.sh` - rebuilds the shared job-search Python runtime.
- `setup-hh-direct-route.sh` - refreshes direct HH routes through the normal
  LAN gateway so HH Web does not use the `personal-office` VPN policy route.
- `run-headhunter-web-mcp.sh` - launches the active HH Web MCP through the shared runtime.

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

Generate and import the job-intake history backfill manifest:

```bash
python3 tools/job-search-runtime/job_search_runtime.py generate-vacancy-backfill-manifest --output automation/state/job-search-backfill-manifest.json
python3 tools/job-search-runtime/job_search_runtime.py import-vacancy-backfill --manifest automation/state/job-search-backfill-manifest.json --mode dry-run
python3 tools/job-search-runtime/job_search_runtime.py import-vacancy-backfill --manifest automation/state/job-search-backfill-manifest.json --mode apply
```

The importer writes `vacancies` and `artifact_links` only. It does not write
`processed_messages` because historical rows do not prove a real Gmail message
id. Existing non-backfill Pi rows win unless the incoming manifest row is an
explicit `active` or `waiting` task state.

Acquire and release a run lock:

```bash
python3 tools/job-search-runtime/job_search_runtime.py acquire-lock --lock-name pi-job-search-gmail-monitor --owner manual-test --ttl-seconds 300
python3 tools/job-search-runtime/job_search_runtime.py lock-status --lock-name pi-job-search-gmail-monitor
python3 tools/job-search-runtime/job_search_runtime.py release-lock --lock-name pi-job-search-gmail-monitor --owner manual-test
```

Check and mark Gmail messages:

```bash
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id <GMAIL_ID>
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source hh --gmail-message-id <GMAIL_ID> --classification noise --status noise
```

Check and mark Telegram updates:

```bash
python3 tools/job-search-runtime/job_search_runtime.py telegram-update-status --update-id <UPDATE_ID>
python3 tools/job-search-runtime/job_search_runtime.py mark-telegram-update --update-id <UPDATE_ID> --received-at <ISO_TIME> --status processed --summary "short summary"
```

Use a custom database path:

```bash
python3 tools/job-search-runtime/job_search_runtime.py --db /path/to/job-search-runtime.sqlite status
```

## Shared Python Runtime

Target shape for Pi and canonical Personal Office:

- apt owns only the system base: `python3`, `python3-venv`, `git`, `curl`, Chromium/browser libraries, and native build libraries when needed.
- Python application dependencies use one shared job-search runtime at:

```text
<repo-root>/.runtime/job-search-venv
```

- uv, when available, uses the shared cache:

```text
<repo-root>/.cache/uv
```

- Per-tool `.venv` directories under `tools/headhunter-web-mcp/` and
  `tools/linkedin-mcp/` are migration/fallback state, not the target steady
  state.
- `tools/headhunter-mcp-server/` is a disabled historical HH API experiment.
  There is no usable API key/OAuth contour for the applicant workflow, so the
  shared runtime must not install or launch it. HH Web is the only active HH MCP
  contour.
- `tools/zenmoney-mcp/.venv` is outside this policy because finance tooling is a
  separate sensitive contour.

Build or refresh the shared runtime:

```bash
tools/job-search-runtime/setup-shared-env.sh
```

If Pi downloads from `files.pythonhosted.org` are slow, download large ARM
wheels on the workstation and copy them into:

```text
<repo-root>/.cache/wheelhouse
```

Then rerun setup with normal pip behavior; direct file installs can also be used
for especially large wheels before rerunning the setup script.

The setup script uses `uv` when available and falls back to standard
`python3 -m venv` plus pip when the Pi only has distro-managed Python.

## HH Direct Route

HH Web should bypass the `personal-office` VPN policy route. Russian HH pages
can become slow or challenge-heavy when opened through the VPN path.

On the Pi, install the system-level route refresher:

```bash
sudo cp automation/systemd/personal-office-hh-direct-route.service /etc/systemd/system/
sudo cp automation/systemd/personal-office-hh-direct-route.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now personal-office-hh-direct-route.timer
sudo systemctl start personal-office-hh-direct-route.service
```

The service resolves `hh.ru`, `www.hh.ru`, `auth.hh.ru`, and `api.hh.ru`, then
adds `/32` routes for the current IPv4 addresses into table `51820` via the main
LAN default gateway.

The setup script installs:

- shared standalone job-search packages from `shared-requirements.txt`;
- editable/project dependencies from `tools/headhunter-web-mcp/`.

LinkedIn currently starts through `tools/linkedin-mcp/scripts/start-local.sh`.
That launcher now prefers `<repo-root>/.runtime/job-search-venv/bin/linkedin-mcp-server`
and falls back to `tools/linkedin-mcp/.venv/bin/linkedin-mcp-server` while the
Pi migration is in progress.

After the shared runtime is verified on the Pi, the archivist may treat old
job-search per-tool `.venv` directories as removable rebuildable runtime state.

## Rule

SQLite may drive idempotency, locks, cursors, retries, and duplicate checks. It must not become the only record of decisions, next actions, CV choices, cover letters, or user-visible outcomes.
