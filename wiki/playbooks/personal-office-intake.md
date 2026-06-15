# Personal Office Intake Playbook

## Flow

1. Capture important raw input in `inbox/raw/` when the source itself matters.
2. Extract people, dates, promises, decisions, money, risks, opportunities, and next steps.
3. Route using `secretaries/routing-map.md`.
4. Save a processed trace in `inbox/processed/`.
5. Create or update tasks, waiting items, calendar notes, people contacts, company indexes, finance records, life facts, memory, or wiki maps.

## Clarification Stop

If the raw input is important but the target route cannot be chosen from the available facts, stop before making a domain decision.

Required actions:

1. Mark the intake as `routing blocked / needs clarification`.
2. Create `inbox/processed/needs-clarification-YYYY-MM-DD-topic.md`.
3. In that note, record:
   - what raw evidence was captured;
   - what is already known;
   - which route choices are plausible;
   - the exact missing facts or decisions that block routing;
   - what must not be done until clarification is received.
4. If the intake implies follow-up work, create a task in `tasks/active/` or `tasks/waiting/` to resolve the blocker.
5. Resume routing only after the blocking facts are supplied or a responsible owner confirms the intended route.

Do not pick a target domain just because one route seems likely. For example, a company-shaped opportunity that might belong to Fincom, personal consulting, or internal research must stay in clarification until the work contour, owner, expectation, deadline, and next action are explicit enough to route.

## Rules

- Do not leave important outcomes only in chat.
- Do not invent facts.
- If unclear, create `inbox/processed/needs-clarification-YYYY-MM-DD.md`.
- Keep sensitive data minimal and route it to the narrowest useful artifact.
