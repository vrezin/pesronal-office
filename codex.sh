#!/usr/bin/env bash
set -euo pipefail

exec codex --add-dir "$HOME/projects/aistudio" --add-dir "$HOME/projects/fincom" --add-dir "$HOME/projects/setronica" "$@"
