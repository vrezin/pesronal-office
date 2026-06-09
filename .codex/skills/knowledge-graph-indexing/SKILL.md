---
name: knowledge-graph-indexing
description: Use when Personal Office needs to add or refresh machine-readable knowledge graph nodes and edges for domains, topics, entities, projects, companies, tools, skills, artifacts, or source-of-truth relationships.
metadata:
  short-description: Update file-backed knowledge graph
---

# Knowledge Graph Indexing

## Inputs

- `memory/knowledge-graph/schema.md`
- relevant `wiki/maps/*.md`
- relevant source artifacts
- `memory/semantic/topics/`
- `memory/entities/`

## Workflow

1. Read the schema.
2. Identify stable nodes and relationships.
3. Add or update `memory/knowledge-graph/nodes.jsonl`.
4. Add or update `memory/knowledge-graph/edges.jsonl`.
5. Keep ids stable and labels non-sensitive.
6. Update `memory/knowledge-graph/indexing-rules.md` only if process rules change.

## Rules

- Do not encode sensitive details in graph labels.
- Prefer one clear edge over several vague edges.
- Use repo-relative paths or approved aliases.
