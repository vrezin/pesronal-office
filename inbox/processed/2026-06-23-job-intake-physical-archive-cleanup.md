# Job Intake Physical Archive Cleanup

Date processed: 2026-06-23
Status: processed

## Decision

Do not delete reviewed vacancy artifacts from `personal-projects/personal-brand/workspace/job-intake/`.

Instead, physically archive low-signal or closed artifacts into subdirectories while keeping `INDEX.md` and `COMPANY_NOTES.md` as the lookup surface.

## Archive Layout

Created / populated:

- `personal-projects/personal-brand/workspace/job-intake/analyses/closed/`
- `personal-projects/personal-brand/workspace/job-intake/analyses/parked/`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/closed/`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/parked/`

## Moved On 2026-06-23

- 33 analysis files moved to `analyses/closed/`.
- 19 analysis files moved to `analyses/parked/`.
- 31 JD archive files moved to `jd-archive/closed/`.
- 19 JD archive files moved to `jd-archive/parked/`.

Some closed analyses did not have a one-to-one JD archive file with the same slug, so the JD count is lower than the analysis count.

## Link Hygiene

Updated exact `analyses/...` and `jd-archive/...` references across markdown files after the move.

Validation:

- `INDEX.md`, `COMPANY_NOTES.md`, and `TODAY.md` had zero missing real job-intake links after the move.
- Remaining missing matches from the broad checker are template examples only, not broken artifact links.

## Rule Going Forward

- Keep active/live/waiting analyses and JD files at top level.
- Move rejected, closed, unavailable, explicit skip, or no-further-action items to `closed/`.
- Move C-class, market-signal, location-gated, long-shot, and no-active-pursuit items to `parked/`.
- Do not move an `applied / waiting` item just because it is weak; close or park it only after rejection, closure evidence, user decision, or stale-waiting policy.
