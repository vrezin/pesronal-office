# HH Vacancy 134845968 Job Search Dispatch

- Run date: 2026-07-04
- Source agent: `job-search`
- Trigger: Telegram direct intake handoff
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134845968-handoff.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram mutation: none
- Gmail / Calendar mutation: none
- Monitor state mutation: none
- Git commands: none

## Exact Identifier Extraction

- Source type: HH URL
- HH vacancy id: `134845968`
- URL: `https://novosibirsk.hh.ru/vacancy/134845968?from=applicant_recommended&hhtmFrom=main`
- Company: Норникель
- Role: Архитектор по ИИ (ML/AI/LLM)

## Duplicate Check

Exact id search was limited first to:

- `inbox/processed/`
- `automation/runs/`
- `personal-projects/personal-brand/workspace/job-intake/processed/`
- `personal-projects/personal-brand/workspace/job-intake/`

Matches found only in the intake handoff and dispatch stubs. No existing JD archive or analysis for vacancy `134845968` was found.

## Live Source Evidence

HH connector call:

- Tool: `headhunter_web.hh_web_get_vacancy`
- Input: `134845968`
- Result: success
- Returned source: `hh-web`
- Returned company: Норникель
- Returned role title: Архитектор по ИИ (ML/AI/LLM)
- Returned URL: `https://novosibirsk.hh.ru/vacancy/134845968`
- Returned application status: `unknown`
- Returned screening questions: none
- Returned extraction warnings: none

Substantive JD was present. It included AI/ML strategy, industrial production-process automation, scalable platform model, architecture governance, LLM inference, agent systems, MCP/tool integrations, guardrails, observability, MLOps/monitoring, Data Lake/ODS/data marts, АСУТП/production-system integrations, CI/CD and DevSecOps.

## Artifacts Written

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-nornickel-ai-architect-ml-ai-llm.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-nornickel-ai-architect-ml-ai-llm-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`
- `automation/runs/2026-07-04-hh-vacancy-134845968-job-search-dispatch.md`

## Decision

- Verdict: go
- Effort class: B+-class
- CV: `personal-projects/personal-brand/workspace/final-cv/AI Transformation Lead - AI Automation Architect.pdf`
- Cover letter: no separate file; short HH response text is embedded in analysis
- Next action: send existing AI Transformation CV with short response; clarify Moscow cadence, compensation and first-year mandate before tailoring

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: "HH vacancy 134845968 is a full Норникель AI/ML/LLM architect posting; JD archived and analysis created."
verdict: go
reasons:
  - "Strong content fit: AI/ML strategy, LLM inference, agent systems, MCP/tool integrations, architecture governance and production operation."
  - "Use existing AI Transformation CV first; no targeted package before recruiter interest."
  - "Main gates are Moscow hybrid cadence, hidden compensation and how deep the ML/GPU platform screen is."
cv: "personal-projects/personal-brand/workspace/final-cv/AI Transformation Lead - AI Automation Architect.pdf"
cover_letter: null
next_action: "Send existing AI Transformation CV and clarify Moscow cadence, compensation and first-year mandate."
artifacts:
  - "personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-nornickel-ai-architect-ml-ai-llm.md"
  - "personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-nornickel-ai-architect-ml-ai-llm-analysis.md"
  - "automation/runs/2026-07-04-hh-vacancy-134845968-job-search-dispatch.md"
blocked_on: []
```
