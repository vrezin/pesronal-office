# JD Matching Rules Draft

Черновик правил. Это не финальная политика, а стартовая версия для обсуждения и правки на реальных вакансиях.

## 1. First Question

Главный вопрос при разборе JD:

> Что у них болит на самом деле?

Не выбирать резюме только по названию роли. Смотреть на обязанности, масштаб, язык вакансии и скрытый контекст.

## 2. CV Selection

### AI Transformation Lead

Выбирать, если JD содержит:

- AI / GenAI / LLM / agents / RAG;
- automation of business processes;
- внедрение AI в поддержку, продажи, документы, knowledge base, SDLC;
- нужен человек между бизнесом, процессами, архитектурой и внедрением.

### Startup / Scale-up CTO

Выбирать, если JD содержит:

- MVP, first version, first customers, pilots;
- product roadmap, customer development, product engineering;
- co-founder / founding CTO / early team;
- нужно быстро собирать продукт и проверять гипотезы;
- небольшая или растущая команда.

### Heavy Enterprise

Выбирать, если JD содержит:

- VP Engineering / Director of Engineering / CTO for large org;
- 50+ / 100+ engineers;
- platform scale, complex org, multiple teams;
- architecture, governance, budget, leadership layer;
- enterprise delivery, high-load, production programs.

### Digital / Technology Transformation

Выбирать, если JD содержит:

- digital transformation;
- modernization program;
- CIO / CTO transformation;
- business processes, operating model, portfolio management;
- нужно менять IT как функцию, а не только чинить delivery.

### Stability & Governance

Выбирать, если JD содержит:

- production stability;
- incidents, monitoring, support, reliability;
- technical debt, legacy modernization;
- SDLC, release management, quality gates;
- predictable delivery, process discipline;
- hands-on engineering leadership.

### Business Unit / Integration

Выбирать или предложить tailored track, если JD содержит:

- systems integrator;
- ERP / 1C / enterprise automation;
- business unit head;
- P&L, sales, delivery, implementation;
- mini-CEO / mini-CTO format.

## 3. Risk Signals

### Overqualification

Риск высокий, если:

- команда меньше 20 человек;
- роль звучит как Head of Development, но требует ежедневной операционки;
- много "hands-on" и мало стратегии;
- JD явно ищет middle/senior manager, а не executive.

Что делать:

- подчеркивать playing manager / hands-on format;
- не начинать с 200+ people;
- выбирать Stability или Startup CV вместо Heavy Enterprise.

### Age / Long Career Signal

Риск высокий, если:

- роль явно ниже CTO/Head level;
- JD просит 5-7 years experience;
- компания early-stage или небольшая;
- HH-фильтр может читать общий стаж.

Что делать:

- выбирать версии с 11-15 years;
- не писать "20+ years" в cover letter;
- выносить ранний опыт в одну строку или убирать.

### Tech-Stack Gap

Риск средний, если:

- JD перечисляет конкретные языки / frameworks;
- роль при этом management/architecture.

Что делать:

- не притворяться hands-on expert во всем stack;
- писать "управлял направлениями / принимал архитектурные решения / обеспечивал quality and delivery";
- если нужно, добавить фразу про ability to go deep into architecture and code review at decision level.

### Domain Gap

Риск зависит от роли:

- Для CTO / Engineering Leadership domain gap обычно ниже, если есть scale, production and delivery match.
- Для industry-specific roles нужен мостик через похожие процессы: logistics, fintech, e-commerce, on-demand, enterprise integrations.

## 4. Cover Letter Rules

Сопроводительное должно:

- начинаться с прямого match к их боли;
- не пересказывать резюме;
- содержать 4-6 evidence bullets;
- заранее снимать 1-2 риска;
- завершаться вопросом про текущий challenge / expected impact in first 3-6 months.

Не использовать:

- "более 20 лет";
- слишком общие "ответственный, коммуникабельный";
- длинные биографии;
- сарказм про странности JD, даже если хочется.

## 5. Output Style

Для пользователя:

- коротко и прямо;
- сначала вердикт и рекомендуемое CV;
- затем cover letter;
- затем вопросы и риски.

Для архивного анализа:

- сохранять структурно по шаблону `jd-analysis-template.md`.

## 6. Relocation Filter

Когда вакансия зависит от географии, идти по этой последовательности:

1. Возможна ли полная удаленка без переезда?
2. Если нет, какая страна/город указаны как preferred or required location?
3. Открыть соответствующую country card и сравнить:
   - аренду;
   - школы для двух дочерей;
   - безопасность;
   - медицину;
   - образование;
   - разовые costs релокации;
   - ежемесячный cost delta;
   - помогает ли компания с релокацией.
4. Если помощи от компании нет, оценить вариант self-relocation.
5. Принять verdict:
   - `go`, если fit и экономика сходятся;
   - `maybe`, если надо уточнить comp / support / school path;
   - `no`, если relocation ломает family economics.

## 7. Country Card Maintenance

- Карточки стран должны обновляться периодически, а не только при конкретной вакансии.
- Новая страна сначала добавляется в `relocation/country-index.md`, затем получает отдельную карточку.
- Для новой страны сначала собрать базовые цифры из интернета и записать source URLs / date in the card.
- Если data point не проверен, помечать его как `TBD`, а не выдумывать.
