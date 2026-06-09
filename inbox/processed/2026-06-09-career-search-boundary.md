# 2026-06-09 - Career Search Boundary

## Decision

Job search and career positioning have one canonical source of truth:

- `personal-projects/personal-brand/`
- `personal-projects/personal-brand/workspace/job-intake/`
- `personal-projects/personal-brand/workspace/final-cv/`
- `wiki/maps/personal-brand.md`

## Boundary

`work/employment-search/` is only a tombstone/redirect. It exists to prevent old routing rules from recreating a duplicate job-search system.

## Rule

If input contains a vacancy, HH context, CV choice, cover letter, screening answer, recruiter communication, or career positioning, use `personal-brand-routing` and the personal-brand workspace.

Use `work/` only for factual current employment, role conditions, and contracts if a separate job actually appears.
