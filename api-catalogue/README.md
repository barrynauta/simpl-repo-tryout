# API catalogue

All APIs exposed by Simpl-Open solutions, grouped by service. Solutions with a single API use `doc/api.md`; solutions with multiple APIs use an `api/` folder. Solutions whose API is not yet documented do not appear here (stub API files have been removed).

## Solutions with multiple APIs (`api/` folder)

### Authorisation
[`security/access-control-and-trust/authorisation/authorisation/api/`](../security/access-control-and-trust/authorisation/authorisation/api/README.md)

| API | Type | Description |
|-----|------|-------------|
| `tier1-gateway.openapi.yaml` | OpenAPI 3.x (REST) | Tier 1 gateway — RBAC enforcement for end-user-facing inbound traffic |
| `tier2-gateway.openapi.yaml` | OpenAPI 3.x (REST) | Tier 2 gateway — ABAC enforcement for agent-to-agent inbound traffic |

### Catalogue Client Application
[`integration/resource-discovery/search-engine/catalogue-client-application/api/`](../integration/resource-discovery/search-engine/catalogue-client-application/api/README.md)

| API | Type | Description |
|-----|------|-------------|
| `advanced-search.openapi.yaml` | OpenAPI 3.x (REST) | Advanced search backend — schema-driven search query API |
| `contract-consumption.openapi.yaml` | OpenAPI 3.x (REST) | Contract consumption adapter — resource offering retrieval and contract negotiation initiation |

### Connector
[`integration/resource-sharing/resource-sharing-runtime/connector/api/`](../integration/resource-sharing/resource-sharing-runtime/connector/api/README.md)

| API | Type | Description |
|-----|------|-------------|
| `management.openapi.yaml` | OpenAPI 3.x (REST) | Management API — asset/policy/contract management (EDC Management API) |
| `control-plane.openapi.yaml` | OpenAPI 3.x (REST) | Control plane DSP API — Data Space Protocol contract negotiation |
| `data-plane.openapi.yaml` | OpenAPI 3.x (REST) | Data plane API — data transfer initiation and management |

### Schema Management Service
[`data/semantics-and-vocabulary/schema-management/schema-management-service/api/`](../data/semantics-and-vocabulary/schema-management/schema-management-service/api/README.md)

| API | Type | Description |
|-----|------|-------------|
| `schema-management-api.openapi.yaml` | OpenAPI 3.x (REST) | Management API — private, authenticated; schema lifecycle management |
| `resolver-interface.openapi.yaml` | OpenAPI 3.x (REST) | Resolver Interface — public, read-only; raw RDF schema retrieval at stable URIs |

---

## Solutions with single API (`doc/api.md`)

| Solution | API doc | Summary |
|----------|---------|---------|
| Simpl Catalogue | [`doc/api.md`](../integration/resource-discovery/resource-catalogue/simpl-catalogue/doc/api.md) | Self-description publication, search, and management |
| Notification Service | [`doc/api.md`](../administration/notification-and-messaging/notification/notification-service/doc/api.md) | AsyncAPI v3.0.0 — `notifications` Kafka topic |

Solutions not listed above either use the `api/` folder pattern above, or have no documented API in the current release (no `doc/api.md` file). When API content becomes available for those solutions, a `doc/api.md` should be created and an entry added here.
