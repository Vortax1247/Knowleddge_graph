# Publication security checklist

Before creating any public repository:

- remove `.env`, tokens, cookies, OAuth material and local service credentials;
- remove raw conversations, owner identity, memories and preference records;
- remove model weights, adapters and licensed datasets;
- replace absolute local paths and usernames;
- exclude runtime logs, audit details that contain user data and crash dumps;
- scan the complete Git history, not only the current tree;
- verify every source and dataset license;
- obtain human confirmation for the final file manifest;
- publish from a new clean repository, never by exposing the private development history.

## Reporting a concern

Do not open a public issue containing a suspected secret, private path or personal record. Contact the repository owner privately and provide only the minimum information needed to identify the affected file.

The presence of this package does not authorize publication of any file outside this repository.
