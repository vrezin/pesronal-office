---
id: memory-protocol-retirement-policy
type: Playbook
title: Memory Retirement Policy
description: Rules for marking Personal Office memory stale, superseded, retired, or archived.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - memory/protocol/lifecycle.md
confidence: high
sensitivity: internal
tags: [memory, retirement]
review_after: 2026-09-28
---

# Memory Retirement Policy

Retirement prevents stale context from steering agents incorrectly.

## Status Meanings

- `active` - usable for routing or context.
- `stale` - may be outdated; verify before use.
- `superseded` - replaced by another concept; follow `superseded_by`.
- `retired` - should not guide future work except as history.
- `archived` - preserved for historical/reference reasons.

## When To Retire

Retire or mark stale when:

- a source artifact says the fact is no longer true;
- the route moved;
- a project ended;
- a person/company relationship changed materially;
- a better concept card replaces an old summary;
- the memory is too vague to guide agents safely.

## Required Metadata

For `superseded`:

```yaml
status: superseded
superseded_by: new-id-or-path
retired_reason: Replaced by newer source-backed concept.
```

For `retired` or `archived`:

```yaml
status: retired
retired_reason: Short reason
```

Never delete v1 history just to make indexes cleaner.
