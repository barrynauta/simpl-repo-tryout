<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access control and trust</a><br/>
            <a href="../README.md">Service: Authentication provider federation</a><br/>
                <strong>Solution: authentication-provider</strong><br/>
</p>
</div>

# authentication-provider

Central authentication backend microservice for the SIMPL/IAA ecosystem. Manages X.509 credential lifecycle, validates Tier 2 ephemeral-proof challenges, caches dataspace identity attributes and participant organisation metadata, and exposes internal APIs that other Simpl components on the same agent use to resolve authentication state without round-tripping to the Governance Authority on every call.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Role in the architecture

This is the **source-code repository** for the authentication-provider service. It is deployed per agent (one instance per Consumer / Provider / Authority / Participant agent) via the agent-IAA Helm bundles under [cross-cutting/agents/agent-iaa/](../../../../cross-cutting/agents/agent-iaa/README.md).

| Layer | Catalogue placement | Source upstream |
|---|---|---|
| **Tier 1** — edge SSO (Keycloak) | [tier-1-authentication-provider](../tier-1-authentication-provider/README.md) | `iaa/keycloak-authenticator` |
| **Tier 2** — per-agent deployment of this service | [tier-2-authentication-provider](../tier-2-authentication-provider/README.md) | `iaa/agent-iaa/{provider,consumer,authority,participant}-iaa` (Helm umbrellas) |
| **Frontend** — administrative UI | [fe-authentication-provider](../fe-authentication-provider/README.md) | `iaa/fe-authentication-provider` |
| **This solution** — central backend source | (this folder) | `iaa/authentication-provider` |

## Tech stack

- Java 21
- Maven 3.9+
- Helm 3.19+ (deployment via the agent-IAA umbrella charts)
- Docker (multi-stage build via provided Dockerfile)

## Source

- <https://code.europa.eu/simpl/simpl-open/development/iaa/authentication-provider>
