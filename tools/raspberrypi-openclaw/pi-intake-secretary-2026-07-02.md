# Pi Intake Secretary

- Date: 2026-07-02
- Status: Target + setup scaffold
- Runtime target: Raspberry Pi OpenClaw
- Proposed agent: `intake`
- Proposed Telegram account: `personal-office-intake-telegram`

## Decision

The Pi-primary Personal Office should have a general `intake` secretary for
incoming non-domain-specific mess.

`job-search` remains a specialized downstream contour. It should not become the
universal router for life, finance, company, calendar, and project inputs.

## Role

The intake secretary is the first routing layer:

1. receive raw input from Telegram/Gmail/manual messages;
2. classify it using `secretaries/routing-map.md`;
3. create the smallest durable trace;
4. update the owning artifact or create a domain handoff;
5. create active/waiting tasks when needed;
6. ask a clarification question when the route is unsafe to guess.

## Boundary

The intake secretary must not own every domain.

Examples:

- vacancies, HH, LinkedIn, CV, cover letters -> hand off to `job-search`;
- meetings, interview prep, reminders -> Calendar secretary route;
- money, debts, assets, payments -> Finance secretary route;
- AI Studio / Fincom / Setronica -> Company secretary route;
- weekly cleanup and repeated noise -> Archivist route.

## Telegram Account Strategy

Do not rebind the existing `job-search-telegram` account yet.

That account is already proven for the job-search contour. Rebinding it to a
general intake router would risk breaking the working vacancy workflow.

Safer first step:

- create a separate Telegram bot/account for general intake;
- configure it as `personal-office-intake-telegram`;
- bind it to OpenClaw agent `intake`;
- keep `job-search-telegram` bound to `job-search`.

Later, if router quality is good, one Telegram bot can become the only public
front door and delegate job-search inputs downstream.

## Repo Artifacts Added

- `secretaries/operating-model.md` - secretary roles and composition model.
- `automation/prompts/pi-intake-secretary.md` - Pi intake prompt.
- `automation/scripts/setup-pi-intake-telegram-channel.sh` - secret-free setup
  helper for a separate intake Telegram account.
- `tools/raspberrypi-openclaw/intake-agent-workspace-AGENTS.md` - bootstrap
  instructions copied to the OpenClaw `intake` workspace.

## Runtime Evidence

2026-07-02:

- OpenClaw agent `intake` was created on the Pi.
- Workspace:
  `/home/openclaw/personal-office-agent/openclaw-workspaces/intake`.
- Agent dir:
  `/home/openclaw/personal-office-agent/openclaw-agents/intake`.
- Model: `openai/gpt-5.5`.
- Routing rules: `0` until a separate Telegram account/bot is configured.

## Setup Sketch

Create or choose a Telegram bot for general Personal Office intake, then on the
Pi:

```bash
printf '%s\n' '<bot-token-from-botfather>' > /home/openclaw/.config/personal-office/secrets/telegram-intake-bot-token.txt
chmod 600 /home/openclaw/.config/personal-office/secrets/telegram-intake-bot-token.txt

OPENCLAW_TELEGRAM_BOT_TOKEN_FILE=/home/openclaw/.config/personal-office/secrets/telegram-intake-bot-token.txt \
TELEGRAM_INTAKE_TARGET=<owner-chat-id> \
automation/scripts/setup-pi-intake-telegram-channel.sh
```

Expected binding:

```text
intake <- telegram accountId=personal-office-intake-telegram
job-search <- telegram accountId=job-search-telegram
```

## Acceptance

First slice is done when:

- OpenClaw has an `intake` agent;
- Telegram account `personal-office-intake-telegram` is configured and bound to
  `intake`;
- a manual Telegram message such as "remind me tomorrow to call X" creates or
  updates the correct repo artifact;
- the bot replies with route, artifact path, and next action;
- `job-search-telegram` still routes vacancy links to `job-search`.
