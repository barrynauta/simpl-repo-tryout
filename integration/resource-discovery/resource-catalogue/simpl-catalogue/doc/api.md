Source: functional-and-technical-architecture-specifications.md, §4.5 Interfaces (row 9, "Catalogue"), §6.5 Federated Catalogue.

# Simpl Catalogue — API

The Catalogue exposes a single synchronous REST API, branded in the spec as the **GAIA-X Federated Catalogue API**. The canonical OpenAPI definition lives in the upstream/forked source repository.

- Upstream technical definition: <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-fc-service/-/blob/develop/openapi/fc_openapi.yaml?ref_type=heads>

When this documentation catalogue adds a local mirror of the OpenAPI file, it will live alongside this page as `fc_openapi.yaml`. Until then, treat the upstream link as authoritative.

## Endpoints

From §4.5 interfaces table, row 9 (Catalogue):

| Method | Path | Description |
|---|---|---|
| GET | `/schemas` | Get a full list of all vocabularies and schemas stored in the catalogue. |
| POST | `/schemas` | Add a vocabulary or schema to the catalogue. |
| GET | `/schemas/{schemaId}` | Get a specific schema or vocabulary. |
| DELETE | `/schemas/{schemaId}` | Delete a schema or vocabulary. |
| POST | `/self-descriptions` | Publish a self-description to the catalogue. |
| GET | `/self-descriptions/{self_description_hash}` | Get the complete self-description. |
| POST | `/self-descriptions/{self_description_hash}/revoke` | Revoke a self-description. |
| POST | `/query` | Send a Cypher query to the Neo4j database for search (used for both quick and advanced search). |
| POST | `/verification` | Validate a self-description on Semantics, VPSignature and/or VCSignature depending on the options selected in the request. |

## Callers

The Catalogue REST API is called by:

- [Catalogue Client Application](../../../search-engine/catalogue-client-application/doc/architecture.md) — issues search requests (via Query Mapper Adapter) and retrieves full self-descriptions.
- [SD Tooling](../../../../../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md) — publishes signed self-descriptions.
- [Query Mapper Adapter](../doc/architecture.md#internal-decomposition) — forwards translated, policy-filtered queries on behalf of search clients.

## Asynchronous interfaces

The Catalogue does not expose an asynchronous / event-driven API of its own in Release 3.0. Schema lifecycle events it reacts to are produced by the [Schema Management Service](../../../../../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md) and dispatched by the Schema Sync Service; the Catalogue consumes schema updates from its Vocabulary Datastore rather than via a Kafka topic on its own perimeter.

## Authentication

All calls require a JWT issued by the Tier 1 Authentication Provider (Keycloak). RBAC and ABAC enforcement happen in the [Authorisation](../../../../../security/access-control-and-trust/authorisation/authorisation/doc/architecture.md) gateway that fronts the Catalogue. See also `doc/architecture.md` → Security view.

## API guidelines compliance

Per §4.5 interfaces table (row 9), the "API Guidelines Phase 1 Compliancy" column for the Catalogue is blank — the upstream XFSC endpoints have not been marked as compliant with Simpl's Phase 1 API guidelines. This is a known gap; `Status: compliance not yet verified.`
