# Dockerize Tools Runtime Isolation

- Created: 2026-06-10
- Status: active
- Area: personal-office / tools
- Related workspace: `tools/`

## Context

The `tools/` directory now contains sensitive local runtimes and authenticated helpers such as the LinkedIn MCP server. Keeping these tools on the host filesystem is convenient, but it increases exposure and makes lifecycle management clumsy.

## Desired Outcome

Move personal-office tools toward a containerized runtime model where:

- tool code and helper scripts can live in Docker images or compose services;
- sensitive auth state is mounted or injected at runtime, not committed;
- starting a tool is a single command;
- stopping a tool cleans up the container and leaves no host residue;
- the same pattern can be used for both third-party tools and our own tools.

## Deliverables

1. A short runtime policy for `tools/` explaining what stays in git and what stays local.
2. A containerization plan for `linkedin-mcp` and `zenmoney-mcp`.
3. A minimal Docker or Compose wrapper for at least one tool.
4. A repeatable start/stop pattern that does not depend on a permanently running host machine.

## Next Step

Audit the current tools and choose the smallest viable Dockerized wrapper path, starting with the LinkedIn MCP server because it already proved useful and currently depends on local auth state.

