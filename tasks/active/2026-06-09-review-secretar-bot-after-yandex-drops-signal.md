# Review Secretar Bot After Yandex Drops Signal

- Created: 2026-06-09
- Status: active
- Area: personal-projects / experiments
- Related signal: `personal-projects/experiments/2026-06-09-yandex-drops-secretar-bot-market-signal.md`
- Related project entity: `memory/entities/projects/secretar-bot.md`
- Review output: `personal-projects/experiments/2026-06-09-secretar-bot-repositioning-review.md`

## Context

Yandex opened sales of Yandex Drops with Alice AI and a "My Memory" feature, according to the Forbes link shared by the user on 2026-06-09. User had earlier built a YandexGPT-based `secretar_bot` prototype and experienced dismissive feedback that the idea was not needed.

This needs a grounded reassessment rather than an emotional discard.

## Desired Outcome

Create a short, evidence-based review of `secretar_bot`:

- what the prototype actually does now;
- what is missing for the "capture thoughts -> structure -> retrieve/edit -> act" loop;
- what changed in the market signal after Yandex Drops;
- whether the project should be revived privately, turned into a portfolio case, productized in a niche, or parked.

## Acceptance Criteria

- Inspect the real repository at the local `secretar_bot` checkout.
- Do not assume current capabilities from memory.
- Compare against the Yandex Drops / Alice "My Memory" feature only at the level of user-visible workflow, not by claiming internal implementation details.
- Produce a one-page repositioning note under `personal-projects/experiments/`.
- Add or update follow-up tasks only if there is a concrete next action.

## First Step

Read the `secretar_bot` README and top-level architecture, then summarize the existing core loop.

## Progress

- 2026-06-09: Inspected the local `secretar_bot` checkout, README files, repo map, user stories, core handlers, speech pipeline, GPT handler, database schema, LangGraph secretary agent, prompt, tests, task index, corporate concept note, and test requirements.
- 2026-06-09: Created the repositioning review artifact linked above.
- 2026-06-09: Attempted `uv run pytest -q`; blocked because `fakeredis` is not installed in the current environment, although it is listed in `requirements-test.txt`.
