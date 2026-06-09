# SEO Content Agent Project Review

- Created: 2026-06-09
- Area: personal-projects / experiments / content automation
- Reviewed repository: local `seo-content-agent` checkout outside Personal Office
- Scope: documentation and repository-shape review; no changes in the project repository.

## Short Verdict

`seo-content-agent` is another expression of the user's recurring pipeline instinct, but aimed at SEO/content operations:

> keyword / SERP chaos -> structured outline -> generated article -> post-processing -> WordPress publication -> cost/trace/control events.

It is not yet a mature implementation. The documentation/specification is much stronger than the code.

## What Exists

Observed repository shape:

- FastAPI backend skeleton;
- Celery worker skeleton;
- pipeline steps:
  - `serp_analysis`;
  - `generate_outline`;
  - `generate_article`;
  - `postprocess`;
  - `wp_publish`;
- Dockerfiles and docker-compose;
- API and worker requirements;
- detailed technical design document;
- supporting docs split into architecture, pipeline, API, observability, cost control, nonfunctional requirements, risks, and appendix.

## Specification Strength

The spec describes a full automated AI agent for SEO content generation:

1. user submits keyword;
2. system creates job;
3. worker performs SERP analysis;
4. outline is generated;
5. article content is generated;
6. post-processing handles style, tone, anti-duplication, metadata, HTML/Markdown;
7. optional WordPress publication.

The strongest design points:

- async job pipeline;
- structured JSON logging;
- `trace_id` / `span_id` tracing;
- cost events for LLM/SERP calls;
- job-level cost snapshot;
- retries, idempotency, timeouts, fallback;
- WordPress as a concrete publication target.

## Implementation State

The code appears skeletal:

- auth returns a stub token;
- job creation returns a generated UUID without real DB persistence;
- job lookup returns a hardcoded `in_progress`;
- SERP step returns empty results;
- outline step returns a placeholder title and empty sections;
- content step returns empty article sections;
- WordPress publish is a TODO.

This is a designed MVP shell / scaffold, not a working production content agent.

## Relationship To Owned Context Pattern

This project extends the same pattern into content/SEO:

- messy input: keyword and SERP landscape;
- structured context: SERP analysis, outline, content plan, job steps;
- concrete output/action: article and optional WordPress publication;
- later control/search context: logs, traces, cost events, job status, generated article record.

Compared with other projects:

- `secretar_bot`: voice/text thoughts -> structured notes/actions;
- CRM voice bot: sales voice report -> CRM fields/opportunity/task;
- `mind_muscle_v02`: medical documents -> health facts/actions;
- Setronica: task intent -> spec/evidence/handoff;
- `seo-content-agent`: keyword/SERP -> article pipeline/publication.

## Commercial Use

This is not the best first paid wedge because SEO content generation is crowded and easy to commoditize.

Useful commercial uses:

- portfolio proof of pipeline architecture and cost-control thinking;
- internal demo of async AI job orchestration;
- small implementation offer for agencies that need controlled WordPress content production;
- source of reusable architecture for other job-based AI pipelines.

Avoid leading with:

> I can generate SEO articles with AI.

Better framing:

> I design controlled AI production pipelines: job lifecycle, external data, generation steps, cost events, observability, retries, and publication.

## Follow-Up Targets

If revisiting technically:

1. Add real persistence for jobs and steps.
2. Wire the worker queue from API to Celery.
3. Implement one SERP provider.
4. Implement one LLM provider and prompt registry.
5. Add cost-event recording.
6. Implement WordPress draft publication, not direct production publish.
7. Add tests around job state transitions and step failure behavior.

This should remain secondary to the CRM voice workflow unless a concrete buyer asks for controlled content production.
