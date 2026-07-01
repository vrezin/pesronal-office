# Raspberry Pi OpenClaw Runtime

This directory tracks the Personal Office experiment to run an OpenClaw agent on the Raspberry Pi reachable through SSH profile `raspberrypi-codex`.

## Purpose

Use the Raspberry Pi as a local home-network agent host for Personal Office.

First role:

- run OpenClaw on the Pi;
- give it controlled access to Personal Office cookbooks and routing rules;
- keep the first deployment local and single-user;
- use it to test whether a private/local Personal Office agent host is practical.

## Verified Host Facts

- SSH profile: `raspberrypi-codex`
- Hostname: `raspberrypi`
- User: `pi`
- OS: Raspbian GNU/Linux 13 `trixie`
- Kernel architecture: `aarch64`
- Userland architecture after reimage: `arm64`, 64-bit
- Sudo: passwordless sudo available
- Available tools: `git`, `python3`
- Node.js for OpenClaw runtime: 22.23.1 under `/home/openclaw/.local/opt/node-current`

Pre-reimage historical finding: the old image had `armhf` 32-bit userland. That blocked the native Codex app-server runtime with `Unsupported platform: linux (arm)`.

## OpenClaw Install Constraint

OpenClaw currently documents Node.js 24 as recommended and Node.js 22.19+ as supported.

The Pi apt repository currently offers Node.js 20.19.2, so installing `nodejs` from apt is not enough for OpenClaw. Because the userland is 32-bit `armhf`, verify the Node install route before assuming standard ARM64 binaries will run.

Pre-reimage finding from 2026-06-25:

- user-local Node.js 22.23.1 runs as `linux arm` because the OS userland is `armhf`;
- OpenClaw 2026.6.10 installs and its Gateway runs;
- the external `@openclaw/codex` plugin installs and loads;
- OpenAI/Codex device-code OAuth succeeds for `po-router`;
- the actual Codex app-server executable from `@openai/codex` fails with `Unsupported platform: linux (arm)`.

Implication at that point: Codex subscription auth was viable conceptually, but the old Pi image had the wrong userland for native Codex runtime. This was resolved by reimaging to Raspberry Pi OS Lite 64-bit.

## First Safe Deployment Shape

1. Install a supported Node.js runtime for the Pi userland.
2. Install OpenClaw.
3. Create a dedicated runtime directory on the Pi, for example `~/personal-office-agent/`.
4. Put a Personal Office cookbook bundle under an explicit path inside that directory.
5. Teach the agent to use the cookbook bundle as operating instructions and to request narrow context instead of reading raw personal data by default.
6. Start OpenClaw with local/loopback or local-network-only Gateway binding.
7. Do not enable public exposure, broad credentials, browser profiles, finance tokens, or unattended destructive actions during the first smoke test.

## Cookbook-Only Boundary

The Pi-side OpenClaw agent should not start with a full copy of Personal Office data.

Allowed first-sync materials:

- `AGENTS.md`
- `wiki/README.md`
- `wiki/maps/`
- `wiki/playbooks/`
- `secretaries/`
- `.codex/skills/`
- `tools/README.md`
- `tools/raspberrypi-openclaw/`

Excluded until explicitly approved:

- `finance/`
- `people/`
- `life/`
- `inbox/raw/`
- `inbox/processed/`
- `companies/`
- `personal-projects/`
- `memory/`
- `calendar/`
- `tasks/`
- browser profiles, cookies, tokens, `.env` files, SSH keys, and full tool state.

If the agent needs facts from excluded areas, it should ask for a narrow handoff or use a future approved tool/API that returns only the needed context.

## First Smoke Tests

- `openclaw --version`
- `openclaw gateway status`
- local dashboard or CLI-only message
- read cookbook bundle from the Pi
- explain the routing protocol from cookbooks
- request a narrow Personal Office context handoff instead of reading raw data
- one controlled file update only after the access boundary is reviewed

## Current Pi State

- After reimage, Raspberry Pi OS is 64-bit: `dpkg --print-architecture` returns `arm64`, and Node reports `linux arm64`.
- VPN is restored as root/system service: `wg-quick@personal-office` is active, interface `personal-office` has `10.200.173.81/32`, and observed external IPv4 is `195.181.173.207`.
- Dedicated runtime user `openclaw` exists with home `/home/openclaw` and no sudo group membership.
- Node.js 22.23.1 is installed for `openclaw` under `/home/openclaw/.local/opt/node-current`.
- OpenClaw 2026.6.10 is installed for `openclaw` and available as `/home/openclaw/.local/bin/openclaw`.
- Gateway is installed as `openclaw` user systemd service, enabled, running on loopback port `18789`, and reports `write-capable`.
- `po-router` is registered under `/home/openclaw/personal-office-agent/`.
- `default` is registered as the dashboard/default route, uses the same cookbook workspace as `po-router`, and has its own agent state directory at `/home/openclaw/personal-office-agent/openclaw-agents/default`.
- Cookbook-only bundle is synced to `/home/openclaw/personal-office-agent/cookbooks/personal-office/` with repo-like paths (`AGENTS.md`, `wiki/`, `secretaries/`, `.codex/skills/`, `tools/raspberrypi-openclaw/`).
- Minimal non-sensitive context pack is synced to `/home/openclaw/personal-office-agent/cookbooks/personal-office/tools/raspberrypi-openclaw/personal-office-context-pack.md`.
- Live `po-router` workspace `AGENTS.md` points the agent to that context pack before real intake tests.
- Detailed routing procedures remain in cookbook/context/template files, not in `AGENTS.md`.
- Added Pi-side cookbook templates:
  - `tools/raspberrypi-openclaw/templates/narrow-context-handoff-template.md`
  - `tools/raspberrypi-openclaw/templates/draft-patch-bundle-template.md`
  - `tools/raspberrypi-openclaw/review-checklists/router-output-review-checklist.md`
- Cookbook verification found no top-level raw-data directories: no `finance/`, `people/`, `life/`, `inbox/`, `companies/`, `personal-projects/`, `memory/`, `calendar/`, or `tasks/`.
- `@openclaw/codex` is installed, enabled, and allowlisted through `plugins.allow=["codex"]`.
- OpenAI/Codex device-code OAuth profile exists for `po-router`; it expires on 2026-07-05T08:50:10Z unless refreshed.
- OpenAI/Codex device-code OAuth profile exists for `default`; it expires on 2026-07-05T09:13:19Z unless refreshed.
- Agent smoke tests passed:
  - `Personal Office router online.`
  - `Gateway path online.`
  - `Default route online.`
  - `context-pack-smoke`: the agent named `personal-office-context-pack.md` and correctly refused to infer current private/project facts from it.
- `openclaw status` reports `default`, `po-router`, and prior `main` sessions running on `OpenAI Codex` with model `gpt-5.5`; new dashboard/default traffic should use `default`.
- The old too-wide partial repository copy was on the pre-reimage filesystem and is no longer present after reimage.

## Test Contour Access Policy

For the current test contour, use only:

- CLI over SSH;
- dashboard through SSH tunnel to the loopback Gateway.

Do not enable Telegram, public tunnels, Tailscale exposure, or other external channels yet.

CLI example:

```bash
ssh raspberrypi-codex 'sudo -u openclaw bash -lc "cd ~; PATH=~/.local/bin:~/.local/opt/node-current/bin:\$PATH; openclaw agent --session-key agent:default:test --message '\''<test intake>'\'' --timeout 180"'
```

Dashboard tunnel from the workstation:

```bash
ssh -N -L 18789:127.0.0.1:18789 raspberrypi-codex
```

Then open:

```text
http://127.0.0.1:18789/
```

## Runtime Decision

Resolved: Raspberry Pi 5 with 64-bit Raspberry Pi OS works for the OpenClaw + Codex subscription path.

Correct image selected and verified on 2026-06-25:

- Raspberry Pi OS Lite 64-bit
- Debian 13 `trixie`
- release date 2026-06-18
- download endpoint: `https://downloads.raspberrypi.com/raspios_lite_arm64_latest`
- local verified copy: `/tmp/2026-06-18-raspios-trixie-arm64-lite.img.xz`
- persistent workstation copy: `<external-downloads>/2026-06-18-raspios-trixie-arm64-lite.img.xz`
- SHA256: `acff736ca7945e3b305f07cda4abdb870910e12634991da69783611756e381b3`

Reimage runbook:

- `tools/raspberrypi-openclaw/reimage-64bit-runbook.md`

Alternatives:

- use an OpenAI API key instead of Codex subscription auth, if the goal is only to prove OpenClaw agent behavior on this existing OS image;
- use another host with supported `x64` or `arm64` userland as the first OpenClaw/Codex runtime;
- keep this Pi as VPN/local-network infrastructure and move the agent runtime elsewhere.

## Related Artifacts

- `tasks/active/2026-06-25-try-personal-office-on-raspberry-pi-openclaw.md`
- `inbox/processed/2026-06-25-raspberry-pi-openclaw-agent.md`
- `tools/raspberrypi-openclaw/openclaw-personal-office-operating-model.md`
