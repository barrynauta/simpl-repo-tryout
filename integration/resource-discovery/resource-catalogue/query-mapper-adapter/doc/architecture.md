Source: source repo `gaia-x-edc/poc-gaia-edc/README.md`. FTA spec, §4.3.1 (Catalogue Service — Query Mapper Adapter), §6.1.2 (Spring Cloud Gateway implementation).

# Query Mapper Adapter — architecture

## Business view

Backend that **maps queries from the Gaia-X EDC** ecosystem (and, in Simpl, from the Catalogue Client Application) into the Simpl-Open Federated Catalogue's native query language. Acts as a bridge between EDC-side discovery requests and the GAIA-X Federated Catalogue's API, **registering service offerings on the federated catalogue** for downstream search.

The Query Mapper Adapter also hosts the **Policy Filter Service** — every query that flows through it is rewritten so that results respect the access-control rules embedded in each self-description.

Capability-map placement: Integration dimension → Resource discovery capability → Resource catalogue business service.

**Business processes supported:**
- [BP06 Consumer searches resources](../../../../../foundations/business-processes/BP06-consumer-searches-resources/README.md) — every search query from the Catalogue Client Application transits this adapter.
- [BP05B Provider manages resource descriptions](../../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/README.md) — service-offering registration on the catalogue.

## Data view

This component holds **no first-party persistent data**. Inputs:

- **User-defined search parameters** from the Catalogue Client Application (free-text or schema-driven advanced-search field bindings).
- **Identity context** from the Tier 1 Gateway (the requesting user's policies, used by the Policy Filter Service).

Outputs:

- **Native catalogue queries** sent to the [Simpl Catalogue](../simpl-catalogue/doc/architecture.md), with policy-based filters merged in.
- **Service-offering registration** calls into the federated catalogue when a provider publishes a new self-description.

## Application view

### Internal decomposition

- **Query translation engine** — converts user-defined parameters into the Catalogue's native query language.
- **Policy Filter Service** — embedded; rewrites every query before forwarding so that the response only contains items the requesting identity is authorised to see.
- **Service-offering registration client** — calls into the [Simpl Catalogue](../simpl-catalogue/doc/architecture.md)'s Federated Catalogue API to register newly-published self-descriptions for searchability.

### Key integrations

- [Simpl Catalogue](../simpl-catalogue/doc/architecture.md) — the registration and query target. Sits behind this adapter in every read flow.
- [Catalogue Client Application](../../search-engine/catalogue-client-application/doc/architecture.md) — typical upstream caller; routes user-driven queries through this adapter.
- [Authorisation](../../../../../security/access-control-and-trust/authorisation/authorisation/doc/architecture.md) — the Tier 1 Gateway terminates the user session; this adapter consumes the resolved identity context to drive policy filtering.

## Technical view

- **Source repo**: `gaia-x-edc/poc-gaia-edc` (per FTA §6.1.2 the Query Mapper Adapter is implemented as **Spring Cloud Gateway**; the source-repo README confirms the Spring Boot stack with **Java 21+, Maven 3.6+**).
- **Framework**: Spring Cloud Gateway — chosen specifically for its built-in route-rewriting and filter chain, which is a natural fit for the Policy Filter Service.
- **Deployment**: standalone Spring Boot service deployable on Provider/Consumer agents that need EDC ↔ FC bridging.

### Dependencies

- **Federated Catalogue** — `gaia-x-edc/simpl-fc-service` (the [Simpl Catalogue](../simpl-catalogue/doc/architecture.md)). Service-offering registration target.

## Security view

- **Policy Filter Service** is the load-bearing security mechanism — by embedding policy filters into queries before they hit the Catalogue, the adapter ensures that no user can ever observe a self-description they aren't authorised to see, even by abusing query parameters.
- **No public ingress** — the adapter only accepts requests from the Tier 1 Gateway's resolved identity context; direct external requests are not honoured.
- **Service-offering registration** uses the agent's machine credentials against the Catalogue API.

Threat model: not yet documented.

Secrets management: catalogue API credentials sourced from the agent's Vault.

## Testing

Strategy: integration tests against a stub catalogue API (the Spring Cloud Gateway route table is the unit under test). CI/CD runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
