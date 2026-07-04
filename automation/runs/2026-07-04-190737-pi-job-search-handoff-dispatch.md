# Pi Job Search Handoff Dispatch

- Started at: 2026-07-04T19:07:37+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram mutation: none
- Status: completed

## Result

- Completed at: 2026-07-04T19:07:37+07:00
- LinkedIn job id: `4436302720`
- Company: `Techmunity | AI Startup Recruitment`
- Role: `Head of Software Engineering`
- Location: `United Kingdom`
- Compensation: `100K GBP/yr - 120K GBP/yr`
- Work mode: `remote`
- Employment type: `full-time`
- Live source: LinkedIn details fetched once.
- Live source content level: posting shell only; no full JD/body exposed.
- Existing exact-id artifacts: intake handoff plus prior dispatch/run logs already record this job and the thin-source status.
- Decision: `no-op`

## Exact-ID Search

Searched exact LinkedIn job id `4436302720` in:

- `inbox/processed/`
- `automation/runs/`
- `personal-projects/personal-brand/workspace/job-intake/processed/`

Existing durable references found:

- `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md`
- `automation/runs/2026-07-04-1858-pi-job-search-handoff-dispatch.md`
- `automation/runs/2026-07-04-185817-pi-job-search-handoff-async.md`
- `automation/runs/2026-07-04-185817-pi-job-search-handoff-async-dispatch.md`
- `automation/runs/2026-07-04-190623-pi-job-search-handoff-async.md`
- `automation/runs/2026-07-04-1906-pi-job-search-handoff-dispatch.md`

## Thin LinkedIn Evidence

LinkedIn `sections.job_posting` was present and contained only:

- company and role header;
- location and recency/status fields;
- promoted/active-candidate-review status;
- applicant count;
- compensation range;
- remote/full-time/Easy Apply status;
- skill-match count;
- LinkedIn Premium upsell, hiring ad, footer, account/privacy/help, and language links.

Full JD markers missing from `sections.job_posting`:

- no `About this job` / `Об этой вакансии` section;
- no substantive role responsibilities;
- no company/team context beyond the company header;
- no requirements or qualifications paragraphs;
- no hiring process, reporting line, or logistics beyond remote/full-time and compensation;
- no benefits, tech stack, or product/domain details.

Because the live source still exposes only a posting shell and prior durable logs already record the same status, no JD archive, analysis artifact, CV, or cover letter was created.

## Secretary Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: "LinkedIn job 4436302720 is already recorded as Techmunity | AI Startup Recruitment, Head of Software Engineering, UK remote full-time; the live LinkedIn source still exposes only a posting shell."
verdict: no-op
reasons:
  - "Exact-id search found prior durable dispatch/run logs for this same LinkedIn job."
  - "Live LinkedIn lookup exposed header/status fields only, with no About this job section or substantive JD paragraphs."
  - "No new job evidence was available, so creating duplicate JD/archive/analysis artifacts would be noise."
cv: null
cover_letter: null
next_action: "Wait for a full JD, recruiter message, or changed LinkedIn posting body before preparing CV or reply."
artifacts:
  - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md"
  - "automation/runs/2026-07-04-1858-pi-job-search-handoff-dispatch.md"
  - "automation/runs/2026-07-04-190737-pi-job-search-handoff-dispatch.md"
blocked_on:
  - "Full job description is not available from the current LinkedIn source."
```
