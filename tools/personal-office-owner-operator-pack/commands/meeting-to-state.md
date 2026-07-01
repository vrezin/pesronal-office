---
id: po-meeting-to-state
type: Workflow
title: /po:meeting-to-state
description: Convert a meeting, transcript, or email thread into routed lanes, artifacts, tasks, and handoffs.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - tools/raspberrypi-openclaw/personal-office-context-pack.md
confidence: high
sensitivity: internal
tags: [personal-office, command, meeting]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, enrich, create, change]
requires_human_review: true
do_not_load_raw: true
---

# /po:meeting-to-state

## Purpose

Turn messy meeting context into durable Personal Office state.

## Procedure

1. Preserve raw input only when the source itself matters.
2. Split mixed-context lanes before routing.
3. Extract facts, hypotheses, ideas, risks, people, projects, decisions, promises, dates, and next actions.
4. Route each lane to Personal Office, company, project, people, task, or waiting artifacts.
5. Create draft patch bundle or direct updates depending on sensitivity and user instruction.

## Output

- Meeting note or processed trace.
- Contact/company/project updates.
- Active or waiting tasks.
- Handoff envelope when execution belongs to another workspace.
