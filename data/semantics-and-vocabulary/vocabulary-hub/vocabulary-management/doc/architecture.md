Source: functional-and-technical-architecture-specifications.md, sections 4.3.1 (ACV Static — Vocabulary Management Service), 6.1.2 (TCV Static — Vocabulary Management Service).

# Vocabulary Management — architecture

## Business view

The Vocabulary Management component manages ontologies and controlled vocabularies used across the Simpl-Open data space to ensure semantic consistency in self-descriptions, resource discovery, and validation. The architecture specification lists this component under the Vocabulary hub capability; however, the ACV Static section for this service contains no body description — only the section heading and diagram reference. This document is a stub pending further content from the architecture team.

Note (from step 3, flag f-2): the ACV Static body for Vocabulary Management is empty in the architecture spec. The capmap note A7 observes that the vocabulary-hub may merge vocabulary and ontology management. Do not invent content; this stub reflects current spec state.

Capability-map placement: Data dimension → Semantics and vocabulary capability → Vocabulary hub business service.

![ACV Static view — Vocabulary Management Service](./media/image56.jpeg)

## Data view

Status: not yet documented. The TCV notes that the Vocabulary Management Backend is implemented as a File System, suggesting ontology/vocabulary files are stored as files rather than in a database.

## Application view

### Internal decomposition

**Vocabulary Management Backend:**
- Manages ontologies and controlled vocabularies.
- Implemented as a File System.

**Vocabulary Management Frontend:**
- User interface for Governance Authority users to manage vocabularies.
- Implemented as a ReactJS application.

### Key integrations

- [Schema Management Service](../../../schema-management/schema-management-service/doc/architecture.md) — vocabularies managed here may be referenced by schemas in the SMS; the relationship between vocabulary lifecycle and schema validation is not yet fully documented.
- [Simpl Catalogue](../../../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/doc/architecture.md) — the Catalogue's Vocabulary Datastore contains loaded ontologies and schemas used for semantic validation of self-descriptions.

## Technical view

- **Vocabulary Management Backend** — implemented as a File System.
- **Vocabulary Management Frontend** — implemented as a ReactJS application.

Deployment: deployed in Governance Authority Agents.

![TCV Static view — Vocabulary Management Service](./media/image146.jpeg)

## Security view

Status: not yet documented.

Threat model: Status: not yet documented.

Secrets management: Status: not yet documented.

## Testing

Strategy: Status: not yet documented.

PSO validation status: Status: not yet documented.

Requirements traceability: Status: not yet documented.
