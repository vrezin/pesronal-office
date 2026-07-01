---
id: po-memory-retire
type: Workflow
title: /po:memory-retire
description: Retire stale, superseded, or unsafe memory without deleting history.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - memory/protocol/retirement-policy.md
confidence: high
sensitivity: internal
tags: [personal-office, command, memory-retirement]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, change, retire]
requires_human_review: true
do_not_load_raw: true
---

# /po:memory-retire

## Purpose

Mark obsolete memory as stale, superseded, retired, or archived.

## Procedure

1. Verify the source artifact or replacement route.
2. Choose status according to `memory/protocol/retirement-policy.md`.
3. Add `retired_reason` or `superseded_by`.
4. Update retrieval or graph indexes if this memory was a route.
5. Do not delete v1 history.
