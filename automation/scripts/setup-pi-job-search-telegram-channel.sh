#!/usr/bin/env bash
set -euo pipefail

CONFIG_DIR="${PERSONAL_OFFICE_CONFIG_DIR:-$HOME/.config/personal-office}"
OPENCLAW_BIN="${OPENCLAW_BIN:-/home/openclaw/.local/bin/openclaw}"
ENV_FILE="${JOB_SEARCH_TELEGRAM_ENV_FILE:-$CONFIG_DIR/job-search-telegram.env}"
TOKEN_FILE="${OPENCLAW_TELEGRAM_BOT_TOKEN_FILE:-}"
TOKEN="${OPENCLAW_TELEGRAM_BOT_TOKEN:-}"
TARGET="${TELEGRAM_JOB_SEARCH_TARGET:-}"
ACCOUNT="${TELEGRAM_JOB_SEARCH_ACCOUNT:-job-search-telegram}"

mkdir -p "$CONFIG_DIR"
chmod 700 "$CONFIG_DIR"

if [[ -z "$TOKEN" && -n "$TOKEN_FILE" ]]; then
  TOKEN="$(tr -d '\r\n' <"$TOKEN_FILE")"
fi

if [[ -z "$TOKEN" ]]; then
  printf 'OPENCLAW_TELEGRAM_BOT_TOKEN or OPENCLAW_TELEGRAM_BOT_TOKEN_FILE is required.\n' >&2
  exit 2
fi

if [[ -z "$TARGET" ]]; then
  printf 'TELEGRAM_JOB_SEARCH_TARGET is required. Use your Telegram chat id or @username.\n' >&2
  exit 2
fi

"$OPENCLAW_BIN" channels add \
  --channel telegram \
  --account "$ACCOUNT" \
  --name "Personal Office Job Search" \
  --token "$TOKEN"

umask 077
cat >"$ENV_FILE" <<EOF
TELEGRAM_JOB_SEARCH_ACCOUNT=$ACCOUNT
TELEGRAM_JOB_SEARCH_TARGET=$TARGET
EOF

printf 'Configured OpenClaw Telegram account `%s`.\n' "$ACCOUNT"
printf 'Wrote wrapper env file: %s\n' "$ENV_FILE"
printf 'Token was not written to the Personal Office repo.\n'
