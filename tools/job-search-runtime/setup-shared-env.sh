#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VENV="${PERSONAL_OFFICE_JOB_SEARCH_VENV:-$ROOT/.runtime/job-search-venv}"
UV_BIN="${UV_BIN:-uv}"
PYTHON_VERSION="${PERSONAL_OFFICE_JOB_SEARCH_PYTHON:-3.13}"
PYTHON_BIN="${PERSONAL_OFFICE_JOB_SEARCH_SYSTEM_PYTHON:-python3}"
UV_CACHE_DIR="${UV_CACHE_DIR:-$ROOT/.cache/uv}"

cd "$ROOT"
mkdir -p "$(dirname "$VENV")" "$UV_CACHE_DIR"

export UV_CACHE_DIR

if command -v "$UV_BIN" >/dev/null 2>&1; then
  "$UV_BIN" venv --python "$PYTHON_VERSION" "$VENV"
  "$UV_BIN" pip install --python "$VENV/bin/python" -r "$SCRIPT_DIR/shared-requirements.txt"

  if [[ -f "$ROOT/tools/headhunter-web-mcp/pyproject.toml" ]]; then
    UV_PROJECT_ENVIRONMENT="$VENV" "$UV_BIN" sync --inexact --directory "$ROOT/tools/headhunter-web-mcp"
  fi
else
  "$PYTHON_BIN" -m venv "$VENV"
  "$VENV/bin/python" -m pip install --upgrade pip
  "$VENV/bin/python" -m pip install -r "$SCRIPT_DIR/shared-requirements.txt"
  if [[ -f "$ROOT/tools/headhunter-web-mcp/pyproject.toml" ]]; then
    "$VENV/bin/python" -m pip install -e "$ROOT/tools/headhunter-web-mcp"
  fi
fi

"$VENV/bin/python" - <<'PY'
import importlib.util
import sys

required = [
    "linkedin_mcp_server",
    "mcp",
    "playwright",
    "pydantic",
    "httpx",
]
missing = [name for name in required if importlib.util.find_spec(name) is None]
if missing:
    print(f"Missing shared runtime modules: {', '.join(missing)}", file=sys.stderr)
    raise SystemExit(1)
from pathlib import Path

commands = ["linkedin-mcp-server"]
root = Path.cwd()
if (root / "tools/headhunter-web-mcp/pyproject.toml").exists():
    commands.append("headhunter-web-mcp")
for command in commands:
    if not (sys.prefix and Path(sys.prefix, "bin", command).exists()):
        print(f"Missing shared runtime command: {command}", file=sys.stderr)
        raise SystemExit(1)
print("Shared job-search runtime is ready.")
PY
