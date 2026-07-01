# Telegram Job Search Setup

- Date: 2026-07-01
- Host: Raspberry Pi
- User: `openclaw`
- Repo: `/home/openclaw/personal-office-agent/personal-office`
- Status: setup runbook; channel not configured yet

## Goal

Enable the job-search contour to receive ad-hoc vacancy links/JDs from Telegram and send concise decision packets back to the same Telegram target.

## Secret Boundary

Do not commit Telegram bot tokens, chat ids, or generated OpenClaw auth state.

The repository contains only:

- wrapper scripts;
- prompts;
- systemd templates;
- run logs;
- non-secret setup instructions.

Local Pi secrets/config live outside Git:

```text
/home/openclaw/.config/personal-office/job-search-telegram.env
/home/openclaw/.config/personal-office/secrets/telegram-job-search-bot-token.txt
```

## Setup

Run on the Raspberry Pi as `openclaw`.

Required inputs:

- `OPENCLAW_TELEGRAM_BOT_TOKEN` or `OPENCLAW_TELEGRAM_BOT_TOKEN_FILE`;
- `TELEGRAM_JOB_SEARCH_TARGET`, usually your Telegram chat id or allowed target.

Recommended token location:

```bash
mkdir -p /home/openclaw/.config/personal-office/secrets
chmod 700 /home/openclaw/.config/personal-office /home/openclaw/.config/personal-office/secrets
printf '%s\n' '<bot-token-from-botfather>' > /home/openclaw/.config/personal-office/secrets/telegram-job-search-bot-token.txt
chmod 600 /home/openclaw/.config/personal-office/secrets/telegram-job-search-bot-token.txt
```

Command:

```bash
cd /home/openclaw/personal-office-agent/personal-office
OPENCLAW_TELEGRAM_BOT_TOKEN_FILE=/home/openclaw/.config/personal-office/secrets/telegram-job-search-bot-token.txt \
TELEGRAM_JOB_SEARCH_TARGET=<chat-id-or-username> \
automation/scripts/setup-pi-job-search-telegram-channel.sh
```

The script runs:

```bash
openclaw plugins enable telegram
openclaw channels add --channel telegram --account job-search-telegram --token-file <token-file>
```

and writes the non-token wrapper env file.

## Verify

```bash
openclaw channels list
openclaw channels status
source /home/openclaw/.config/personal-office/job-search-telegram.env
automation/scripts/run-pi-job-search-telegram-intake.sh
```

Expected before Telegram is configured:

- wrapper writes a blocked run log;
- no Telegram reads are attempted if `TELEGRAM_JOB_SEARCH_TARGET` is missing.

Expected after Telegram is configured:

- wrapper reads recent Telegram messages through OpenClaw;
- each Telegram update id is checked through SQLite before processing;
- actionable inputs create/update job-intake artifacts;
- bot reply follows the Telegram output contract in `automation/prompts/pi-job-search-telegram-intake.md`.

## Timer

Templates exist but should not be enabled until the channel and target are configured:

```text
automation/systemd/personal-office-pi-job-search-telegram-intake.service
automation/systemd/personal-office-pi-job-search-telegram-intake.timer
```

Enable manually after setup:

```bash
mkdir -p ~/.config/systemd/user
cp automation/systemd/personal-office-pi-job-search-telegram-intake.* ~/.config/systemd/user/
XDG_RUNTIME_DIR=/run/user/1001 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1001/bus systemctl --user daemon-reload
XDG_RUNTIME_DIR=/run/user/1001 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1001/bus systemctl --user enable --now personal-office-pi-job-search-telegram-intake.timer
```
