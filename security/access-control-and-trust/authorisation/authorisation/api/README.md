# Authorisation — API index

The Authorisation component exposes two Spring Cloud Gateway-based APIs, one per trust tier.

| API | File | Description |
|-----|------|-------------|
| Tier 1 Gateway API | [tier1-gateway.openapi.yaml](tier1-gateway.openapi.yaml) | RBAC gateway for human user (Tier 1) inbound traffic |
| Tier 2 Gateway API | [tier2-gateway.openapi.yaml](tier2-gateway.openapi.yaml) | ABAC gateway for agent-to-agent (Tier 2) inbound traffic |

Both APIs are routing/proxy interfaces: they accept requests, validate credentials/tokens, enforce policy rules, and forward to downstream Simpl-Open services. The downstream service APIs are documented in the respective solution `doc/api.md` files.

Status: OpenAPI specifications not yet available in this documentation catalogue — see source repositories for runtime API documentation.
