# Memory System Playbook

## Retrieval

Before planning or answering from prior context, check:

- `wiki/maps/` for the domain map;
- `memory/semantic/topics/`;
- `memory/entities/`;
- `memory/knowledge-graph/`;
- direct source-of-truth folders.

## Capture

Durable facts belong first in their domain source of truth. Memory can summarize, link, and index them.

Use:

- `memory/short-term/` for current context and open loops;
- `memory/episodic/` for dated session/event summaries;
- `memory/semantic/topics/` for stable domain summaries;
- `memory/entities/` for people/projects/companies/tools;
- `memory/knowledge-graph/` for machine-readable nodes and edges.

## Graph

Keep `nodes.jsonl` and `edges.jsonl` as valid JSONL. Do not put sensitive details such as family birth dates into graph nodes when a private contact card is enough.
