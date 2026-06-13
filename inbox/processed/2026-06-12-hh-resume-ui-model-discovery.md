# HH Resume UI Model Discovery

Date: 2026-06-12

## Context

User wanted to validate the current HH resume editing model before building resume-generation and resume-management automation.

Working hypothesis before discovery:

- HH has a profile-level experience block library.
- Individual resumes can include or exclude reusable experience blocks.

## Method

Authenticated headless Playwright session using local HH cookies from `tools/headhunter-web-mcp`.

Additional evidence: user-provided browser screenshot from `novosibirsk.hh.ru/profile/me?hhtmFrom=ProfileActivator`.

No submit/save actions were performed.

Checked:

- `https://hh.ru/profile/me?hhtmFrom=ProfileActivator`
- `https://hh.ru/applicant/resumes`
- `https://hh.ru/resume/<resume_hash>`
- `https://hh.ru/resume/edit/<resume_hash>/position`
- `https://hh.ru/resume/edit/<resume_hash>/experience`
- `https://hh.ru/resume/edit/<resume_hash>/about`
- `https://hh.ru/resume/edit/<resume_hash>/keySkills`
- `https://hh.ru/profile/edit/primaryEducation?resumeFrom=<resume_hash>&hhtmFrom=resume`

## Findings

- The first headless pass against `https://hh.ru/profile/me` exposed contacts, search status, education, driving, and languages, but did not expose work experience.
- User screenshot from `novosibirsk.hh.ru/profile/me?hhtmFrom=ProfileActivator` does expose profile-level work experience:
  - "Опыт работы: 23 года и 10 месяцев";
  - profile-level `+ Добавить`;
  - company grouping under `ООО Финкомтех`;
  - multiple separate `CTO / сооснователь` blocks for the same period;
  - per-block edit pencil controls.
- Resume view exposes partial edit actions for title/position, contacts, skills, education, and about.
- Add work experience opens `https://hh.ru/resume/edit/<resume_hash>/experience`.
- Work-experience form fields observed:
  - `resume-editor-experience-company-input`
  - `resume-editor-experience-position-input`
  - `resume-editor-experience-start-year-input`
  - `resume-editor-experience-end-year-input`
  - `resume-editor-experience-description-input`
  - `resume-partial-edit-cancel`
  - `resume-partial-edit-save`
- The add-experience form did not show resume inclusion checkboxes.
- Education edit is profile-level and did show resume inclusion checkboxes under "Резюме с этим учебным заведением".

## Current Conclusion

The safest current model is:

- repo holds the canonical planning library for targeted blocks;
- HH profile is the live profile-level experience block library;
- HH resumes are publication targets assembled from profile/resume data;
- direct resume edit routes still exist and may be resume-scoped;
- HH profile-level reuse is confirmed for education and profile-level experience exists visually;
- the exact resume linkage mechanics for profile-level experience still need mapping;
- write automation for HH resume fields should stay confirmation-gated.

## Follow-Up

Update `wiki/playbooks/hh-targeted-resume-block-library.md` with these UI facts.

Next discovery step: use the regional profile URL and inspect profile-level `+ Добавить` plus per-block pencil actions for experience, without saving, to learn whether HH exposes resume inclusion checkboxes for experience blocks.

## Automation Attempt

Later on 2026-06-12, an authenticated headless Playwright attempt against `https://novosibirsk.hh.ru/profile/me?hhtmFrom=ProfileActivator` did not render the work-experience section that is visible in the user's normal Chrome screenshot.

Observed behavior:

- headless page saw profile top sections and footer, but not "Опыт работы";
- `text=Добавить` controls were detected for other profile sections, but interaction timed out;
- after an interaction attempt, HH returned a `DDOS-GUARD` page.

Implication:

- profile-level experience exists, but the current headless route is blocked or incomplete;
- next automation attempt should either reuse a less-detectable browser/profile setup or drive the already-authenticated visible browser/session rather than plain headless Playwright.
