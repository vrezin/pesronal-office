#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "$DIR/.venv/bin/linkedin-mcp-server" \
  --transport streamable-http \
  --host 127.0.0.1 \
  --port "${LINKEDIN_MCP_PORT:-8019}" \
  --path /mcp \
  --timeout 30000 \
  --tool-timeout 240 \
  --user-data-dir "$DIR/profile"
