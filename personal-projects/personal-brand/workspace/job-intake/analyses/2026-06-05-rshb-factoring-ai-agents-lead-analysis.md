# JD Analysis - РСХБ Факторинг - Руководитель направления / Lead AI

## Metadata

- Date: 2026-06-08
- Source: HH vacancy text from user
- Company: РСХБ Факторинг
- Role title: Руководитель направления Лид ИИ
- Location / format: Moscow, first 3 months fully onsite, then hybrid 2-3 days office
- Salary: not specified
- Link: hidden / unavailable
- Archive file: `../jd-archive/2026-06-05-rshb-factoring-ai-agents-lead.md`

## Raw JD Summary

РСХБ Факторинг ищет владельца направления AI-агентов: не менеджера людей и не исполнителя ТЗ, а hands-on engineering/architecture lead, который с нуля построит production-grade мультиагентную систему для обработки документов, заключений по рискам/безопасности/кредитованию и интеграции с банковскими системами. Главный фильтр - доказанный production agentic AI, async Python, reliability, observability, graceful degradation, бизнес-метрики и готовность 3 месяца работать в офисе в Москве.

## Classification

- Primary track: AI Transformation
- Secondary track: Stability & Governance / Heavy Enterprise
- Seniority: lead/principal AI engineer / AI architect without people management
- Role shape: hands-on architecture owner, production AI systems lead, autonomous IC/lead
- Business context: banking/factoring, risk/security decision support, document workflows, high cost of error

## Match Score

- Overall: maybe / selective high if they accept AI application architecture instead of pure senior Python IC
- Leadership: high for autonomous ownership and cross-functional influence
- Architecture: high
- Delivery / operations: high
- Domain: high for fintech/banking/high-load/transaction reliability; medium for factoring specifics
- Tech stack: medium risk because they explicitly ask strong async Python
- Hands-on: medium-high risk if they expect daily senior Python coding
- Risk: high on "confirmed production agentic systems" wording

## Best CV

- Recommended CV: `AI Transformation Lead - AI Automation Architect.pdf`
- Use as-is / tailor: better to tailor cover letter strongly; CV can be sent as-is for quick HH response.
- Tailoring notes:
  - Lead with production LLM/agent orchestration, internal API tool use, human-in-the-loop, traceability, fallback, quality and business metrics.
  - Bring banking/fintech and financial transaction reliability higher.
  - Defuse hands-on risk honestly: architecture owner who can read/write/review Python and build prototypes, but not position as full-time senior Python developer if that is not true.
  - Do not lead with 200+ people; use it as proof of production discipline and standards.

## Evidence To Use

- GenAI/LLM support automation in production: orchestration, internal API/tool integration, quality control, human escalation and measured business effect.
- High-load financial/transaction context: 100k+ delivery orders/day, peak 130k/day, 5+ financial orders per delivery order, up to 1M+ financial transactions/day.
- Engineering reliability: unit testing, SonarQube, quality gates, CI/CD/release discipline; production defects -60%, manual QA -90%, TTM -20%.
- Banking/fintech enterprise background: projects for Sberbank, Gazprombank and 10+ banks; financial workflows and enterprise integrations.
- MedVoice / sensitive-domain AI assistant: human verification, traceability, structured workflow, high cost of error.

## Risks

- Risk 1: JD is written as a very technical individual contributor role; "Async Python, strict typing, testing LLM behavior, observability" may be hard filter.
- Risk 2: They explicitly ask for "production agentic systems", not generic GenAI/LLM automation; need to describe agent/tool orchestration as a real production system without overclaiming.
- Risk 3: First 3 months fully onsite in Moscow, then 2-3 office days; practical location risk from Novosibirsk.
- Risk 4: No salary listed and experience "3-6 years" may hide a compensation/level mismatch despite senior wording.

## Risk Mitigation

- Mitigation 1: Use cover letter to focus on the hardest architecture decision: separating probabilistic LLM reasoning from deterministic business/process gates.
- Mitigation 2: Attach or offer a short private description of the production system: context, architecture, tool use, guardrails, observability, metrics, limits.
- Mitigation 3: Ask immediately about compensation range and exact Moscow presence expectation.
- Mitigation 4: If recruiter screens for daily coding, answer honestly: strong architecture/review/prototyping profile, not pure senior Python IC.

## Cover Letter

```text
Добрый день.

В вашей вакансии вижу сильное совпадение с моим текущим фокусом: production AI/LLM systems, agentic workflows, интеграция с внутренними сервисами, reliability, traceability и измеримый бизнес-эффект в доменах с высокой ценой ошибки.

Кратко по релевантному опыту:
- внедрял GenAI/LLM automation в production: LLM работала как оркестратор, обращалась к внутренним API и инструментам, а рисковые случаи уходили на human-in-the-loop;
- строил production discipline для крупных систем: quality gates, unit testing, SonarQube, release governance, наблюдаемость и контроль деградации;
- работал с high-load financial workflows: до 100k+ delivery orders/day, peak 130k/day, каждый заказ порождал 5+ финансовых операций, суммарно до 1M+ financial transactions/day;
- имею banking/fintech enterprise background: проекты для Сбербанка, Газпромбанка и 10+ банков;
- умею переводить неопределенность AI/LLM в управляемый бизнес-процесс: явные критерии качества, fallback, эскалации, логи, метрики и ответственность человека в критичных точках.

Самое сложное архитектурное решение при построении агентной системы для меня было не в выборе LangGraph/CrewAI/самописной оркестрации, а в разделении зон ответственности между LLM и детерминированным контуром.

LLM не должна "принимать решение" как черный ящик. Она должна выполнять ограниченные роли: классифицировать контекст, выбирать следующий шаг, готовить черновик действия или заключения, вызывать разрешенные инструменты и объяснять основание. А критичные переходы workflow - права доступа, бизнес-правила, финансовые действия, эскалации, финальное заключение, аудит и rollback - должны оставаться в проверяемом deterministic layer.

Это решение было правильным, потому что оно позволило совместить пользу LLM с production-требованиями: трассируемость, контроль качества, graceful degradation, возможность тестировать поведение, измерять бизнес-метрики и объяснять результат службам, которые не должны доверять "магии модели".

Буду рад обсудить, какие AI-agent сценарии у вас уже есть в прототипах и что считается главным результатом первых 3-6 месяцев: скорость обработки заявок, качество заключений, снижение ручной работы или запуск промышленного контура с observability и guardrails.
```

## Short Production System Description

```text
Production-кейс, который готов описать подробнее на интервью: GenAI/LLM automation для клиентской поддержки.

Архитектурно это был не простой чат-бот, а LLM orchestration layer вокруг внутренних API и инструментов. Система анализировала обращение, определяла сценарий, подтягивала контекст из внутренних систем, готовила ответ или действие, а неоднозначные/рисковые случаи эскалировала человеку. Важные элементы: tool/API access через ограниченные контракты, human-in-the-loop, fallback-сценарии, логирование, контроль качества, rollout по сценариям, метрики автоматизации и экономического эффекта.

Главный принцип: LLM отвечает за работу с неструктурированным текстом и выбор ограниченного следующего шага, но не получает неограниченную свободу действий. Критичные бизнес-решения, права доступа, финальные действия и аудит остаются в deterministic/process layer.
```

## Questions For Recruiter / Hiring Manager

- Какой фактический баланс в роли между hands-on async Python development, архитектурой, ревью и управлением AI-направлением?
- Какие agentic/LLM-прототипы уже есть и что именно нужно довести до production за первые 3-6 месяцев?
- Какие внутренние системы должны использовать агенты: документооборот, скоринг/риски, DWH, CRM, BPM, security systems?
- Какие метрики успеха уже определены: время обработки заявки, качество заключения, доля автоматизации, SLA, cost per decision?
- Какая компенсационная вилка заложена и насколько обсуждаем формат первых 3 месяцев в офисе для кандидата не из Москвы?

## Decision

- Apply: maybe / apply only if Moscow onsite and salary can be clarified early.
- Priority: medium-high by content, medium by practical constraints.
- Next action: send `AI Transformation Lead - AI Automation Architect.pdf` with the cover letter above; ask salary and onsite expectations in the employer question.
