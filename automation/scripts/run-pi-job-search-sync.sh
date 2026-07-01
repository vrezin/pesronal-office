#!/usr/bin/env bash
set -euo pipefail

ROOT="${PERSONAL_OFFICE_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
REMOTE="${PERSONAL_OFFICE_SYNC_REMOTE:-origin}"
BRANCH="${PERSONAL_OFFICE_SYNC_BRANCH:-main}"
MODE="${PERSONAL_OFFICE_SYNC_MODE:-dry-run}"
RUN_CMD="${*:-}"

cd "$ROOT"

log() {
  printf '[job-search-sync] %s\n' "$*" >&2
}

changed_allowed_paths() {
  git status --porcelain -- \
    automation/runs \
    automation/state \
    inbox/processed \
    tasks/active \
    tasks/waiting \
    personal-projects/personal-brand/workspace/job-intake
}

changed_disallowed_paths() {
  git status --porcelain \
    ':!automation/runs' \
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
  exit 0
fi

log "allowed changes:"
changed_allowed_paths >&2

if [[ "$MODE" == "dry-run" ]]; then
  log "dry-run: not committing or pushing"
  exit 0
fi

git add \
  automation/runs \
  automation/state \
  inbox/processed \
  tasks/active \
  tasks/waiting \
  personal-projects/personal-brand/workspace/job-intake

git commit -m "job-search: sync pi runtime artifacts"
git push "$REMOTE" "HEAD:$BRANCH"

log "sync complete"
