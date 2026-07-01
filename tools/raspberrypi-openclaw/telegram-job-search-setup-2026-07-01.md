# Telegram Job Search Setup

- Date: 2026-07-01
- Host: Raspberry Pi
- User: `openclaw`
- Repo: `/home/openclaw/personal-office-agent/personal-office`
- Status: Telegram channel configured on 2026-07-01; bot probe works

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

OpenClaw plugin allowlist must include Telegram. Check:

```bash
openclaw config get plugins.allow
```

If it only contains `codex`, allow Telegram:

```bash
openclaw config set plugins.allow '["codex","telegram"]' --strict-json
```

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

Bind this Telegram account to the dedicated job-search agent:

```bash
openclaw agents bind --agent job-search --bind telegram:job-search-telegram
openclaw gateway restart
openclaw agents bindings
```

Expected binding:

```text
job-search <- telegram accountId=job-search-telegram
```

Approve the Telegram sender before expecting normal agent routing. The first DM
from a new Telegram user is treated as a pairing request:

```bash
openclaw pairing list --channel telegram
openclaw pairing approve --channel telegram --account job-search-telegram --notify <PAIRING_CODE>
openclaw config get commands.ownerAllowFrom
```

Expected owner allow entry:

```text
telegram:<telegram-user-id>
```

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

Observed on 2026-07-01:

```text
Telegram job-search-telegram: installed, configured, enabled, token=tokenFile
Probe: running, mode=polling, bot:@adreclawbot, works
Routing: job-search <- telegram accountId=job-search-telegram
Pairing approved: telegram:113174019
```

OpenClaw 2026.6.10 does not support reading Telegram history through:

```bash
openclaw message read --channel telegram
```

It returns `Unsupported Telegram action: read`. Inbound Telegram processing should happen through Gateway routing into the `job-search` agent.

## E2E Smoke

Observed on 2026-07-01:

- Input: Telegram DM from approved sender with LinkedIn job `4434492291`.
- Route: `telegram:job-search-telegram` -> `job-search`.
- Enrichment: LinkedIn MCP plus Xapo Greenhouse.
- Created artifacts:
  - `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-01-xapo-bank-head-of-engineering.md`;
  - `personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-01-xapo-bank-head-of-engineering-analysis.md`;
  - updated `personal-projects/personal-brand/workspace/job-intake/INDEX.md`;
  - updated `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`.
- Telegram reply sent: `messageId=352`.

## Timer

Templates exist but should not be enabled until the wrapper is rewritten for Gateway event logs or another supported inbound source:

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
