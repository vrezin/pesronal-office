#!/usr/bin/env bash
set -euo pipefail

ROOT="${PERSONAL_OFFICE_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
REMOTE="${PERSONAL_OFFICE_SYNC_REMOTE:-origin}"
BRANCH="${PERSONAL_OFFICE_SYNC_BRANCH:-main}"
MODE="${PERSONAL_OFFICE_SYNC_MODE:-dry-run}"
RUN_CMD="${*:-}"
RUN_STAMP="$(date +%Y-%m-%d-%H%M)"
RUN_LOG="${PERSONAL_OFFICE_SYNC_RUN_LOG:-$ROOT/automation/runs/${RUN_STAMP}-pi-job-search-sync.md}"

cd "$ROOT"

mkdir -p automation/runs automation/state

cat >"$RUN_LOG" <<EOF
# Pi Job Search Sync

- Started at: $(date -Iseconds)
- Root: \`$ROOT\`
- Remote: \`$REMOTE\`
- Branch: \`$BRANCH\`
- Mode: \`$MODE\`
- Status: running

EOF

exec > >(tee -a "$RUN_LOG") 2>&1

FINALIZED=0

finalize_run_log() {
  local status="$1"
  {
    printf '\n## Wrapper Result\n\n'
    printf -- '- Finished at: %s\n' "$(date -Iseconds)"
    printf -- '- Exit code: `%s`\n' "$status"
    if [[ "$status" -eq 0 ]]; then
      printf -- '- Status: completed\n'
    else
      printf -- '- Status: blocked\n'
    fi
  } >>"$RUN_LOG"
  FINALIZED=1
}

on_exit() {
  local status=$?
  if [[ "$FINALIZED" -eq 0 ]]; then
    finalize_run_log "$status"
  fi
}
trap on_exit EXIT

log() {
  printf '[job-search-sync] %s\n' "$*" >&2
}

skip_if_runtime_lock_active() {
  local lock_name="$1"
  local lock_output
  local lock_status

  set +e
  lock_output="$(python3 tools/job-search-runtime/job_search_runtime.py lock-status --lock-name "$lock_name" --active-exit-code 75 2>&1)"
  lock_status=$?
  set -e

  if [[ "$lock_status" -eq 75 ]]; then
    log "skipped: runtime lock is active: $lock_name"
    printf '    %s\n' "$lock_output"
    {
      printf '\n## Sync Skip\n\n'
      printf -- '- Reason: runtime lock `%s` is active; avoiding partial artifact commit.\n' "$lock_name"
      printf '    %s\n' "$lock_output"
    } >>"$RUN_LOG"
    finalize_run_log 0
    exit 0
  fi

  if [[ "$lock_status" -ne 0 ]]; then
    log "blocked: failed to inspect runtime lock: $lock_name"
    printf '    %s\n' "$lock_output"
    exit "$lock_status"
  fi
}

changed_allowed_paths() {
  git status --porcelain -- \
    automation/state \
    inbox/processed \
    tasks/active \
    tasks/waiting \
    personal-projects/personal-brand/workspace/job-intake
}

changed_disallowed_paths() {
  git status --porcelain \
    ':!automation/state' \
    ':!inbox/processed' \
    ':!tasks/active' \
    ':!tasks/waiting' \
    ':!personal-projects/personal-brand/workspace/job-intake'
}

log "root=$ROOT remote=$REMOTE branch=$BRANCH mode=$MODE"

if [[ "$MODE" != "dry-run" && "$MODE" != "apply" ]]; then
  log "PERSONAL_OFFICE_SYNC_MODE must be dry-run or apply"
  exit 2
fi

python3 tools/job-search-runtime/job_search_runtime.py init
python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state

skip_if_runtime_lock_active "pi-job-search-gmail-monitor"
skip_if_runtime_lock_active "pi-job-search-telegram-intake"

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if [[ "$MODE" == "apply" ]]; then
    log "pulling $REMOTE/$BRANCH"
    git pull --ff-only "$REMOTE" "$BRANCH"
  else
    log "dry-run: skipping git pull"
  fi
else
  log "not inside a git worktree; skipping git sync"
fi

if [[ -n "$RUN_CMD" ]]; then
  log "running command: $RUN_CMD"
  bash -lc "$RUN_CMD"
else
  log "no run command provided; initialized runtime state only"
fi

if [[ -d memory/protocol && -x tools/memory-os/memory_os.py ]]; then
  if [[ -n "$(git status --porcelain -- memory tools/personal-office-owner-operator-pack 2>/dev/null || true)" ]]; then
    log "memory files changed; running Memory OS gates"
    python3 tools/memory-os/memory_os.py validate
    python3 tools/memory-os/memory_os.py graph-check
    python3 tools/memory-os/memory_os.py stale
  fi
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  log "not inside a git worktree; done"
  exit 0
fi

if [[ -n "$(changed_disallowed_paths)" ]]; then
  log "blocked: disallowed path changes detected"
  changed_disallowed_paths >&2
  exit 3
fi

if [[ -z "$(changed_allowed_paths)" ]]; then
  log "no allowed path changes to sync"
  finalize_run_log 0
  exit 0
fi

log "allowed changes:"
changed_allowed_paths >&2

if [[ "$MODE" == "dry-run" ]]; then
  log "dry-run: not committing or pushing"
  finalize_run_log 0
  exit 0
fi

log "committing and pushing allowed changes"
finalize_run_log 0

git add \
  automation/state \
  inbox/processed \
  tasks/active \
  tasks/waiting \
  personal-projects/personal-brand/workspace/job-intake

git commit -m "job-search: sync pi runtime artifacts" >/tmp/personal-office-job-search-sync-git.log 2>&1
git push "$REMOTE" "HEAD:$BRANCH" >>/tmp/personal-office-job-search-sync-git.log 2>&1
