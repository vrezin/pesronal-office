# Memory

Private memory layer for Personal Office.

Memory helps agents recall relevant context without rereading the whole repository. It does not replace the source of truth in `life/`, `finance/`, `calendar/`, `tasks/`, `people/`, `companies/`, or `personal-projects/`.

## Layers

- `short-term/` - current focus, open loops, working context.
- `episodic/` - dated event history and session traces.
- `semantic/` - stable compressed knowledge by topic.
- `entities/` - stable records about people, companies, projects, places, and tools.
- `knowledge-graph/` - machine-readable nodes and relations.
- `retrieval/` - search rules, indexes, and retrieval logs.
- `long-term/` - durable preferences, principles, and recurring rules.

## Rules

- Keep sensitive details minimal.
- Link to source artifacts instead of copying raw private data.
- Separate observed facts from interpretations.
- When source artifacts disagree with memory, update memory from the source artifact.
- If a fact affects planning, tasks, money, health, or obligations, update the source artifact too.

## Operating Loop

1. Route new input through `wiki/README.md` and `secretaries/routing-map.md`.
2. Capture durable facts through `memory-capture`.
3. Search relevant memory through `memory-retrieval` before planning or answering.
4. Consolidate dated events into semantic/entity/graph memory through `memory-consolidation`.
5. Rebuild graph and retrieval indexes through `knowledge-graph-indexing`.
