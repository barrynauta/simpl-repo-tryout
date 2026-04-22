# Authentication provider federation

Tier 1 and Tier 2 authentication providers for Simpl-Open participant agents. Tier 1 authenticates end-users within a participant's agent (Keycloak + extensions). Tier 2 authenticates participant agents to each other via mTLS with X.509 credentials.

## Solutions

- [Tier 1 Authentication Provider](tier-1-authentication-provider/README.md) — Keycloak-based OIDC identity provider with Simpl-Open custom authenticator plugin.
- [Tier 2 Authentication Provider](tier-2-authentication-provider/README.md) — X.509 mTLS credential holder and validator for agent-to-agent communication.
