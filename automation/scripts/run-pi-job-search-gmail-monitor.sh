#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${PERSONAL_OFFICE_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
PROMPT_FILE="$ROOT/automation/prompts/pi-job-search-gmail-monitor.md"
AGENT="${OPENCLAW_JOB_SEARCH_AGENT:-job-search}"
SESSION_KEY="${OPENCLAW_JOB_SEARCH_SESSION_KEY:-agent:job-search:pi-gmail-monitor}"
TIMEOUT_SECONDS="${OPENCLAW_JOB_SEARCH_TIMEOUT_SECONDS:-3600}"
RUN_STAMP="$(date +%Y-%m-%d-%H%M)"
RUN_LOG="$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-gmail-monitor.md"
AGENT_OUTPUT="$(mktemp)"

cd "$ROOT"

mkdir -p automation/runs automation/state

cat >"$RUN_LOG" <<EOF
# Pi Job Search Gmail Monitor

- Started at: $(date -Iseconds)
- Trigger: scheduled/manual wrapper
- Agent: \`$AGENT\`
- Session key: \`$SESSION_KEY\`
- Repo root: \`$ROOT\`
- Timeout seconds: \`$TIMEOUT_SECONDS\`
- Status: running

EOF

python3 tools/job-search-runtime/job_search_runtime.py init
python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state
python3 tools/job-search-runtime/job_search_runtime.py status >>"$RUN_LOG"

MESSAGE="$(printf 'Pi-primary Personal Office repo root: %s\n\n' "$ROOT"; cat "$PROMPT_FILE")"

set +e
timeout --kill-after=30s "$TIMEOUT_SECONDS" openclaw agent \
  --agent "$AGENT" \
  --session-key "$SESSION_KEY" \
  --timeout "$TIMEOUT_SECONDS" \
  --message "$MESSAGE" >"$AGENT_OUTPUT" 2>&1
status=$?
set -e

{
  printf '\n## Agent Output\n\n'
  if [[ -s "$AGENT_OUTPUT" ]]; then
    sed 's/^/    /' "$AGENT_OUTPUT"
  else
    printf '    <no output>\n'
  fi
  printf '\n## Wrapper Result\n\n'
  printf -- '- Finished at: %s\n' "$(date -Iseconds)"
  printf -- '- Exit code: `%s`\n' "$status"
  if [[ "$status" -eq 0 ]]; then
    printf -- '- Status: completed\n'
  elif [[ "$status" -eq 124 || "$status" -eq 137 ]]; then
    printf -- '- Status: blocked\n'
    printf -- '- Reason: OpenClaw agent did not return before wrapper timeout. Legacy monitor state was not advanced by wrapper.\n'
  else
    printf -- '- Status: blocked\n'
    printf -- '- Reason: OpenClaw agent exited non-zero. Legacy monitor state was not advanced by wrapper.\n'
  fi
} >>"$RUN_LOG"

rm -f "$AGENT_OUTPUT"
exit "$status"
