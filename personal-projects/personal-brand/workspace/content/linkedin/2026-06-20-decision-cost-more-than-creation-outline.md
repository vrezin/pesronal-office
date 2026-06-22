# Зачем ускорять SDLC, если решение принять дороже, чем создать?

Status: outline / second article candidate  
Author: Vladimir Rezin  
Relation: expands the "Когда согласование дороже разработки" meaning from `../2026-06-20-governance-chaos-meaning-extraction.md`

## Core Thesis

AI changes the economics of software delivery by lowering the cost of producing artifacts: analysis, requirements, architecture drafts, code, tests, documentation, acceptance criteria.

But if the organization does not lower the cost of decision-making, approval, ownership and acceptance, then AI only exposes a new economic absurdity:

> the solution becomes cheaper to create than to approve.

In that world, accelerating SDLC is not enough. The organization needs to accelerate decision throughput.

## Hook

Мы много говорим о том, как AI ускоряет SDLC.

Но есть неудобный вопрос:

> Зачем ускорять создание решения, если стоимость принятия этого решения становится выше стоимости его разработки?

## Argument

AI can make engineering artifacts cheaper:

- requirements analysis;
- specification;
- architecture options;
- code;
- tests;
- documentation;
- RACI drafts;
- acceptance criteria.

But AI does not automatically make organizational decisions cheaper.

If a one-month implementation requires three months of stakeholder discovery, re-briefing, late approvals, infrastructure clarification, security loops, operations review and repeated scope reopening, then the economic center of the project is no longer development.

It is decision cost.

## Key Distinction

Creation cost:

- how expensive it is to produce the solution.

Decision cost:

- how expensive it is for the organization to accept that solution as valid, owned, approved and implementable.

AI lowers creation cost.

Bad governance keeps decision cost high.

Therefore the bottleneck does not disappear; it moves.

## Core Line

AI can make a solution cheaper to create.

Only an executable organization can make it cheaper to accept.

## Practical Consequence

Before selling or starting an AI-accelerated delivery project, check decision economics:

- Who owns the decision?
- Who must be in the first decision quorum?
- Which stakeholders can reopen scope?
- Which acceptance gates are mandatory?
- What is the cost of new requirements after baseline?
- Is this a delivery project or a paid discovery / architecture alignment project?

## Final Direction

If decision cost is higher than implementation cost, the right answer is not more AI.

The right answer is to redesign the decision loop.

