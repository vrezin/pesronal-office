#!/usr/bin/env bash
set -euo pipefail

SPIKE_DIR="/home/openclaw/personal-office-agent/job-search-contour/tools/google-workspace-mcp-spike"
ENV_FILE="$SPIKE_DIR/.env.google-workspace.local"

if [[ ! -r "$ENV_FILE" ]]; then
  echo "Missing readable Google Workspace env file: $ENV_FILE" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

exec "$SPIKE_DIR/.venv/bin/workspace-mcp" "$@"
