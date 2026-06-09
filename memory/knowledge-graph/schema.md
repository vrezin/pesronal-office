# Knowledge Graph Schema

The knowledge graph is file-backed in v1.

## Files

- `nodes.jsonl` - one JSON object per node.
- `edges.jsonl` - one JSON object per relationship.
- `indexing-rules.md` - when and how to update the graph.

## Node Shape

```json
{"id":"topic:memory-system","type":"topic","label":"Memory System","source":"memory/semantic/topics/memory-system.md","updated":"2026-06-09"}
```

Required fields:

- `id`
- `type`
- `label`
- `source`
- `updated`

## Edge Shape

```json
{"from":"repo:personal-office","to":"topic:memory-system","type":"contains","source":"memory/README.md","updated":"2026-06-09"}
```

Required fields:

- `from`
- `to`
- `type`
- `source`
- `updated`

## Node Types

- `repo`
- `domain`
- `topic`
- `entity`
- `project`
- `company`
- `tool`
- `skill`
- `artifact`

## Edge Types

- `contains`
- `routes_to`
- `source_of_truth_for`
- `uses_skill`
- `depends_on`
- `summarizes`
- `managed_in`
- `external_truth_in`
- `redirects_from`
