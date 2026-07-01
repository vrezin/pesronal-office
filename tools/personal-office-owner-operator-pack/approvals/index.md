---
id: personal-office-owner-operator-approvals
type: ApprovalRule
title: Owner Operator Approval Rules
description: Human approval checkpoints for Personal Office owner/operator workflows.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - tools/personal-office-owner-operator-pack/index.md
confidence: high
sensitivity: internal
tags: [personal-office, approvals]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, enrich]
requires_human_review: false
do_not_load_raw: true
---

# Approval Rules

Human approval is required before:

- external sends;
- money movement or finance categorization writes;
- health or medication decisions;
- legal/compliance claims;
- publishing;
- credential/access changes;
- broad raw-data access;
- destructive or irreversible actions;
- project-space creation outside Personal Office.
