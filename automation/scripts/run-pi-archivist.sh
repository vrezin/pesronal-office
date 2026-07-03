#!/usr/bin/env bash
set -euo pipefail

ROOT="${PERSONAL_OFFICE_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
MODE="${PERSONAL_OFFICE_ARCHIVIST_MODE:-dry-run}"

cd "$ROOT"

mkdir -p automation/runs automation/state

if [[ "$MODE" != "dry-run" && "$MODE" != "apply" ]]; then
  printf 'PERSONAL_OFFICE_ARCHIVIST_MODE must be dry-run or apply\n' >&2
  exit 2
fi

python3 tools/personal-office-archivist/archivist.py --mode "$MODE"
