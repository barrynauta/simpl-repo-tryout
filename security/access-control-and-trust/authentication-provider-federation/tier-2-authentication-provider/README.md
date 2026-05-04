<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access control and trust</a><br/>
            <a href="../README.md">Service: Authentication provider federation</a><br/>
                <strong>Solution: Tier 2 Authentication Provider</strong><br/>
</p>
</div>

# Tier 2 Authentication Provider

Per-agent **deployment composition** that brings up the [authentication-provider](../authentication-provider/README.md) backend on a Simpl-Open agent so that agent can perform Tier 2 (mTLS / X.509 + ephemeral-proof) authentication on incoming traffic and enrich its requests with dataspace identity attributes.

This folder represents the **Tier 2 enforcement layer** of the Authentication Provider Federation capability — i.e. *how* the central authentication backend ships and runs inside each Consumer / Provider / Authority / Participant agent. Together with [tier-1-authentication-provider](../tier-1-authentication-provider/README.md) (Keycloak edge SSO) it implements the **Authentication provider federation** business service.

> **Upstream cross-reference.** The same Helm umbrella is also catalogued at [`cross-cutting/agents/agent-iaa/provider-iaa/`](../../../../cross-cutting/agents/agent-iaa/provider-iaa/README.md), where it's framed as the *agent-IAA bundle for provider agents*. Same code, two capability-map placements — security view here, agent-deployment view there.

## What's deployed

- The [authentication-provider](../authentication-provider/README.md) backend microservice — see its README for the actual functionality (X.509 keypair lifecycle, ephemeral-proof validation, dataspace-attribute caching, internal APIs to other on-agent components).
- A local cache of identity attributes refreshed against the Governance Authority's [Security Attributes Provider](../../security-attribute-provider-federation/security-attributes-provider/README.md).
- Helm 3.19+ chart that wires the backend into a single agent.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document for the Tier 2 deployment.
- [LICENSE](LICENSE) — EUPL 1.2.

## API

[`api/`](api/README.md) — 4 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).

## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `frontend/` (4 files), `installation-guide/` (2 files), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source

- **Deployment composition (this folder):** <https://code.europa.eu/simpl/simpl-open/development/iaa/agent-iaa/provider-iaa>
- **Backend code (deployed by this composition):** see [authentication-provider](../authentication-provider/README.md) → <https://code.europa.eu/simpl/simpl-open/development/iaa/authentication-provider>
- **Frontend (administrative UI):** see [fe-authentication-provider](../fe-authentication-provider/README.md) → <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-authentication-provider>
