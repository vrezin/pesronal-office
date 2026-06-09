---
name: wiki-routing
description: Use before repository work in Personal Office when the agent needs to choose the relevant domain, source artifacts, memory files, and local skills without reading the whole repository.
metadata:
  short-description: Route work through machine-readable wiki maps
---

# Wiki Routing

## Workflow

1. Read `wiki/README.md`.
2. Choose one relevant `wiki/maps/*.md`.
3. Read the map frontmatter.
4. Open only the needed `source_of_truth`, `skills`, `memory`, and `retrieval` entries.
5. If no map fits, use `secretaries/routing-map.md` and create a clarification note if needed.

## Rules

- Do not read the whole repository by default.
- Treat `do_not_read_by_default` as sensitive or irrelevant unless the task clearly needs it.
- Source artifacts beat memory summaries.
- If the task creates a durable fact or decision, route it into the repository.
