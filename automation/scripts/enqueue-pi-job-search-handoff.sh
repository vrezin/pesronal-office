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
CONFIG_DIR="${PERSONAL_OFFICE_CONFIG_DIR:-$HOME/.config/personal-office}"
INTAKE_ENV_FILE="${INTAKE_TELEGRAM_ENV_FILE:-$CONFIG_DIR/intake-telegram.env}"
DISPATCH_SCRIPT="${JOB_SEARCH_HANDOFF_DISPATCH_SCRIPT:-$ROOT/automation/scripts/dispatch-pi-job-search-handoff.sh}"
HANDOFF_PATH="$1"
RUN_STAMP="$(date +%Y-%m-%d-%H%M%S)"
RUN_LOG="$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-handoff-async.md"
DISPATCH_OUTPUT="$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-handoff-async-dispatch.md"

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
- Dispatch output: \`${DISPATCH_OUTPUT#"$ROOT/"}\`
- Telegram account: \`$TELEGRAM_ACCOUNT\`
- Telegram target: \`${TELEGRAM_TARGET:-unset}\`
- Status: queued

EOF

(
  set +e

  {
    printf '\n## Worker\n\n'
    printf -- '- Started at: %s\n' "$(date -Iseconds)"
    printf -- '- PID: `%s`\n' "$$"
  } >>"$RUN_LOG"

  OPENCLAW_JOB_SEARCH_HANDOFF_SESSION_SUFFIX="${RUN_STAMP}-async" \
    "$DISPATCH_SCRIPT" "$HANDOFF_PATH" >"$DISPATCH_OUTPUT" 2>&1
  dispatch_status=$?

  {
    printf '\n## Dispatcher Result\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    printf -- '- Exit code: `%s`\n' "$dispatch_status"
    printf '\n## Dispatcher Output\n\n'
    sed 's/^/    /' "$DISPATCH_OUTPUT"
  } >>"$RUN_LOG"

  reply="$(
    python3 - "$dispatch_status" "$HANDOFF_PATH" "${DISPATCH_OUTPUT#"$ROOT/"}" <<'PY'
import re
import sys

status = int(sys.argv[1])
handoff_path = sys.argv[2]
dispatch_output_path = sys.argv[3]

try:
    text = open(dispatch_output_path, "r", encoding="utf-8").read()
except FileNotFoundError:
    text = ""

match = re.search(r"JOB_SEARCH_OUTPUT_BEGIN\n(?P<body>.*)\nJOB_SEARCH_OUTPUT_END", text, re.S)
body = match.group("body").strip() if match else text.strip()

yaml_match = re.search(r"```yaml\n(?P<yaml>.*?)\n```", body, re.S)
yaml = yaml_match.group("yaml") if yaml_match else body

data = {}
current_key = None
for raw_line in yaml.splitlines():
    line = raw_line.rstrip()
    if not line.strip():
        continue
    if re.match(r"^[A-Za-z_]+:", line):
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value:
            data[key] = value.strip('"')
        else:
            data[key] = []
    elif current_key and line.strip().startswith("- "):
        data.setdefault(current_key, [])
        if not isinstance(data[current_key], list):
            data[current_key] = [str(data[current_key])]
        data[current_key].append(line.strip()[2:].strip('"'))

def value(key, default=""):
    item = data.get(key, default)
    if item in ("null", "[]", None):
        return default
    return item

def as_list(key):
    item = data.get(key, [])
    if item in ("null", "[]", None, ""):
        return []
    if isinstance(item, list):
        return [x for x in item if x and x != "null"]
    return [str(item)]

summary = value("summary", "job-search обработал handoff")
verdict = value("verdict", "blocked" if status else "done")
next_action = value("next_action", "проверить run log")
cv = value("cv", "")
cover_letter = value("cover_letter", "")
reasons = as_list("reasons")[:4]
artifacts = as_list("artifacts")[:6]
blocked = as_list("blocked_on")[:4]
run_log_match = re.search(r"^RUN_LOG=(?P<path>.+)$", text, re.M)
run_log = run_log_match.group("path").strip() if run_log_match else dispatch_output_path

lines = []
if status == 0:
    lines.append(f"Готово по job-search handoff: {summary}")
else:
    lines.append(f"Job-search handoff завершился нештатно: {summary}")

lines.append("")
lines.append(f"Вердикт: {verdict}")

if reasons:
    lines.append("Почему:")
    lines.extend(f"- {item}" for item in reasons)

if cv or cover_letter:
    lines.append("")
    if cv:
        lines.append(f"CV: {cv}")
    if cover_letter:
        lines.append(f"CL/reply: {cover_letter}")

lines.append("")
lines.append(f"Next: {next_action}")

if artifacts:
    lines.append("Artifacts:")
    lines.extend(f"- {item}" for item in artifacts)
else:
    lines.append(f"Artifact: {handoff_path}")

if blocked:
    lines.append("Blocked:")
    lines.extend(f"- {item}" for item in blocked)

lines.append(f"Run log: {run_log}")

print("\n".join(lines))
PY
  )"

  if [[ -n "$TELEGRAM_TARGET" ]]; then
    send_output="$("$OPENCLAW_BIN" message send \
      --channel telegram \
      --account "$TELEGRAM_ACCOUNT" \
      --target "$TELEGRAM_TARGET" \
      -m "$reply" \
      --json 2>&1)"
    send_status=$?
  else
    send_output="TELEGRAM_INTAKE_TARGET is unset"
    send_status=2
  fi

  {
    printf '\n## Telegram Follow-Up\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    printf -- '- Exit code: `%s`\n' "$send_status"
    printf '\n### Message\n\n'
    printf '%s\n' "$reply" | sed 's/^/    /'
    printf '\n### Send Output\n\n'
    printf '%s\n' "$send_output" | sed 's/^/    /'
    printf '\n## Wrapper Result\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    if [[ "$dispatch_status" -eq 0 && "$send_status" -eq 0 ]]; then
      printf -- '- Status: completed\n'
    elif [[ "$dispatch_status" -eq 0 ]]; then
      printf -- '- Status: completed_without_telegram\n'
    else
      printf -- '- Status: blocked\n'
    fi
  } >>"$RUN_LOG"
) >/dev/null 2>&1 </dev/null &

worker_pid=$!

{
  printf '\n## Enqueue Result\n\n'
  printf -- '- Queued at: %s\n' "$(date -Iseconds)"
  printf -- '- Worker PID: `%s`\n' "$worker_pid"
  printf -- '- Status: queued\n'
} >>"$RUN_LOG"

printf 'ENQUEUE_STATUS=queued\n'
printf 'RUN_LOG=%s\n' "${RUN_LOG#"$ROOT/"}"
printf 'WORKER_PID=%s\n' "$worker_pid"
printf 'DISPATCH_OUTPUT=%s\n' "${DISPATCH_OUTPUT#"$ROOT/"}"
