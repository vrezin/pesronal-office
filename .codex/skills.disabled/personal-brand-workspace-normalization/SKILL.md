---
name: personal-brand-workspace-normalization
description: Use when the personal-brand workspace feels inconsistent, duplicated, stale, or split across README, operating model, job intake, final CVs, resume targets, wiki, memory, and graph. Reviews source-of-truth order, fixes stale paths, reconciles CV portfolio statements, and records normalization decisions.
metadata:
  short-description: Normalize personal-brand workspace truth
---

# Personal Brand Workspace Normalization

## Start

Read:

- `personal-projects/personal-brand/workspace/OPERATING_MODEL.md`
- `personal-projects/personal-brand/workspace/README.md`
- `personal-projects/personal-brand/workspace/final-cv/README.md`
- `personal-projects/personal-brand/workspace/job-intake/README.md`
- `wiki/maps/personal-brand.md`

## Audit

Search for:

- stale paths: `personal-brand-vladimir-rezin`, absolute machine paths;
- outdated portfolio language: `4 резюме`, `4 основных`, `not finalized`;
- source-of-truth conflicts between `master-profile.md`, `final-cv/README.md`, job-intake docs, and skills;
- duplicated routing into `work/employment-search/`;
- missing wiki/memory/graph references after adding an operating artifact.

## Fix

1. Update the smallest set of docs that define current truth.
2. Preserve old analyses as history unless they now mislead current routing; add historical notes when needed.
3. Update `wiki/maps/personal-brand.md`, semantic memory, retrieval index, and graph if routing changed.
4. Add a decision note in `inbox/processed/YYYY-MM-DD-*.md`.

## Done

- No stale path or outdated portfolio marker remains, except explicit tombstone references.
- Source-of-truth order is clear.
- New routing is reflected in wiki, memory, graph, and relevant skills.
