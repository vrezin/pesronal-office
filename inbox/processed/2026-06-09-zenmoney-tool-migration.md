# 2026-06-09 - ZenMoney MCP Tool Migration

## Source

User noted that ZenMoney stores the full personal money movement history and should not live in `aistudio`.

## Decision

Personal tools and MCP servers belong in `personal-office/tools/`.

The ZenMoney MCP server is part of the personal finance operating system and should be managed from:

`<repo-root>/tools/zenmoney-mcp`

## Migration

Moved from:

`<aistudio-root>/tools/zenmoney-mcp`

Moved to:

`<repo-root>/tools/zenmoney-mcp`

The old `<aistudio-root>/tools` directory was empty after the move and was removed.

## Safety

ZenMoney contains personal finance history. Prefer read-only operation by default.

The MCP server now supports `ZENMONEY_READ_ONLY=1` to avoid registering write tools unless writes are explicitly needed.
