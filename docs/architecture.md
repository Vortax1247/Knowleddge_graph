# Architecture boundary

```text
User / Desktop
      |
Conversation contract
      |
Governance gates -------- Human confirmation
      |
LLM runtime ----- Knowledge graph ----- Provenance
      |                 |
Evaluation         Bounded memory
      |
Canary / audit / rollback
```

The LLM proposes language. The graph stores structured knowledge with provenance. Memory has a dedicated namespace. Governance decides whether a transition or external effect is allowed. Evaluation datasets remain separate from candidate preparation.

The public showcase does not include private data paths or executable production configuration.
