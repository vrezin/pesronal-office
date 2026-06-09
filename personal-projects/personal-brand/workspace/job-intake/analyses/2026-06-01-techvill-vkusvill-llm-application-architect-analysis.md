# JD Analysis - ТехВилл / ВкусВилл - Архитектор LLM-приложений

## Metadata

- Date: 2026-06-01
- Source: HH chat / ИИ-помощник
- Company: ТехВилл / ВкусВилл
- Role title: Архитектор LLM-приложений
- Location / format: fully remote, 5/2
- Salary: from 400 000 RUB gross/month
- Link: hidden / unavailable
- Archive file: `../jd-archive/2026-06-01-techvill-vkusvill-llm-application-architect.md`

## Raw JD Summary

Роль архитектора LLM-приложений для цифровой экосистемы ВкусВилл. Нужен опыт ML/AI 5+ лет, LLM 2+ года, RAG, agents, local inference, architecture of AI solutions, MLOps/LLMOps, Python, microservices, event-driven/serverless, cloud and message brokers. Роль ближе к AI architect / LLM solution architect, чем к CTO.

## Classification

- Primary track: AI Transformation / AI Automation Architect
- Secondary track: Stability & Governance only as platform/architecture proof
- Seniority: senior architect / tech lead
- Role shape: hands-on/architecture-heavy AI role
- Business context: retail ecosystem, internal digital products, LLM products for business/users/employees

## Best CV

- Recommended CV: `AI Transformation Lead - AI Automation Architect.pdf`
- Tailoring need: high if process continues.
- Possible tailored title: `LLM Application Architect / AI Automation Architect`
- Do not use: Heavy Enterprise, Startup CTO, Transformation.

## Match

Strengths:

- LLM/GenAI automation and AI implementation experience.
- RAG / agents / prompt engineering / OpenAI API / LLMOps skills in AI CV.
- Strong architecture, integration, production, high-load and enterprise background.
- Business-facing AI implementation, not research-only.

Gaps / Risks:

- JD asks for 5+ years ML/AI and 2+ years LLM.
- JD asks about local inference specifically.
- JD may expect strong Python/MLOps hands-on.
- Risk of being seen as AI transformation leader rather than LLM engineer/architect.

## Screening Question

Question: "Сколько лет вы работаете с LLM и был ли у вас опыт локального инференса?"

Recommended answer: be honest. Claim 2+ years with LLM only if counted from practical GenAI adoption in 2023. For local inference, say evaluation/prototyping/architecture familiarity unless there was production local inference.

## Suggested Answer

```text
С LLM практически работаю около 2 лет: с 2023 года использую LLM/GenAI в задачах автоматизации, анализа, knowledge base/RAG-подходов, внутренних ассистентов, AI-assisted development и интеграции LLM в бизнес-процессы через API и внутренние системы.

Мой основной опыт — архитектура и внедрение LLM-приложений: выбор сценариев, проектирование контура данных и интеграций, orchestration, prompt/RAG-подходы, контроль качества, human-in-the-loop, безопасность и эксплуатационная модель. На production/enterprise уровне работал больше с API/cloud-инференсом и интеграцией LLM в существующие процессы.

Опыт локального инференса есть на уровне прототипирования/оценки архитектуры и понимания ограничений: выбор open-source моделей, требования к GPU/памяти, latency/throughput, приватность данных, варианты развертывания и trade-off между локальным inference и API-based подходом. Глубоким ML-инженером по обучению моделей себя не позиционирую; моя сильная сторона — LLM application architecture и доведение AI-решений до работающего business/production контура.
```

## Screening Question 2

Question: "Какие MLOps или LLMOps инструменты и процессы вам доводилось внедрять на практике?"

Recommended answer: frame experience around practical LLMOps/application operations: prompt/version control, evaluation, monitoring, logs, human-in-the-loop, API integration, quality gates, access control, cost/latency, rollback. Avoid claiming full ML training pipeline ownership unless true.

## Suggested Answer 2

```text
Мой практический опыт ближе к LLMOps для прикладных LLM-сервисов, чем к классическому MLOps полного цикла обучения моделей.

Что внедрял / выстраивал на практике:
- версионирование prompts, системных инструкций и конфигураций LLM-сценариев;
- контур оценки качества ответов: тестовые наборы, ручная разметка, сравнение версий, критерии качества и регрессии;
- human-in-the-loop процессы: эскалация сложных кейсов человеку, контроль качества, разбор ошибок и донастройка сценариев;
- интеграцию LLM с внутренними API, knowledge base и бизнес-процессами;
- логирование запросов/ответов, анализ ошибок, мониторинг качества, latency и стоимости;
- ограничения доступа, privacy/security требования и контроль чувствительных данных;
- release-процесс для AI-функций: пилот, ограниченный rollout, сбор обратной связи, доработка и масштабирование.

Из инструментального стека использовал OpenAI API / ChatGPT, orchestration через backend/API слой, RAG/knowledge-base подходы, Git-based versioning, CI/CD и quality gates вокруг прикладного кода. В production engineering части опирался на привычные DevOps/SRE-практики: логи, метрики, мониторинг, rollback, code review, SonarQube, CI/CD.

Классические MLOps-платформы для обучения моделей с нуля не были моим основным фокусом. Моя зона — архитектура LLM-приложений и эксплуатационный контур вокруг них: качество, безопасность, интеграции, управляемый rollout и измеримый эффект для процесса.
```

## Screening Question 3

Question: "Был ли опыт проектирования event-driven или serverless архитектур именно в продакшене?"

Recommended answer: separate event-driven production architecture from serverless. Be clear if serverless was not the core production model.

## Suggested Answer 3

```text
Да, опыт проектирования event-driven / asynchronous архитектур в production был. В high-load продуктах я участвовал в проектировании транзакционных и интеграционных контуров, где было важно развязать сервисы, обеспечить надежную обработку событий, идемпотентность, ретраи, очереди, контроль статусов и наблюдаемость.

На практике это касалось интеграций между backend-сервисами, платежными/финансовыми операциями, accounting/settlement процессами, уведомлениями, внутренними API и внешними системами. В таких контурах ключевыми были не только брокеры сообщений, но и архитектурные принципы: event contracts, error handling, replay/retry strategy, dead-letter сценарии, consistency boundaries, мониторинг и разбор инцидентов.

По serverless: я хорошо понимаю архитектурный подход, сценарии применения и ограничения serverless, но полноценная production-платформа, где serverless был бы основным runtime-подходом, не была моей основной зоной ответственности. Обычно я работал с cloud / container / Kubernetes / CI/CD архитектурами и рассматривал serverless как точечный инструмент для подходящих задач, а не как базовую платформенную модель.
```

## Decision

- Apply: applied via HH / AI assistant.
- Outcome: rejected on 2026-06-03 by recruiter with a generic refusal; no detailed reason provided.
- Priority: closed.
- Likely reason: profile probably read as AI transformation / LLM application architecture rather than hands-on LLM architect with strong Python, local inference, MLOps/LLMOps and 5+ years ML/AI.
- Lesson: for future LLM Architect roles, treat local inference + MLOps/LLMOps + Python-heavy wording as a high-risk filter unless the vacancy also values product/enterprise AI implementation and cross-team architecture.
- Next action: do not pursue this vacancy further; keep similar roles only if they emphasize AI application/product architecture over deep ML platform hands-on.
