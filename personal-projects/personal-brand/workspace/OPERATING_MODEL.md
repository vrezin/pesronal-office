# Personal Brand Operating Model

Дата актуализации: 2026-06-09

Этот документ задает единую картину workspace: где источник правды, какие артефакты актуальны, как агент должен выбирать CV и куда сохранять новые входы.

## Source Of Truth Order

1. `resume-targets/master-profile.md` - канонические факты: роли, даты, метрики, формулировки, запреты и публичная политика.
2. `resume-targets/evidence-bank.md` - банк доказательств и метрик; если факт спорный, проверять здесь и в master-profile.
3. `final-cv/README.md` - актуальные финальные PDF и назначение каждой версии.
4. `job-intake/README.md` + `job-intake/rules-draft.md` - процесс разбора вакансий и выбора CV.
5. `positioning/brand-architecture.md` - стратегическое позиционирование и рынок.
6. `cv-originals/` и `source/` - доноры/архив, не источник актуальной публичной версии.

Если документы расходятся, для публичного CV побеждает `master-profile.md`, затем `final-cv/README.md`, затем текущий job-intake analysis.

## Current CV Portfolio

| Track | Final CV | Use When |
|---|---|---|
| AI Transformation | `final-cv/AI Transformation Lead - AI Automation Architect.pdf` | AI, GenAI, LLM, RAG, agents, AI implementation, AI transformation. |
| Startup / Product Engineering | `final-cv/CTO - Co-founder CTO - Head of Product Engineering.pdf` | Startup, scale-up, MVP, first customers, product roadmap, founding/fractional CTO. |
| Heavy Enterprise | `final-cv/CTO - VP Engineering - Director of Engineering.pdf` | CTO, VP Engineering, Director Engineering, large org, 50+/100+ engineers, platform scale. |
| Digital Transformation | `final-cv/Digital - Technology Transformation Director.pdf` | CIO/CTO transformation, modernization, operating model, business-process transformation. |
| Stability & Governance | `final-cv/CTO - Head of Engineering - Stability and Governance.pdf` | Production stability, technical debt, SDLC, CI/CD, quality gates, predictable delivery. |
| Business Unit / Integration | `final-cv/Director of Development - Business Unit Technical Leader.pdf` | Integrator, custom development, P&L, margin, enterprise implementation, presale, delivery portfolio. |

## Workspace Areas

- `source/` - raw HH/exported source text.
- `cv-originals/` - old resumes, cover letters, certificates, exports; donors only.
- `positioning/` - strategic market framing and feedback.
- `resume-targets/` - master profile, experience strategy, outlines, evidence bank.
- `final-cv/` - current final PDFs and registry.
- `job-intake/` - JD archive, analyses, matching rules, templates.

## Job Intake Flow

1. Save full JD to `job-intake/jd-archive/YYYY-MM-DD-company-role.md`.
2. Save analysis to `job-intake/analyses/YYYY-MM-DD-company-role-analysis.md`.
3. Select one primary CV from the current portfolio.
4. If needed, recommend a tailored copy, but do not fork facts from `master-profile.md`.
5. Capture next action in the analysis.

## Guardrails

- Do not invent facts, dates, stacks, metrics, education years, or domain experience.
- Do not reintroduce RTK.
- Do not use `20+ years`, `23+ years`, or `26+ years` in HH/ATS-facing text unless executive/direct-search context makes it useful.
- Do not treat `cv-originals/` as current truth.
- Do not create career artifacts in `work/employment-search/`.
