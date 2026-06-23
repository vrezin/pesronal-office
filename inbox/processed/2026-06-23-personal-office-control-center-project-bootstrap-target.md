# Personal Office Control Center / Project Bootstrap Target

## Source

User clarified on 2026-06-23 that Personal Office should be the main control center for new activities.

Example target scenario:

- Vladimir enters from mobile after a conversation.
- Input shape: "I just spoke with person X, and we agreed to start activity Y."
- Personal Office agent captures the input, enriches it, finds relevant people/artifacts/context, and creates a new project space that follows the engineering standard developed in the Setronica work.

## Target Picture

Personal Office is not only a notes repository.

It is the intake, context-enrichment, decision-routing, and project-spawning control center.

The desired chain:

`mobile/raw input -> Personal Office intake -> people/context/artifact enrichment -> opportunity/project envelope -> generated project space -> Setronica-style Task-to-Handoff operating rules`

## Required Agent Behavior

When a new activity is mentioned:

1. Capture the incoming request according to Personal Office rules.
2. Extract people, promises, decisions, dates, risks, opportunities, and next steps.
3. Find involved people and update relationship/interaction facts.
4. Search local context for:
   - related people;
   - related companies;
   - prior meetings;
   - existing tasks;
   - relevant documents;
   - reusable standards;
   - potential collaborators or interested people.
5. Propose who else could be pulled in and why.
6. Propose which existing artifacts can be attached to the activity.
7. Create a project/activity envelope in Personal Office.
8. Generate or prepare a project space using rules/scripts/standards based on the Setronica engineering standard.

## Home Decision

The next prototype should be a `Personal Office / tooling` prototype.

Setronica engineering standard remains the source of project operating discipline.

Personal Office owns:

- intake;
- enrichment;
- people/context graph;
- project spawning decision;
- local tooling entrypoint;
- owner-level project envelope.

Generated project spaces own:

- project-local `AGENTS.md`;
- project-local task lifecycle;
- project-local wiki routes;
- project-local bootstrap manifest;
- implementation/discovery artifacts.

## Follow-Up Artifacts

- Target playbook: `../wiki/playbooks/project-bootstrap-control-center.md`
- Tooling task: `../tasks/active/2026-06-23-build-project-bootstrapper-standard-and-tooling.md`
- Setronica standard draft: `../companies/setronica/standards/2026-06-23-new-project-bootstrap-framework-standard.md`
