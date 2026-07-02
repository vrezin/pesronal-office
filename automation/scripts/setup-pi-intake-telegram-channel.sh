#!/usr/bin/env bash
set -euo pipefail

CONFIG_DIR="${PERSONAL_OFFICE_CONFIG_DIR:-$HOME/.config/personal-office}"
OPENCLAW_BIN="${OPENCLAW_BIN:-/home/openclaw/.local/bin/openclaw}"
ENV_FILE="${INTAKE_TELEGRAM_ENV_FILE:-$CONFIG_DIR/intake-telegram.env}"
TOKEN_FILE="${OPENCLAW_TELEGRAM_BOT_TOKEN_FILE:-}"
TOKEN="${OPENCLAW_TELEGRAM_BOT_TOKEN:-}"
TARGET="${TELEGRAM_INTAKE_TARGET:-}"
ACCOUNT="${TELEGRAM_INTAKE_ACCOUNT:-personal-office-intake-telegram}"
AGENT="${OPENCLAW_INTAKE_AGENT:-intake}"

mkdir -p "$CONFIG_DIR"
chmod 700 "$CONFIG_DIR"

if [[ -z "$TOKEN" && -n "$TOKEN_FILE" && ! -r "$TOKEN_FILE" ]]; then
  printf 'OPENCLAW_TELEGRAM_BOT_TOKEN_FILE is not readable: %s\n' "$TOKEN_FILE" >&2
  exit 2
fi

if [[ -z "$TOKEN" && -z "$TOKEN_FILE" ]]; then
  printf 'OPENCLAW_TELEGRAM_BOT_TOKEN or OPENCLAW_TELEGRAM_BOT_TOKEN_FILE is required.\n' >&2
  exit 2
fi

if [[ -z "$TARGET" ]]; then
  printf 'TELEGRAM_INTAKE_TARGET is required. Use your Telegram chat id or @username.\n' >&2
  exit 2
fi

"$OPENCLAW_BIN" plugins enable telegram

if [[ -n "$TOKEN_FILE" ]]; then
  "$OPENCLAW_BIN" channels add \
    --channel telegram \
    --account "$ACCOUNT" \
    --name "Personal Office Intake" \
    --token-file "$TOKEN_FILE"
else
  "$OPENCLAW_BIN" channels add \
    --channel telegram \
    --account "$ACCOUNT" \
    --name "Personal Office Intake" \
    --token "$TOKEN"
fi

"$OPENCLAW_BIN" agents bind --agent "$AGENT" --bind "telegram:$ACCOUNT"

umask 077
cat >"$ENV_FILE" <<EOF
TELEGRAM_INTAKE_ACCOUNT=$ACCOUNT
TELEGRAM_INTAKE_TARGET=$TARGET
OPENCLAW_INTAKE_AGENT=$AGENT
EOF

printf 'Configured OpenClaw Telegram account `%s`.\n' "$ACCOUNT"
printf 'Bound Telegram account `%s` to agent `%s`.\n' "$ACCOUNT" "$AGENT"
printf 'Wrote wrapper env file: %s\n' "$ENV_FILE"
printf 'Token was not written to the Personal Office repo.\n'
