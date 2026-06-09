---
name: life-intake-router
description: Use when the user provides raw personal-life input, health/lifestyle facts, household updates, money/life constraints, schedule changes, meals, medication information, or asks to feed events into the life planning system. Routes facts into personal-office artifacts and creates or updates plans/tasks.
metadata:
  short-description: Route life inputs into facts and plans
---

# Life Intake Router

## Core Rule

Important life input must become facts, plans, tasks, or clarification notes. Do not leave it only in chat.

## Routing

- Health facts: `life/health-lifestyle/health-facts/`
- Lifestyle facts: `life/health-lifestyle/lifestyle-facts/`
- Home/family/rest: `life/home-family-rest/`
- Meetings/time: `calendar/`
- Tasks/waiting: `tasks/`
- Money/obligations: `finance/`
- People/follow-ups: `people/`

## Workflow

1. Identify facts, dates, obligations, risks, decisions, recurring patterns, and open questions.
2. Update stable fact files when the input changes the user's known reality.
3. Create tasks for next actions and waiting items.
4. Update current daily/weekly/monthly plans if the input changes capacity or priorities.
5. If unclear, create `inbox/processed/needs-clarification-YYYY-MM-DD.md`.

## Safety

For health, medications, diet, and exercise, record only supplied facts. Do not prescribe, change dosage, or invent constraints.
