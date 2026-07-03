#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VENV="${PERSONAL_OFFICE_JOB_SEARCH_VENV:-$ROOT/.runtime/job-search-venv}"

if [[ ! -x "$VENV/bin/headhunter-web-mcp" ]]; then
  echo "Shared job-search runtime is missing headhunter-web-mcp." >&2
  echo "Run: tools/job-search-runtime/setup-shared-env.sh" >&2
  exit 1
fi

export UV_CACHE_DIR="${UV_CACHE_DIR:-$ROOT/.cache/uv}"
export HH_WEB_STORAGE_STATE="${HH_WEB_STORAGE_STATE:-$ROOT/tools/headhunter-web-mcp/.local/state/hh-storage-state.json}"
if [[ -z "${HH_WEB_CHROMIUM_EXECUTABLE:-}" && -x /usr/bin/chromium ]]; then
  export HH_WEB_CHROMIUM_EXECUTABLE=/usr/bin/chromium
fi
if [[ -n "${HH_WEB_CHROMIUM_EXECUTABLE:-}" ]]; then
  export HH_WEB_CHROMIUM_NO_SANDBOX="${HH_WEB_CHROMIUM_NO_SANDBOX:-1}"
fi

cd "$ROOT/tools/headhunter-web-mcp"
exec "$VENV/bin/headhunter-web-mcp" "$@"
