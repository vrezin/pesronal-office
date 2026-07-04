#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: dispatch-pi-job-search-handoff.sh <handoff-path>

Runs the Pi job-search agent for an intake-created handoff and prints a compact
dispatcher result for the intake/output secretary.
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ "$#" -ne 1 ]]; then
  usage
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${PERSONAL_OFFICE_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
OPENCLAW_BIN="${OPENCLAW_BIN:-/home/openclaw/.local/bin/openclaw}"
export PATH="/home/openclaw/.local/opt/node-v22-arm64/bin:$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
PROMPT_FILE="${JOB_SEARCH_HANDOFF_PROMPT_FILE:-$ROOT/automation/prompts/pi-job-search-handoff-dispatch.md}"
AGENT="${OPENCLAW_JOB_SEARCH_AGENT:-job-search}"
TIMEOUT_SECONDS="${OPENCLAW_JOB_SEARCH_HANDOFF_TIMEOUT_SECONDS:-900}"
THINKING="${OPENCLAW_JOB_SEARCH_HANDOFF_THINKING:-medium}"
LOCK_NAME="pi-job-search-handoff-dispatch"
RUN_STAMP="$(date +%Y-%m-%d-%H%M)"
LOCK_OWNER="${RUN_STAMP}-$$"
LOCK_TTL_SECONDS="${OPENCLAW_JOB_SEARCH_HANDOFF_LOCK_TTL_SECONDS:-1800}"
RUN_LOG="$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-handoff-dispatch.md"
AGENT_OUTPUT="$(mktemp)"
SANITIZED_OUTPUT="$(mktemp)"
LOCK_ACQUIRED=0

cd "$ROOT"

HANDOFF_PATH="$1"
case "$HANDOFF_PATH" in
  /*)
    HANDOFF_ABS="$HANDOFF_PATH"
    ;;
  *)
    HANDOFF_ABS="$ROOT/$HANDOFF_PATH"
    ;;
esac

if [[ ! -f "$HANDOFF_ABS" ]]; then
  printf 'Dispatcher blocked: handoff file does not exist: %s\n' "$HANDOFF_PATH" >&2
  exit 2
fi

if [[ ! -f "$PROMPT_FILE" ]]; then
  printf 'Dispatcher blocked: prompt file does not exist: %s\n' "$PROMPT_FILE" >&2
  exit 2
fi

mkdir -p automation/runs automation/state

cat >"$RUN_LOG" <<EOF
# Pi Job Search Handoff Dispatch

- Started at: $(date -Iseconds)
- Trigger: intake handoff dispatcher
- Agent: \`$AGENT\`
- OpenClaw binary: \`$OPENCLAW_BIN\`
- Handoff path: \`$HANDOFF_PATH\`
- Prompt file: \`$PROMPT_FILE\`
- Repo root: \`$ROOT\`
- Timeout seconds: \`$TIMEOUT_SECONDS\`
- Thinking: \`$THINKING\`
- Telegram mutation: none
- Status: running

EOF

python3 tools/job-search-runtime/job_search_runtime.py init

set +e
lock_output="$(python3 tools/job-search-runtime/job_search_runtime.py acquire-lock --lock-name "$LOCK_NAME" --owner "$LOCK_OWNER" --ttl-seconds "$LOCK_TTL_SECONDS" 2>&1)"
lock_status=$?
set -e

{
  printf '\n## Lock\n\n'
  printf '    %s\n' "$lock_output"
  printf -- '- Lock exit code: `%s`\n' "$lock_status"
} >>"$RUN_LOG"

if [[ "$lock_status" -ne 0 ]]; then
  {
    printf '\n## Wrapper Result\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    printf -- '- Exit code: `0`\n'
    printf -- '- Status: skipped\n'
    printf -- '- Reason: another `%s` run lock is active. No job-search dispatch attempted.\n' "$LOCK_NAME"
  } >>"$RUN_LOG"
  printf 'DISPATCH_STATUS=skipped\n'
  printf 'RUN_LOG=%s\n' "${RUN_LOG#"$ROOT/"}"
  printf 'REASON=another %s run lock is active\n' "$LOCK_NAME"
  rm -f "$AGENT_OUTPUT"
  exit 0
fi

LOCK_ACQUIRED=1
cleanup() {
  if [[ "$LOCK_ACQUIRED" -eq 1 ]]; then
    python3 tools/job-search-runtime/job_search_runtime.py release-lock --lock-name "$LOCK_NAME" --owner "$LOCK_OWNER" >>"$RUN_LOG" 2>&1 || true
  fi
  rm -f "$AGENT_OUTPUT" "$SANITIZED_OUTPUT"
}
trap cleanup EXIT

SESSION_KEY_BASE="$(printf '%s' "$HANDOFF_PATH" | tr -c '[:alnum:]' '-' | tr '[:upper:]' '[:lower:]' | cut -c1-90)"
SESSION_KEY_SUFFIX="${OPENCLAW_JOB_SEARCH_HANDOFF_SESSION_SUFFIX:-$RUN_STAMP}"
SESSION_KEY="agent:job-search:handoff-dispatch:${SESSION_KEY_BASE}:${SESSION_KEY_SUFFIX}"

{
  printf -- '- Session key: `%s`\n' "$SESSION_KEY"
} >>"$RUN_LOG"

MESSAGE="$(
  printf 'Pi-primary Personal Office repo root: %s\n' "$ROOT"
  printf 'Handoff path: %s\n\n' "$HANDOFF_PATH"
  cat "$PROMPT_FILE"
  printf '\n\n## Handoff Body\n\n'
  cat "$HANDOFF_ABS"
)"

set +e
timeout --kill-after=30s "$TIMEOUT_SECONDS" "$OPENCLAW_BIN" agent \
  --agent "$AGENT" \
  --session-key "$SESSION_KEY" \
  --timeout "$TIMEOUT_SECONDS" \
  --thinking "$THINKING" \
  --message "$MESSAGE" >"$AGENT_OUTPUT" 2>&1
agent_status=$?
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
  printf -- '- Exit code: `%s`\n' "$agent_status"
  if [[ "$agent_status" -eq 0 ]]; then
    printf -- '- Status: completed\n'
  else
    printf -- '- Status: blocked\n'
    printf -- '- Reason: OpenClaw job-search agent did not complete successfully.\n'
  fi
} >>"$RUN_LOG"

grep -v -E '^(⚠️|🛠️|[[:space:]]*⚠️|[[:space:]]*🛠️)' "$AGENT_OUTPUT" >"$SANITIZED_OUTPUT" || true

printf 'DISPATCH_STATUS=%s\n' "$([[ "$agent_status" -eq 0 ]] && printf completed || printf blocked)"
printf 'RUN_LOG=%s\n' "${RUN_LOG#"$ROOT/"}"
printf 'JOB_SEARCH_OUTPUT_BEGIN\n'
cat "$SANITIZED_OUTPUT"
printf '\nJOB_SEARCH_OUTPUT_END\n'

exit "$agent_status"
