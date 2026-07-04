# Pi Job Search Handoff Dispatch - LinkedIn 4436302720

- Run time: 2026-07-04 19:22:20 Asia/Novosibirsk
- Agent: `job-search`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md`
- LinkedIn job id: `4436302720`
- Source URL: `https://www.linkedin.com/jobs/view/4436302720/`

## Narrow Identifier Search

Searched exact LinkedIn job id `4436302720` in:

- `inbox/processed/`
- `automation/runs/`
- `personal-projects/personal-brand/workspace/job-intake/processed/`

Existing durable artifacts found:

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-techmunity-head-software-engineering.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-techmunity-head-software-engineering-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`

## Live LinkedIn Check

Called LinkedIn MCP `get_job_details` once for job id `4436302720`.

The returned `sections.job_posting` is not thin. It includes:

- header: `Techmunity | AI Startup Recruitment`, `Head of Software Engineering`, UK, 2 days ago, 98 applicants;
- compensation and logistics: `100K GBP/yr - 120K GBP/yr`, remote, full-time, easy apply;
- full JD marker: `Об этой вакансии`;
- substantive role body: `Head of Engineering (route to CTO) | UK, Remote First | £120K equity`;
- company body: UK AI startup, Imperial/Cambridge founders, bootstrapped to GBP 1M ARR and profitability, GBP 2.7M seed;
- product/problem body: fragmented mobility data from cameras, sensors and roadside infrastructure, data platform engineering, geospatial modelling and AI recommendations;
- role/scope body: hands-on code, spikes, architecture, release lifecycle, lightweight people management, 7 IC team, AI-generated code and agentic systems;
- requirements body: Seed to Series A/B B2B SaaS scaling, managed 5+ engineers, data-volume/modelling product ownership, customer-facing AI shipped in last 18 months, daily AI coding tools, enterprise customer calls, React/TypeScript/Python/FastAPI/Dagster/dbt/Snowflake/AWS comfort;
- compensation/logistics body: GBP 100,000-120,000 base, 0.5-0.75% equity, UK-based remote, 2-4 in-person team days per month in London or Bristol.

Because the current artifacts already archive and analyze this full JD, no duplicate JD archive or analysis was created.

## Existing Decision

- Company / recruiter: Techmunity | AI Startup Recruitment
- Role: Head of Software Engineering / Head of Engineering route to CTO
- Verdict: clarify first / likely no-go unless UK logistics are workable
- Effort class: B-class content, low practical probability
- Recommended CV if applying: `personal-projects/personal-brand/workspace/final-cv/CTO - Co-founder CTO - Head of Product Engineering.pdf`
- Cover letter: not prepared; logistics should pass first
- Next action: clarify UK residence/right-to-work, London/Bristol team days, international B2B possibility from Novosibirsk, hands-on coding screen and route-to-CTO terms before CV/application effort.

## Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: "LinkedIn job 4436302720 is already fully archived and analyzed as Techmunity / unnamed UK AI mobility startup, Head of Software Engineering / Head of Engineering route to CTO."
verdict: maybe
reasons:
  - "Full LinkedIn JD is available and already archived/analyzed; no duplicate artifacts were created."
  - "Content match is plausible for startup/product engineering and AI-assisted engineering leadership."
  - "Main blocker is practical: UK-based remote with 2-4 London/Bristol team days per month, plus likely UK right-to-work/logistics and hands-on stack screens."
cv: "personal-projects/personal-brand/workspace/final-cv/CTO - Co-founder CTO - Head of Product Engineering.pdf"
cover_letter: null
next_action: "Clarify UK residence/right-to-work, London/Bristol team-day requirement, international B2B from Novosibirsk, and hands-on coding screen before applying."
artifacts:
  - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md"
  - "personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-techmunity-head-software-engineering.md"
  - "personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-techmunity-head-software-engineering-analysis.md"
  - "personal-projects/personal-brand/workspace/job-intake/INDEX.md"
  - "personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md"
blocked_on:
  - "Is UK residence/right-to-work mandatory, or is international B2B work from Novosibirsk possible?"
```
