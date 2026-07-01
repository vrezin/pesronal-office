---
id: po-project-envelope
type: Workflow
title: /po:project-envelope
description: Convert a new sustained activity into an owner-side project envelope and optional generated project space.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - tools/project-bootstrapper/README.md
confidence: high
sensitivity: internal
tags: [personal-office, command, project-bootstrapper]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, enrich, create]
requires_human_review: true
do_not_load_raw: true
---

# /po:project-envelope

## Purpose

Create a routeable owner-side envelope for a new project, business, client request, or sustained activity.

## Output

- Processed trace or owner envelope.
- Source references.
- Candidate route.
- Missing context and blockers.
- Optional `tools/project-bootstrapper/` dry-run command.

## Approval

User approval is required before creating a new project space outside Personal Office.
