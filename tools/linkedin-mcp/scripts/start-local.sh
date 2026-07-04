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

PATCH_FILE="$DIR/patches/2026-07-04-job-posting-lazy-body-extraction.patch"
if [[ -r "$PATCH_FILE" ]]; then
  shopt -s nullglob
  extractor_candidates=(
    "$SHARED_VENV"/lib/python*/site-packages/linkedin_mcp_server/scraping/extractor.py
    "$DIR"/.venv/lib/python*/site-packages/linkedin_mcp_server/scraping/extractor.py
  )
  shopt -u nullglob

  for extractor_file in "${extractor_candidates[@]}"; do
    if [[ ! -f "$extractor_file" ]]; then
      continue
    fi
    if grep -q "_extract_loaded_job_posting" "$extractor_file"; then
      continue
    fi
    if ! command -v patch >/dev/null 2>&1; then
      echo "LinkedIn MCP runtime patch is pending, but 'patch' is unavailable." >&2
      exit 1
    fi
    patch --forward --silent "$extractor_file" "$PATCH_FILE"
  done
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
