---
domain: finance
source_of_truth:
  - finance/
  - tools/zenmoney-mcp/
skills:
  - memory-retrieval
memory:
  - memory/semantic/topics/finance.md
  - memory/entities/tools/
retrieval:
  - memory/retrieval/search-rules.md
  - memory/knowledge-graph/nodes.jsonl
  - memory/knowledge-graph/edges.jsonl
safety:
  - minimize_sensitive_financial_data
  - use_zenmoney_read_only_by_default
do_not_read_by_default:
  - life/health-lifestyle/health-facts/
---
# Finance Map

Use for personal and family money, assets, obligations, taxes, investments, major financial decisions, and ZenMoney-backed transaction history.
