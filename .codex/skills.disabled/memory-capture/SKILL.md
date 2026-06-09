---
name: memory-capture
description: Use when new input contains durable facts, decisions, events, preferences, relations, risks, people, projects, tools, or obligations that should be captured in Personal Office memory and source artifacts.
metadata:
  short-description: Capture durable facts into memory
---

# Memory Capture

## Workflow

1. Route the input through `wiki/README.md` and `secretaries/routing-map.md`.
2. Update source-of-truth artifacts first when the input affects life, finance, calendar, tasks, people, companies, or projects.
3. Add dated event context to `memory/episodic/` if history matters.
4. Add stable summaries to `memory/semantic/topics/` only when the fact is durable.
5. Add or update entity records in `memory/entities/` when a person, company, project, place, or tool becomes recurring.
6. Add graph nodes/edges through `knowledge-graph-indexing` when a relationship becomes important.

## Rules

- Do not invent missing facts.
- Separate facts from interpretation.
- Minimize sensitive data.
- If the route is unclear, create a clarification note.
