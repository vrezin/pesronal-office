# Raspberry Pi OpenClaw Cookbook Sync Manifest

This manifest defines the first safe Personal Office payload for the Raspberry Pi OpenClaw agent.

## Principle

Sync cookbooks, not raw life data.

The Pi-side agent should learn how to operate Personal Office from routing rules, playbooks, and skills. It should not start with unrestricted access to personal records, finance, contacts, raw inbox, memory stores, or company internals.

## Destination

```text
/home/openclaw/personal-office-agent/cookbooks/personal-office/
```

## Include

```text
AGENTS.md
wiki/README.md
wiki/maps/
wiki/playbooks/
secretaries/
.codex/skills/
tools/README.md
tools/raspberrypi-openclaw/
tools/memory-os/
tools/personal-office-owner-operator-pack/
memory/README.md
memory/protocol/
memory/templates/
memory/retrieval/index.md
memory/retrieval/search-rules.md
memory/knowledge-graph/nodes.jsonl
memory/knowledge-graph/edges.jsonl
```

## Exclude

```text
finance/
people/
life/
inbox/
companies/
personal-projects/
memory/short-term/
memory/episodic/
memory/semantic/
memory/entities/
memory/long-term/
calendar/
tasks/
tools/*/.env
tools/*/.venv
tools/linkedin-mcp/profile/
tools/linkedin-mcp/cookies.json
tools/linkedin-mcp/.run/
.git/
.cache/
.idea/
```

## Agent Behavior

The agent may:

- read the cookbook bundle;
- use the shared `wiki/`, `memory/protocol/`, `tools/memory-os/`, and `tools/personal-office-owner-operator-pack/` layers as common Personal Office routing and validation infrastructure across agents;
- follow `tools/raspberrypi-openclaw/personal-office-agent-cookbook.md` as the Pi-side operating entrypoint;
- use `tools/raspberrypi-openclaw/openclaw-personal-office-operating-model.md` as the consolidated research and operating model;
- use `tools/raspberrypi-openclaw/personal-office-context-pack.md` as the minimal non-sensitive world map before testing real intake;
- use `tools/raspberrypi-openclaw/openclaw-capabilities-and-best-practices.md` for OpenClaw multi-agent, channel, model, provider, workspace and best-practice decisions;
- use `tools/raspberrypi-openclaw/personal-office-openclaw-decomposition.md` as the to-be component/workflow/skill map;
- explain how a new input should be routed;
- propose the narrow source files needed for a task;
- ask for a specific context handoff when needed;
- prepare changes as patches or instructions before touching live Personal Office artifacts.

The agent must not:

- assume the cookbook bundle contains current personal facts;
- treat Memory OS as raw personal memory or as a replacement for domain source artifacts;
- infer sensitive facts from missing data;
- copy broad Personal Office directories onto the Pi;
- use credentials, cookies, browser profiles, finance tokens, or external-account sessions unless explicitly approved.

## Next Implementation Step

Remove or quarantine the accidental broad copy at:

```text
/home/openclaw/personal-office-agent/workspaces/personal-office/
```

Then sync only the include list to the cookbook destination.
