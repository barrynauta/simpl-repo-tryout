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

Spring Cloud Gateway-based API gateway that processes all Tier 1 and Tier 2 inbound traffic originating from external sources. Enforces RBAC (Tier 1) and ABAC (Tier 2) rules. Covers both inbound paths; relies on the Tier 1 Authentication Provider for role retrieval.

Capability-map placement: `security / access-control-and-trust / authorisation / authorisation`. This solution implements the **Authorisation** business service.

Provenance: built by Simpl. Source repositories: `iaa/tier1-gateway`, `iaa/tier2-gateway`, and `iaa/tier2-proxy` are treated as one logical component per the architecture spec. Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [api/README.md](api/README.md) — API index (two gateway APIs).
- [api/tier1-gateway.openapi.yaml](api/tier1-gateway.openapi.yaml) — Tier 1 gateway OpenAPI specification (stub).
- [api/tier2-gateway.openapi.yaml](api/tier2-gateway.openapi.yaml) — Tier 2 gateway OpenAPI specification (stub).
- [LICENSE](LICENSE) — EUPL 1.2.

## Source code

- Tier 1 gateway: `code.europa.eu/simpl/simpl-open/development/iaa/tier1-gateway`
- Tier 2 gateway: `code.europa.eu/simpl/simpl-open/development/iaa/tier2-gateway`
- Tier 2 proxy: `code.europa.eu/simpl/simpl-open/development/iaa/tier2-proxy`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
