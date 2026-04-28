Source: source repo `data1/contract-consumption-be/README.md`. FTA spec, §4.3.1 (ACV Static — Catalogue Client Service, Contract Consumption Adapter sub-component) and §6.1.2 (TCV Static — Catalogue Client Service).

# Contract Consumption Adapter — architecture

## Business view

Consumer-side backend that lets the [Catalogue Client Application](../catalogue-client-application/doc/architecture.md) frontend **initiate** Contract Negotiation and Transfer Process workflows from a chosen catalogue entry, and **monitor** their progress in real time. Bridges the search-side experience (where the user finds an offering they want) and the resource-sharing runtime (where the actual contract negotiation and data transfer happen).

Capability-map placement: Integration dimension → Resource discovery capability → Search engine business service. Sits beside the [Catalogue Client Application](../catalogue-client-application/doc/architecture.md) within the same business service.

**Business processes supported:**
- [BP07 Establish usage contract](../../../../../foundations/business-processes/BP07-establish-usage-contract/README.md) — primary consumer.
- [BP09A Consumer consumes a data resource](../../../../../foundations/business-processes/BP09A-consume-data-resource/README.md) — the transfer-process side.

## Data view

This component does not own a primary store; it caches in-flight negotiation state in PostgreSQL so the Catalogue Client UI can poll status without hitting the Connector API on every refresh.

- **In-flight negotiation state** — per-request lifecycle records (offering ID, consumer identity, current state of the DSP Contract Negotiation state machine, current state of the DSP Transfer Process state machine).
- The authoritative state lives in the [Connector](../../../resource-sharing/resource-sharing-runtime/connector/doc/architecture.md)'s Control Plane (DSP-spec state machines); this adapter mirrors enough of it to drive the UI and its audit trail.

## Application view

### Internal decomposition

Spring Boot service exposing a REST API consumed by the Catalogue Client UI through the Tier-1 Gateway:

- **Negotiation initiation endpoint** — accepts an offering ID + the consumer's accepted policies, then drives Contract Negotiation through the [EDC Connector Adapter](../../../resource-sharing/resource-sharing-runtime/edc-connector-adapter/doc/architecture.md) into the local [Connector](../../../resource-sharing/resource-sharing-runtime/connector/doc/architecture.md).
- **Transfer Process kick-off endpoint** — once a contract is finalised, initiates the Transfer Process (Consumer Pull or Provider Push, per DSP).
- **Status / monitoring endpoints** — paginated query over in-flight and historical negotiations and transfers.

### Key integrations

- [Catalogue Client Application](../catalogue-client-application/doc/architecture.md) — sole upstream UI consumer.
- [EDC Connector Adapter](../../../resource-sharing/resource-sharing-runtime/edc-connector-adapter/doc/architecture.md) — the abstraction this service uses to drive the Connector. All actual EDC interaction routes through the adapter.
- [Connector](../../../resource-sharing/resource-sharing-runtime/connector/doc/architecture.md) — the eventual target of every negotiation and transfer call.
- [Authorisation](../../../../../security/access-control-and-trust/authorisation/authorisation/doc/architecture.md) — exposed through the Tier-1 Gateway; only authorised frontend clients or services can initiate or query operations.
- **Apache Kafka** — used for asynchronous coordination with the Connector and for status updates.

## Technical view

- **Source repo**: `data1/contract-consumption-be`.
- **Language / runtime**: Java 21+, Maven 3.9+, Spring Boot.
- **Persistence**: PostgreSQL.
- **Messaging**: Apache Kafka for event-driven status updates.
- **Inter-service comms**: Tier-1 Gateway from the UI; Vault for secrets; in-cluster service-to-service for the EDC Connector Adapter.
- **Deployment**: Consumer Agent only (the Provider side does not run this — providers register offerings via SD-Tooling, consumers buy them via this).

## Security view

- **No public ingress** — exposed only through the Tier-1 Gateway, which authenticates and applies RBAC before requests reach this service.
- **Per-request authorisation** — every negotiation initiation is bound to the consuming identity's Tier-1 token; that identity flows down into the Connector's policy evaluation.
- **Process tracking and auditability** — full lifecycle visibility under SIMPL governance; every negotiation and transfer is logged with the originating identity.
- **Secure access control** — only authorised frontend clients or services may initiate or query contractual operations.

Threat model: not yet documented.

Secrets management: HashiCorp Vault for any DB and Kafka credentials.

## Testing

Strategy: Spring Boot integration tests against an embedded Postgres and an in-process Kafka; contract tests against the [EDC Connector Adapter](../../../resource-sharing/resource-sharing-runtime/edc-connector-adapter/doc/architecture.md). CI/CD runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
