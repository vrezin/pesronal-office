# Pi Job Search Handoff Dispatch

- Started at: 2026-07-04T18:16:24+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram mutation: none
- Status: blocked/clarify

## Exact Source Facts

- Source: Telegram direct intake
- Source type: `plain_hh_vacancy_link`
- HH vacancy id: `134804503`
- URL: `https://novosibirsk.hh.ru/vacancy/134804503?utm_source=hh-chatbot&utm_campaign=push_recommend_vacancy_no_image&utm_medium=chatbot_tg`
- Company: inferred from handoff filename as `Emphasoft`
- Role: not available from this handoff body; earlier thin digest mentions `Руководитель Проектного офиса`

## Exact Artifact Search

Searched exact identifiers before any broad index reads:

- `134804503`
- `emphasoft`
- `Emphasoft`
- `EMPHASOFT`

Search scope:

- `inbox/processed/`
- `automation/runs/`
- `personal-projects/personal-brand/workspace/job-intake/processed/`

Findings:

- Current handoff exists at `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md`.
- Earlier Emphasoft handoff exists at `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-rukovoditel-proektnogo-ofisa-emphasoft-handoff.md`.
- Earlier thin digest exists at `inbox/processed/2026-07-04-hh-ai-solution-architect-thin-digest.md` and lists `Emphasoft | Руководитель Проектного офиса | not shown`.
- Previous run log `automation/runs/2026-07-04-180555-pi-job-search-handoff-dispatch.md` already records that authenticated HH enrichment was unavailable for the Emphasoft role.
- No full JD archive, analysis, CV decision, or cover-letter artifact was found for HH vacancy `134804503`.

## Enrichment Result

The authenticated HH connector required by the job-search contour was unavailable in this runtime:

- `tool_search` did not expose `headhunter_web` or any HH vacancy details tool.
- LinkedIn and Gmail/Calendar tools are not the source of truth for this HH vacancy.
- Per tool-boundary rules, no public-web substitute or guessed JD extraction was used.

## Actions Taken

- Created this blocked run log.
- Left monitor state unchanged.
- Did not create JD archive, analysis, CV, or cover-letter artifacts.
- Did not send Telegram directly.

## Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: HH vacancy 134804503 from Telegram was identified, but authenticated HH enrichment is unavailable and no durable full JD artifact exists.
verdict: clarify
reasons:
  - The handoff contains a stable HH vacancy id and URL, but no full JD text.
  - Exact artifact search found only the intake handoff, an earlier thin Emphasoft digest mention, and prior blocked HH-enrichment logs.
  - The required headhunter_web connector is unavailable in this runtime, so the vacancy cannot be verified or evaluated.
cv: null
cover_letter: null
next_action: rerun with headhunter_web available or provide the full HH vacancy text.
artifacts:
  - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md
  - inbox/processed/2026-07-04-hh-ai-solution-architect-thin-digest.md
  - automation/runs/2026-07-04-180555-pi-job-search-handoff-dispatch.md
  - automation/runs/2026-07-04-181624-pi-job-search-handoff-dispatch.md
blocked_on:
  - Authenticated headhunter_web access or pasted full HH vacancy text is needed to fetch and verify the JD.
```
