# BP02 Dynamic View

## Source

> **See also: [Business process overview](./README.md)** — narrative
> description of this business process, including actors, prerequisites,
> outcomes, and the full hierarchy of sub-processes.

Extracted from functional-and-technical-architecture-specifications.md, section 4.4.2 (titled "ACV Dynamic - BP 02C – Manage Resource Description Schemas").

---

## Trace

This dynamic view describes the process by which a Governance Authority end user manages schemas for resource descriptions. A schema defines the structure that Providers must follow when creating self-descriptions for their resources (datasets, applications, infrastructure).

The end user can perform one of three actions:
- **Create a new resource description schema** — define a new schema from scratch.
- **Revoke an existing schema** — mark a schema as no longer valid, preventing its use in new self-descriptions.
- **Create a new version of an existing schema** — update a schema while preserving the previous version for backwards compatibility.

> **Image not available**: The sequence diagram (image70) referenced in the source document is not present in this repository. Embed it once available: `![BP02C sequence diagram](./media/BP02C-sequence.png)`.

> Note: The source document provides only a brief description for this dynamic view. More detail may be added in a future revision of the architecture specification.

---

## Participants

- [schema-management-service/](../../../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) — Schema Management Service (enables Governance Authority to create, version, and revoke resource description schemas)
