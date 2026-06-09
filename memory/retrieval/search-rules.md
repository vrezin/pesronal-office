# Memory Retrieval Search Rules

## Default Order

1. Read `wiki/README.md`.
2. Select relevant `wiki/maps/<domain>.md`.
3. Read only the map's source-of-truth and skill list.
4. Search semantic memory for stable summaries.
5. Search entity memory for people, company, project, place, or tool context.
6. Search episodic memory only when event history matters.
7. Use source artifacts to verify before writing important outcomes.

## Search Commands

Prefer targeted `rg` searches:

```text
rg --hidden -n "<query>" wiki memory life finance calendar tasks people companies personal-projects tools -g "*.md" -g "*.jsonl"
```

Use graph files for relation search:

```text
rg --hidden -n "<entity-or-topic-id>" memory/knowledge-graph
```

## Logging

When retrieval materially influences an artifact, add a short line to `memory/retrieval/retrieval-log.md`.
