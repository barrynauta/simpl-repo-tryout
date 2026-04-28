Source: source repo `data1/edcconnectoradapter/README.md`. FTA spec, §4.3.1 and §6.1.2 — abstraction over EDC for SD-Tooling and Contract Consumption.

# EDC Connector Adapter — architecture

## Business view

Abstraction layer between the [Connector](../connector/doc/architecture.md) (Eclipse Dataspace Connector) and the upper-layer Simpl-Open components — primarily **SD-Tooling** (asset & policy registration) and **Contract Consumption** (Contract Negotiation and Transfer Process initiation). Decouples the business logic of those modules from the specific EDC implementation, enabling alternative connector technologies to be plugged in later without changing the consumers.

Capability-map placement: Integration dimension → Resource sharing capability → Resource sharing runtime business service. Sits beside the [Connector](../connector/doc/architecture.md) within the same business service — the adapter is *above* the Connector, not in front of it: callers reach the adapter, the adapter reaches the Connector's Management API.

## Data view

The EDC Connector Adapter is **stateless**. It carries no first-party persistent store — every call is a translation of the upstream request into one or more EDC API calls, with the response normalised before being returned. State machines live in the Connector's Control Plane.

## Application view

### Internal decomposition

Spring Boot service exposing a unified REST API. Internally:

- **Asset / policy registration façade** — exposes API methods for asset and policy registration on the EDC Connector, consumed by [SD Tooling](../../../../governance/resource-management/metadata-description/sd-tooling/doc/architecture.md). Translates each call into the equivalent EDC Management API request.
- **Negotiation initiation façade** — exposes API methods for initiating Contract Negotiation and Transfer Process operations, consumed by the [Contract Consumption Adapter](../../../resource-discovery/search-engine/contract-consumption-adapter/doc/architecture.md). Calls into the EDC Control Plane via the DSP API.
- **Translation layer** — request/response normalisation between Simpl-Open business calls and EDC protocol endpoints, including normalised error reporting.
- **Extensibility hook** — the abstraction is designed so a future replacement for EDC could be plugged in by swapping the implementation behind the same façades, without changing any upper-layer caller. This is one of the load-bearing reasons this service exists.

### Deployment topology

Deployed as an **internal cluster service** on both the Consumer Agent and the Provider Agent. It is *not* exposed through any public gateway — its callers are themselves agent-internal services.

- **Provider Agent**: between [SD Tooling](../../../../governance/resource-management/metadata-description/sd-tooling/doc/architecture.md) and the EDC **Provider** Connector. Handles asset registration and publication.
- **Consumer Agent**: between [Contract Consumption Adapter](../../../resource-discovery/search-engine/contract-consumption-adapter/doc/architecture.md) and the EDC **Consumer** Connector. Handles negotiation and transfer initiation.

This dual deployment ensures consistent interaction patterns across both agents, promotes connector-agnostic integration, and supports long-term maintainability and interoperability.

### Key integrations

- [Connector](../connector/doc/architecture.md) — sole downstream target. Every adapter call resolves to one or more EDC API calls.
- [SD Tooling](../../../../governance/resource-management/metadata-description/sd-tooling/doc/architecture.md) — Provider-side caller for asset & policy registration.
- [Contract Consumption Adapter](../../../resource-discovery/search-engine/contract-consumption-adapter/doc/architecture.md) — Consumer-side caller for Contract Negotiation / Transfer Process initiation.
- **Apache Kafka** — used for event-driven status updates back to upstream callers.
- **Security Vault** — credentials for talking to the EDC Connector.

## Technical view

- **Source repo**: `data1/edcconnectoradapter`.
- **Language / runtime**: Java 21+, Maven 3.9+, Spring Boot.
- **Connectivity prerequisites** (per source):
  - Kafka cluster connectivity (event-driven status updates).
  - EDC Consumer/Provider Connector connectivity (the downstream API).
  - Security Vault connectivity (credentials).
  - Lombok-aware IDE for development.

## Security view

- **Internal-only service** — not reachable from outside the cluster. Callers (SD Tooling, Contract Consumption Adapter) are themselves in-cluster Spring Boot services.
- **mTLS / Service Mesh** for east-west traffic between this adapter, the Connector, and its upstream callers (the agents enforce service-mesh policy, not this adapter).
- **No first-party authorisation logic** — the adapter trusts that upstream callers have been authenticated and authorised by the Tier-1/Tier-2 Gateways before reaching them. Role-based access to the actual operations is enforced upstream.
- **Centralised error handling** — homogeneous error responses prevent EDC-internal error structures (which can leak implementation detail) from reaching upstream business services.

Threat model: not yet documented.

Secrets management: HashiCorp Vault — credentials for the EDC Connector API, sourced via the agent's standard Vault path.

## Testing

Strategy: Spring Boot integration tests against a stub EDC Management API; contract tests guarantee the adapter's API stays stable across EDC version bumps. CI/CD runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
