# Alexandra Kashun AI-First SDLC Draft Agent Review

- Created: 2026-06-22
- Reviewer: subagent `Meitner`
- Reviewed draft: `personal-projects/personal-brand/workspace/content/2026-06-22-alexandra-kashun-ai-first-sdlc-qa-draft.md`
- Related task: `tasks/active/2026-06-22-answer-alexandra-kashun-setronica-content-questions.md`
- Review workspace: `<setronica-root>/engineering-task-to-handoff-standard`

## Overall Verdict

The draft hits the main point well:

> start not by giving everyone an agent, but by stabilizing specification, understanding, verification, and a shared result standard.

This aligns with Setronica's Task-to-Handoff framing.

## Setronica Sources Checked

- `<setronica-root>/engineering-task-to-handoff-standard/README.md`
- `<setronica-root>/engineering-task-to-handoff-standard/framework/policies/19-development-policy.md`
- `<setronica-root>/engineering-task-to-handoff-standard/framework/standards/01-development-control-package.md`
- `<setronica-root>/engineering-task-to-handoff-standard/rollout-stages/stage-1/ru/process/what-stage-1-is.md`
- `<setronica-root>/engineering-task-to-handoff-standard/workspace/design/open-design/108-first-wave-adoption-followup-notes-20260511.md`
- `<setronica-root>/engineering-task-to-handoff-standard/workspace/design/open-design/109-stage-2-ai-development-followup-notes-20260517.md`
- `<setronica-root>/engineering-task-to-handoff-standard/workspace/design/open-design/113-stage-2-operational-goals-yulia-followup-20260603.md`

## Good Coverage

- Starts from specification rather than tool rollout.
- Includes `understanding` as "how I understood the task".
- Emphasizes verifiability, acceptance boundaries, and task formulation quality.
- Says the shared result standard matters more than one shared tool.
- Mentions manual review of specifications.

## Missing Or Weak

- Draft is too AI-only in places. The standard should be framed as compatible with AI-assisted development, but not dependent on AI.
- Needs the core chain: `source -> understanding -> spec -> implementation -> evidence -> handoff`.
- Needs Stage 2 framing: spec becomes the control surface for implementation, not a report after the fact.
- Needs `AI Implementation Readiness Gate`: do not launch AI if it must make execution-critical decisions.
- Quality gates should be explained as controls with owner, evidence, status, and blocking semantics.
- Handoff is underdeveloped: the output is not only code/PR, but an explainable package with evidence.
- Learning loop is underdeveloped: collect review patterns, prompts/skills, typical mistakes, and process improvements.
- "Good code is not needed by business" is directionally useful but risky. Safer framing: business needs verifiable system properties; readability/structure matter as ways to support review, maintenance, and drift control.

## Questions Still Weak

- What concrete tasks are being tested? Add 1-2 anonymized examples.
- How does people-management experience help? Connect it to delegation, ownership, clarity of intent, review, and acceptance criteria.
- How do you know the experiment goes wrong? Name mechanisms: spec review, gates, evidence, PR comments, adoption stats, repeated failure patterns.
- How is negative experience captured? Add learning loop: typical errors, review comments, skills/prompts improvement.
- What is the scale-up signal? Current "15 participants daily to production" may be too strict and sensitive; consider softer Stage 2 indicators: regular specs, review evidence, participation stats, and spec->code->evidence linkage.

## Publication Risks

- Needs anonymization: "Yuliya", "Denis Shalaev", exact 15/7 pilot numbers, direct Setronica involvement.
- Needs anonymization: client SDLC, client repositories, internal accesses, concrete projects.
- Tone risk: "one foot in the grave", "infantilism", "brilliant five-year-old", and "nobody needs good code except programmers" may fit personal LinkedIn but are risky for corporate blog.
- Positioning risk: "our company" conflicts with current guardrail; safer: "in one working contour", "in a pilot group", "in my practice with teams".
- Accuracy risk: production/deploy scaling claims should not be published without confirming current state.
- Corporate safety: direct Setronica/client attribution only after explicit clearance.

## Recommended Next Revision

1. Keep this raw draft as source material.
2. Create a second, publication-safe version.
3. Add the Task-to-Handoff chain and Stage 2 control-surface framing.
4. Replace direct names/numbers with anonymized phrasing.
5. Preserve the strong personal voice only if the target format is personal LinkedIn; soften for corporate blog.
