<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Data</a><br/>
        <a href="../README.md">Capability: Semantics And Vocabulary</a><br/>
            <strong>Service: Schema Management</strong><br/>
</p>
</div>

# Schema management

Authoritative lifecycle management of self-description schemas (SHACL files) and their synchronisation to Provider and Consumer Nodes.

## Solutions

- [Apache Jena Fuseki](apache-jena-fuseki/README.md) — the SHACL store backing schema validation. _(External OSS.)_
- [Schema Sync Adapter](schema-sync-adapter/README.md) — Synch adapter that distributes schema updates from the Schema Manager to participant nodes.
- [Schema Sync Service](schema-sync-service/README.md) — the umbrella documentation for the schema synchronisation flow.
- [Sd Schema Util](sd-schema-util/README.md) — Python tool that generates ontology and SHACL shape files from YAML definitions.
- [Sd Tooling Api](sd-tooling-api/README.md) — Backend API for the SD Tooling user flow.
- [Sdtooling Sd Schemas](sdtooling-sd-schemas/README.md) — Repository of authored schemas / shape definitions used by SD Tooling.
- [Shacl](shacl/README.md) — Shapes Constraint Language reference and conventions used across schemas. _(External OSS.)_
- [Simpl Schema Manager](simpl-schema-manager/README.md) — Schema Manager backend (gaia-x-edc) — definitive source of truth for schema lifecycle.
- [Simpl Schema Manager Ui](simpl-schema-manager-ui/README.md) — Schema Manager Vue 3 frontend.
- [Simpl Schema Versioning](simpl-schema-versioning/README.md) — Versioning logic / store for schema iterations.


# Schema Management Service

## Key features

- **Schema management** — upload new schemas, create new versions, publish, and revoke. Schemas are stored and downloaded in **Turtle (TTL)** format.
- **Versioning** — explicit version creation per schema, with publish/revoke as distinct lifecycle transitions.
- **SHACL validation** with detailed, human-readable error messages on failure (surfaced in the UI for authoring feedback).
- **Browsing** — paginated list with filtering by status and resource type.
- **Eventing** — publishes lifecycle events (publication, revocation) consumed by the [Schema Sync Service](../schema-sync-service/README.md) on Provider/Consumer agents.
- **Authentication** — Keycloak with OAuth 2.0 PKCE flow and automatic token refresh on the UI side.

## Frontend configuration

Runtime environment is injected via an `env-config.js` file (read into `window._env_`):

| Variable | Purpose |
|----------|---------|
| `PUBLIC_AUTH_KEYCLOAK_SERVER_URL` | Keycloak base URL |
| `PUBLIC_AUTH_KEYCLOAK_REALM` | Realm (e.g. `participant`) |
| `PUBLIC_AUTH_KEYCLOAK_CLIENT_ID` | OAuth client ID (e.g. `frontend-cli`) |
| `PUBLIC_SCHEMA_MANAGER_API_URL` | Backend API base URL (no trailing slash) |

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [api/](api/README.md) — API specifications (OpenAPI: `gaia-x-edc/simpl-schema-manager/openapi/schema_openapi.yaml`).
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP02 Manage Resource Description Schemas](../../../../foundations/business-processes/BP02-configuration-governance-authority/dynamic-view.md)
- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
- [BP06 Consumer searches resources](../../../../foundations/business-processes/BP06-consumer-searches-resources/dynamic-view.md)

## Source code

- Backend: <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-schema-manager>
- Frontend: <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-schema-manager-ui>


