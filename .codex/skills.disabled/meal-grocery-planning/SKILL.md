---
name: meal-grocery-planning
description: Use when planning weekly meals, Saturday grocery shopping, food prep, pantry checks, or shopping lists from lifestyle facts, preferences, constraints, calendar capacity, and user-provided dietary rules.
metadata:
  short-description: Plan meals and Saturday groceries
---

# Meal And Grocery Planning

## Inputs

- `life/health-lifestyle/lifestyle-facts/food-preferences.md`
- `life/health-lifestyle/lifestyle-facts/profile.md`
- `life/health-lifestyle/health-facts/medical-notes.md` only for user-provided dietary constraints.
- current weekly plan and calendar constraints.

## Output

Usually update the weekly plan with:

- weekly menu;
- Saturday grocery activity;
- shopping list: must buy / check before buying / optional;
- quick prep tasks;
- constraints and unknowns.

## Rules

- Do not invent medical diets.
- Prefer simple repeatable meals unless the user asks for variety.
- Account for time, energy, cooking capacity, and leftovers.
- If pantry state is unknown, add "check before buying" instead of assuming.
