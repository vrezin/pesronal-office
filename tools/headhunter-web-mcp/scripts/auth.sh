#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
STATE_DIR="$PROJECT_DIR/.local/state"
STATE_FILE="$STATE_DIR/hh-storage-state.json"

mkdir -p "$STATE_DIR"

export HH_WEB_HEADLESS=0
export HH_WEB_STORAGE_STATE="$STATE_FILE"
export HH_WEB_SLOWMO_MS=200

cd "$PROJECT_DIR"

echo "=== HeadHunter Auth ==="
echo "A browser window will open to hh.ru."
echo "Log in manually (OTP, email, whatever)."
echo "Take your time — the script waits for you."
echo ""

uv run python -c "
import sys
import asyncio
from playwright.async_api import async_playwright

async def main():
    pw = await async_playwright().start()
    browser = await pw.chromium.launch(headless=False)
    context = await browser.new_context(
        viewport={'width': 1280, 'height': 900},
    )
    page = await context.new_page()

    print('Opening hh.ru ...')
    await page.goto('https://hh.ru', wait_until='domcontentloaded', timeout=60000)
    print('Browser is ready. Log in now.')
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
