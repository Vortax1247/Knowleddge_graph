# Governance model

## Authority boundary

The system treats these concepts as separate:

- **generation**: a model proposes language;
- **knowledge**: structured information remains attributable;
- **memory**: retained context uses a bounded namespace;
- **authority**: policy and human confirmation determine what may change or execute.

No memory entry or model response can grant itself authority.

## Candidate lifecycle

```text
prepare candidate
      |
run deterministic contracts
      |
evaluate on frozen holdout
      |
blind human comparison
      |
human release decision
      |
canary checks
      |
promote or roll back
```

## Invariants

- Holdout content is not opened to prepare the candidate.
- Automatic case approval is forbidden.
- Automatic model promotion is forbidden.
- Protected-file drift blocks promotion.
- A rollback path must exist before a release change.
- External effects require a distinct authorization gate.

## Why this matters

LLM quality is only one property of a production system. Provenance, permissions, reversibility and explicit abstention determine whether a generated answer can be trusted in context.
