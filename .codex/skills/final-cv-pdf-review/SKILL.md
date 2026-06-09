---
name: final-cv-pdf-review
description: Use when the user uploads, exports, validates, or asks to save a final PDF resume/CV. Checks PDF page/text/layout, risky markers, and updates the final CV inventory.
metadata:
  short-description: Review and register final CV PDFs
---

# Final CV PDF Review

## Workspace

`<repo-root>/personal-projects/personal-brand/workspace`

Final PDFs live in:

`final-cv/`

## Workflow

1. Use `pdfinfo` to check page count.
2. Use `pdftotext -layout` to inspect extracted text.
3. Use `pdftoppm` plus visual inspection when layout matters.
4. Check for forbidden or risky markers:
   - `RTK`
   - `150k` where canonical scale should not use it
   - wrong `3k` / `30k` style scale references
   - `20+ years`, `23+ years`, `26+ years` where HH/ATS risk matters
   - wrong education year
   - recommendations bloat
5. If OK, save/copy to `final-cv/` with a stable filename.
6. Update `final-cv/README.md` with title, filename, target use, HH experience years, important exclusions, and save date.

## Canonical Checks

Inspect `resume-targets/master-profile.md` before correcting facts.

Do not invent missing education dates or metrics. If the user wants HH validator compliance, note that `1998` has been treated as preferable to a false education year.

## Output

Report:

- pass/fail;
- page count;
- risky markers found or absent;
- file saved/updated;
- any remaining manual check needed.
