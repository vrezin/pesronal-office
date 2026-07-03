# LinkedIn MCP Server

Local packaged LinkedIn MCP runtime for authenticated job/profile lookup.

This tool is registered for Codex in `<repo-root>/.codex/config.toml` as the `linkedin` MCP server.
Codex connects to the local streamable HTTP endpoint at `http://127.0.0.1:8019/mcp`.

## What Lives Here

- Authenticated browser profile copied from the working Linux host.
- Shared Personal Office job-search Python runtime preferred. The old local
  virtualenv fallback is migration-only and should not be used by the Pi service.
- Helper scripts for start/stop and one-shot task execution.

## Run

Start the server locally:

```bash
./scripts/start-local.sh
```

Start the local agent-facing server on loopback:

```bash
./scripts/start-local.sh
```

`start-local.sh` first checks:

```text
<repo-root>/.runtime/job-search-venv/bin/linkedin-mcp-server
```

and falls back to:

```text
tools/linkedin-mcp/.venv/bin/linkedin-mcp-server
```

The Pi user service is managed from:

```text
automation/systemd/personal-office-linkedin-mcp.service
```

Build the shared runtime with:

```bash
tools/job-search-runtime/setup-shared-env.sh
```

Start the daemon-friendly singleton wrapper:

```bash
./scripts/start-daemon.sh
```

Run a one-shot task with the server up, then stop it automatically:

```bash
./scripts/with-server.sh -- ./scripts/example-smoke-check.sh
```

You can also set a custom port:

```bash
LINKEDIN_MCP_PORT=8010 ./scripts/with-server.sh -- ./scripts/example-smoke-check.sh
```

Stop the server if it was started in background mode:

```bash
./scripts/stop.sh
```

## Notes

- Keep this tool local to `personal-office`; do not move auth material into company repos.
- Do not commit `profile/`, `cookies.json`, browser caches, or Python runtime directories.
- If LinkedIn invalidates the copied session, log in again through this local profile and refresh the state here.
- The Codex runtime configuration points to the streamable HTTP endpoint, not to a launcher script.
- Use `scripts/start-daemon.sh` to ensure the server is running once per machine session.
