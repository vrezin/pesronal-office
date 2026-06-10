#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${LINKEDIN_MCP_PORT:-8019}"
LOGFILE="$DIR/.run/manual-start.log"
PIDFILE="$DIR/.run/linkedin-mcp.pid"

mkdir -p "$DIR/.run"

if curl -sS --max-time 1 -o /dev/null -X POST \
  "http://127.0.0.1:$PORT/mcp" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","clientInfo":{"name":"codex","version":"1.0"},"capabilities":{}}}' >/dev/null 2>&1; then
  echo "LinkedIn MCP server already running on 127.0.0.1:$PORT"
  exit 0
fi

nohup env LINKEDIN_MCP_PORT="$PORT" "$DIR/scripts/start-local.sh" >"$LOGFILE" 2>&1 &
echo $! >"$PIDFILE"

for _ in $(seq 1 30); do
  if curl -sS --max-time 1 -o /dev/null -X POST \
    "http://127.0.0.1:$PORT/mcp" \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json, text/event-stream' \
    -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","clientInfo":{"name":"codex","version":"1.0"},"capabilities":{}}}' >/dev/null 2>&1; then
    echo "LinkedIn MCP server started on 127.0.0.1:$PORT"
    exit 0
  fi
  sleep 1
done

echo "LinkedIn MCP server did not start on port $PORT." >&2
exit 1
