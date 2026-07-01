---
id: po-weekly-control
type: Workflow
title: /po:weekly-control
description: Prepare an owner-control brief across active work, waiting items, meetings, people, companies, and stale decisions.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - inbox/processed/2026-06-25-anthropic-knowledge-work-plugins-personal-office-analysis.md
confidence: high
sensitivity: internal
tags: [personal-office, command, weekly-control]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, enrich, change]
requires_human_review: true
do_not_load_raw: true
---

# /po:weekly-control

## Purpose

Produce a weekly owner-control brief: what needs attention, what is waiting, what is blocked, what is stale, and what should be ignored.

## Inputs

- `tasks/active/`
- `tasks/waiting/`
- `calendar/meetings/`
- relevant `companies/`, `people/`, `inbox/processed/`, and `memory/` summaries.

## Procedure

1. Start from `memory/retrieval/index.md` and relevant wiki maps.
2. Collect active/waiting/stale signals.
3. Identify decisions, promises, blocked items, and follow-ups.
4. Draft updates to canonical artifacts.
5. Ask for review before changing sensitive or external-facing state.

## Output

- Owner-control brief.
- Suggested task/waiting updates.
- Context handoff requests.
- Optional daily/weekly plan artifact.
