# Memory System Playbook

## Start

1. Read `wiki/maps/memory-system.md`.
2. Read `memory/README.md`.
3. Use `memory/protocol/lifecycle.md` to choose the operation:
   - `use`;
   - `enrich`;
   - `create`;
   - `change`;
   - `retire`.
4. Use `memory/protocol/metadata-contract.md` for new protocol-managed files.

## Retrieval

Before planning or answering from prior context, check:

- `wiki/maps/` for the domain map;
- `memory/retrieval/index.md`;
- `memory/semantic/topics/`;
- `memory/entities/`;
- `memory/knowledge-graph/`;
- direct source-of-truth folders.

Default order is progressive disclosure:

```text
wiki map -> retrieval index -> concept card / semantic topic -> source artifact
```

Do not broad-read raw personal, finance, health, inbox, or tool state unless the selected map allows it and exact source truth is required.

## Capture

Durable facts belong first in their domain source of truth. Memory can summarize, link, and index them.

Use:

- `memory/short-term/` for current context and open loops;
- `memory/episodic/` for dated session/event summaries;
- `memory/semantic/topics/` for stable domain summaries;
- `memory/entities/` for people/projects/companies/tools;
- `memory/knowledge-graph/` for machine-readable nodes and edges.

Use templates from `memory/templates/` for new protocol-managed memory:

- `context-card.md`;
- `semantic-topic.md`;
- `entity-card.md`;
- `decision-memory.md`;
- `handoff-memory.md`;
- `workflow-memory.md`;
- `validation-signal.md`;
- `retirement-note.md`.

## Lifecycle Operations

### Use

Read maps and indexes first. Use memory to locate the source of truth, not to replace it.

### Enrich

Add source-backed summaries, confidence, sensitivity, route links, related concepts, and graph edges. Do not copy full documents or private threads into memory.

### Create

Create protocol-managed memory only when the context is reusable and source-backed. Required metadata is defined in `memory/protocol/metadata-contract.md`.

### Change

When source artifacts change, update memory metadata and summaries. If there is a conflict, source truth wins.

### Retire

Use `memory/protocol/retirement-policy.md`. Mark old memory as `stale`, `superseded`, `retired`, or `archived`; do not delete v1 history.

## Graph

Keep `nodes.jsonl` and `edges.jsonl` as valid JSONL. Do not put sensitive details such as family birth dates into graph nodes when a private contact card is enough.
