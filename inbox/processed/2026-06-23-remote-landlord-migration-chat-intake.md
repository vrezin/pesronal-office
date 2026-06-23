# Remote Landlord Migration Chat Intake

## Source

- User pasted Setronica chat excerpt on 2026-06-23.
- Chat/channel: `mgt-managego-ai-rl-migration`.
- Related project: `../companies/setronica/projects/2026-06-23-legacy-migration-modernization.md`.

## People

- Yuliya Malinina - Setronica founder/CEO; already known contact.
- Andrey Kolpakov - architect; user describes him as exceptionally strong.
- Nadezhda Loshchina - analyst / product manager / team lead; user describes her as very strong professionally.
- Vladimir Rezin - invited participant / reviewer / potential project contributor.

## Chat Facts

- Yuliya joined/created the `mgt-managego-ai-rl-migration` chat and asked Nadezhda to put summary and source/doc references for the Remote Landlord migration there.
- Yuliya suggested scheduling a sync call tomorrow.
- Nadezhda shared a Google Drive folder with current Remote Landlord information:
  - `https://drive.google.com/drive/folders/1p4odaAMBfMgMtkneWktxzz_FLtnjzxZJ`
- The Drive folder reportedly includes an hour-long intro video about the Remote Landlord system.
- Vladimir currently lacks access rights to the documents and cannot open them.

## Current Remote Landlord Understanding

- Remote Landlord wants to rewrite an old legacy monolith on ASP.NET/VB.NET + SQL Server.
- Target stack mentioned by Nadezhda: Python + PostgreSQL + React.
- Goal stated by RL: preserve all existing features.
- There is reportedly no complete documentation or definitive feature/needs inventory.
- Nadezhda is concerned that a straight rewrite may recreate the same problems on a new technology stack.
- A more useful strategy may be to solve concrete business problems while rewriting relevant parts, but RL has not yet provided a list of concrete current-system problems.

## Existing Analysis Documents Mentioned

- `MIGRATION-BREAKDOWN` - baseline codebase inventory: 25 modules, 604 screens, 480 tables, 700 stored procedures; human migration estimate 270-400 person-months.
- `AI-MIGRATION-BREAKDOWN` - migration estimate with Claude Code acceleration: about 140-205 person-months, roughly 45-50% reduction; AI helps with UI, DDL, and code porting but not regulatory/financial validation.
- `MIGRATION-EFFORT-RECUT` - splits effort into AI-build, Human-gate, and calendar waiting block; key point: adding people stops accelerating after a point.
- `RL-AI-CHAT-INTEGRATION-EFFORT` - AI chatbot integration estimate: about 0.7-1.1 person-months, or 2-4 weeks with a two-person team; no regulatory dependency.
- `rl-integration-proposal` - technical design for chatbot integration into `TenantPayPortal` through a disposable bridge adapter over existing `MakeTicket()`, without changing the existing AI agent.
- `SERVICE-TICKETS-DOMAIN` - service-ticket domain model: actors, objects, statuses, provenance rules (`IssuedBy` / `RequestedBy`), and AP/GL links.

## Current Work In Progress

- Andrey is working on a document/instruction for companies, including Remote Landlord, to integrate with Setronica's AI Chat on their own.

## Blocker

- Vladimir does not yet have access to the Google Drive documents.

## Immediate Actions

- Request / wait for Drive access.
- Create a project space under `<setronica-root>` for this activity.
- Transfer current known context into that project space without inventing missing facts.
