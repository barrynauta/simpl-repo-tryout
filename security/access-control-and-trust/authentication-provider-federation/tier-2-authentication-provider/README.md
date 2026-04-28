<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access Control And Trust</a><br/>
            <a href="../README.md">Service: Authentication Provider Federation</a><br/>
                <strong>Solution: Tier 2 Authentication Provider</strong><br/>
</p>
</div>

# Tier 2 Authentication Provider

Centralises **Tier 2 authentication** for a Simpl-Open Agent. Manages Tier 2 security credentials (**x.509 keypairs**), validates Tier 2 credentials (ephemeral proof + security credentials) on agent-to-agent traffic, and keeps a local copy of the dataspace identity attributes and participant organisation details so other Simpl components can resolve them without round-tripping to the Governance Authority on every call.

Capability-map placement: `security / access-control-and-trust / authentication-provider-federation / tier-2-authentication-provider`. This solution and `tier-1-authentication-provider` together implement the **Authentication provider federation** business service (flag d-2 in step 3 checkpoint).

Provenance: built by Simpl. Source repositories: `iaa/authentication_provider` (backend, Java 21 / Maven 3.9+) and `iaa/fe-authentication-provider` (frontend). Licence: EUPL 1.2.

## Key features

- **Manages x.509 keypair lifecycle** for the local agent (issuance, rotation, revocation).
- **Validates incoming Tier 2 credentials** in agent-to-agent communication — ephemeral-proof challenge plus the security credential carried in the request.
- **Local cache** of dataspace identity attributes and participant organisation metadata, refreshed against the Governance Authority's [Security Attributes Provider](../../security-attribute-provider-federation/security-attributes-provider/README.md).
- **Internal APIs** exposed to other Simpl components on the same agent so they can fetch participant info and attribute data.
- Helm 3.19 deployment.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.


## API

[`api/`](api/README.md) — 4 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).

## Source code

- Backend: <https://code.europa.eu/simpl/simpl-open/development/iaa/authentication_provider>
- Frontend: <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-authentication-provider>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
