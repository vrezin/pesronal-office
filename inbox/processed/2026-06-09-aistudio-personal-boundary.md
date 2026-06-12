# 2026-06-09 - AI Studio vs Personal Office Boundary

## Source

User input about separating non-AI-Studio personal material from `<aistudio-root>` into the new `personal-office` repository.

## Decision

`aistudio` should remain the company / studio / portfolio truth for AI Studio work.

`personal-office` should become the personal operating layer: what Vladimir needs to do as a person, owner, founder, family member, consultant, or project lead.

Company repositories answer:

> Where is the official working truth of the company or product?

`personal-office` answers:

> What do I personally need to decide, do, remember, follow up on, or schedule?

## Initial Routing

| Current item | Observed source | Target handling |
|---|---|---|
| `personal-brand-vladimir-rezin/` | `<aistudio-root>/personal-brand-vladimir-rezin` | Moved to `<repo-root>/personal-projects/personal-brand/workspace`; manage from `personal-office/personal-projects/personal-brand/` unless later split into a dedicated repo. |
| `vladimir-rezin-ai-automation-portfolio/` | `<aistudio-root>/vladimir-rezin-ai-automation-portfolio` | Moved to `<repo-root>/personal-projects/ai-automation-portfolio/site`; can later become a dedicated public/static site repo. |
| `country house/` | `<aistudio-root>/country house` | Moved to `<repo-root>/life/home-family-rest/country-house/repo`; preserve nested git repository. |
| AI Studio docs, MedVoice, AI board, tools | `<aistudio-root>` | Keep in `aistudio` unless a later review proves a file is personal rather than company/studio material. |

## Important Observation

`<repo-root>/life/home-family-rest/country-house/repo` is already a git repository with many untracked files. Preserve it as a nested repo unless a later cleanup explicitly flattens it.

The root `<aistudio-root>` also appears to have many untracked directories. Any physical migration should be done as a deliberate migration task with before/after checks.

## Physical Migration

Completed on 2026-06-09:

- `<aistudio-root>/personal-brand-vladimir-rezin` -> `<repo-root>/personal-projects/personal-brand/workspace`
- `<aistudio-root>/vladimir-rezin-ai-automation-portfolio` -> `<repo-root>/personal-projects/ai-automation-portfolio/site`
- `<aistudio-root>/country house` -> `<repo-root>/life/home-family-rest/country-house/repo`

Tombstone README files were left at the old AI Studio paths.

## Follow-Up

Created migration task:

- `tasks/done/2026-06-09-migrate-non-aistudio-assets.md`
