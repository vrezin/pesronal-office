# 2026-06-09 - Life Planning Engine

## Source

User requested a system where incoming personal-life data becomes a life plan rather than hardcoded daily notes.

## Decision

Create a fact-driven life planning system:

- health facts live in `life/health-lifestyle/health-facts/`;
- lifestyle facts live in `life/health-lifestyle/lifestyle-facts/`;
- daily plans live in `calendar/daily/`;
- weekly plans live in `calendar/weekly/`;
- monthly plans live in `calendar/monthly/`;
- planning rules live in `calendar/planning/personal-daily-weekly-planning.md`;
- planning workflows live as repo-local skills in `.codex/skills/`.

## Required Capabilities

- Intake new facts and route them into stable artifacts.
- Build weekly plans from health, lifestyle, calendar, tasks, projects, and obligations.
- Plan medication reminders only from saved medication instructions.
- Plan Saturday groceries and weekly menu from lifestyle facts.
- Rebalance day/week/month plans after new intake.

## Safety

The system must not invent medical advice, medication changes, diets, or training prescriptions. It can structure facts, plan from explicit instructions, and create clarification questions.
