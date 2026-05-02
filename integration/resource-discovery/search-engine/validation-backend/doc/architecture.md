Source: source repo `data1/sdtooling-validation-api-be/README.md`. FTA spec, §4.3.1 (ACV Static — Catalogue Client Service, Validation Backend sub-component) and §6.1.2 (TCV Static — Catalogue Client Service).

# Validation Backend — architecture

## Business view

API service that performs **syntactic and structural validation** of self-descriptions against the active SHACL schema before publication to the federated catalogue, and validates the **resource-address parameters** that identify the source (Provider Agent) and destination (Consumer Agent) sides of a data exchange.

By validating on the agent side, this service catches malformed self-descriptions and bad address values before they hit the Catalogue's Quality Rule Validation, surfacing actionable error messages directly to the SD-Tooling UI on the Provider side and to the Catalogue Client UI on the Consumer side.

Capability-map placement: Integration dimension → Resource discovery capability → Search engine business service. Sits beside the [Catalogue Client Application](../catalogue-client-application/doc/architecture.md) and the [Contract Consumption Adapter](../contract-consumption-adapter/doc/architecture.md) within the same business service.

**Business processes supported:**
- [BP05B Provider manages resource descriptions](../../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/README.md) — Provider-side syntactic validation before publication.
- [BP09A Consumer consumes a data resource](../../../../../foundations/business-processes/BP09A-consume-data-resource/README.md) — Consumer-side Destination-Address validation before transfer.

## Data view

The Validation Backend is **stateless**. It reads from the local schema cache populated by the [Schema Sync Service](../../../../../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/doc/architecture.md) (TTL files on a shared persistent volume); validation results are returned synchronously to the caller and not persisted.

## Application view

### Internal decomposition

Spring Boot service exposing a small REST API:

- **Self-description validation endpoint** — accepts a JSON-LD self-description, runs syntactic validation against the active SHACL schema (loaded from the local schema cache), and returns a structured error report.
- **Resource Address validation endpoint** — checks the Resource Address fields of a self-description (Provider side: Source Address — where the asset physically lives; Consumer side: Destination Address — where transferred assets land).
- **Structured error reporting** — every validation outcome includes detailed error info for troubleshooting and audit.

The service is deliberately small and modular so that validation logic can be extended for future schema evolutions or domain-specific rules without changing the API surface.

### Deployment topology

Deployed on **both the Provider Agent and the Consumer Agent**, with subtly different invocation patterns:

- **Provider Agent**: invoked by [SD Tooling](../../../../../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md) to validate a self-description before catalogue registration and publication. The first step of the SD Tooling publication flow (`enrichAndValidate`) is the entry into this service.
- **Consumer Agent**: validates the **Destination Address** in a self-description — the endpoint where a transferred asset will be delivered. The [Contract Consumption Adapter](../contract-consumption-adapter/doc/architecture.md) calls this service before initiating a Transfer Process.

### Key integrations

- [SD Tooling](../../../../../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md) — primary Provider-side caller (the `enrichAndValidate` step of its publication flow).
- [Contract Consumption Adapter](../contract-consumption-adapter/doc/architecture.md) — primary Consumer-side caller.
- [Schema Sync Service](../../../../../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/doc/architecture.md) — provides the local TTL schema cache that this service reads on each validation request.
- [Authorisation](../../../../../security/access-control-and-trust/authorisation/authorisation/doc/architecture.md) — Tier-1 Gateway routes inbound calls.

## Technical view

- **Source repo**: `data1/sdtooling-validation-api-be`.
- **Language / runtime**: Java 21+, Maven 3.9+, Spring Boot.
- **SHACL processing**: pulls TTL constraints from the local persistent-volume cache; validates JSON-LD documents against them.
- **Connectivity prerequisites** (per source): SD-Tooling and Contract Consumption are the inbound clients; reads from the agent-local persistent volume populated by Schema Sync.

## Security view

- **No public ingress** — only Tier-1-Gateway-mediated traffic from the agent-local SD-Tooling and Contract Consumption services. There's no externally-callable validation endpoint.
- **Stateless** — no persistent store to compromise; failure mode is "validation request denied", not "data leaked".
- The service has **no write access** to anything outside its own JVM (logging excepted). It reads from the schema cache (which the [Schema Sync Service](../../../../../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/doc/architecture.md) keeps writable to itself only); a compromise here cannot poison schema content.

Threat model: not yet documented.

Secrets management: not applicable — no first-party secrets. The Tier-1 Gateway handles auth-token validation upstream.

## Testing

Strategy: Spring Boot tests with fixtures of valid and invalid SHACL/JSON-LD documents per resource type. CI/CD runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
