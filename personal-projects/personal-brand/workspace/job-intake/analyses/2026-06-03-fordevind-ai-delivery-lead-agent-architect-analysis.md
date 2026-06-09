# JD Analysis - Фордевинд - AI Delivery Lead / архитектор разработки на AI-агентах

## Metadata

- Date: 2026-06-03
- Source: HH chat / ИИ-помощник
- Company: Фордевинд
- Role title: AI Delivery Lead / архитектор разработки на AI-агентах
- Location / format: fully remote, flexible schedule
- Salary: 270 000 - 420 000 RUB net/month
- Link: hidden / unavailable
- Archive file: `../jd-archive/2026-06-03-fordevind-ai-delivery-lead-agent-architect.md`

## Raw JD Summary

AI-first product engineering role for B2B/B2C products. Need a technical leader / lead engineer who can audit architecture and build a repeatable AI-agent-based development process instead of chaotic crunch. Requires practical AI coding agents experience such as Cursor, Claude Code, Copilot; understanding of agent workflows; web/mobile/backend architecture; CI/CD; automated testing; English C1. Product LandComp 2.0 is positioned as having a real AI core, not CRUD with AI wrapper.

## Classification

- Primary track: AI Transformation
- Secondary track: Stability & Governance
- Seniority: AI Delivery Lead / hands-on architect / technical lead
- Role shape: playing architect, AI-first SDLC/process builder, delivery lead
- Business context: AI-first product development, remote, likely compact team

## Match Score

- Overall: high
- Leadership: high
- Architecture: high
- Delivery / operations: high
- AI-first SDLC / coding agents: high if framed honestly through practical usage and process
- CI/CD / testing automation: high
- English C1: likely screening risk if they verify live communication
- Hands-on: medium risk; avoid sounding like pure executive CTO
- Risk: medium

## Best CV

- Recommended CV: `AI Transformation Lead - AI Automation Architect.pdf`
- Use as-is / tailor: use as-is for initial screening; tailor later if employer responds.
- Tailoring notes: if process continues, tailor headline toward `AI Delivery Lead / AI-first Engineering Architect`.

## Evidence To Use

- AI-assisted development and practical use of LLM/coding agents in SDLC.
- Arameem / ToYou: CI/CD, unit testing, quality gates, SonarQube, release governance, production discipline.
- Arameem / ToYou: GenAI/LLM customer support automation with internal APIs, quality control and human escalation.
- Fincomtech: CTO/co-founder, product from zero, architecture, cloud infrastructure, DevOps basics, pilots.
- Enterprise / high-load architecture: web/backend/mobile-adjacent product platforms, APIs, integrations, payment/transaction workflows.

## Risks

- They may expect very current hands-on daily usage of Cursor / Claude Code / Copilot and deep agent workflow design.
- Salary range may indicate role below full CTO level; overqualification needs to be softened.
- English C1 can be a practical filter.

## Risk Mitigation

- Answer as playing architect: uses AI agents for research, design alternatives, code review, tests, refactoring, documentation and prototypes.
- Emphasize process: decomposition, context package, prompts, verification, tests, review, CI/CD, rollback.
- Do not claim unsupervised autonomous coding in production; stress human review and quality gates.
- Keep 200+ org scale as background proof, not the opening.

## Screening Answer

Question: "Расскажите, доводилось ли вам использовать Cursor или Copilot в реальных проектах? Если да - как именно они вписывались в ваш рабочий процесс?"

```text
Да, использовал AI coding assistants в реальной работе. Больше всего - как инструмент для ускорения engineering workflow, но не как замену архитектурного решения или code review.

Как это обычно вписывалось в процесс:
- на этапе анализа - быстро разобрать существующий код, зависимости, контракты API, возможные точки риска;
- на этапе проектирования - подготовить варианты реализации, проверить edge cases, сформулировать technical plan и критерии приемки;
- при разработке - генерировать черновики кода, тесты, миграции, вспомогательные скрипты, документацию, затем вручную доводить и проверять;
- при ревью - искать регрессии, несоответствие требованиям, security/privacy риски, проблемы с поддерживаемостью;
- в CI/CD и качестве - использовать agents как часть процесса вокруг тестов, статического анализа, quality gates и release discipline.

Для меня важен не просто факт использования Cursor/Copilot, а повторяемый agent workflow: правильно собрать контекст, дать агенту ограниченную задачу, зафиксировать expected result, прогнать тесты, проверить diff, не пускать изменения в production без инженерной валидации. В таком формате AI ускоряет delivery и снижает рутину, но ответственность за архитектуру, качество, безопасность и эксплуатацию остается у engineering lead.

Отдельно я использую этот подход шире, чем просто autocomplete: для прототипирования AI/LLM-сценариев, анализа архитектуры, подготовки тест-кейсов, документации, разборов production/process issues и улучшения SDLC. Поэтому сама задача построить AI-first инженерную практику с понятным процессом мне близка.
```

## Screening Answer 2

Question: "Можете привести пример архитектуры agent workflow, где есть роли planner и executor? Как бы вы их распределили и организовали взаимодействие?"

```text
Да. Я бы разделял planner и executor по принципу "планирование и контроль контекста" vs "ограниченное выполнение конкретной задачи".

Пример workflow для изменения в продукте:

1. Planner получает business/technical requirement, текущий контекст системы, ограничения по архитектуре, тестам, безопасности и срокам. Его задача - не писать код сразу, а разложить работу:
   - уточнить цель и acceptance criteria;
   - определить затронутые модули, API, данные, миграции, интеграции;
   - выявить риски и зависимости;
   - разбить задачу на небольшие executable steps;
   - для каждого шага сформировать контракт: что сделать, какие файлы смотреть, какие тесты должны пройти, что считать готовым.

2. Executor получает только один ограниченный step, нужный контекст и критерии приемки. Его задача - выполнить изменение: написать код, тест, миграцию, документацию или подготовить diff. Executor не должен самостоятельно расширять scope без возврата к planner.

3. После выполнения planner или отдельный reviewer-agent проверяет результат:
   - соответствует ли diff задаче;
   - не сломаны ли контракты и архитектурные ограничения;
   - есть ли тесты и проходят ли они;
   - нет ли security/privacy/regression рисков;
   - нужен ли следующий iteration или rollback.

Я бы организовал взаимодействие через явные артефакты: task brief, implementation plan, список touched files, acceptance criteria, test results, review notes. То есть агенты общаются не свободным потоком мыслей, а через структурированный handoff.

В production-процессе важны guardrails:
   - planner не имеет права молча менять бизнес-цель;
   - executor не имеет права делать broad refactoring вне задачи;
   - каждый diff проходит human/code review и CI;
   - опасные операции, миграции, security-sensitive изменения и production actions требуют отдельного approval;
   - если agent confidence низкий или тесты не проходят, workflow возвращается на планирование, а не проталкивает изменение дальше.

В таком подходе planner отвечает за декомпозицию, контекст, риски и критерии качества, executor - за локальное выполнение, reviewer/human - за инженерную валидацию. Это делает agent workflow повторяемым: можно измерять cycle time, defect rate, percentage of accepted diffs, причины rollback и постепенно улучшать процесс.
```

## Screening Answer 3

Question: "Какие CI/CD инструменты вы внедряли и как организовали процесс code review в командах?"

```text
В разных командах я выстраивал CI/CD и code review не как отдельный инструмент, а как часть engineering governance: чтобы изменения проходили через понятный pipeline, тесты, quality gates и review до попадания в production.

По инструментам и практикам:
- Git-based workflow: feature branches, pull/merge requests, обязательное review перед merge;
- CI/CD pipelines в GitLab CI / Jenkins / аналогичных системах;
- automated build, unit tests, integration checks, статический анализ;
- SonarQube / quality gates как обязательный контроль качества;
- release branches / staged rollout / rollback-подходы для production изменений;
- инфраструктурные и deployment-процессы вокруг cloud/backend-сервисов;
- контроль миграций, конфигураций и environment-specific настроек.

В Arameem / ToYou я внедрял обязательное unit testing, SonarQube / quality gates и более дисциплинированный release process в большой распределенной инженерной организации. Эффект был измеримый: production defects снизились примерно на 60%, ручной QA effort - примерно на 90%, time-to-market - примерно на 20%, code review стал быстрее и предсказуемее.

Code review организовывал так:
- ни один значимый change не попадает в main/master без pull/merge request;
- review делают engineers, которые понимают соответствующий модуль или архитектурный контекст;
- reviewer смотрит не только стиль, но и contracts, tests, backward compatibility, security/privacy, performance и maintainability;
- для крупных изменений сначала делается короткий design/technical review, чтобы не спорить об архитектуре уже после написания всего кода;
- CI должен быть зеленым до merge, а quality gate - обязательным, а не рекомендательным;
- спорные архитектурные решения выносятся на tech lead / architecture review, чтобы не превращать обычный PR в бесконечную дискуссию.

Если переносить это на AI-first delivery, то я бы добавил к этому процессу AI-assisted review: agent может предварительно проверить diff, найти потенциальные edge cases, предложить тесты и подсветить рискованные места. Но финальное решение о merge все равно должно оставаться за инженером и pipeline: тесты, статический анализ, security checks, review и понятный rollback path.
```

## Questions For Recruiter / Hiring Manager

- Какая доля роли связана с личным hands-on coding в Cursor/Claude Code/Copilot, а какая - с архитектурой, процессом и ревью?
- Сколько людей сейчас в команде и какой уровень зрелости CI/CD, тестов и code review?
- Какие agents/tools уже используются и где сейчас основные боли: качество, скорость, архитектура, хаотичный delivery, onboarding?
- Что означает "реальное AI-ядро" LandComp 2.0: LLM agents, workflow engine, domain reasoning, data pipeline, RAG, internal tools?
- Какой measurable outcome ожидается за первые 3 месяца?

## Decision

- Apply: already applied.
- Priority: high.
- Next action: answer screening question; if contact continues, clarify hands-on expectations, English C1 verification and first 3-month scope.
