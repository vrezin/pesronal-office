#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROMPT_FILE="$REPO_ROOT/automation/prompts/hh-gmail-monitor.md"

cd "$REPO_ROOT"
exec timeout 45m "$REPO_ROOT/codex.sh" \
  --ask-for-approval never \
  --sandbox workspace-write \
  exec "$(cat "$PROMPT_FILE")"
