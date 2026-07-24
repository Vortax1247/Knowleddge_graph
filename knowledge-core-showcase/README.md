# Knowledge Core

> A governed, local-first GenAI engineering showcase.

Knowledge Core explores how to build a personal GenAI system without confusing language generation, knowledge, memory and authority. This public repository is a sanitized architectural showcase, not the private runtime.

![Knowledge Core architecture](assets/architecture.svg)

## Engineering question

How can a local assistant learn and specialize while keeping facts attributable, evaluation independent, releases reversible and external actions under human control?

## Architecture principles

1. **Generation is not knowledge.** The LLM proposes language; structured facts remain connected to provenance.
2. **Memory is not authority.** A stored preference cannot grant permission.
3. **Evaluation is isolated.** Frozen holdouts remain separate from candidate preparation.
4. **Promotion is governed.** Human review, canary checks and rollback precede release changes.
5. **Limits are product features.** The current state is documented as precisely as the results.

## Verified snapshot

| Evidence | Result |
|---|---:|
| V6 governance architecture | 9 layers |
| Verified knowledge graph | 1,642 nodes |
| Verified graph relations | 5,143 |
| Corrected V4 blind human review | 20 candidate preferences, 0 control |
| Desktop build | 3.1.0 |
| Test files in the private repository | 123 |
| Frozen V5 holdout | 60 cases |
| Planned V5 curriculum | 72 cases |

## Current state

- V4.1 is the active transitional parent.
- V5 is prepared but not trained or promoted.
- Tri-Core remains an inactive shadow architecture.
- External execution remains subject to explicit human confirmation.
- The project makes no claim of subjective consciousness or physical quantum mechanisms.

## Repository map

```text
assets/       Public architecture diagram
docs/         Architecture, governance, evidence and roadmap
examples/     Sanitized contracts and result summaries
scripts/      Offline package validation
```

## Validate the package

```bash
python scripts/validate_showcase.py
```

## Security boundary

This repository contains no model weights, private memories, identity records, raw conversations, secrets, production configuration or private Git history. Read [SECURITY.md](SECURITY.md) before proposing a disclosure.

## Author

Adrien Hummel - GenAI Engineer  
[GitHub](https://github.com/Vortax1247)

## License

Copyright © 2026 Adrien Hummel. All rights reserved.
