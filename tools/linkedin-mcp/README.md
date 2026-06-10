# LinkedIn MCP Server

Local packaged LinkedIn MCP runtime for authenticated job/profile lookup.

## What Lives Here

- Authenticated browser profile copied from the working Linux host.
- Local Python virtualenv with `linkedin-scraper-mcp` installed.
- Helper scripts for start/stop and one-shot task execution.

## Run

Start the server locally:

```bash
./scripts/start.sh
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
- Do not commit `profile/`, `cookies.json`, browser caches, or the virtualenv.
- If LinkedIn invalidates the copied session, log in again through this local profile and refresh the state here.
