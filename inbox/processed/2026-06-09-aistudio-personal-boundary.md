# 2026-06-09 - AI Studio vs Personal Office Boundary

## Source

User input about separating non-AI-Studio personal material from `/home/adre/projects/aistudio` into the new `personal-office` repository.

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
| `personal-brand-vladimir-rezin/` | `/home/adre/projects/aistudio/personal-brand-vladimir-rezin` | Move out of `aistudio`; manage from `personal-office/personal-projects/personal-brand/` unless later split into a dedicated repo. |
| `vladimir-rezin-ai-automation-portfolio/` | `/home/adre/projects/aistudio/vladimir-rezin-ai-automation-portfolio` | Split into a dedicated public/static site repo; keep only tasks and planning notes in `personal-office`. |
| `country house/` | `/home/adre/projects/aistudio/country house` | Treat as personal/family home project; target home is `personal-office/life/home-family-rest/country-house/` or a separate repo referenced from there. |
| AI Studio docs, MedVoice, AI board, tools | `/home/adre/projects/aistudio` | Keep in `aistudio` unless a later review proves a file is personal rather than company/studio material. |

## Important Observation

`/home/adre/projects/aistudio/country house` is already a git repository with many untracked files. Do not move it casually as a plain folder without first deciding whether to preserve it as a separate repo.

The root `/home/adre/projects/aistudio` also appears to have many untracked directories. Any physical migration should be done as a deliberate migration task with before/after checks.

## Follow-Up

Created migration task:

- `tasks/active/2026-06-09-migrate-non-aistudio-assets.md`
