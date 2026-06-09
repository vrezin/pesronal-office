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
- `job-intake/README.md`
- `job-intake/rules-draft.md`
- `job-intake/jd-analysis-template.md`
- `resume-targets/master-profile.md`
- `final-cv/README.md`

## Workflow

1. Save the full JD to `job-intake/jd-archive/YYYY-MM-DD-company-role.md`.
2. Save analysis to `job-intake/analyses/YYYY-MM-DD-company-role-analysis.md`.
3. Use `job-intake/jd-analysis-template.md` as the analysis structure.
4. If company is unknown, use `unknown-company` in the filename.
5. If the user pasted screening questions rather than a full JD, answer directly and append Q/A to the relevant analysis when one exists.

## Chat Output

Answer briefly in Russian unless asked otherwise:

- verdict: apply / apply after adaptation / maybe / low priority / risky / already rejected;
- best CV;
- match reasons;
- risks;
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
