# Router Output Review Checklist

- Purpose: review whether a Personal Office router response is useful and safe before using it as an artifact or patch basis.
- Use when: an agent routes a meeting, transcript, opportunity, project signal, or mixed-context input.

## Core Checks

```yaml
review:
  invented_facts:
    pass: true|false
    notes:
  facts_have_evidence_or_confidence:
    pass: true|false
    notes:
  hypotheses_labeled:
    pass: true|false
    notes:
  ideas_labeled:
    pass: true|false
    notes:
  weak_signals_labeled:
    pass: true|false
    notes:
  risks_labeled:
    pass: true|false
    notes:
```

## Topic And Contour Checks

The key question is not only "Personal Office or project workspace?"

The key question is: did the agent understand that the source may contain different topics with different routes?

```yaml
topic_review:
  distinct_topics_identified:
    pass: true|false
    notes:
  lanes_named_clearly:
    pass: true|false
    notes:
  validator_not_confused_with_owner_contour:
    pass: true|false
    notes:
  suspected_mixing_escalated_to_user:
    pass: true|false
    notes:
  route_confidence_stated:
    pass: true|false
    notes:
```

If the agent suspects topics or contours are mixed, it must ask the user to confirm the split before applying changes.

## Boundary Checks

```yaml
boundary_review:
  personal_office_owner_side_state_identified:
    pass: true|false
    notes:
  project_or_company_execution_truth_identified:
    pass: true|false
    notes:
  no_broad_raw_private_access_requested:
    pass: true|false
    notes:
  narrow_context_requests_are_specific:
    pass: true|false
    notes:
  live_writes_require_approval:
    pass: true|false
    notes:
```

## Output Quality Checks

```yaml
output_review:
  target_artifacts_are_plausible:
    pass: true|false
    notes:
  open_questions_are_actionable:
    pass: true|false
    notes:
  next_action_is_safe:
    pass: true|false
    notes:
  patch_bundle_status_is_clear:
    pass: true|false
    notes:
```

## Fail Conditions

Treat the output as failed if it:

- invents current facts;
- collapses several unrelated lanes into one route;
- routes product feedback into a validator's company by default;
- applies or proposes live writes without approval status;
- asks for broad raw/private access instead of a narrow handoff;
- ignores the user's uncertainty or asks no clarifying question when contours appear mixed.
