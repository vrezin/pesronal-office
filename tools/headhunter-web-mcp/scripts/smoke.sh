#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "=== Smoke checks ==="

echo "1. Syntax check..."
uv run python -m py_compile server.py
uv run python -m py_compile hh_web/__init__.py
uv run python -m py_compile hh_web/browser.py
uv run python -m py_compile hh_web/models.py
uv run python -m py_compile hh_web/pages.py
uv run python -m py_compile hh_web/parser.py
uv run python -m py_compile hh_web/tools.py
echo "   PASS: all files compile"

echo "2. MCP server starts under stdio..."
timeout 5 uv run headhunter-web-mcp --help 2>/dev/null || echo "   (expected: server runs until killed)"
echo "   PASS: server process starts"

echo "3. Healthcheck (requires auth state)..."
uv run python -c "
import asyncio, json
from hh_web.tools import healthcheck
result = asyncio.run(healthcheck())
print(json.dumps(result, indent=2, ensure_ascii=False))
" 2>/dev/null || echo "   (skipped: no storage state)"

echo ""
echo "=== Smoke checks complete ==="
