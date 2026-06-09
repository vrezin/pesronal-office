---
name: vacancy-history-indexing
description: Use after creating, changing, or reviewing job-intake analyses to maintain the reviewed vacancy index with date, company, role, track, CV, decision, priority, next action, and analysis link.
metadata:
  short-description: Maintain reviewed vacancy index
---

# Vacancy History Indexing

## Artifact

`personal-projects/personal-brand/workspace/job-intake/INDEX.md`

## When To Use

- After saving a new JD analysis.
- After updating an existing analysis decision, CV, priority, or next action.
- Before analyzing a similar vacancy, to check prior decisions and repeated risks.

## Row Contract

Each reviewed vacancy needs one row:

- date;
- company;
- role;
- primary track;
- recommended CV;
- decision;
- priority;
- next action;
- link to `analyses/*.md`.

## Rules

- Keep this as an index, not a full duplicated analysis.
- Links must be repo-relative from `job-intake/`.
- If a company-level pattern emerges, use `job-intake-company-notes`.
- If the index schema changes, update `job-intake/README.md`, `OPERATING_MODEL.md`, wiki, memory, and skills.
