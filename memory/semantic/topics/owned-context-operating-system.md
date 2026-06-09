# Owned Context Operating System

## Summary

User's recurring product/engineering pattern across projects:

> chaotic human input -> structured owned memory -> concrete actions -> later search/context.

This is visible in:

- `secretar_bot`;
- `mind_muscle` / `mind_muscle_v02`;
- the current `personal-office` repository itself;
- Setronica `Delivery Standard` / `Task-to-Handoff`;
- `seo-content-agent`.

## Pattern

1. Capture messy real-world input.
   - voice notes;
   - chat messages;
   - medical documents;
   - company/project signals;
   - life/admin facts;
   - opportunities, risks, obligations, and decisions.

2. Route and structure it.
   - classify target domain;
   - extract facts, people, dates, money, risks, promises, and open questions;
   - turn unstructured language into stable artifacts.

3. Store it as owned context.
   - local repo files;
   - source-of-truth documents;
   - tasks;
   - memory layers;
   - entity records;
   - knowledge graph;
   - project artifacts.

4. Derive concrete next actions.
   - tasks;
   - waiting items;
   - calendar events;
   - action plans;
   - follow-ups;
   - reminders.

5. Make it retrievable later.
   - wiki maps;
   - memory retrieval rules;
   - indexes;
   - graph nodes/edges;
   - source artifact links;
   - context-aware agents.

## Project Evidence

### Personal Office

The repository README states the core loop directly:

> incoming life flow should become schedules, tasks, decisions, documents, and memory that secretary agents can work with.

The repo implements this through:

- `secretaries/routing-map.md`;
- `secretaries/intake-rules.md`;
- `tasks/`;
- `memory/`;
- `wiki/maps/`;
- `people/`;
- `companies/`;
- `personal-projects/`;
- knowledge graph records.

### secretar_bot

Pattern expression:

- voice/text input;
- Yandex SpeechKit + YandexGPT;
- structured notes and summaries;
- session state;
- idea-capture agent;
- future direction toward searchable memory, reminders, and action routing.

### Mind Muscle

Pattern expression:

- medical checkups and health logs;
- parsing/OCR/normalization;
- fact extraction;
- clinical findings and lifestyle recommendations;
- action plans and reminders;
- grounded context for later Q&A.

### Setronica Delivery Standard

Pattern expression:

- unclear task, business, and implementation intent;
- developer-owned understanding;
- working change documents;
- change specifications;
- implementation evidence;
- honest handoff;
- reviewable context for humans and AI agents;
- project bootstrapper artifacts for creating the same operating layer in new repositories.

This is the engineering-process version of the same loop:

> source intent -> understanding -> specification -> implementation -> evidence -> handoff.

### SEO Content Agent

Pattern expression:

- keyword and SERP landscape;
- SERP analysis;
- structured outline;
- article generation;
- post-processing;
- WordPress publication;
- job status, traces, logs, and cost events.

This is the content-operations version of the loop:

> keyword/SERP -> outline -> content -> publish -> cost/trace/control context.

## Positioning Use

This can become a personal positioning line:

> I build owned-context systems that turn messy human input into structured memory, decisions, and next actions.

Longer version:

> My recurring engineering pattern is building private operating systems for real-world context: capture unstructured input, preserve source trace, structure it into owned memory or specifications, derive concrete next actions, and make the result retrievable and reviewable for future humans and agents.

## Boundary

This is not the same as a generic chatbot or generic AI assistant.

The differentiator is artifact-backed context ownership:

- source artifacts are durable;
- memory is structured;
- actions are explicit;
- agents can retrieve and update the system later;
- important outcomes do not remain only in chat.
