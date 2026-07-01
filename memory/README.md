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
- `protocol/` - product-grade lifecycle, metadata, retrieval, and retirement rules.
- `templates/` - protocol-managed memory templates.

## Rules

- Keep sensitive details minimal.
- Link to source artifacts instead of copying raw private data.
- Separate observed facts from interpretations.
- When source artifacts disagree with memory, update memory from the source artifact.
- If a fact affects planning, tasks, money, health, or obligations, update the source artifact too.

## Operating Loop

1. Route new input through `wiki/README.md` and `secretaries/routing-map.md`.
2. Use `memory-system` for durable fact capture, retrieval, consolidation, entities, and graph updates.
3. Search relevant memory before planning or answering.
4. Rebuild graph and retrieval indexes when source artifacts materially change.

## Memory OS Protocol

New protocol-managed memory follows `protocol/metadata-contract.md`.

Agents should use the lifecycle in `protocol/lifecycle.md`:

- `use` - navigate maps, indexes, and narrow concept cards before source artifacts.
- `enrich` - add summaries, source links, confidence, and relations without copying long raw content.
- `create` - create memory only from source artifacts, user-provided facts, or cited external sources.
- `change` - update memory when source truth, route, confidence, or status changes.
- `retire` - mark memory stale, superseded, retired, or archived instead of deleting history.

Protocol-managed memory is an agent navigation layer. It is not a replacement for domain truth and must not become a dump of raw documents.
