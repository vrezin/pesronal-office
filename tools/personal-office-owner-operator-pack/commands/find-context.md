---
id: po-find-context
type: Workflow
title: /po:find-context
description: Find source-backed Personal Office context through maps, indexes, and narrow source reads.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - memory/protocol/retrieval-policy.md
confidence: high
sensitivity: internal
tags: [personal-office, command, retrieval]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use]
requires_human_review: false
do_not_load_raw: true
---

# /po:find-context

## Purpose

Find relevant context with source paths, freshness, and confidence without broad raw-data reads.

## Inputs

- Query or question.
- Optional domain, person, company, project, date, or source hint.

## Procedure

1. Read `wiki/README.md`.
2. Select the narrowest `wiki/maps/<domain>.md`.
3. Read `memory/retrieval/index.md`.
4. Search semantic/entity/context memory.
5. Open source artifacts only when exact truth is needed.

## Output

- Answer summary.
- Source paths.
- Confidence/freshness.
- Missing context requests.

## Approval

No approval needed for read-only retrieval. Approval is required before writes or external actions.
