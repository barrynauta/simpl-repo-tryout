Source: source repo `orchestration-platform/asset-orchestrator/README.md`. FTA spec, §4.3.1 ACV Static — Data Orchestration Service (Asset Orchestrator sub-component) and §6.1.2 TCV Static — Data Orchestration Service.

# Asset Orchestrator — architecture

## Business view

Bridge service between the **Provider Connector** and the **Workflow Engine** (Dagster). The Provider declaratively binds a workflow definition to a self-described resource; when a Consumer accesses that resource through the connector, the Asset Orchestrator validates the configuration, submits the corresponding job to Dagster, and tracks its execution status.

Without the Asset Orchestrator, every data-resource sharing flow that needs pre-processing or transformation would require the Provider to glue connector events to orchestration jobs by hand. With it, that wiring is config-driven and runs as a standard piece of the Provider Agent.

Capability-map placement: Data dimension → Supporting data services capability → Data orchestration business service. Sits beside the [Orchestration Platform](../../orchestration-platform/doc/architecture.md) (the Dagster runtime) within the same business service.

**Business processes supported:**
- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/README.md)
- [BP09B Consumer receives a data processing service via application](../../../../foundations/business-processes/BP09B-consume-data-via-application/README.md)
- [SA01 Data orchestration](../../../../foundations/business-processes/SA01-data-orchestration/README.md)

## Data view

The Asset Orchestrator persists three things in PostgreSQL:

- **Workflow definitions** — a workflow is identified by name + version; references the Dagster code-location/job that implements it.
- **Resource ↔ workflow associations** — a self-description ID bound to a workflow definition plus a (validated) default configuration. May contain template variables resolved at run time from the consumption request.
- **Run history** — per-run metadata (resource ID, workflow ID, configuration snapshot, Dagster run ID, status, start/end times). Sourced from Dagster but cached locally so callers don't need to hit Dagster's GraphQL on every status query.

## Application view

### Internal decomposition

Spring Boot service exposing a REST API. Major endpoints:

- **Workflow registration** — POST/PUT a workflow definition, validated against a JSON schema.
- **Resource-workflow association** — bind a self-description to a workflow + default config; configuration is validated against the workflow's expected parameter schema before being accepted.
- **Execution submission** — invoked when the Provider Connector signals a consumer access; the orchestrator submits the job to Dagster (via the GraphQL API of the [Orchestration Platform](../../orchestration-platform/doc/architecture.md)).
- **Execution status & history** — query endpoints that return cached status from the local DB.

Errors follow **RFC 7807 — Problem Details** (`application/problem+json`).

### Key integrations

- [Orchestration Platform](../../orchestration-platform/doc/architecture.md) — submits jobs to the Dagster GraphQL API; resolves run state from there.
- [Connector](../../../../integration/resource-sharing/resource-sharing-runtime/connector/doc/architecture.md) — receives consumption events that trigger workflow execution.
- [SD Tooling](../../../../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md) — Provider authors workflow associations through the same UI/API surface that authors self-descriptions.
- Dagster code-locations under [Anonymisation and Pseudonymisation](../../../data-processing/anonymisation-and-pseudonymisation/README.md) — typical workflow targets when the Provider wants pre-processing applied before delivery.

## Technical view

- **Language / runtime**: Java 21+, Maven 3.9+.
- **Framework**: Spring Boot.
- **Persistence**: PostgreSQL 13+.
- **Build / packaging**: Maven → container image. Local dev: Docker 20.10+.
- **Repository access**: requires reachability of the EU GitLab Package Registry (Maven dependencies declared in the POM).
- **Deployment**: standalone microservice (not a library); typically deployed only on the **Provider Agent**.
- **Inter-service comms**: internal cluster only — relies on network-level security (mTLS / Service Mesh).

## Security view

- **No public ingress** — the Asset Orchestrator is an internal service; the only external entry to the Provider Agent is via the [Authorisation gateways](../../../../security/access-control-and-trust/authorisation/README.md). All authentication / authorisation for the orchestrator's APIs is handled by those gateways before the request reaches it.
- **mTLS / Service Mesh** for east-west traffic between the orchestrator, Dagster, and the connector.
- **Configuration validation** before execution prevents invalid or malicious configurations from being persisted or submitted to Dagster.
- **Audit trail** — every association change and every execution submission is recorded in PostgreSQL with the originating identity (resolved from the gateway's auth context).

Threat model: not yet documented.

Secrets management: Vault for DB credentials; service mesh handles in-cluster TLS material.

## Testing

Strategy: Spring Boot integration tests against an embedded Postgres; contract tests against the Dagster GraphQL API. CI/CD pipeline runs unit tests, SAST (SonarQube), and security tests (Fortify) on every commit.

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
