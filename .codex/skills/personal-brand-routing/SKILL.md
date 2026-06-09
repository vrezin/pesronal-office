---
name: personal-brand-routing
description: Use when work concerns Vladimir Rezin's personal brand, career positioning, HH profile, resumes, final CVs, job search process, JD archive, role positioning, or personal public portfolio routing. This skill routes work to the moved personal-office workspace and prevents use of stale AI Studio paths.
metadata:
  short-description: Route personal brand and career work
---

# Personal Brand Routing

## Canonical Location

Use this workspace, not the old AI Studio path:

`<repo-root>/personal-projects/personal-brand/workspace`

The old path `<aistudio-root>/personal-brand-vladimir-rezin` is only a tombstone pointer.

## First Files To Inspect

- `OPERATING_MODEL.md` for source-of-truth order and current CV portfolio.
- `README.md` for the workspace map.
- `resume-targets/master-profile.md` for canonical facts, dates, metrics, and exclusions.
- `resume-targets/experience-block-strategy-ru.md` for experience block framing.
- `final-cv/README.md` for current final CV inventory.
- `job-intake/README.md` and `job-intake/rules-draft.md` for vacancy processing.

## Routing

- Vacancy/JD pasted by the user: use `job-intake-analysis`.
- "Which resume/CV should I use?": use `cv-selection`.
- Cover letter or bot screening answers: use `cover-letter-screening`.
- Final PDF resume review or import: use `final-cv-pdf-review`.
- Public personal site work: route to `<repo-root>/personal-projects/ai-automation-portfolio/site`.

## Guardrails

- Do not invent facts, dates, stacks, education years, or domain experience.
- Do not reintroduce RTK.
- Do not browse HH by default; HH pages often require auth/context. Ask for pasted JD text, screenshot, or exported page if needed.
- Preserve important decisions and analyses in the repo, not only in chat.
