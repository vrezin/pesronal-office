# PO Path Validator Slimming Test

- Date: 2026-06-25
- Host: `raspberrypi-codex`
- Purpose: compare the normal `default` Personal Office router with a slimmer OpenClaw utility agent for path validation.
- Baseline session: `agent:default:yuliya-path-validation`
- Slim agent: `po-path-validator`
- Slim sessions:
  - `agent:po-path-validator:yuliya-path-validation-slim`
  - `agent:po-path-validator:yuliya-path-validation-slim-v2`
  - `agent:po-path-validator:yuliya-path-validation-slim-v3`
  - `agent:po-path-validator:yuliya-path-validation-slim-v4-minimal-tools`
  - `agent:po-path-validator:yuliya-path-validation-slim-v5-context-never`

## Setup

Created a dedicated OpenClaw agent:

```json
{
  "id": "po-path-validator",
  "name": "po-path-validator",
  "workspace": "/home/openclaw/personal-office-agent/openclaw-workspaces/po-path-validator",
  "agentDir": "/home/openclaw/personal-office-agent/openclaw-agents/po-path-validator",
  "model": "openai/gpt-5.5",
  "default": false,
  "skills": [],
  "memorySearch": { "enabled": false },
  "bootstrapTotalMaxChars": 2500,
  "bootstrapMaxChars": 2500
}
```

Workspace intent:

- only a narrow `AGENTS.md`;
- one explicit path-validation handoff file;
- no raw Personal Office data;
- no channel bindings;
- not the default route.

Authentication:

- device-code login was required for the new agent;
- OAuth profile now exists under `~/personal-office-agent/openclaw-agents/po-path-validator/openclaw-agent.sqlite`;
- auth expires `2026-07-05T10:26:28.070Z`.

Config safety:

- backup created before changes: `/home/openclaw/.openclaw/openclaw.json.backup-2026-06-25-before-po-path-validator`;
- `tools.profile` was temporarily changed to `minimal` for v4 and then restored to `coding`;
- final checked `tools.profile`: `coding`.

## Baseline: Default Router

Session: `agent:default:yuliya-path-validation`

```yaml
inputTokens: 1362
outputTokens: 1030
cacheRead: 17792
agentMetaTotal: 19154
runtimeMs: 35955
systemPromptChars: 13938
skillsPromptChars: 5106
skillsCount: 14
toolsCount: 18
```

Injected workspace files:

- `AGENTS.md`
- `SOUL.md`
- `TOOLS.md`
- `IDENTITY.md`
- `USER.md`
- `HEARTBEAT.md` detected, not injected

## Slim V1: New Agent, No Skills, Memory Search Off

Session: `agent:po-path-validator:yuliya-path-validation-slim`

```yaml
inputTokens: 1140
outputTokens: 1296
cacheRead: 15232
agentMetaTotalFromRun: 17668
promptTokensFromRun: 16372
runtimeMs: 50108
systemPromptChars: 5870
skillsPromptChars: 0
skillsCount: 0
toolsCount: 16
```

What improved:

- removed all 14 skill prompt entries;
- removed `memory_search` and `memory_get`;
- system prompt chars dropped from `13938` to `5870`.

What remained:

- OpenClaw still injected/restored `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, and `HEARTBEAT.md`;
- `tools.profile = coding` still exposed 16 tools.

## Slim V2/V3: Remove Extra Bootstrap Files

Extra bootstrap files were renamed out of the workspace, then the agent was run before and after Gateway restart.

Finding:

- OpenClaw restored `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, and `HEARTBEAT.md` automatically.
- Removing files from the workspace is not a durable slimming mechanism.

Representative v3 metrics:

```yaml
inputTokens: 1077
outputTokens: 1154
cacheRead: 15744
promptTokensFromRun: 16821
runtimeMs: 40602
systemPromptChars: 5870
skillsPromptChars: 0
skillsCount: 0
toolsCount: 16
```

Quality note:

- v3 made one worse path suggestion: it proposed `personal-projects/personal-brand/setronica-publicity-guardrail.md` instead of keeping route-only.
- This suggests that aggressive slimming must preserve exact path-validation instructions, not just reduce context.

## Slim V4: Temporary Global `tools.profile = minimal`

For this test only:

1. Set `tools.profile` to `minimal`.
2. Restarted Gateway.
3. Ran the same slim-agent path-validation prompt.
4. Restored `tools.profile` to `coding`.
5. Restarted Gateway again.

Session: `agent:po-path-validator:yuliya-path-validation-slim-v4-minimal-tools`

Run response metrics:

```yaml
inputTokens: 13552
outputTokens: 1444
cacheRead: 0
agentMetaTotalFromRun: 14996
promptTokensFromRun: 13552
runtimeMs: 41470
systemPromptChars: 3557
skillsPromptChars: 0
skillsCount: 0
toolsCount: 1
tools:
  - session_status
```

What improved:

- tool exposure dropped from 16 tools to 1 tool;
- system prompt chars dropped from `5870` to `3557`;
- total run usage dropped from baseline `19154` to `14996`;
- no skills were injected.

What did not improve enough:

- runtime stayed around 40 seconds;
- identity/runtime files still existed and `SOUL.md` still contributed `1704` injected chars;
- `tools.profile` is global, so using `minimal` affects the whole Gateway unless there is a per-provider/sender policy that fits the deployment.

## Quality Comparison

All slim runs correctly identified the invalid path:

- `content/personal-brand/setronica-publicity-guardrail.md`

Best behavior:

- baseline and v4 kept the correction at route level: `personal-projects/personal-brand/`.

Weaker behavior:

- v3 invented a deeper filename under `personal-projects/personal-brand/`.

Setronica handoff behavior:

- Some runs marked `<setronica-root>` paths as `yes` but blocked until approval.
- Some runs marked them as `partial`.
- The safer contract is `partial` or `handoff_envelope_only` until explicit user approval.

## Slim V5: `contextInjection = never`

Session: `agent:po-path-validator:yuliya-path-validation-slim-v5-context-never`

Run response metrics:

```yaml
inputTokens: 1065
outputTokens: 1422
cacheRead: 15744
agentMetaTotalFromRun: 18231
promptTokensFromRun: 16809
runtimeMs: 45981
systemPromptChars: 5870
projectContextChars: 0
nonProjectContextChars: 5870
skillsPromptChars: 0
skillsCount: 0
toolsCount: 16
```

What this proved:

- `contextInjection: "never"` did not remove the workspace bootstrap files from the prompt report;
- `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, and `HEARTBEAT.md` were still injected;
- the hidden overhead is therefore not only project-context injection; the agent still carries its workspace identity/runtime layer;
- compared with the v4 minimal-tools run, this version is heavier mainly because tool exposure returned to `tools.profile = coding`.

## Conclusions

The first real slimming win is per-agent `skills: []`.

The second real slimming win is tool profile reduction, but OpenClaw currently applies `tools.profile` globally in this setup.

The harder remaining issue is OpenClaw's agent workspace identity/runtime files:

- `SOUL.md`;
- `TOOLS.md`;
- `IDENTITY.md`;
- `USER.md`;
- `HEARTBEAT.md`;
- sometimes `BOOTSTRAP.md`.

OpenClaw restores these files automatically, so deleting them is not enough. A production Personal Office local install needs a supported way to declare utility agents that do not carry personality/identity/runtime prose for mechanical validation tasks.

`contextInjection: "never"` on its own does not solve that problem; it appears to stop project-context injection, not the bootstrap/workspace layer.

## Product Implication

For Personal Office, there should be at least two classes of agents:

- owner-facing agents: richer identity/context is acceptable;
- utility agents: no personality, no broad skills, minimal tools, explicit input files only.

The `po-path-validator` experiment proves the architecture direction, but also shows that OpenClaw needs config-level support for utility-agent slim prompts before this is truly production-clean.

## Next Experiment

Test config-level context slimming:

- a much lower `bootstrapTotalMaxChars`;
- `agents.defaults.skills: []` plus explicit skills only where needed;
- investigate whether `tools.byProvider`, `tools.toolsBySender`, or separate Gateway/profile can give per-agent tool profiles instead of global `tools.profile`;
- look for a supported utility-agent mode that suppresses the bootstrap/workspace prose entirely.
