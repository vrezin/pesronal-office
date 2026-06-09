# Migrate Non-AI-Studio Assets Out Of Aistudio

Status: Active
Created: 2026-06-09
Area: personal-office / aistudio boundary
Owner: Vladimir
Due:

## Context

Some directories currently under `/home/adre/projects/aistudio` are personal rather than AI Studio company material.

The first routing pass identified:

- `/home/adre/projects/aistudio/personal-brand-vladimir-rezin`
- `/home/adre/projects/aistudio/vladimir-rezin-ai-automation-portfolio`
- `/home/adre/projects/aistudio/country house`

## Desired Outcome

AI Studio contains only studio/company/product/portfolio material.

Personal material is moved into `personal-office` or split into dedicated personal repositories with clear pointers from `personal-office`.

## Proposed Target State

- Personal brand working files: managed by `personal-office/personal-projects/personal-brand/`, possibly later as a dedicated repo.
- AI automation portfolio static site: dedicated repo, with planning/tasks in `personal-office/personal-projects/ai-automation-portfolio/`.
- Country house: managed from `personal-office/life/home-family-rest/country-house/`, preserving its existing git history or explicitly deciding to flatten it.
- AI Studio company truth: remains in `/home/adre/projects/aistudio`.

## Next Step

Decide physical migration mode for each directory:

- move into `personal-office`;
- convert to a separate repo;
- leave in place and add a tombstone/index pointer.

## Waiting On

Decision on whether `country house` should remain its own git repository.

## Evidence

Routing decision captured in `inbox/processed/2026-06-09-aistudio-personal-boundary.md`.
