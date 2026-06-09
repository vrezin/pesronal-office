# SEO Content Agent

- Entity type: project
- First captured: 2026-06-09
- Primary area: SEO / content automation / AI job pipeline
- Known local checkout: local `seo-content-agent` checkout outside Personal Office; exact machine-specific path intentionally omitted from repo docs.
- Related review: `personal-projects/experiments/2026-06-09-seo-content-agent-project-review.md`

## Summary

`seo-content-agent` is a pet project / scaffold for an AI pipeline that turns a keyword into an SEO article and optionally publishes it to WordPress.

The intended loop:

> keyword -> SERP analysis -> outline -> article generation -> post-processing -> WordPress publication.

## Current State

The specification is detailed and covers architecture, pipeline, API, observability, cost control, nonfunctional requirements, and risks.

The implementation is currently skeletal:

- FastAPI app and controllers exist;
- Celery worker exists;
- pipeline step modules exist;
- most business logic is stubbed or TODO;
- no production-ready persistence or real provider integration was observed during review.

## Relationship To User Pattern

This project expresses the owned-context / structured-action pattern in SEO/content operations:

- raw input: keyword and SERP landscape;
- structured intermediate context: SERP results, outline, job steps, article plan;
- action/output: generated article and optional WordPress publication;
- control layer: logs, traces, cost events, job status.

It is commercially less differentiated than the CRM voice workflow, but it is useful as portfolio evidence for AI pipeline architecture and cost/observability thinking.
