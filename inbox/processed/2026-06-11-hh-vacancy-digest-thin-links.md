# HH Vacancy Digest - Thin Links

- Date: 2026-06-11
- Source: HH digest email for `CTO / Co-founder CTO / Head of Product Engineering`
- Gmail message id: `19eb6098ba5c311c`
- Gmail timestamp: `2026-06-11T09:35:37+03:00`

## What Arrived

The message was another thin vacancy digest with links only:

- `Технический директор ИИ` - БКС
- `Продуктовый руководитель команды` - МАГНИТ, Розничная сеть
- `Lead AI Engineer / AI Platform Architect` - Millennium
- `Head of Development / CTO` - HRScan
- `IT-партнёр AI-департамента` - Компания БКС
- `AI project manager` - СБЕР

## Routing Note

No full JD text was included, so this cannot be analyzed safely as a new vacancy.

Update on 2026-06-12: `Head of Development / CTO` - HRScan was retrieved through `headhunter_web` and routed into full job-intake artifacts:

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-12-hrscan-head-of-development-cto.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-12-hrscan-head-of-development-cto-analysis.md`
- `tasks/waiting/2026-06-12-hrscan-head-of-development-cto-employer-response.md`

Update on 2026-06-12: `headhunter_web.hh_web_extract_from_digest_urls` was used to process the remaining non-duplicate links from this digest.

Created full job-intake artifacts:

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/parked/2026-06-12-magnit-product-team-lead.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-06-12-magnit-product-team-lead-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-12-millennium-lead-ai-engineer-ai-platform-architect.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-12-millennium-lead-ai-engineer-ai-platform-architect-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/parked/2026-06-12-sber-ai-project-manager.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-06-12-sber-ai-project-manager-analysis.md`
- `tasks/active/2026-06-12-apply-millennium-lead-ai-engineer-ai-platform-architect.md`

Duplicate / already routed:

- `134025820` - HRScan - already applied / waiting.
- `134024015` - БКС IT-партнер AI-департамента - already analyzed and active apply/targeted-resume package exists.

Unavailable:

- `134025277` - БКС - `Технический директор ИИ`: HH returned "Вам недоступна эта вакансия" through the browser-backed tool.

Tooling gaps observed:

- `hh_web_extract_from_digest_urls` currently marks an inaccessible HH vacancy page as `success: true` with empty title/company and low-quality raw text. It should classify pages containing "Вам недоступна эта вакансия" as `inaccessible` / `access_denied`, not successful extraction.
- Digest processing should auto-deduplicate by vacancy id against `job-intake/INDEX.md` and existing `jd-archive`/`analyses` before creating work.
- Digest processing should emit a compact per-email processing report with: new full JDs, duplicates, inaccessible links, and recommended next tasks.

Mailbox cleanup:

- Gmail message `19eb6098ba5c311c` is fully processed and can be moved to Trash.
