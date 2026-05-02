---
id: bp:BP05B:dynamic-view
type: dynamic-view
name: BP05B - Provider manages resource descriptions – Dynamic view
of: bp:BP05B
since: r3.0
---

# BP05B Dynamic View

## Source

> **See also: [Business process overview](./README.md)** — narrative
> description of this business process, including actors, prerequisites,
> outcomes, and the full hierarchy of sub-processes.

Extracted from functional-and-technical-architecture-specifications.md, section 4.3.2.

---

## Trace

BP05B covers four sub-flows that a Provider uses to manage self-descriptions (SDs) — the metadata records describing their offered resources.

> **Images not available**: The four sequence diagrams (image58–image61) referenced in the source document are not present in this repository. Embed them here once available, using the pattern `![BP05B-<sub-flow>](./media/BP05B-<sub-flow>.png)`.

### Sub-flow 1 — Define and Publish Self-Description

This flow describes how a provider creates and publishes a self-description in the Catalogue. Resources referenced by the SD (e.g., deployment scripts for infrastructure offerings) must be created first.

1. **Schema Syncronisation** — The SD Tooling component on the Provider node requests schema definitions from its local Schema Registry, which is kept in sync with the Governance Authority's Schema Registry. Retrieved schemas are stored locally for quick access.
2. **Create Self-Description** — The Provider creates a new SD or modifies an existing one via the SD Manager user interface.
3. **Syntax Validation** — The Syntax Validation component within SD Tooling checks the SD's structure and format. If issues are found, the Provider is prompted to correct them.
4. **Registering Self-Description** — The validated SD is sent to the Connector, where it is registered as an asset and linked to a connector instance for controlled consumer access.
5. **Signing and Publication** — The Signing/Publication Service signs the SD with the Provider's private key and publishes it to the Catalogue. A signed copy is also stored in the Provider's Wallet.
6. **Semantic Validation** — The Catalogue on the Governance Authority node checks the SD against the data space's vocabularies and ontology standards.
7. **Quality Check** — The Catalogue applies quality rules. If issues are found, the end user is notified; if all checks pass, a confirmation is sent.
8. **Database Storage** — The validated SD and its metadata are stored in the Catalogue's database, making it discoverable by other participants.

### Sub-flow 2 — Retrieve SD Metadata

A Provider retrieves the metadata (e.g., publication status) of a previously published SD.

1. **Initiate Metadata Request** — The Provider sends the SD's unique identifier to the Catalogue on the Governance Authority Node.
2. **Query Metadata** — The Catalogue queries its Metadata Database for the requested record.
3. **Return Metadata** — The Catalogue returns the metadata to the Provider's SD Manager.
4. **Display to User** — The SD Manager presents the metadata, including current status, to the end user.

### Sub-flow 3 — Retrieve Full Self-Description

A Provider retrieves the complete content of a previously published SD.

1. **Initiate SD Request** — The SD Manager sends the SD ID to the Management Service on the Governance Authority Node.
2. **Query Self-Descriptions** — The Management Service queries the Self-Description Database for the matching record.
3. **Respond with Self-Description** — The full SD is returned to the Provider.
4. **Display to User** — The SD Manager displays the SD to the end user via its interface.
5. **Optional Storage** — The Provider may optionally store the retrieved SD in their Wallet for offline access.

### Sub-flow 4 — Revoke a Self-Description

A Provider changes a published SD's status to revoked, removing it from active circulation.

1. **Initiate Status Change** — The Provider sends the SD ID and a revocation request to the Catalogue on the Governance Authority Node.
2. **Revoke SD** — The Catalogue updates the SD's status in its database.
3. **Response and Display** — The Catalogue returns the updated status to the SD Manager, which displays it to the end user.

---

## Participants

- [sd-tooling/](../../../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md) — SD Tooling / SD Manager (self-description creation, syntax validation, signing, publication)
- [simpl-schema-manager/](../../../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md) — Schema Management Service / Schema Registry (provides schema definitions for SD creation and validation)
- [schema-sync-service/](../../../data/semantics-and-vocabulary/schema-management/schema-sync-service/README.md) — Schema Sync Service (keeps Provider-side schema registry in sync with Governance Authority)
- [connector/](../../../integration/resource-sharing/resource-sharing-runtime/connector/README.md) — Connector (registers the SD as an asset for controlled consumer access)
- [simpl-catalogue/](../../../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) — Simpl Catalogue (semantic validation, quality checks, SD storage and discoverability)
- [signer-service/](../../../security/credential-management/signing/signer-service/README.md) — Signer Service (signs the SD with the Provider's private key before publication)
- [wallet/](../../../security/credential-management/wallet/wallet/README.md) — Wallet (stores signed copies of published SDs; temporary storage during retrieve flow)
