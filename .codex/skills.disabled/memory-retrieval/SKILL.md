---
name: memory-retrieval
description: Use when answering, planning, or updating artifacts in Personal Office may depend on prior context, stable facts, entity records, knowledge graph relations, or semantic/episodic memory.
metadata:
  short-description: Retrieve relevant memory before acting
---

# Memory Retrieval

## Workflow

1. Start with `wiki/README.md` and the relevant map.
2. Read `memory/retrieval/search-rules.md`.
3. Search semantic memory for stable topic knowledge.
4. Search entity memory for relevant people, companies, projects, places, or tools.
5. Search the knowledge graph for relations if dependencies matter.
6. Search episodic memory only when dated history matters.
7. Verify important facts against source-of-truth artifacts before updating them.

## Rules

- Retrieval is an access layer, not the source of truth.
- Prefer narrow `rg` searches over broad reading.
- Log retrieval in `memory/retrieval/retrieval-log.md` when it materially influences a durable artifact.
