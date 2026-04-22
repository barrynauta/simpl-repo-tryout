# Access control and trust

Two-tier identity, authentication, and authorisation (IAA) for Simpl-Open. Tier 1 covers participant-internal user access (RBAC via Keycloak + Spring Cloud Gateway). Tier 2 covers cross-participant agent-to-agent communication (ABAC via mTLS, X.509 credentials, and ephemeral proofs).

## Business services

- [Authentication provider federation](authentication-provider-federation/README.md) — Tier 1 (Keycloak) and Tier 2 (X.509 mTLS) authentication providers.
- [Authorisation](authorisation/README.md) — Tier 1 (RBAC) and Tier 2 (ABAC) API gateway enforcement via Spring Cloud Gateway.
- [Identity provider](identity-provider/README.md) — Governance Authority–managed identity federation and Tier 2 credential issuance.
- [Security attribute provider federation](security-attribute-provider-federation/README.md) — management and assignment of identity attributes used for ABAC policy enforcement.
