# Knowledge Graph Indexing Rules

## When To Update

Update `nodes.jsonl` and `edges.jsonl` when:

- a new durable domain appears;
- a new recurring project/company/tool/person becomes important;
- a wiki map adds a source-of-truth route;
- semantic memory changes a stable relationship;
- a tool or skill becomes part of an operating workflow.

## How To Update

1. Read the relevant wiki map.
2. Check the source artifact.
3. Add or update the smallest set of nodes.
4. Add or update explicit edges.
5. Keep ids stable.
6. Do not encode sensitive private details in graph labels.

## Cadence

- Light update: whenever a source artifact creates a new durable relation.
- Weekly: check whether short-term and episodic memory introduced new nodes.
- Monthly: remove obsolete edges only when the source artifact clearly changed.
