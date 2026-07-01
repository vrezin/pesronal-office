---
id: memory-protocol-concept-types
type: Playbook
title: Memory Concept Types
description: Supported concept types for Personal Office protocol-managed memory.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - memory/protocol/metadata-contract.md
confidence: high
sensitivity: internal
tags: [memory, concept-types]
review_after: 2026-09-28
---

# Memory Concept Types

Consumers must tolerate unknown future types, but new protocol-managed files should use one of these first.

## Navigation And Process

- `RouteMap` - domain/source routing.
- `Playbook` - reusable procedure.
- `Skill` - short agent router.
- `Workflow` - command or repeated operating flow.
- `Runbook` - operational steps for tools or services.
- `Connector` - source/tool integration boundary.
- `ApprovalRule` - human approval requirement.

## Context And Entities

- `ContextCard` - compact reusable context for a domain, company, project, or tool.
- `Contact` - person/contact memory.
- `Company` - company memory.
- `ProjectContour` - project/work contour and source-of-truth route.
- `Tool` - local tool or service.

## Decisions And Signals

- `Decision` - durable decision and evidence.
- `Risk` - reusable risk context.
- `Handoff` - owner-to-project or project-to-owner context package.
- `ValidationSignal` - market/product/user feedback signal.
- `ProductFrame` - product positioning or architecture frame.

## Type Guidance

Use the narrowest type that matches the artifact's purpose. If the artifact is mostly a route, use `RouteMap` or `ContextCard`; if it records a market reaction, use `ValidationSignal`; if it records a reusable procedure, use `Playbook` or `Workflow`.
