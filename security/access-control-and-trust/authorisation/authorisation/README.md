<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access Control And Trust</a><br/>
            <a href="../README.md">Service: Authorisation</a><br/>
                <strong>Solution: Authorisation</strong><br/>
</p>
</div>

# Authorisation

Spring Cloud Gateway-based API gateway pair that processes all inbound traffic to a Simpl-Open Agent. The **Tier 1 Gateway** handles end-user / browser traffic from the Internet (Keycloak / Onboarding / Users-Roles); the **Tier 2 Gateway** handles agent-to-agent traffic over **mTLS only**. Enforces RBAC at Tier 1 and ABAC at Tier 2.

Capability-map placement: `security / access-control-and-trust / authorisation / authorisation`. This solution implements the **Authorisation** business service.

Provenance: built by Simpl. Source repositories — Java 21 / Maven 3.9+, all three pieces:

- **Tier 1 Gateway** (`iaa/tier1-gateway`) — mediates Internet → Tier 1 components (Keycloak, Onboarding, Users-Roles); handles authn/authz between agents and participants; enforces access policies based on identity attributes and governance rules; supports interoperability with other European data spaces.
- **Tier 2 Gateway** (`iaa/tier2-gateway`) — gateway for inbound Tier 2 API operations between agents; **HTTPS + mTLS only**.
- **Tier 2 Proxy** (`iaa/tier2-proxy`) — companion proxy mediating outbound Tier 2 calls.

Per the architecture spec these three repos are treated as one logical component. Licence: EUPL 1.2.

## Key features

- **RBAC at Tier 1** — role retrieval via the Tier 1 Authentication Provider (Keycloak).
- **ABAC at Tier 2** — attribute resolution via the [Security Attributes Provider](../../security-attribute-provider-federation/security-attributes-provider/README.md), enforced inline on each Tier 2 request.
- **mTLS termination** at Tier 2 — every agent-to-agent call presents an x.509 client cert that the gateway validates.
- **Policy enforcement** based on identity attributes and dataspace governance rules.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [api/README.md](api/README.md) — API index (two gateway APIs).
- [api/tier1-gateway.openapi.yaml](api/tier1-gateway.openapi.yaml) — Tier 1 gateway OpenAPI specification (stub).
- [api/tier2-gateway.openapi.yaml](api/tier2-gateway.openapi.yaml) — Tier 2 gateway OpenAPI specification (stub).
- [LICENSE](LICENSE) — EUPL 1.2.

## Source code

- Tier 1 gateway: <https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-gateway>
- Tier 2 gateway: <https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-gateway>
- Tier 2 proxy: <https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-proxy>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
