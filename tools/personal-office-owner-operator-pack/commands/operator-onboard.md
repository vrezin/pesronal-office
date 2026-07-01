---
id: po-operator-onboard
type: Workflow
title: /po:operator-onboard
description: Onboard a trusted assistant/operator to Personal Office routes, boundaries, approvals, and weekly cadence.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - inbox/processed/2026-06-25-alena-maltseva-human-assistant-objection.md
confidence: high
sensitivity: internal
tags: [personal-office, command, operator]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, enrich, create]
requires_human_review: true
do_not_load_raw: true
---

# /po:operator-onboard

## Purpose

Define how a trusted operator works with Personal Office without becoming a privacy or source-of-truth risk.

## Output

- Accessible sources.
- Forbidden sources.
- Approval rules.
- Weekly cadence.
- Escalation rules.
- Handoff boundaries.
