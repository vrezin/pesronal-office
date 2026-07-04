#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: enqueue-pi-job-search-handoff.sh <handoff-path>

Queues a Pi job-search handoff for asynchronous dispatch.

The caller should reply to Telegram immediately with a short acknowledgement.
This wrapper starts the dispatcher in the background and sends the final
follow-up through the Personal Office intake Telegram account.
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
CONFIG_DIR="${PERSONAL_OFFICE_CONFIG_DIR:-$HOME/.config/personal-office}"
INTAKE_ENV_FILE="${INTAKE_TELEGRAM_ENV_FILE:-$CONFIG_DIR/intake-telegram.env}"
DISPATCH_SCRIPT="${JOB_SEARCH_HANDOFF_DISPATCH_SCRIPT:-$ROOT/automation/scripts/dispatch-pi-job-search-handoff.sh}"
WORKER_SCRIPT="${JOB_SEARCH_HANDOFF_WORKER_SCRIPT:-$ROOT/automation/scripts/worker-pi-job-search-handoff.sh}"
HANDOFF_PATH="$1"
RUN_STAMP="$(date +%Y-%m-%d-%H%M%S)"
RUN_LOG="$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-handoff-async.md"
DISPATCH_OUTPUT="$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-handoff-async-dispatch.md"
UNIT_NAME="personal-office-job-search-handoff-${RUN_STAMP}"

cd "$ROOT"

case "$HANDOFF_PATH" in
  /*)
    HANDOFF_ABS="$HANDOFF_PATH"
    ;;
  *)
    HANDOFF_ABS="$ROOT/$HANDOFF_PATH"
    ;;
esac

if [[ ! -f "$HANDOFF_ABS" ]]; then
  printf 'Async dispatcher blocked: handoff file does not exist: %s\n' "$HANDOFF_PATH" >&2
  exit 2
fi

if [[ ! -x "$DISPATCH_SCRIPT" ]]; then
  printf 'Async dispatcher blocked: dispatch script is not executable: %s\n' "$DISPATCH_SCRIPT" >&2
  exit 2
fi

if [[ ! -x "$WORKER_SCRIPT" ]]; then
  printf 'Async dispatcher blocked: worker script is not executable: %s\n' "$WORKER_SCRIPT" >&2
  exit 2
fi

if [[ -r "$INTAKE_ENV_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$INTAKE_ENV_FILE"
fi

TELEGRAM_ACCOUNT="${TELEGRAM_INTAKE_ACCOUNT:-personal-office-intake-telegram}"
TELEGRAM_TARGET="${TELEGRAM_INTAKE_TARGET:-${TELEGRAM_JOB_SEARCH_TARGET:-}}"

mkdir -p automation/runs automation/state

cat >"$RUN_LOG" <<EOF
# Pi Job Search Handoff Async

- Started at: $(date -Iseconds)
- Trigger: intake async enqueue
- Handoff path: \`$HANDOFF_PATH\`
- Dispatcher: \`$DISPATCH_SCRIPT\`
- Worker: \`$WORKER_SCRIPT\`
- Dispatch output: \`${DISPATCH_OUTPUT#"$ROOT/"}\`
- Systemd unit: \`$UNIT_NAME\`
- Telegram account: \`$TELEGRAM_ACCOUNT\`
- Telegram target: \`${TELEGRAM_TARGET:-unset}\`
- Status: queued

EOF

set +e
systemd_output="$(systemd-run --user \
  --collect \
  --unit "$UNIT_NAME" \
  --working-directory "$ROOT" \
  -E "PERSONAL_OFFICE_ROOT=$ROOT" \
  -E "OPENCLAW_BIN=$OPENCLAW_BIN" \
  -E "JOB_SEARCH_HANDOFF_DISPATCH_SCRIPT=$DISPATCH_SCRIPT" \
  "$WORKER_SCRIPT" \
  "$HANDOFF_PATH" \
  "$RUN_LOG" \
  "$DISPATCH_OUTPUT" \
  "$RUN_STAMP" \
  "$TELEGRAM_ACCOUNT" \
  "$TELEGRAM_TARGET" 2>&1)"
systemd_status=$?
set -e

{
  printf '\n## Enqueue Result\n\n'
  printf -- '- Queued at: %s\n' "$(date -Iseconds)"
  printf -- '- Systemd exit code: `%s`\n' "$systemd_status"
  printf '\n### Systemd Output\n\n'
  printf '%s\n' "$systemd_output" | sed 's/^/    /'
  if [[ "$systemd_status" -eq 0 ]]; then
    printf -- '- Status: queued\n'
  else
    printf -- '- Status: blocked\n'
  fi
} >>"$RUN_LOG"

if [[ "$systemd_status" -ne 0 ]]; then
  printf 'Async dispatcher blocked: systemd-run failed for unit %s\n' "$UNIT_NAME" >&2
  printf '%s\n' "$systemd_output" >&2
  exit "$systemd_status"
fi

printf 'ENQUEUE_STATUS=queued\n'
printf 'RUN_LOG=%s\n' "${RUN_LOG#"$ROOT/"}"
printf 'WORKER_UNIT=%s\n' "$UNIT_NAME"
printf 'DISPATCH_OUTPUT=%s\n' "${DISPATCH_OUTPUT#"$ROOT/"}"
