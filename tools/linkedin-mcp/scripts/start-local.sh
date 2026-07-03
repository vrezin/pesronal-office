#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(cd "$DIR/../.." && pwd)"
SHARED_VENV="${PERSONAL_OFFICE_JOB_SEARCH_VENV:-$ROOT/.runtime/job-search-venv}"
LINKEDIN_BIN="$SHARED_VENV/bin/linkedin-mcp-server"

if [[ ! -x "$LINKEDIN_BIN" ]]; then
  LINKEDIN_BIN="$DIR/.venv/bin/linkedin-mcp-server"
fi

if [[ ! -x "$LINKEDIN_BIN" ]]; then
  echo "LinkedIn MCP runtime is missing." >&2
  echo "Run: tools/job-search-runtime/setup-shared-env.sh" >&2
  exit 1
fi

args=(
  --transport streamable-http
  --host 127.0.0.1
  --port "${LINKEDIN_MCP_PORT:-8019}"
  --path /mcp
  --timeout 30000
  --tool-timeout 240
)
if [[ -n "${LINKEDIN_CHROME_PATH:-}" ]]; then
  args+=(--chrome-path "$LINKEDIN_CHROME_PATH")
fi
args+=(--user-data-dir "$DIR/profile")

exec "$LINKEDIN_BIN" "${args[@]}"
