---
id: memory-protocol-metadata-contract
type: Playbook
title: Memory Metadata Contract
description: OKF-inspired metadata contract for protocol-managed Personal Office memory.
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - inbox/processed/2026-06-28-google-okf-personal-office-relevance.md
confidence: high
sensitivity: internal
tags: [memory, metadata, okf]
review_after: 2026-09-28
---

# Memory Metadata Contract

This contract is for new protocol-managed memory and workflow files. Existing repository artifacts remain valid without this metadata until they are touched or migrated.

## Universal Required Fields

```yaml
---
id: stable-kebab-case-id
type: ContextCard
title: Human-readable title
description: One-sentence summary
status: active
created: 2026-06-28
updated: 2026-06-28
source_refs:
  - path/or/external-uri
confidence: high
sensitivity: internal
tags: [personal-office]
---
```

## Known Values

`status`:

- `active`
- `stale`
- `superseded`
- `retired`
- `archived`

`confidence`:

- `high`
- `medium`
- `low`
- `unknown`

`sensitivity`:

- `public`
- `internal`
- `sensitive`
- `restricted`

## Optional Lifecycle Fields

```yaml
review_after: 2026-09-28
retention_policy: keep
supersedes:
  - old-id
superseded_by: new-id
retired_reason: Short reason
```

## Optional Navigation Fields

```yaml
canonical_path: memory/semantic/topics/example.md
owned_by_domain: memory-system
source_of_truth:
  - companies/example/context.md
related:
  - other-id
depends_on:
  - route-or-concept-id
```

## Optional Agent-Use Fields

```yaml
agent_read_policy: summary_first
allowed_operations: [use, enrich]
requires_human_review: false
do_not_load_raw: true
```

Use `requires_human_review: true` for money, health, legal/compliance, external sends, access, or sensitive personal facts.

## Optional Product Fields

```yaml
schema_version: memory-os-v1
portable: true
export_class: private
support_mode: client-controlled
```

These fields are for future Private AI Office packaging and export/support flows.
