# Prepare Setronica Legacy Migration Sync

- Created: 2026-06-22
- Status: active
- Related meeting: `../../calendar/meetings/2026-06-22-yuliya-malinina-multi-topic-call.md`
- Waiting item: `../waiting/2026-06-22-wait-yuliya-andrei-legacy-migration-sync-materials.md`
- Company context: `../../companies/setronica/active.md`

## Goal

Prepare Vladimir to join Yuliya, Andrei, and Nadya for a 2026-06-23 sync about a client legacy migration / modernization opportunity.

## Current Understanding

The client appears to have:

- legacy Visual Basic / .NET / web forms / old framework code;
- long business-logic procedures;
- two systems after acquiring a competitor;
- no obvious clean base system to migrate to;
- business-critical payment-related scope;
- a competing Israeli vendor/product with potential IP/license lock-in risk.

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

- Actual code/files/findings from Andrei.
- Confirmed call time / chat from Yuliya.

