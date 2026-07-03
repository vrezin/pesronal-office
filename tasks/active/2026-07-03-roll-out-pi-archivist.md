# Roll Out Pi Archivist

Status: active

## Goal

Turn the Personal Office archivist contour into a regular Pi-primary maintenance
job that prevents logs, generated files, dependency caches, and stale job-intake
artifacts from silently consuming the 120GB flash/runtime storage.

## Current State

- Canonical scanner: `tools/personal-office-archivist/archivist.py`.
- Wrapper: `automation/scripts/run-pi-archivist.sh`.
- Prompt: `automation/prompts/pi-archivist.md`.
- State: `automation/state/pi-archivist-state.md`.
- Pi timer templates:
  - `automation/systemd/personal-office-pi-archivist.service`;
  - `automation/systemd/personal-office-pi-archivist.timer`.
- Latest Pi proof run: `automation/runs/2026-07-03-123315-pi-archivist.md`.
- Pi timer status: installed and enabled under the `openclaw` user on
  2026-07-03. `personal-office-pi-archivist.timer` is active/waiting.
- First observed next trigger: 2026-07-04 03:44:34 +07.
- Weekly monitor-log rollup artifact:
  `automation/rollups/2026-W27-monitor-run-rollup.md`.
- Job-intake compaction ledger:
  `personal-projects/personal-brand/workspace/job-intake/summaries/2026-07-03-archivist-job-intake-compaction-ledger.md`.
- The 2026-07-03 guarded monitor-log prune proof run:
  - applied 53.3 KB of safe cleanup on Pi;
  - deleted 25 old HH/LinkedIn monitor logs after verifying they were already
    listed in `automation/rollups/2026-W27-monitor-run-rollup.md`;
  - identified 88 stale full job-intake artifacts ready for compaction review;
  - left job-intake Markdown review-only.
- The 2026-07-03 guarded job-intake prune proof runs:
  - compacted Techvill / Vkusvill LLM Architect intake into
    `personal-projects/personal-brand/workspace/job-intake/summaries/2026-07-03-techvill-vkusvill-llm-architect-rollup.md`;
  - updated `INDEX.md` and `COMPANY_NOTES.md` to point to the compact summary;
  - deleted the full Techvill analysis and JD artifacts locally and on Pi only
    after the compaction ledger and safe-reference checks passed;
  - left the remaining Pi-side closed/parked and Noora candidates review-only.
- The accepted 2026-07-03 dependency-runtime policy:
  - apt is for system base packages only;
  - shared job-search Python dependencies live in
    `<repo-root>/.runtime/job-search-venv`;
  - uv cache lives in `<repo-root>/.cache/uv`;
  - setup command: `tools/job-search-runtime/setup-shared-env.sh`;
  - LinkedIn prefers the shared runtime and falls back to its local `.venv`
    during migration;
  - HH Web has a shared-runtime launch wrapper under `tools/job-search-runtime/`.
  - HH API was explicitly removed from the target runtime plan: there is no
    usable API key/OAuth contour for the applicant workflow, so
    `tools/headhunter-mcp-server/` is historical reference only.
- Local proof:
  - `tools/job-search-runtime/setup-shared-env.sh` built
    `<repo-root>/.runtime/job-search-venv`;
  - shared entrypoints exist for `linkedin-mcp-server` and
    `headhunter-web-mcp`;
  - stale local `tools/headhunter-mcp-server/.venv` and the old shared
    `headhunter-mcp` entrypoint were removed after confirming HH API is not a
    live contour;
  - checked imports: `linkedin_mcp_server`, `mcp`, `playwright`, `pydantic`,
    and `httpx`.
- Pi rollout state:
  - shared-runtime scripts and docs were copied to the Pi canonical checkout;
  - Pi has Python 3.13, `venv`, and `pip`, so no separate `uv` install is
    required;
  - Pi uses a WireGuard-style `personal-office` policy-routing interface:
    `ip rule` routes unmarked external traffic through table `51820`, and
    `ip route get` for PyPI/Fastly addresses resolves via `personal-office`
    with source `10.200.173.81`;
  - the first quick check only looked at the main routing table, which showed
    the physical `wlan0` route via `192.168.1.1`; that was incomplete for
    diagnosing external dependency downloads;
  - direct download from `files.pythonhosted.org` to Pi was extremely slow
    during diagnosis: 515 KB of a 5 MB range in 60 seconds;
  - the same ARM wheels downloaded locally at about 2.8-2.9 MB/s and were moved
    to Pi over LAN into `<repo-root>/.cache/wheelhouse`;
  - Pi wheelhouse now carries the two large ARM wheels:
    `patchright-1.61.1` and `playwright-1.61.0`;
  - `tools/job-search-runtime/setup-shared-env.sh` completed successfully on
    the Pi after using the local wheelhouse;
  - Pi shared runtime imports verified: `linkedin_mcp_server`, `mcp`,
    `playwright`, `pydantic`, and `httpx`;
  - Pi shared runtime entrypoints verified: `linkedin-mcp-server` and
    `headhunter-web-mcp`;
  - the Pi canonical checkout had no `tools/*/.venv` directories after setup.
- LinkedIn MCP shared-runtime cutover on 2026-07-03:
  - Pi user service `linkedin-mcp.service` now uses the canonical Personal
    Office checkout and `<repo-root>/.runtime/job-search-venv`;
  - canonical LinkedIn auth/browser state was copied into
    `<repo-root>/tools/linkedin-mcp/`;
  - `PLAYWRIGHT_BROWSERS_PATH` points at
    `<repo-root>/tools/linkedin-mcp/patchright-browsers`;
  - Patchright install validation passed after adding `ffmpeg-1011`;
  - port `127.0.0.1:8019` listens and MCP `list-tools` returns 17 tools;
  - the old `job-search-contour/tools/linkedin-mcp/.venv` and
    `job-search-contour/tools/linkedin-mcp/patchright-browsers` runtime
    directories were removed after the service was verified on the shared
    runtime, releasing about 1.2 GB;
  - first canonical profile transfer excluded browser cache/storage material and
    made `get_my_profile` report `Session expired`;
  - retesting the old full `job-search-contour` profile with the shared runtime
    proved the old auth state was still valid;
  - the canonical `<repo-root>/tools/linkedin-mcp/profile` was replaced with
    the full old profile, and non-mutating `get_my_profile` now passes on the
    main `127.0.0.1:8019` service;
  - legacy `job-search-contour` LinkedIn `profile/`, `cookies.json`, and
    `source-state.json` were intentionally preserved as auth rollback material.
- HH Web shared-runtime smoke on 2026-07-03:
  - `tools/job-search-runtime/run-headhunter-web-mcp.sh` starts through the
    shared runtime;
  - canonical HH Web storage state was copied into
    `<repo-root>/tools/headhunter-web-mcp/.local/state/hh-storage-state.json`
    with mode `600`;
  - shared `headhunter-web-mcp` entrypoint exists and the dead HH API
    `headhunter-mcp` entrypoint is absent;
  - `hh_web_healthcheck` reaches the browser/session layer but the current HH
    storage state opens an anonymous/login page, so HH auth is not green;
  - `tools/headhunter-web-mcp/scripts/auth.sh` now uses the shared runtime and
    Pi system Chromium defaults for the next interactive auth refresh;
  - the historical `adrelinux-codex` X11 screen route was unavailable from the
    current session (`No route to host`), so auth refresh could not be completed
    yet;
  - local headed Playwright Chromium on the current workstation failed before
    opening the HH login window with a crashpad `Operation not permitted` error;
  - direct `ssh -Y openclaw@raspberrypi-codex` X11 forwarding is available, but
    Pi-side Chromium exits before a login window stays open;
  - HH route issue was confirmed: HH traffic went through the
    `personal-office` VPN policy route, causing unstable HH/ddos-guard behavior;
  - direct HH `/32` routes were added to table `51820` via the normal LAN
    gateway, and a system-level refresh timer was installed;
  - after route correction and interactive auth refresh,
    `hh_web_healthcheck` returned `storage_state_exists=true`,
    `hh_reachable=true`, and `logged_in=true`;
  - `hh_web_list_resumes` returned without error and found 6 resumes;
  - old `tools/headhunter-web-mcp/.venv` directories were removed from both the
    canonical Personal Office checkout and the legacy `job-search-contour`.

## Next Actions

- Monitor the HH direct-route timer after reboot or network changes:
  `personal-office-hh-direct-route.timer`.
- If future Pi Python setup stalls, download large ARM wheels on the workstation
  and move them into `<repo-root>/.cache/wheelhouse` before rerunning setup.
- Compact the remaining stale full job-intake artifacts listed in
  `personal-projects/personal-brand/workspace/job-intake/summaries/2026-07-03-archivist-job-intake-compaction-ledger.md`
  only after confirming the useful state is preserved in `INDEX.md`,
  `COMPANY_NOTES.md`, task state, and summaries.
- Treat the Pi-side `closed/` and `parked/` job-intake candidates as Pi truth:
  the local checkout does not currently contain those source files, so do not
  overwrite the Pi job-intake tree from local without a deliberate sync plan.

## Safety

The archivist can apply generated-file cleanup automatically, but semantic
Markdown remains review-only until a rollup or compaction artifact preserves the
useful facts.
