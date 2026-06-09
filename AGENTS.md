# Personal Office Agent Protocol

This repository is a private operating system for personal life, family matters, finances, projects, companies, meetings, tasks, and memory.

## Prime Directive

Important outcomes must not remain only in chat.

If an input contains a decision, promise, deadline, meeting, amount of money, obligation, risk, opportunity, person, or next step, create or update the relevant artifact in this repository.

## Routing

Start with `secretaries/routing-map.md`.

- Raw unprocessed input belongs in `inbox/raw/`.
- Processed input should leave a trace in `inbox/processed/`.
- Meetings belong in `calendar/meetings/`.
- Active next actions belong in `tasks/active/`.
- Waiting items belong in `tasks/waiting/`.
- Personal and family matters belong in `life/`.
- Money, assets, obligations, taxes, investments, and major financial decisions belong in `finance/`.
- Profi.ru, consulting, experiments, and personal opportunities belong in `personal-projects/`.
- Company matters belong in `companies/<company>/`.
- People, relationship context, and follow-ups belong in `people/`.

If the target is unclear, create `inbox/processed/needs-clarification-YYYY-MM-DD.md` with the specific question that blocks routing.

## Artifact Rules

- Use stable filenames: `YYYY-MM-DD-topic.md`.
- Do not invent missing facts.
- Keep sensitive details minimal; follow `secretaries/privacy-rules.md`.
- When a note implies a task, create or update the task file.
- When a meeting changes a project, company, finance item, or personal commitment, update that target artifact too.

## Local Skills

Repo-local Codex skills live in `.codex/skills/`.

For personal brand / career work, prefer these skills instead of copying long process rules into chat:

- `personal-brand-routing` - route career, CV, HH, JD, and personal portfolio work.
- `job-intake-analysis` - archive and analyze pasted vacancies/JDs.
- `cv-selection` - choose the best final CV for a role.
- `cover-letter-screening` - draft cover letters, recruiter replies, and screening answers.
- `final-cv-pdf-review` - validate and register final PDF resumes.

## Working Style

Before closing a request, state what files were created or updated and what still needs attention.
