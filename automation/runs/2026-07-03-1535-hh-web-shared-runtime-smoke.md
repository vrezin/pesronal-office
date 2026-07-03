# HH Web Shared Runtime Smoke

- Date: 2026-07-03 15:35 +07
- Host: `raspberrypi-codex`
- Status: shared runtime and HH auth smoke healthy

## Checks

- `tools/job-search-runtime/run-headhunter-web-mcp.sh` starts through the shared
  runtime.
- Shared runtime entrypoint exists:
  `<repo-root>/.runtime/job-search-venv/bin/headhunter-web-mcp`.
- HH API entrypoint is absent:
  `<repo-root>/.runtime/job-search-venv/bin/headhunter-mcp`.
- Canonical HH Web storage state was copied from the old job-search contour to:
  `<repo-root>/tools/headhunter-web-mcp/.local/state/hh-storage-state.json`.
- Storage state permissions on Pi are `600`.

## Result

- Initial `hh_web_healthcheck` saw `storage_state_exists=true`, but the browser
  session reached an anonymous HH/login page instead of a logged-in applicant
  session.
- After route correction and interactive auth refresh, final `hh_web_healthcheck`
  returned:
  - `storage_state_exists=true`;
  - `hh_reachable=true`;
  - `logged_in=true`;
  - `Session active (resumes content)`.
- `hh_web_list_resumes` returned without error and found 6 resumes.

## Decision

- Removed the old HH Web per-tool `.venv` after the shared-runtime auth smoke
  passed.
- HH Web is now the only active HH contour. HH API remains historical-only.

## Auth Refresh Attempts

- Updated `tools/headhunter-web-mcp/scripts/auth.sh` to use the shared
  `<repo-root>/.runtime/job-search-venv` runtime instead of a tool-local `uv`
  environment.
- On Pi, the auth script defaults to `/usr/bin/chromium` and `--no-sandbox`.
- The first historical `adrelinux-codex` X11 screen route check was not
  reachable from this session (`No route to host`).
- Follow-up attempt from the current workstation found `DISPLAY=:0`, but the
  local Playwright Chromium failed before opening a window with a crashpad
  `Operation not permitted` error.
- Direct `ssh -Y openclaw@raspberrypi-codex` X11 forwarding is available and
  exposes `DISPLAY=localhost:11.0`, but Pi-side Playwright Chromium also exits
  before the login window opens. A raw `/usr/lib/chromium/chromium` X11 launch
  exits immediately without leaving a browser process.
- After `adrelinux-codex` returned, the working route was:
  `ssh adrelinux-codex`, set `DISPLAY=:0` and `XAUTHORITY=$HOME/.Xauthority`,
  then `ssh -Y openclaw@192.168.1.44` and run
  `bash tools/headhunter-web-mcp/scripts/auth.sh`.

## Route Fix

- HH traffic was using the `personal-office` VPN policy table and HH/ddos-guard
  saw the VPN egress address.
- Added direct `/32` HH routes into table `51820` via the normal LAN gateway so
  HH uses the household ISP route instead of VPN.
- Installed system-level refresh templates:
  - `automation/systemd/personal-office-hh-direct-route.service`;
  - `automation/systemd/personal-office-hh-direct-route.timer`.
- Timer is enabled on Pi and refreshes every 30 minutes.

## Final State

- LinkedIn: shared runtime, auth smoke green.
- HH Web: shared runtime, auth smoke green.
- HH API: historical-only; no shared `headhunter-mcp` entrypoint.
- Per-tool HH/LinkedIn `.venv`: no longer target runtime; HH Web old `.venv`
  was removed after verification.
