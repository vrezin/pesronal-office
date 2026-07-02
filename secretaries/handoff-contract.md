# Secretary Handoff Contract

Internal agents should communicate with the intake/output secretary through a
small structured handoff, not through user-facing logs.

The intake secretary owns Telegram-facing language. Domain agents should write
durable artifacts and return concise machine-readable facts.

## Minimal Handoff

Use this shape in run logs, processed notes, or future outbox items:

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: short factual summary
verdict: go | maybe | no-go | clarify | wait | no-op
reasons:
  - reason one
  - reason two
cv: path or null
cover_letter: path or null
next_action: one short action
artifacts:
  - path
blocked_on:
  - question if any
```

## Rules

- Domain agents should not stream tool logs, shell output, stack traces, or
  implementation chatter to Telegram.
- Domain agents may write detailed run logs under `automation/runs/`.
- User-facing replies should be rewritten by the intake/output secretary in
  clear human language.
- If a route is ambiguous, the handoff verdict should be `clarify` and include
  one blocking question.
