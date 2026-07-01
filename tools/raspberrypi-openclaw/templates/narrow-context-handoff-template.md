# Narrow Context Handoff Template

- Purpose: request the smallest safe context needed for a Personal Office routing, review, or draft-patch task.
- Use when: the agent cannot safely route, update, or hand off work from the provided input and cookbook context alone.

## Rule

Ask for the smallest useful context, not a directory, repository, account, browser profile, or raw private store.

If there is a chance that several topics or contours are mixed, ask the user to confirm the split before requesting large context.

## Template

```yaml
handoff_request:
  task:
  why_context_is_needed:
  suspected_lanes:
    - lane:
      likely_owner_contour:
      confidence: high|medium|low
      why:
  preferred_source:
    type: file_summary|task_summary|contact_summary|meeting_summary|project_summary|user_answer|other
    path_or_alias:
  minimum_fields:
    - field:
      reason:
  do_not_include:
    - raw directory dumps
    - credentials
    - cookies/browser profiles
    - unrelated private facts
    - full finance/health/people/calendar stores
  safe_alternative_if_not_available:
  blocked_until:
    - exact missing fact, decision, or approval
  must_not_do_yet:
    - unsafe or speculative action
```

## Examples

### Mixed Meeting

```yaml
handoff_request:
  task: route a meeting that includes Setronica work, product feedback, and personal-brand content
  why_context_is_needed: current state is needed before drafting updates
  suspected_lanes:
    - lane: Setronica execution
      likely_owner_contour: companies/setronica + <setronica-root>
      confidence: high
      why: meeting discusses Setronica work and project handoff
    - lane: Private AI Office feedback
      likely_owner_contour: unresolved personal/product contour
      confidence: medium
      why: meeting includes product feedback from a validator, not ownership
  preferred_source:
    type: file_summary
    path_or_alias: companies/setronica/active.md
  minimum_fields:
    - field: current Setronica status
      reason: avoid overwriting stale owner state
    - field: open Setronica obligations
      reason: route follow-ups correctly
  do_not_include:
    - full Setronica repo
    - raw people directory
  safe_alternative_if_not_available: user-provided bullet summary of current status and open obligations
  blocked_until:
    - current Setronica status is known
  must_not_do_yet:
    - apply live task or project updates
```

### Validator Feedback

```yaml
handoff_request:
  task: decide where product feedback belongs
  why_context_is_needed: validator's company is not automatically the owner contour
  suspected_lanes:
    - lane: product idea feedback
      likely_owner_contour: unresolved
      confidence: medium
      why: the source gave feedback but did not sponsor or own the work
  preferred_source:
    type: user_answer
    path_or_alias: n/a
  minimum_fields:
    - field: should this become a new project contour, stay as an idea, or remain parked?
      reason: owner contour is a user decision
  do_not_include:
    - unrelated company internals
  safe_alternative_if_not_available: keep the route unresolved and draft only a feedback note
  blocked_until:
    - owner contour decision
  must_not_do_yet:
    - route the idea into the validator's company workspace
```
