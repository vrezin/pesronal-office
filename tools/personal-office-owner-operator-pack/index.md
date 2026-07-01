---
id: personal-office-owner-operator-pack
type: Workflow
title: Personal Office Owner Operator Pack
description: OKF-like workflow pack for owner and trusted-operator Personal Office workflows.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - inbox/processed/2026-06-25-anthropic-knowledge-work-plugins-personal-office-analysis.md
  - inbox/processed/2026-06-28-google-okf-personal-office-relevance.md
confidence: high
sensitivity: internal
tags: [personal-office, owner-operator, workflow-pack]
review_after: 2026-09-28
schema_version: memory-os-v1
agent_read_policy: index_first
allowed_operations: [use, enrich, change, retire]
requires_human_review: false
do_not_load_raw: true
---

# Personal Office Owner Operator Pack

This pack defines repeatable workflows for the owner/trusted-operator contour. It is a navigation and command contract, not a new source of truth.

## Commands

- `commands/find-context.md` - locate source-backed context without broad raw-data reads.
- `commands/weekly-control.md` - prepare owner-control brief from tasks, waiting items, meetings, people, and company signals.
- `commands/meeting-to-state.md` - convert meeting/transcript/email thread into lanes, artifacts, tasks, and handoffs.
- `commands/project-envelope.md` - turn new sustained activity into owner-side project envelope.
- `commands/operator-onboard.md` - onboard a trusted assistant/operator to Personal Office boundaries.
- `commands/memory-retire.md` - retire stale/superseded memory safely.

## Boundaries

- Read maps and indexes before source artifacts.
- Keep sensitive sources read-only unless explicitly approved.
- Create durable artifacts, not chat-only outcomes.
- Use `approvals/index.md` before external sends, money, health, legal, access, or sensitive personal changes.
