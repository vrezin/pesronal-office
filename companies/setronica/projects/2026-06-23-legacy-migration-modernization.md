# Remote Landlord Legacy Migration / Modernization Activity

## Status

`new / source links received / access blocked`

## Source

- Yuliya Malinina multi-topic call on 2026-06-22.
- Processed trace: `../../inbox/processed/2026-06-22-yuliya-malinina-multi-topic-call.md`.
- Remote Landlord migration chat intake: `../../inbox/processed/2026-06-23-remote-landlord-migration-chat-intake.md`.
- Preparation task: `../../tasks/active/2026-06-22-prepare-setronica-legacy-migration-sync.md`.
- Project space: `<setronica-root>/remote-landlord-migration-discovery/`.

## What Yuliya Asked For

Yuliya described a possible new client migration / modernization stream and wants Vladimir involved before the client-facing position is formed.

Near-term expected participants:

- Vladimir
- Yuliya
- Andrey Kolpakov - architect; exact level unclear, likely solution/enterprise architecture or above.
- Nadezhda Loshchina - analyst / product manager / team lead.

Expected next step:

- sync call after Nadezhda shares references and Vladimir receives access.

## Current Understanding

The activity appears to involve:

- Remote Landlord legacy monolith on ASP.NET/VB.NET + SQL Server;
- target rewrite stack mentioned in chat: Python + PostgreSQL + React;
- intent to preserve all existing features;
- no complete documentation or definitive feature/needs inventory yet;
- concern that a straight rewrite may reproduce the same problems on a new stack;
- possible better strategy: solve concrete business problems while rewriting relevant parts, but RL has not yet provided a list of concrete problems;
- Andrey's codebase inventory reportedly found 25 modules, 604 screens, 480 tables, and 700 stored procedures;
- human-only migration estimate mentioned in chat: 270-400 person-months;
- AI-assisted migration estimate mentioned in chat: about 140-205 person-months, with regulatory/financial validation still calendar-bound;
- separate AI-chat integration looks much smaller: about 0.7-1.1 person-months / 2-4 weeks with two people.

## Known Source Links

- Google Drive folder shared by Nadezhda: `https://drive.google.com/drive/folders/1p4odaAMBfMgMtkneWktxzz_FLtnjzxZJ`

Vladimir currently lacks access rights.

## Mentioned Documents

- `MIGRATION-BREAKDOWN`
- `AI-MIGRATION-BREAKDOWN`
- `MIGRATION-EFFORT-RECUT`
- `RL-AI-CHAT-INTEGRATION-EFFORT`
- `rl-integration-proposal`
- `SERVICE-TICKETS-DOMAIN`

## Vladimir's Potential Role

- Help form a unified technical and delivery position before client discussion.
- Bring prior legacy Microsoft-stack migration experience.
- Separate modernization strategy from naive rewrite/code generation.
- Frame where AI agents can help safely:
  - system mapping;
  - business-rule extraction;
  - characterization-test planning;
  - migration-option analysis;
  - documentation and decision records;
  - repetitive transformation work.
- Keep risk ownership explicit where AI does not remove human accountability:
  - payment correctness;
  - ambiguous business rules;
  - acceptance criteria;
  - go/no-go decisions;
  - client-facing risk posture.

## Missing Inputs

- Drive access for Vladimir.
- Actual documents and source materials from the shared folder.
- Confirmed sync time.
- Client constraints and scope boundaries.
- Whether Setronica is expected to own payment-related scope or adjacent non-payment scope.

## Recommended First Project Artifact

When source materials arrive, create a project-local `Working Change / Discovery Document` before proposing implementation.

Minimum sections:

- `Source / Request Reference`
- `Understanding / Intake`
- `System Inventory`
- `Business-Critical Flows`
- `Risk Register`
- `Migration Options`
- `Validation / Characterization Strategy`
- `AI-Assisted Work Boundary`
- `Client Discussion Position`

## Current Next Action

Wait for Drive access, then review the source materials and update the generated project space.
