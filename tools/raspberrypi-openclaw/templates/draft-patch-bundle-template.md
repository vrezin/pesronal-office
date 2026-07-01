# Draft Patch Bundle Template

- Purpose: describe proposed Personal Office or project-handoff changes before applying them.
- Use when: the agent has enough handed context to propose artifacts but live writes are not yet approved.

## Rule

Default to `draft_only`.

Do not apply changes unless the user explicitly approves the patch bundle or a narrower subset of it.

## Template

```yaml
patch_bundle:
  status: draft_only|ready_for_user_review|approved_to_apply
  source_context:
    - path_or_description:
      handed_explicitly: true|false
      evidence_scope:
  topic_lanes:
    - lane:
      owner_contour:
      confidence: high|medium|low
      user_confirmation_needed: true|false
      why:
  proposed_changes:
    - path:
      operation: create|update|move|no_op
      owner_contour:
      rationale:
      source_evidence:
        - source:
          claim:
      facts_to_record:
        - fact:
          confidence: high|medium|low
          evidence:
      hypotheses_to_record:
        - hypothesis:
          basis:
      open_questions:
        - question:
      risks:
        - risk:
      apply_status: draft_only|ready_for_user_review|approved_to_apply|blocked
      must_not_apply_until:
        - condition:
  handoff_envelopes:
    - target_contour:
      target_path_or_alias:
      purpose:
      payload_summary:
      missing_context:
      confidentiality_or_boundary_notes:
  user_decisions_needed:
    - decision:
      options:
      default_safe_action:
  safe_next_action:
```

## Required Before Applying

Before any live write, verify:

- source context was explicitly handed or approved;
- topic lanes are separated;
- validator context is not confused with owner contour;
- target paths are known and current;
- no proposed path starts with an unknown top-level route;
- no raw/private directories are requested broadly;
- open questions are not blocking the specific change;
- user approval is explicit.

## Path Validation Rule

If the route is known but the exact path is not known, do not invent a path.

Use:

```yaml
path_validation:
  original_path:
  route_valid: yes|no|partial
  corrected_path_or_route:
  reason:
  apply_status: draft_only|blocked_until_route_confirmed|requires_explicit_user_approval
```

Rules:

- If a proposed path starts with an unknown top-level directory, set `route_valid: no`.
- If the lane is valid but the exact artifact path is unclear, set `route_valid: partial` and return the closest valid route only.
- If the change belongs in a project workspace such as `<setronica-root>`, treat it as a handoff envelope until the user explicitly approves project-side writes.
- Do not mark a bundle `ready_for_user_review` until invalid or partial routes are either corrected or explicitly blocked.

## Compact Human Summary

After the YAML bundle, include a short human summary:

```text
I propose N changes:
1. Create/update <path> because <reason>.
2. Draft handoff to <contour> because <reason>.

Blocked:
- <question/approval needed>.

Apply status: draft only.
```
