#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ROOT="$(cd "$PROJECT_DIR/../.." && pwd)"
VENV="${PERSONAL_OFFICE_JOB_SEARCH_VENV:-$ROOT/.runtime/job-search-venv}"
STATE_DIR="$PROJECT_DIR/.local/state"
STATE_FILE="$STATE_DIR/hh-storage-state.json"

mkdir -p "$STATE_DIR"

export HH_WEB_HEADLESS=0
export HH_WEB_STORAGE_STATE="$STATE_FILE"
export HH_WEB_SLOWMO_MS=200
if [[ -z "${HH_WEB_CHROMIUM_EXECUTABLE:-}" && -x /usr/bin/chromium ]]; then
  export HH_WEB_CHROMIUM_EXECUTABLE=/usr/bin/chromium
fi
if [[ -n "${HH_WEB_CHROMIUM_EXECUTABLE:-}" ]]; then
  export HH_WEB_CHROMIUM_NO_SANDBOX="${HH_WEB_CHROMIUM_NO_SANDBOX:-1}"
fi

if [[ ! -x "$VENV/bin/python" ]]; then
  echo "Shared job-search runtime is missing: $VENV" >&2
  echo "Run: tools/job-search-runtime/setup-shared-env.sh" >&2
  exit 1
fi

cd "$PROJECT_DIR"

echo "=== HeadHunter Auth ==="
echo "A browser window will open to hh.ru."
echo "Log in manually (OTP, email, whatever)."
echo "Take your time — the script waits for you."
echo ""

"$VENV/bin/python" -c "
import sys
import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    pw = await async_playwright().start()
    launch_args = {
        'headless': False,
        'slow_mo': int(os.environ.get('HH_WEB_SLOWMO_MS', '0')),
    }
    chromium_executable = os.environ.get('HH_WEB_CHROMIUM_EXECUTABLE', '')
    if chromium_executable:
        launch_args['executable_path'] = chromium_executable
    browser_args = ['--disable-crash-reporter', '--disable-crashpad']
    if os.environ.get('HH_WEB_CHROMIUM_NO_SANDBOX', '0') == '1':
        browser_args.append('--no-sandbox')
    launch_args['args'] = browser_args

    browser = await pw.chromium.launch(**launch_args)
    context = await browser.new_context(
        viewport={'width': 1280, 'height': 900},
    )
    page = await context.new_page()

    print('Browser is ready.')
    print('Open https://hh.ru in the browser window and log in now.')
    print()
    print('>>> Press ENTER here when done <<<')
    print()

    # Wait for user to press Enter — no timeout
    await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)

    print('Saving session state...')
    await context.storage_state(path='$STATE_FILE')
    print(f'Session saved to: $STATE_FILE')

    await browser.close()
    await pw.stop()
    print('Done.')

asyncio.run(main())
"

echo ""
echo "You can now use the MCP server."
