# Migrate Non-AI-Studio Assets Out Of Aistudio

Status: Done
Created: 2026-06-09
Area: personal-office / aistudio boundary
Owner: Vladimir
Due:

## Context

Some directories previously under `<aistudio-root>` were personal rather than AI Studio company material.

The first routing pass identified:

- `<aistudio-root>/personal-brand-vladimir-rezin`
- `<aistudio-root>/vladimir-rezin-ai-automation-portfolio`
- `<aistudio-root>/country house`

## Desired Outcome

AI Studio contains only studio/company/product/portfolio material.

Personal material is moved into `personal-office` with clear pointers from old AI Studio paths.

## Proposed Target State

- Personal brand working files: moved to `personal-office/personal-projects/personal-brand/workspace/`, with the management index in `personal-office/personal-projects/personal-brand/`.
- AI automation portfolio static site: moved to `personal-office/personal-projects/ai-automation-portfolio/site/`, with the management index in `personal-office/personal-projects/ai-automation-portfolio/`.
- Country house: moved to `personal-office/life/home-family-rest/country-house/repo/`, preserving its existing nested git repository.
- AI Studio company truth: remains in `<aistudio-root>`.

## Result

Completed physical migration on 2026-06-09.

Tombstone README files were left at old locations under `<aistudio-root>`.

## Follow-Up

- Decide later whether the AI automation portfolio site should become a dedicated standalone repo.
- Decide later whether `country-house/repo` should remain nested or be promoted to a separate top-level personal repo.

## Evidence

Routing decision captured in `inbox/processed/2026-06-09-aistudio-personal-boundary.md`.
