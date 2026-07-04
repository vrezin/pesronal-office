#!/usr/bin/env bash
set -u

usage() {
  cat >&2 <<'EOF'
Usage: worker-pi-job-search-handoff.sh <handoff-path> <run-log> <dispatch-output> <run-stamp> <telegram-account> <telegram-target>

Runs the durable Pi job-search handoff worker. This script is intended to be
started by enqueue-pi-job-search-handoff.sh through systemd-run --user.
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ "$#" -ne 6 ]]; then
  usage
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${PERSONAL_OFFICE_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
OPENCLAW_BIN="${OPENCLAW_BIN:-/home/openclaw/.local/bin/openclaw}"
export PATH="/home/openclaw/.local/opt/node-v22-arm64/bin:$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
DISPATCH_SCRIPT="${JOB_SEARCH_HANDOFF_DISPATCH_SCRIPT:-$ROOT/automation/scripts/dispatch-pi-job-search-handoff.sh}"

HANDOFF_PATH="$1"
RUN_LOG="$2"
DISPATCH_OUTPUT="$3"
RUN_STAMP="$4"
TELEGRAM_ACCOUNT="$5"
TELEGRAM_TARGET="$6"

cd "$ROOT"

{
  printf '\n## Worker\n\n'
  printf -- '- Started at: %s\n' "$(date -Iseconds)"
  printf -- '- PID: `%s`\n' "$$"
  printf -- '- Systemd unit: `%s`\n' "${INVOCATION_ID:-unknown}"
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

if [[ "$dispatch_status" -eq 0 && "$send_status" -eq 0 ]]; then
  exit 0
fi

if [[ "$dispatch_status" -eq 0 ]]; then
  exit "$send_status"
fi

exit "$dispatch_status"
