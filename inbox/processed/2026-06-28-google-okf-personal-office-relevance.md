# 2026-06-28 Google OKF / Personal Office Relevance

- Raw note: `inbox/raw/2026-06-28-google-open-knowledge-format-signal.md`
- Source article: `https://www.frandroid.com/marques/google/3145563_open-knowledge-format-pourquoi-le-nouveau-format-de-google-fait-du-bruit`
- Primary sources:
  - Google Cloud announcement: `https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing`
  - OKF repository: `https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf`
  - OKF v0.1 spec: `https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md`
- Related local task: `tasks/active/2026-06-25-prototype-personal-office-role-workflow-pack.md`

## Summary

Yes, OKF is relevant to Personal Office, but not as a wholesale migration or urgent rewrite.

The useful import is a compact convention for making Personal Office knowledge more agent-readable:

```text
directory of markdown files
-> YAML frontmatter
-> one concept per file
-> index.md for progressive disclosure
-> log.md for local history
-> markdown links as graph edges
-> permissive consumers that tolerate unknown types and broken links
```

Personal Office already follows much of this informally:

- `wiki/maps/` route agents to domains;
- `memory/` stores retrievable context;
- `people/contacts/` stores person dossiers;
- `companies/*/context.md` can act like compact company concept cards;
- `tools/raspberrypi-openclaw/personal-office-context-pack.md` is already a cookbook / routing context pack;
- project handoffs are markdown artifacts with links.

OKF's value is to make that pattern explicit and portable.

## Why It Matters

The Frandroid article frames OKF as "Markdown for AI agents": a simple way to organize internal knowledge so agents can navigate it without dumping everything into context.

Google's own framing is stronger:

- OKF formalizes the LLM-wiki pattern;
- it is vendor-neutral and not tied to Google Cloud;
- it uses markdown files plus YAML frontmatter;
- it is meant for metadata, context and curated knowledge around data and systems;
- the format is the contribution, not the reference tools.

This matches an existing Personal Office need:

> Agents need a map, not the whole office in context.

That is exactly the same direction as the Raspberry Pi / OpenClaw cookbook-only boundary.

## What To Adopt

### 1. Minimal Frontmatter For Agent-Readable Concepts

Start adding OKF-compatible frontmatter to new durable context artifacts where useful:

```yaml
---
type: PersonalOfficeConcept
title: Short human title
description: One-sentence summary
resource: <optional canonical source path or URI>
tags: [personal-office, routing]
timestamp: 2026-06-28T00:00:00+07:00
---
```

Do this first for:

- company context cards;
- people/contact dossiers;
- tool/runbook concepts;
- workflow-pack commands;
- project-envelope templates;
- Private AI Office product frames;
- reusable playbooks.

Do not force this onto every daily note, raw inbox item or transient task yet.

### 2. `index.md` As Progressive Disclosure

OKF's `index.md` pattern is directly useful.

Personal Office should prefer:

```text
open map/index -> choose narrow concept -> read only needed file
```

over:

```text
scan broad repo -> load too much context -> infer route from noise
```

This reinforces:

- `wiki/README.md`;
- `wiki/maps/`;
- `.codex/skills/` as small routers;
- Raspberry Pi cookbook-only context packs.

### 3. `log.md` For Important Knowledge Bundles

Use `log.md` only for bundles where history matters:

- `tools/raspberrypi-openclaw/`;
- `memory/knowledge-graph/`;
- future `tools/personal-office-owner-operator-pack/`;
- `companies/future-companies/private-ai-office` if that becomes a folder.

Do not add logs everywhere.

### 4. A Personal Office OKF Subset

Define a local subset rather than importing Google's examples literally.

Suggested concept types:

- `RouteMap`
- `Playbook`
- `Skill`
- `Command`
- `Connector`
- `ApprovalRule`
- `ContextCard`
- `Contact`
- `Company`
- `ProjectContour`
- `Handoff`
- `Decision`
- `Risk`
- `Runbook`
- `ProductFrame`
- `ValidationSignal`

Consumers should tolerate unknown types.

### 5. OKF Bundle For The Owner-Operator Pack

The best first prototype is not converting the whole repo.

Create a small OKF-like bundle for:

```text
personal-office-owner-operator-pack
```

It should contain:

- `index.md`;
- `commands/weekly-control.md`;
- `commands/find-context.md`;
- `commands/meeting-to-state.md`;
- `commands/project-envelope.md`;
- `commands/operator-onboard.md`;
- `connectors/index.md`;
- `approvals/index.md`;
- `log.md`.

This directly supports the Anthropic workflow-pack analysis.

## What Not To Do

- Do not migrate all existing Personal Office documents to OKF now.
- Do not treat OKF as SEO, public web publishing or schema.org replacement.
- Do not publish private OKF bundles.
- Do not copy Google BigQuery-centric sample types into Personal Office.
- Do not create a second source of truth parallel to current artifacts.
- Do not require every note to have frontmatter before it can be useful.

## Product Implication

For Private AI Office, OKF is useful as part of the "client-controlled but supportable" story:

> Client knowledge lives as portable, versioned, human-readable, agent-readable files, not as opaque provider memory.

This reinforces:

- provider-not-readable deployment;
- client-held context;
- supportable workflow packs;
- migration/export story;
- assistant/operator onboarding;
- graph visualization of concepts without exposing raw data externally.

## Recommendation

Adopt OKF as a lightweight compatibility convention for new knowledge bundles and workflow packs.

Priority:

1. Add OKF subset guidance to the Personal Office role workflow pack task.
2. Prototype the owner-operator pack as an OKF-like bundle under `tools/`.
3. Add frontmatter to new context cards and command docs only.
4. Later consider a small validator/indexer that checks `type`, broken links, timestamps and index coverage.

Decision:

> We need the pattern, not a repo-wide migration.

