# Project Bootstrap Control Center

## Purpose

Describe the target Personal Office workflow for turning a live conversation, opportunity, or new workstream into a routed project space.

Personal Office is the control center.

Setronica engineering standards provide the operating discipline for generated project spaces.

## Target Flow

`incoming conversation -> Personal Office intake -> context enrichment -> project envelope -> generated project space -> Task-to-Handoff execution`

## Trigger

Use this playbook when an input says or implies:

- "I just spoke with someone and we agreed to start something."
- "A company wants me involved in a new project."
- "There is a new client stream or opportunity."
- "We need to create a new repo/project/activity."
- "This should become a structured workstream."

## Step 1. Capture The Incoming Request

Create or update:

- raw or processed intake trace;
- meeting note, if the input is a call/meeting result;
- task or waiting item, if there is a next action or dependency.

Extract:

- people;
- company;
- date/time;
- promises;
- decisions;
- deadline;
- risks;
- opportunity;
- next step;
- missing inputs.

## Step 2. Resolve People And Interaction Facts

For each named person:

- find or create a `people/contacts/` card when the person is durable;
- record the interaction fact in the narrowest useful artifact;
- link the person to the project/activity envelope;
- do not invent missing role, employer, or relationship details.

## Step 3. Enrich From Context

Search for:

- prior meetings;
- related active/waiting tasks;
- company notes;
- people relationship notes;
- relevant contracts or constraints;
- related project artifacts;
- prior decisions;
- reusable standards or playbooks;
- tools that can support the activity.

Then produce:

- artifacts to attach;
- people to involve;
- people who may be interested;
- people who may be blockers/decision makers;
- missing context to request.

## Step 4. Create Project / Activity Envelope

Create an owner-level envelope before creating or modifying project-local implementation truth.

Minimum fields:

- status;
- source;
- sponsor/requester;
- people involved;
- current understanding;
- objective;
- scope known so far;
- missing inputs;
- risks;
- candidate collaborators;
- relevant existing artifacts;
- first next action;
- recommended project profile.

Use company/project routes when applicable:

- company work: `companies/<company>/projects/`;
- personal opportunities: `personal-projects/opportunities/`;
- personal tools: `tools/` plus `tasks/active/`;
- unclear route: processed clarification note.

## Step 5. Choose Project Profile

Choose the smallest useful profile.

Initial profile set:

- `documentation-first-repository`
- `python-service-project`
- `client-modernization-discovery`

Profile selection should be explicit.

If no profile fits, create the envelope and record the missing profile requirement.

## Step 6. Generate Or Prepare Project Space

The generated project space should follow the Setronica-style operating contour:

`source -> understanding -> specification -> implementation/discovery -> evidence -> handoff`

Minimum generated project layer:

- `AGENTS.md`
- `bootstrap-manifest.md`
- `tasks/`
- `tasks/templates/task-template.md`
- `wiki/index.md`
- `wiki/wiki.yaml`
- `workspace/registers/current-focus.md`
- `workspace/registers/decisions.md`
- `.codex/skills/project-operating-context/SKILL.md`

Software profiles may add:

- runtime skeleton;
- test skeleton;
- development/testing policies;
- architecture principles;
- starter CI.

## Step 7. Close The Intake

Before closing:

- state what was created or updated;
- state missing inputs;
- state who or what is waiting;
- state the next action;
- keep project truth and Personal Office owner-context separated.

## Tooling Home

The first prototype belongs in Personal Office tooling:

- `tools/project-bootstrapper/`

Setronica repo remains the standards source and comparison baseline.

Personal Office owns orchestration.
Generated project spaces own local execution truth.
