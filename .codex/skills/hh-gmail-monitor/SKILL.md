---
name: hh-gmail-monitor
description: "Use for scheduled scanning of Gmail messages from HH.ru: update related job-search tasks, promote interview invitations, archive and analyze new vacancies, and maintain job-intake indexes."
metadata:
  short-description: Monitor HH.ru email from Gmail
---

# HH Gmail Monitor

## Goal

Every scheduled run checks Gmail for HH.ru messages since the last successful scan and turns them into durable Personal Office artifacts.

## Required Sources

- Gmail messages from HH.ru / HeadHunter.
- `automation/state/hh-gmail-monitor-state.md`
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`
- `tasks/active/`
- `tasks/waiting/`

## Message Classes

Classify each relevant HH email as one of:

- `status_update`: employer viewed/responded/rejected/resumed/later/closed/no longer available.
- `invitation`: interview invitation, screening request, test task, recruiter wants a call, employer asks to continue.
- `new_vacancy`: vacancy recommendation, saved-search digest, "new vacancies", or role text/link not yet reviewed.
- `noise`: generic promo, duplicate, already processed, or unrelated HH mail.

## Workflow

1. Load `automation/state/hh-gmail-monitor-state.md` and scan only messages newer than the saved marker, plus a small overlap window when the connector supports it.
2. Search Gmail for HH sender/domain and Russian/English HH job-search terms. Prefer unread/recent messages, but do not rely only on unread status.
3. For every relevant message, record enough metadata in the run log: date, subject, sender, Gmail message id if available, class, related vacancy/company, and action taken.
4. For `status_update`, find the related analysis/task by company, role, HH vacancy title, or prior thread subject. Update the relevant `tasks/active/` or `tasks/waiting/` item and the corresponding `job-intake/analyses/*.md` status section when there is a material change.
5. For `invitation`, update the related task to active or high-priority waiting, create a task if missing, and mark the Gmail message as starred/important when the connector permits message mutation. Do not silently drop an invitation if the related vacancy is unclear; create a clarification note.
6. For `new_vacancy`, extract the JD text available in the email. If the email only contains a link or thin digest snippet, save a raw intake note and mark it as needing source text before full analysis. If enough text is present, use `job-intake-analysis`, then `career-offer-life-economics`, `vacancy-history-indexing`, and `job-intake-company-notes`.
7. Update `automation/state/hh-gmail-monitor-state.md` only after successfully processing the batch.
8. Save a run log to `automation/runs/YYYY-MM-DD-HHMM-hh-gmail-monitor.md`.

## Routing Rules

- New JD archive: `personal-projects/personal-brand/workspace/job-intake/jd-archive/`.
- New JD analysis: `personal-projects/personal-brand/workspace/job-intake/analyses/`.
- Reviewed-vacancy history: `personal-projects/personal-brand/workspace/job-intake/INDEX.md`.
- Company/bucket memory: `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`.
- Active user action: `tasks/active/`.
- Waiting for employer/recruiter: `tasks/waiting/`.
- Ambiguous or insufficient email: `inbox/processed/needs-clarification-YYYY-MM-DD-hh-gmail.md`.
- Scheduled run evidence: `automation/runs/`.

## Priority Rules

- Interview invitations and recruiter requests outrank vacancy recommendations.
- Employer responses on already-applied roles outrank fresh cold vacancies.
- New vacancies are ranked by practical fit, compensation/relocation economics, family logistics, and strategic career value.
- Missing salary must trigger market-rate or target-income analysis if the role is otherwise interesting.

## Safety

- Do not invent JD details missing from email.
- Do not treat a digest snippet as a full JD.
- Do not mark an email as processed if artifact updates failed.
- Do not browse HH pages unless the user explicitly allows it or the execution environment has authenticated access.
- If Gmail access is unavailable, write a blocked run log and leave the state marker unchanged.
