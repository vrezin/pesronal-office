# HH Targeted Resume Block Library

Дата UI-проверки: 2026-06-12

Purpose: use HH's two-level resume model correctly:

1. Profile-level experience blocks exist on the applicant profile page.
2. Each HH resume is an assembly/publication target that can reuse profile-level data where HH exposes the linkage.
3. Some edit routes still open resume-specific partial forms, so automation must distinguish profile-level editing from resume-level editing.

This matters because high-priority vacancies may score below target not because the candidate lacks experience, but because the exact vacancy language is absent from the assembled resume.

## Verified HH UI Model

Checked with authenticated headless HH session and user-provided browser screenshot on 2026-06-12.

Confirmed entry points:

- resume list: `https://hh.ru/applicant/resumes`;
- resume view: `https://hh.ru/resume/<resume_hash>`;
- applicant profile with profile-level experience blocks: `https://novosibirsk.hh.ru/profile/me?hhtmFrom=ProfileActivator`;
- edit title/role/format: `https://hh.ru/resume/edit/<resume_hash>/position`;
- add a work-experience block to the current resume: `https://hh.ru/resume/edit/<resume_hash>/experience`;
- edit summary/about: `https://hh.ru/resume/edit/<resume_hash>/about`;
- edit skills: `https://hh.ru/resume/edit/<resume_hash>/keySkills`;
- add or edit education as a profile entity linked to resumes: `https://hh.ru/profile/edit/primaryEducation?resumeFrom=<resume_hash>&hhtmFrom=resume`.

Observed selectors:

- work experience company: `resume-editor-experience-company-input`;
- work experience position: `resume-editor-experience-position-input`;
- work experience start year: `resume-editor-experience-start-year-input`;
- work experience end year: `resume-editor-experience-end-year-input`;
- work experience description: `resume-editor-experience-description-input`;
- partial resume save: `resume-partial-edit-save`;
- partial resume cancel: `resume-partial-edit-cancel`.

Important correction after screenshot review:

- `/profile/me` on the regional HH host can show profile-level work experience blocks.
- The screenshot shows "Опыт работы: 23 года и 10 месяцев", a profile-level `+ Добавить` action, company grouping, and multiple separate `CTO / сооснователь` blocks under `ООО Финкомтех`, each with its own edit pencil.
- My first headless pass against `https://hh.ru/profile/me` saw only upper profile sections and missed the work-experience area; do not treat that pass as proof that profile-level experience does not exist.
- The direct resume add-experience route opens a single form and did not show "resume with this work experience" checkboxes in that context.
- Education does show profile-level reuse: the education edit form displays "Резюме с этим учебным заведением" with resume checkboxes and a "Развернуть" control.
- Therefore, the next automation step is to map the profile-level experience edit pencils and identify whether their edit forms expose resume linkage checkboxes or only mutate the profile block.

## Mental Model

Do not treat each targeted resume as a full rewrite.

Treat the repo as the canonical planning library, the HH profile as the live profile-level block library, and HH resumes as publication targets:

- multiple profile blocks can describe the same employer or period with different emphasis;
- blocks should be truthful and evidence-backed;
- targeted resumes should include the blocks that match the vacancy and avoid distracting/downlevel blocks;
- the same canonical fact can be phrased in different employer language only when the bridge is honest.

## Block Types

Use these block types:

- `ai-transformation`: GenAI/LLM, AI adoption, AI workflows, human-in-the-loop, measurable ROI.
- `ai-sdlc`: AI-assisted development, AI Operating Model, developer productivity, quality gates, governance.
- `platform-scale`: high-load, DAU, orders/day, transactions/day, reliability, cost optimization.
- `stability-governance`: SDLC, CI/CD, SonarQube, unit testing, release control, incident reduction.
- `startup-product`: 0-to-1 product, MVP, first customers, roadmap, first engineering team.
- `business-unit`: P&L, presale, customer-facing delivery, portfolio, budget, commercial ownership.
- `fintech-regulated`: banking, payments, transactions, idempotency, compliance-adjacent delivery.
- `legacy-transformation`: modernization, tech debt, architecture refactoring, support model.

## Targeting Workflow

1. Parse the JD and extract:
   - hard requirements;
   - role-shape keywords;
   - industry/domain keywords;
   - stack/tool keywords;
   - seniority and operating mode.
2. Map every requirement to:
   - existing HH block;
   - new block variant needed;
   - do-not-claim item.
3. Generate or update repo-level block variants first.
4. Decide whether HH should receive:
   - a new profile-level experience block;
   - an edit to an existing profile-level experience block;
   - a new resume-specific experience block if HH opens only a resume-scoped form;
   - an edit to title, summary, skills, or about;
   - a profile-level entity toggle only for sections where HH exposes resume checkboxes.
5. Assemble the HH resume:
   - choose target title;
   - choose summary;
   - add or edit matching experience blocks;
   - include matching skills;
   - remove distracting/downlevel blocks.
6. Run truth check:
   - every strong claim must trace to `master-profile.md`, `evidence-bank.md`, or `selected-cases.md`;
   - no unsupported hard-skill ownership;
   - no invented dates, company names, metrics, or responsibilities.

## High-Value Use Case

If a vacancy is strategically strong and the base CV is scoring below 80 because exact words are missing, generate a targeted HH resume package:

- `keyword_gap`;
- `block_plan`;
- `repo_blocks_to_add_or_update`;
- `hh_sections_to_edit`;
- `resume_assembly`;
- `truth_check`;
- `copy_paste_hh_fields`.

## Output Location

Save packages to:

`personal-projects/personal-brand/workspace/job-intake/targeted-resumes/YYYY-MM-DD-company-role-targeted-resume.md`

Save reusable block library updates to:

`personal-projects/personal-brand/workspace/resume-targets/hh-experience-block-library.md`

## Write Safety

Before changing HH profile or a live HH resume:

- generate the package in repo first;
- show the diff-like plan to the user;
- only click/write in HH after explicit confirmation;
- keep old blocks unless the user explicitly asks to remove them.

## Semi-Manual Fallback

Use this mode when HH blocks headless automation with DDOS-GUARD, but the user's normal Chrome session can access the profile/resume editor.

Agent responsibility:

- parse the JD;
- generate the targeted HH package in `job-intake/targeted-resumes/`;
- produce copy-paste-ready fields for:
  - title;
  - about;
  - skills;
  - profile-level experience blocks;
  - resume assembly notes;
- mark truth-check risks and do-not-claim items;
- provide a short manual sequence for Chrome.

User responsibility:

- open HH in the normal Chrome session;
- paste the prepared fields;
- avoid saving if HH shows unexpected destructive actions or unclear linkage;
- send a screenshot if HH exposes new controls, resume checkboxes, or warnings.

Default manual sequence:

1. Open `https://novosibirsk.hh.ru/profile/me?hhtmFrom=ProfileActivator`.
2. Add or edit profile-level experience blocks in `Опыт работы`.
3. Open the target resume from `https://hh.ru/applicant/resumes`.
4. Update resume title, about, and skills if needed.
5. Confirm the targeted block appears in the intended resume.
6. If the block appears in unwanted resumes and no inclusion controls are visible, rollback only the newly added block.

## Open Questions

- Map the profile-level experience `+ Добавить` and per-block pencil actions from `novosibirsk.hh.ru/profile/me?hhtmFrom=ProfileActivator`.
- Identify whether profile-level experience edit forms expose "resumes with this workplace/block" checkboxes.
- If resume linkage exists, update this playbook before implementing write automation.
- Until then, prefer read/prepare/copy-paste workflows for experience and use Playwright write tools only after explicit confirmation.
