---
id: personal-office-owner-operator-connectors
type: Connector
title: Owner Operator Connector Boundaries
description: Connector risk and access boundaries for owner/operator workflows.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - tools/personal-office-owner-operator-pack/index.md
confidence: high
sensitivity: internal
tags: [personal-office, connectors]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, enrich]
requires_human_review: true
do_not_load_raw: true
---

# Connectors

## Access Ladder

1. Local repo maps/indexes/read-only search.
2. Selected local source artifacts.
3. Gmail/calendar/Drive read-only summaries.
4. Finance read-only summaries.
5. Draft write bundles.
6. Human-approved external actions.

No connector should be broad-write by default.
