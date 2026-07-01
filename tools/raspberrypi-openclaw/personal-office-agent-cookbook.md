# Personal Office Agent Cookbook For OpenClaw

Use this cookbook when OpenClaw runs on the Raspberry Pi and needs to help manage Personal Office.

## Operating Model

The Pi-side agent starts from protocol, not from raw data.

It should learn:

- how Personal Office routes incoming information;
- where durable outcomes belong;
- which local skills and playbooks define each domain;
- how to ask for narrow context before touching sensitive artifacts.

It should not begin with a full copy of Personal Office records.

## Start Here

Read in this order:

1. `AGENTS.md`
2. `wiki/README.md`
3. `secretaries/routing-map.md`
4. `tools/raspberrypi-openclaw/personal-office-context-pack.md`
5. `tools/raspberrypi-openclaw/openclaw-personal-office-operating-model.md`
6. The smallest relevant file from `wiki/maps/`
7. The matching `SKILL.md` from `.codex/skills/`
8. The matching procedure from `wiki/playbooks/`

## Default Rule

If a request contains a decision, promise, deadline, meeting, amount of money, obligation, risk, opportunity, person, or next step, the answer should produce or update an artifact in the source Personal Office repository.

On the Pi, do not invent the missing source artifact. Ask for a narrow context handoff or prepare an explicit patch/request.

## Allowed Without Extra Context

The agent may:

- explain routing;
- identify which source files are needed;
- draft a structured intake note from user-provided text;
- draft a task/update as a patch;
- propose a safe sync scope;
- inspect OpenClaw local status and cookbook files.

## Requires Narrow Context Handoff

Ask before reading or changing:

- finance records;
- people/contact dossiers;
- health/lifestyle facts;
- raw inbox;
- company/project internals;
- calendar/meeting history;
- memory stores;
- external-account tool state.

## Never Do By Default

- Do not copy broad Personal Office directories onto the Pi.
- Do not copy cookies, browser profiles, SSH keys, API keys, `.env` files, or finance tokens.
- Do not expose OpenClaw Gateway outside loopback/local network without a separate security decision.
- Do not treat cookbook files as current personal facts.

## First Useful Agent Behavior

For a new user request, the Pi-side agent should answer:

1. Which cookbook route applies.
2. Which exact source context is needed, if any.
3. What artifact would be created or updated.
4. Whether it can prepare a patch from the user-provided input alone.
