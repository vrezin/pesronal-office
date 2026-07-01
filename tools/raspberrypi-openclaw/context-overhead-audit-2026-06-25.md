# OpenClaw Context Overhead Audit

- Date: 2026-06-25
- Host: `raspberrypi-codex`
- Agent audited: `default` / `po-router-default`
- Workspace: `/home/openclaw/personal-office-agent/openclaw-workspaces/po-router`
- Main inspected session: `agent:default:yuliya-path-validation`
- Session id: `0bd1fd0e-b07f-4203-9b39-37cc7eb06269`

## Why This Audit Exists

The path-validation task was intentionally tiny: read one narrow routing excerpt, validate proposed paths, do not re-analyze the meeting, and do not apply files.

The result was behaviorally good, but token usage showed a heavy baseline. This audit records what OpenClaw actually injected.

## Config Finding

Sanitized `/home/openclaw/.openclaw/openclaw.json` shows:

```json
{
  "tools": {
    "profile": "coding"
  },
  "plugins": {
    "allow": ["codex"]
  },
  "agents": {
    "defaults": {
      "workspace": "/home/openclaw/personal-office-agent/openclaw-workspaces/default",
      "model": {
        "primary": "openai/gpt-5.5"
      }
    },
    "list": [
      {
        "id": "default",
        "name": "po-router-default",
        "default": true,
        "workspace": "/home/openclaw/personal-office-agent/openclaw-workspaces/po-router",
        "agentDir": "/home/openclaw/personal-office-agent/openclaw-agents/default",
        "model": "openai/gpt-5.5"
      },
      {
        "id": "po-router",
        "name": "po-router",
        "workspace": "/home/openclaw/personal-office-agent/openclaw-workspaces/po-router",
        "agentDir": "/home/openclaw/personal-office-agent/openclaw-agents/po-router",
        "model": "openai/gpt-5.5"
      }
    ]
  }
}
```

No per-agent skill allowlist is configured for `default` or `po-router`.

## Main Session Usage

For `agent:default:yuliya-path-validation`:

```yaml
inputTokens: 1362
outputTokens: 1030
cacheRead: 17792
cacheWrite: 0
totalTokens: 19154
runtimeMs: 35955
contextTokens: 272000
systemPromptChars: 13938
projectContextChars: 0
nonProjectContextChars: 13938
```

Interpretation:

- The task itself was compact.
- Most carried context was cached baseline/harness context.
- The run still took about 36 seconds.

## Injected Workspace Files

OpenClaw/Codex injected these workspace files:

| File | Raw chars | Injected chars | Note |
|---|---:|---:|---|
| `AGENTS.md` | 1935 | 1935 | Needed, but should remain bootloader-sized. |
| `SOUL.md` | 1797 | 1797 | Likely unnecessary for narrow utility agents. |
| `TOOLS.md` | 387 | 387 | Small, possibly useful. |
| `IDENTITY.md` | 693 | 693 | Likely unnecessary for path-validation utility tasks. |
| `USER.md` | 674 | 674 | May be useful for owner-facing router, less useful for utility tasks. |
| `HEARTBEAT.md` | 243 | 0 | Detected but not injected. |

Workspace file total injected chars: `5486`.

## Injected Skills

OpenClaw reported `14` eligible skills and injected a skills prompt of `5106` chars.

Injected skill entries:

- `canvas`
- `diagram-maker`
- `healthcheck`
- `meme-maker`
- `node-connect`
- `node-inspect-debugger`
- `notion`
- `python-debugpy`
- `skill-creator`
- `spike`
- `taskflow`
- `taskflow-inbox-triage`
- `video-frames`
- `weather`

Assessment:

- These are mostly irrelevant to Personal Office path validation.
- This is a clear slimming target.
- The router should not carry visual, debugging, weather, notion, meme, or video skills by default.

## Exposed Tools

OpenClaw reported `18` tools:

- `sessions_yield`
- `cron`
- `image_generate`
- `video_generate`
- `get_goal`
- `create_goal`
- `update_goal`
- `skill_workshop`
- `sessions_list`
- `sessions_history`
- `sessions_send`
- `sessions_spawn`
- `subagents`
- `session_status`
- `web_fetch`
- `image`
- `memory_search`
- `memory_get`

Assessment:

- For path validation, only a minimal session/response capability is needed.
- `cron`, image/video generation, subagents, web fetch, and memory tools are unnecessary for this class of task.
- `tools.profile = coding` appears too broad for the Personal Office router/default agent.
- `contextInjection: "never"` was later tested on the slim utility agent and did not remove the bootstrap/workspace layer.

## Session Comparison

Recent default sessions reported:

| Session | Input | Output | Cache read | Total | Runtime |
|---|---:|---:|---:|---:|---:|
| `dashboard-smoke` | 15230 | 8 | 2432 | 17662 | 13.8s |
| `context-pack-smoke` | 3209 | 278 | 24960 | 28169 | 37.9s |
| `yuliya-transcript-handoff` | 2265 | 2986 | 29056 | 31321 | 100.6s |
| `context-pack-v2-smoke` | 2186 | 221 | 27008 | 29194 | 42.5s |
| `yuliya-draft-patch-bundle` | 4483 | 4364 | 18304 | 22787 | 103.0s |
| `yuliya-path-validation` | 1362 | 1030 | 17792 | 19154 | 36.0s |

All these runs injected the same broad workspace files, skills, and tools.

## Conclusions

The current Pi OpenClaw Personal Office router is not bloated because it has raw Personal Office data. It is bloated because the default Codex/OpenClaw harness carries:

- identity/personality/runtime workspace files;
- default skill catalog unrelated to the workflow;
- broad coding tool profile;
- memory/session/web/media/cron/subagent tools even for tiny validation tasks.
- `contextInjection: "never"` is not, by itself, a complete utility-agent slimming mechanism.

This confirms the product concern:

> Local-first deployment does not prevent context bloat. Without per-workflow slimming, even local installs will feel slow and noisy.

## Recommended Slimming Experiments

### Experiment 1: Create `po-path-validator`

Create a dedicated utility agent for path validation with:

- workspace containing only `AGENTS.md` and the handed routing excerpt;
- no `SOUL.md`, `IDENTITY.md`, or broad `USER.md` unless OpenClaw requires them;
- explicit empty or tiny skill allowlist if supported;
- tool profile reduced below `coding` if OpenClaw supports it;
- same Codex auth profile or a copied portable auth profile only if safe.

Success target:

- keep total tokens under `8000` for the same path-validation prompt;
- keep runtime under `20s`;
- preserve the same validation quality.

Result on 2026-06-25:

- Created and tested `po-path-validator`.
- Per-agent `skills: []` worked and removed the `5106` char skills prompt.
- `memorySearch.enabled=false` removed `memory_search` and `memory_get`.
- Temporary `tools.profile = minimal` reduced tools to one exposed tool and system prompt chars to `3557`, but `tools.profile` is global in this setup and was restored to `coding`.
- OpenClaw automatically restored workspace identity/runtime files, so deleting `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, and `HEARTBEAT.md` is not a durable slimming method.
- Follow-up run `agent:po-path-validator:yuliya-path-validation-slim-v5-context-never` confirmed that `contextInjection: "never"` still left `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, and `HEARTBEAT.md` injected.
- Detailed result: `tools/raspberrypi-openclaw/test-runs/2026-06-25-po-path-validator-slimming.md`.

### Experiment 2: Restrict skills

Test OpenClaw per-agent skill config:

- set `agents.list[].skills: []` for the utility agent if supported;
- otherwise set a minimal list only for required Personal Office router skills.

Success target:

- remove the `5106` char default skills prompt from utility tasks.

### Experiment 3: Reduce tool profile

Research and test whether OpenClaw supports a smaller `tools.profile` than `coding` for a local dashboard/CLI router.

Success target:

- remove `cron`, image/video generation, subagents, web fetch, and memory tools from path validation.

### Experiment 4: Workspace file minimization

Test whether OpenClaw injects `SOUL.md`, `IDENTITY.md`, `USER.md`, and `TOOLS.md` only when present.

Success target:

- utility agents should inject only `AGENTS.md` plus explicitly handed files.

## Immediate Product Rule

Every Personal Office OpenClaw agent should declare:

- default injected files;
- allowed skills;
- exposed tools;
- target prompt/token budget;
- which context must be loaded lazily;
- which tasks should be delegated to slimmer utility agents.
