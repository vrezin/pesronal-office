---
id: memory-protocol-retrieval-policy
type: Playbook
title: Memory Retrieval Policy
description: Progressive-disclosure retrieval policy for Personal Office agents.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - memory/retrieval/search-rules.md
confidence: high
sensitivity: internal
tags: [memory, retrieval, agent-navigation]
review_after: 2026-09-28
---

# Memory Retrieval Policy

Agents should use maps and memory as a navigation layer, not as a reason to read every file.

## Default Order

1. `wiki/README.md`
2. Relevant `wiki/maps/<domain>.md`
3. `memory/retrieval/index.md`
4. Narrow semantic topic, entity card, context card, or workflow index.
5. Source artifact only when exact truth is needed.

## Search Rules

- Prefer targeted `rg` queries over broad directory reads.
- Search by stable IDs, people names, company names, project names, and route aliases.
- Read summaries before source artifacts.
- Log retrieval in `memory/retrieval/retrieval-log.md` when it materially affects an artifact.

## Raw Data Boundary

Do not read raw personal, finance, health, inbox, or credential/tool state unless:

- the selected map allows it;
- the task requires exact source truth;
- the user asked for it or it is necessary to update a source artifact;
- sensitive-source rules are followed.
