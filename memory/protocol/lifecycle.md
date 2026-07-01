---
id: memory-protocol-lifecycle
type: Playbook
title: Memory Lifecycle
description: Product-grade lifecycle rules for using, enriching, creating, changing, and retiring Personal Office memory.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - memory/README.md
confidence: high
sensitivity: internal
tags: [memory, lifecycle, personal-office]
review_after: 2026-09-28
---

# Memory Lifecycle

Memory is a navigation and compression layer over source artifacts. It must help agents find the right context without copying or loading raw personal documents by default.

## Source Priority

1. Domain source-of-truth artifacts own facts, obligations, decisions, money, health, people, calendar, and project state.
2. Memory artifacts summarize, route, index, and link to those sources.
3. If memory disagrees with a source artifact, the source artifact wins.

## Operations

### Use

Use memory when prior context may affect routing, planning, promises, people, risk, project state, or product decisions.

Required flow:

1. Read `wiki/README.md`.
2. Select the smallest relevant `wiki/maps/<domain>.md`.
3. Check `memory/retrieval/index.md`.
4. Read narrow concept cards or semantic summaries.
5. Open source artifacts only when the memory card is not enough or a write depends on exact truth.

### Enrich

Enrich memory when a source artifact adds stable reusable context.

Allowed enrichment:

- add a short summary;
- add source references;
- add confidence, sensitivity, and freshness metadata;
- add related concepts;
- update graph nodes or edges.

Do not paste long raw documents, full private threads, or sensitive source content into memory.

### Create

Create a memory artifact only when one of these is true:

- a source artifact exists and the context is reusable;
- the user directly provides a stable fact or preference;
- an external source is explicitly cited;
- a new route/concept is needed for agent navigation.

New protocol-managed memory must use `memory/protocol/metadata-contract.md`.

### Change

Change memory when source truth, status, confidence, or route changes.

Every meaningful change should update:

- `updated`;
- `source_refs` when evidence changes;
- `confidence` when certainty changes;
- `status` when the memory ages or is superseded;
- retrieval or graph indexes when navigation changes.

### Retire

Retire memory when it is no longer current, useful, or safe as a routing cue.

Retirement is metadata, not deletion:

- set `status` to `stale`, `superseded`, `retired`, or `archived`;
- add `retired_reason` or `superseded_by`;
- keep source links;
- do not delete history in v1.

## Human Review

Human review is required before memory changes that affect:

- money;
- health;
- legal/compliance claims;
- external commitments;
- access rights;
- sensitive personal facts;
- source-of-truth replacement.
