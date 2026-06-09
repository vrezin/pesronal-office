---
name: medication-schedule-planning
description: Use when adding medication reminders or schedules to daily/weekly plans based only on saved medication facts, doctor instructions, or explicit user-provided medication intake rules.
metadata:
  short-description: Plan medication reminders from facts
---

# Medication Schedule Planning

## Source Of Truth

Use:

`life/health-lifestyle/health-facts/medications.md`

Do not infer or prescribe medications, doses, timing, interactions, or changes.

## Workflow

1. Read medication instructions.
2. If required fields are missing, create a clarification note.
3. Add reminders to daily or weekly plans.
4. Note dependencies such as "with food" only if present in the source.
5. Preserve source and notes in the plan.

## Refuse To Guess

If the user asks what to take, how much to take, whether to stop, or whether medications conflict, say that this needs a clinician/pharmacist or explicit source instruction. You may help formulate the question and record it.
