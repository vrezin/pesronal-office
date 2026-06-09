# Mind Muscle Project Review

- Created: 2026-06-09
- Area: personal-projects / experiments / health assistant
- Reviewed repositories:
  - local `mind_muscle` checkout outside Personal Office
  - local `mind_muscle_v02` checkout outside Personal Office
- Scope: documentation and repository-shape review; no code-level audit yet.

## Short Verdict

`mind_muscle` and `mind_muscle_v02` show a clear evolution from a broad health-agent platform attempt into a much sharper product: a personal post-checkup assistant that turns long medical documents into facts, findings, lifestyle recommendations, actions, reminders, and personal context.

The important pattern is similar to the `secretar_bot` story and to the current Personal Office repository itself: the user repeatedly builds systems whose core value is:

> messy human/life/medical input -> structured memory -> action plan -> future retrieval.

## mind_muscle

The older `mind_muscle` repo appears to be a large, ambitious health backend and agent system.

Observed from docs and repository shape:

- broad FastAPI/PostgreSQL/GPT-style backend;
- many health log domains: blood pressure, sleep, stress, mood, symptoms, meals, medication, energy, recovery, bioimpedance, activity, nutrition, weight;
- OpenAPI/generated server layer;
- MCP server and agent tools;
- LLM agent runtime for domains such as blood pressure and sleep;
- checkup parsing, sectioning, normalization, agent jobs, Celery tasks, workers, observability, cost tracking;
- large test tree organized by many health domains;
- Qwen/agent support files and project-framework docs;
- README has encoding/mojibake damage, which itself signals documentation entropy.

Interpretation:

This was not a trivial toy. It was a serious attempt to build a broad health operating backend. But it also shows the failure mode named later in v0.2 docs: too much universal platform gravity, OpenAPI-first/agent/MCP/domain expansion, and many runtime paths before the product core stayed narrow enough.

## mind_muscle_v02

The v02 repo is a deliberate restart.

Observed from docs:

- product identity: personal post-checkup assistant;
- one-line mission: help a person live by checkup results, not just store them;
- canonical flow: document upload -> OCR/parser -> fact extraction -> clinical findings -> lifestyle recommendations -> actions -> user context -> reminders -> contextual Q&A;
- explicit non-goals:
  - not a universal medical platform;
  - not generic health API;
  - not OpenAPI-first;
  - old code is experience/archive, not technical foundation;
  - no doctor role in the first live version;
  - no heavy agent infrastructure as the product center.
- monorepo shape:
  - `backend/`;
  - `parser_service/`;
  - `frontend/`;
  - `artifacts/change-artifacts/`;
  - `.ai-skills/`;
  - root coordination docs.
- stack baseline:
  - React + TypeScript + Vite + Tailwind;
  - FastAPI;
  - PostgreSQL;
  - Celery + Redis;
  - SQLAlchemy 2 + Alembic;
  - Pydantic v2;
  - Ollama adapter / central LLM runner / prompt builder / schema validation.
- process discipline:
  - change artifacts with `Understanding` and `Specification`;
  - code index and repo index;
  - architecture-principles gate;
  - development-policy gate;
  - closeout skills;
  - explicit `source -> understanding -> specification -> implementation -> evidence` chain.

Interpretation:

`mind_muscle_v02` looks like a learned restart. It preserves the strong product intuition from the old repo, but tries to keep the project from being swallowed by platform architecture. It also carries a much more mature AI-assisted-development operating model.

## Current State Notes

Working tree state at review time:

- `mind_muscle` has dirty/untracked changes, including AGENTS/CODE_INDEX-related files, Ollama services/tests, chunking/debug files, and generated artifacts.
- `mind_muscle_v02` has many active modifications and added change artifacts around an LLM subsystem migration, async boundaries, reliability, observability, config, tests, and logging.
- No files were changed in either project during this review.

## Relationship To Secretar Bot

These projects make the broader pattern clearer, especially when compared with Personal Office.

`secretar_bot`:

- voice/text thoughts -> structured notes -> summaries/tasks/memory direction.

`mind_muscle`:

- health logs/checkups -> normalized facts -> agents/plans/recommendations.

`mind_muscle_v02`:

- checkup documents -> trusted structured context -> action plan/reminders/Q&A.

`personal-office`:

- raw life/company/project input -> routed artifacts -> tasks/waiting items/memory/entities/wiki maps -> later retrieval by agents.

The repeated capability is not "one random pet project." It is a persistent architecture instinct:

> turn overwhelming unstructured input into owned structured context and concrete next actions.

That is a coherent personal technical theme and can be packaged as portfolio evidence.

Related semantic memory:

- `memory/semantic/topics/owned-context-operating-system.md`

## Suggested Framing

Useful portfolio/commercial framing:

> I build personal operating systems around messy real-world data: voice notes, medical documents, checkups, tasks, and recommendations. The core loop is capture, structure, preserve source trace, derive actions, and make the result queryable.

For `mind_muscle_v02` specifically:

> Personal post-checkup assistant: upload medical checkup documents, extract trusted facts and recommendations, turn them into action plans and reminders, and answer questions from grounded personal context.

## Later Code Review Target

If/when doing a code-level review, start with `mind_muscle_v02`, not the old repo:

1. Read `NEXT-SESSION.md`.
2. Inspect:
   - `backend/app/extraction/service.py`;
   - `backend/app/llm/ollama_adapter.py`;
   - `backend/app/documents/service.py`;
   - `backend/app/health.py`;
   - `parser_service/app/main.py`.
3. Focus on the current stated risk: runtime hardening around async LLM extraction, intake timeout, health-detail leakage, parser blocking, and parse-failed early exit.

The old `mind_muscle` repo should be treated as archive/experience unless a very specific artifact or implementation pattern is needed.
