Source: functional-and-technical-architecture-specifications.md, sections 2.7.6 (Security dimension — Access control & trust), 4.2.1 (ACV Static — Authorisation Service), 6.1.1 (TCV Static — Authorisation Service).

# Authorisation — architecture

## Business view

The Authorisation component processes all Tier 1 and Tier 2 inbound traffic originating from external sources and enforces RBAC and ABAC rules.

- **Tier 1 (RBAC)**: governs human user access to Simpl-Open services. JWT tokens issued by the Tier 1 Authentication Provider (Keycloak) carry role claims used to enforce RBAC at the Tier 1 gateway.
- **Tier 2 (ABAC)**: governs agent-to-agent communication. Tier 2 credentials (x.509 certificates) and identity attributes are used to enforce ABAC at the Tier 2 gateway.

All inbound requests to any Simpl-Open service pass through the Authorisation layer. It is implemented as a Spring Cloud Gateway-based API gateway.

Capability-map placement: Security dimension → Access control and trust capability → Authorisation business service.

![ACV Static view — Authorisation Service. Shows the Tier 1 and Tier 2 authorisation components and their interfaces](./media/image25.jpeg)

## Data view

The Authorisation component does not own a persistent data store. It reads identity and attribute data at request time from:

- **Tier 1 Authentication Provider** (Keycloak) — JWT token validation and role retrieval for RBAC decisions.
- **Security Attributes Provider** — identity attribute retrieval for ABAC decisions in Tier 2 flows.
- **Tier 2 Authentication Provider** — Tier 2 credential (x.509) validation.

## Application view

### Internal decomposition

- **Authorisation Tier 1 RBAC** — Spring Cloud Gateway instance; validates JWT tokens issued by Keycloak, extracts role claims, and applies RBAC routing rules to forward or reject inbound Tier 1 requests.
- **Authorisation Tier 2 ABAC** — Spring Cloud Gateway instance; validates Tier 2 credentials (Ephemeral Proof and Security Credentials) and applies ABAC rules based on identity attributes for agent-to-agent requests.

The architecture spec (§4.3.1, step 5 sample notes) identifies the **Query Mapper Adapter** and **Policy Filter Service** as sub-components of the Catalogue that sit alongside the Tier 1 Gateway in the request path. These are documented in the Simpl Catalogue architecture document, not here, since the ACV Static view places them under the Catalogue Service component.

### Key integrations

- [Tier 1 Authentication Provider](../../../authentication-provider-federation/tier-1-authentication-provider/doc/architecture.md) — JWT token validation and role retrieval for Tier 1 RBAC.
- [Tier 2 Authentication Provider](../../../authentication-provider-federation/tier-2-authentication-provider/doc/architecture.md) — Tier 2 credential validation for agent-to-agent ABAC.
- [Security Attributes Provider](../../../security-attribute-provider-federation/security-attributes-provider/doc/architecture.md) — identity attribute retrieval for ABAC enforcement.

All Simpl-Open service components are downstream of the Authorisation layer — see individual solution architecture documents for how each component is accessed via the gateway.

## Technical view

- **Authorisation Tier 1 RBAC** is implemented with Spring Cloud Gateway.
- **Authorisation Tier 2 ABAC** is implemented with Spring Cloud Gateway.

The two gateways are implemented as separate deployable units corresponding to the two trust tiers, even though both use Spring Cloud Gateway as the underlying technology.

Deployment: deployed in both the Governance Authority Agent and Participant Agents. Each agent has its own Authorisation instance. The Tier 1 Gateway is the entry point for human user traffic; the Tier 2 Gateway handles agent-to-agent communication.

![TCV Static view — Authorisation Service](./media/image118.jpeg)

## Security view

The Authorisation component is the security perimeter of each Simpl-Open agent:

- No request reaches any downstream Simpl-Open service without passing through the Authorisation gateway.
- **Tier 1 RBAC**: JWT validation, token expiry checks, and role-based routing rules.
- **Tier 2 ABAC**: x.509 certificate validation (Ephemeral Proof), identity attribute evaluation, and attribute-based routing rules.
- The gateway is implemented with Spring Cloud Gateway, which allows extensible filter chains for security rule application.

Threat model: Status: not yet documented.

Secrets management: Status: not yet documented.

## Testing

Strategy: Status: not yet documented.

PSO validation status: Status: not yet documented.

Requirements traceability: Status: not yet documented.

## API

Two gateway APIs — see [api/README.md](../api/README.md) for an index.
