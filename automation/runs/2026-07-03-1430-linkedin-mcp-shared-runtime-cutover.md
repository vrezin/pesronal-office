# LinkedIn MCP Shared Runtime Cutover

- Date: 2026-07-03 14:30 +07
- Host: `raspberrypi-codex`
- User service: `linkedin-mcp.service`
- Status: endpoint and LinkedIn auth smoke healthy

## Changed

- Installed `automation/systemd/personal-office-linkedin-mcp.service` as the Pi
  user service template.
- Switched the service from the legacy `job-search-contour` LinkedIn `.venv` to
  the canonical Personal Office shared runtime:
  `<repo-root>/.runtime/job-search-venv`.
- Copied LinkedIn browser/auth state into
  `<repo-root>/tools/linkedin-mcp/`.
- Set `PLAYWRIGHT_BROWSERS_PATH` to
  `<repo-root>/tools/linkedin-mcp/patchright-browsers` and
  `PLAYWRIGHT_SKIP_BROWSER_GC=1`.
- Added the missing Patchright `ffmpeg-1011` browser dependency and validated
  Patchright host requirements.

## Verification

- `linkedin-mcp.service`: active/running.
- Main process:
  `<repo-root>/.runtime/job-search-venv/bin/python ... linkedin-mcp-server`.
- Listener: `127.0.0.1:8019`.
- MCP `list-tools`: returned 17 tools.
- First non-mutating auth smoke `get_my_profile`: reached the tool but returned
  `Session expired` after a partial canonical profile transfer.
- Follow-up check against the old full `job-search-contour` profile using the
  shared runtime succeeded.
- The canonical `<repo-root>/tools/linkedin-mcp/profile` was replaced with the
  full old profile, and `get_my_profile` then passed on the main `127.0.0.1:8019`
  service.

## Cleanup

- Removed legacy dependency/browser runtime directories after cutover:
  - `job-search-contour/tools/linkedin-mcp/.venv` - about 255 MB;
  - `job-search-contour/tools/linkedin-mcp/patchright-browsers` - about 953 MB.
- Removed the failed partial canonical profile backup after the full-profile
  transfer passed.
- Preserved legacy `profile/`, `cookies.json`, and `source-state.json` as auth
  rollback material.

## Next

- Continue HH Web runtime cleanup. HH API is historical-only and must not be
  revived as a shared-runtime target.

## HH API Follow-Up

- 2026-07-03: confirmed operating decision that HH API is not a live contour:
  there is no usable API key/OAuth path for the applicant workflow.
- Removed the shared-runtime HH API launcher from `tools/job-search-runtime/`.
- Updated `tools/job-search-runtime/setup-shared-env.sh` so it installs and
  verifies HH Web only, not `tools/headhunter-mcp-server/`.
- Removed stale local HH API runtime state:
  `tools/headhunter-mcp-server/.venv` and the old shared
  `headhunter-mcp` entrypoint.
