---
name: job-intake-analysis
description: Use when the user pastes or describes a vacancy, job description, recruiter message, HH/LinkedIn role, or asks whether to apply. Saves the JD and an analysis artifact, chooses a CV, identifies risks, and drafts a concise response.
metadata:
  short-description: Archive and analyze job descriptions
---

# Job Intake Analysis

## Workspace

`<repo-root>/personal-projects/personal-brand/workspace`

Before analysis, inspect as needed:

- `OPERATING_MODEL.md`
- `job-intake/INDEX.md`
- `job-intake/COMPANY_NOTES.md`
- `job-intake/README.md`
- `job-intake/rules-draft.md`
- `job-intake/jd-analysis-template.md`
- `finance/personal-budget/career-relocation-baseline.md`
- `resume-targets/master-profile.md`
- `final-cv/README.md`

## Workflow

1. Save the full JD to `job-intake/jd-archive/YYYY-MM-DD-company-role.md`.
2. Save analysis to `job-intake/analyses/YYYY-MM-DD-company-role-analysis.md`.
3. Use `job-intake/jd-analysis-template.md` as the analysis structure.
4. Update `job-intake/INDEX.md` with one row: date, company, role, track, CV, decision, priority, next action, analysis link.
5. Update `job-intake/COMPANY_NOTES.md` when the intake changes company-level or bucket-level memory.
6. If company is unknown, use `unknown-company` in the filename.
7. If the user pasted screening questions rather than a full JD, answer directly and append Q/A to the relevant analysis when one exists.

## Chat Output

Answer briefly in Russian unless asked otherwise:

- verdict: apply / apply after adaptation / maybe / low priority / risky / already rejected;
- best CV;
- match reasons;
- risks;
- lifestyle / relocation / compensation;
- how to defuse risks;
- cover letter or screening answer if useful;
- questions to ask recruiter or hiring manager.

## Matching Defaults

- AI / GenAI / LLM / RAG / agents / AI implementation: AI Transformation CV.
- Early-stage / MVP / first customers / product roadmap / founding CTO: Startup / Product Engineering CV.
- Large engineering org / VP Engineering / Director Engineering / 50+ or 100+ engineers: Heavy Enterprise CV.
- Digital transformation / modernization / CIO transformation: Digital Transformation CV.
- Production stability / incidents / SDLC / CI/CD / quality gates / legacy modernization: Stability & Governance CV.
- Integrator / custom development / P&L / margin / client delivery / project portfolio: Business Unit CV or tailored version.

## Risk Handling

- For small hands-on roles, defuse overqualification and do not lead with `200+ people`.
- Avoid `20+ years`, `23+ years`, `26+ years` in HH/ATS-facing text unless explicitly useful for executive/direct search.
- Be honest about AI/ML, Web3, wallet, smart contract, GPU, or local inference gaps.
- Do not rely on inaccessible HH links; use pasted text as source of truth.
- Always add `Lifestyle / Relocation / Compensation`.
- If salary is missing, check current market rates for similar roles or clearly mark the estimate as unverified.

## Supporting Skills

- Use `vacancy-history-indexing` for `job-intake/INDEX.md`.
- Use `job-intake-company-notes` for `job-intake/COMPANY_NOTES.md`.
- Use `career-offer-life-economics` for relocation, lifestyle, market salary, and target-income analysis.
- Use `routing-sync` if this workflow adds new recurring artifacts or routes.
