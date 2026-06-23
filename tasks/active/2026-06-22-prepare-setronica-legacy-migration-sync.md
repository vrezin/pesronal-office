# Prepare Setronica Legacy Migration Sync

- Created: 2026-06-22
- Status: active
- Related meeting: `../../calendar/meetings/2026-06-22-yuliya-malinina-multi-topic-call.md`
- Waiting item: `../waiting/2026-06-22-wait-yuliya-andrei-legacy-migration-sync-materials.md`
- Company context: `../../companies/setronica/active.md`

## Goal

Prepare Vladimir to join Yuliya, Andrei, and Nadya for a 2026-06-23 sync about a client legacy migration / modernization opportunity.

## Current Understanding

The client / activity is Remote Landlord.

Current understanding from the chat:

- legacy monolith on ASP.NET/VB.NET + SQL Server;
- desired rewrite stack: Python + PostgreSQL + React;
- goal to preserve all existing features;
- no complete documentation or definitive feature/needs inventory yet;
- business-critical payment-related scope;
- codebase inventory mentioned by Nadezhda / Andrey: 25 modules, 604 screens, 480 tables, 700 stored procedures;
- human-only migration estimate: 270-400 person-months;
- AI-assisted migration estimate: about 140-205 person-months;
- separate AI-chat integration estimate: about 0.7-1.1 person-months.

Yuliya's desired direction may be:

- avoid simply adding many cheap developers;
- use a smaller, stronger team;
- consider a third target system rather than choosing either legacy system as the base;
- possibly keep familiar user-facing interfaces while replacing internals;
- take non-payment scope if payment scope is politically assigned to the competitor.

## Vladimir's Preparation Points

- Bring CDEK legacy migration experience as relevant evidence.
- Explain why moving business logic out of the database can reduce risk and unlock delivery.
- Separate "generate code fast" from "verify business behavior safely."
- Emphasize that missing specs/tests make rewrites dangerous unless a characterization/testing strategy is built.
- Discuss strangler-style migration / incremental replacement rather than big-bang rewrite.
- Identify where AI agents can help:
  - code reading and mapping;
  - spec extraction;
  - characterization tests;
  - migration option generation;
  - documentation and decision records;
  - repetitive transformation work.
- Identify where AI agents do not remove human responsibility:
  - payment correctness;
  - business-rule ambiguity;
  - acceptance criteria;
  - go/no-go decisions;
  - ownership of risk.

## Blocked On

- Drive access for Vladimir.
- Confirmed call time.
- Review of the shared Drive documents after access is granted.
