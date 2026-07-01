#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${PERSONAL_OFFICE_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
PROMPT_FILE="$ROOT/automation/prompts/pi-job-search-telegram-intake.md"
AGENT="${OPENCLAW_JOB_SEARCH_AGENT:-job-search}"
SESSION_KEY="${OPENCLAW_JOB_SEARCH_TELEGRAM_SESSION_KEY:-agent:job-search:telegram-intake}"
TIMEOUT_SECONDS="${OPENCLAW_JOB_SEARCH_TELEGRAM_TIMEOUT_SECONDS:-1200}"
TARGET="${TELEGRAM_JOB_SEARCH_TARGET:-}"
ACCOUNT="${TELEGRAM_JOB_SEARCH_ACCOUNT:-}"
LIMIT="${TELEGRAM_JOB_SEARCH_LIMIT:-10}"
RUN_STAMP="$(date +%Y-%m-%d-%H%M)"
RUN_LOG="$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-telegram-intake.md"
READ_OUTPUT="$(mktemp)"
AGENT_OUTPUT="$(mktemp)"
CHANNEL_OUTPUT="$(mktemp)"

cd "$ROOT"
mkdir -p automation/runs automation/state

cat >"$RUN_LOG" <<EOF
# Pi Job Search Telegram Intake

- Started at: $(date -Iseconds)
- Trigger: scheduled/manual wrapper
- Agent: \`$AGENT\`
- Session key: \`$SESSION_KEY\`
- Repo root: \`$ROOT\`
- Telegram target: \`${TARGET:-unset}\`
- Telegram account: \`${ACCOUNT:-default}\`
- Limit: \`$LIMIT\`
- Timeout seconds: \`$TIMEOUT_SECONDS\`
- Status: running

EOF

python3 tools/job-search-runtime/job_search_runtime.py init
python3 tools/job-search-runtime/job_search_runtime.py status >>"$RUN_LOG"

if [[ -z "$TARGET" ]]; then
  {
    printf '\n## Wrapper Result\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    printf -- '- Status: blocked\n'
    printf -- '- Reason: TELEGRAM_JOB_SEARCH_TARGET is not set. Telegram intake was not attempted.\n'
  } >>"$RUN_LOG"
  rm -f "$READ_OUTPUT" "$AGENT_OUTPUT" "$CHANNEL_OUTPUT"
  exit 2
fi

openclaw channels list >"$CHANNEL_OUTPUT" 2>&1 || true
{
  printf '\n## Channel Preflight\n\n'
  sed 's/^/    /' "$CHANNEL_OUTPUT"
} >>"$RUN_LOG"

if grep -q 'no configured chat channels' "$CHANNEL_OUTPUT"; then
  {
    printf '\n## Wrapper Result\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    printf -- '- Status: blocked\n'
    printf -- '- Reason: no OpenClaw chat channels are configured. Configure Telegram outside Git before enabling this intake.\n'
  } >>"$RUN_LOG"
  rm -f "$READ_OUTPUT" "$AGENT_OUTPUT" "$CHANNEL_OUTPUT"
  exit 2
fi

read_args=(message read --channel telegram --target "$TARGET" --limit "$LIMIT" --json)
if [[ -n "$ACCOUNT" ]]; then
  read_args+=(--account "$ACCOUNT")
fi

set +e
openclaw "${read_args[@]}" >"$READ_OUTPUT" 2>&1
read_status=$?
set -e

{
  printf '\n## Telegram Read Output\n\n'
  sed 's/^/    /' "$READ_OUTPUT"
  printf '\n## Telegram Read Exit Code\n\n'
  printf -- '- Exit code: `%s`\n' "$read_status"
} >>"$RUN_LOG"

if [[ "$read_status" -ne 0 ]]; then
  {
    printf '\n## Wrapper Result\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    printf -- '- Status: blocked\n'
    printf -- '- Reason: OpenClaw Telegram read failed. No agent routing attempted.\n'
  } >>"$RUN_LOG"
  rm -f "$READ_OUTPUT" "$AGENT_OUTPUT" "$CHANNEL_OUTPUT"
  exit "$read_status"
fi

MESSAGE="$(
  printf 'Pi-primary Personal Office repo root: %s\n' "$ROOT"
  printf 'Telegram target: %s\n\n' "$TARGET"
  cat "$PROMPT_FILE"
  printf '\n\n## Raw Telegram Read Payload\n\n'
  cat "$READ_OUTPUT"
)"

set +e
timeout --kill-after=30s "$TIMEOUT_SECONDS" openclaw agent \
  --agent "$AGENT" \
  --session-key "$SESSION_KEY" \
  --timeout "$TIMEOUT_SECONDS" \
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
    printf -- '- Reason: OpenClaw agent did not complete successfully.\n'
  fi
} >>"$RUN_LOG"

rm -f "$READ_OUTPUT" "$AGENT_OUTPUT" "$CHANNEL_OUTPUT"
exit "$agent_status"
