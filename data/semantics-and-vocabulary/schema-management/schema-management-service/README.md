<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Semantics And Vocabulary</a><br/>
            <a href="../README.md">Service: Schema Management</a><br/>
                <strong>Solution: Schema Management Service</strong><br/>
</p>
</div>

# Schema Management Service

The authoritative source of truth and lifecycle manager for all **SHACL** schemas and vocabularies within the Simpl-Open data space. Enables the Governance Authority to define, version, publish, and revoke the structure of self-descriptions for datasets, applications, and infrastructure resources. Exposes a Management API, a public Resolver Interface, and an event publisher that notifies downstream services of schema lifecycle changes.

Capability-map placement: `data / semantics-and-vocabulary / schema-management / schema-management-service`. This solution implements the **Schema management** business service.

Provenance: built by Simpl. Source repositories: `gaia-x-edc/simpl-schema-manager` (backend) + `gaia-x-edc/simpl-schema-manager-ui` (Vue 3 frontend). Licence: EUPL 1.2.

## Key features

- **Schema management** — upload new schemas, create new versions, publish, and revoke. Schemas are stored and downloaded in **Turtle (TTL)** format.
- **Versioning** — explicit version creation per schema, with publish/revoke as distinct lifecycle transitions.
- **SHACL validation** with detailed, human-readable error messages on failure (surfaced in the UI for authoring feedback).
- **Browsing** — paginated list with filtering by status and resource type.
- **Eventing** — publishes lifecycle events (publication, revocation) consumed by the [Schema Synch Service](../schema-synch-service/README.md) on Provider/Consumer agents.
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

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
