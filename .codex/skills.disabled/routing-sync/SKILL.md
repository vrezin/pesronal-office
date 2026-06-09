---
name: routing-sync
description: Use when adding or changing a recurring workflow, source-of-truth artifact, wiki map, memory artifact, knowledge graph node, or local skill so repository routing stays consistent across AGENTS.md, wiki, memory, graph, and skill lists.
metadata:
  short-description: Sync routing across wiki memory graph skills
---

# Routing Sync

## When To Use

- A new recurring workflow becomes a skill.
- A new source-of-truth artifact is introduced.
- A domain map changes.
- Memory/retrieval/knowledge-graph references need to point to a new artifact.
- A repeated task should become discoverable by future agents.

## Checklist

Update the relevant subset:

- `AGENTS.md` local skill list;
- `wiki/maps/<domain>.md`;
- `memory/semantic/topics/<topic>.md`;
- `memory/retrieval/index.md`;
- `memory/knowledge-graph/nodes.jsonl`;
- `memory/knowledge-graph/edges.jsonl`;
- related existing skills that should call the new skill;
- decision note in `inbox/processed/`.

## Verification

- JSONL graph parses.
- Graph edges have existing nodes.
- No absolute machine paths were introduced.
- `git status --short` shows only intended changes plus known unrelated state.
