# Memory System

## Related Patterns

- `owned-context-operating-system.md` captures the user's recurring pattern across Personal Office, `secretar_bot`, and `mind_muscle`: chaotic human input -> structured owned memory -> concrete actions -> later search/context.

## Architecture

Personal Office uses hybrid agent memory:

- short-term working memory;
- episodic dated memory;
- semantic compressed topic memory;
- entity memory;
- procedural memory through `.codex/skills/`;
- retrieval/RAG rules;
- file-backed knowledge graph.

## Stable Rules

- Retrieval is not the same as memory; retrieval is the access layer over memory and source artifacts.
- Knowledge graph starts as markdown/jsonl in git.
- Wiki maps route agents to relevant sources so `AGENTS.md` stays small.
