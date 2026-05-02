<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access Control And Trust</a><br/>
            <a href="../README.md">Service: Security Attribute Provider Federation</a><br/>
                <strong>Solution: Security Attributes Provider</strong><br/>
</p>
</div>

# Security Attributes Provider

Source of truth for **identity attributes** in the data space — roles, permissions, and security metadata used for access control and participant classification. Deployed in the Governance Authority Agent. Invoked by [Onboarding](../../../../governance/participant-management/onboarding/fe-onboarding/README.md) on participant approval to associate the right attributes with the participant; consumed by other IAA components to drive ABAC enforcement across agents.

Capability-map placement: `security / access-control-and-trust / security-attribute-provider-federation / security-attributes-provider`. This solution implements the **Security attribute provider federation** business service.

Provenance: built by Simpl. Source repositories: `iaa/security-attributes-provider` (backend, Java 21 / Maven 3.9+) and `iaa/fe-security-attribute-provider` (frontend). Licence: EUPL 1.2.

Note on naming: the capability in the capmap uses the singular `security-attribute-provider-federation`; the architecture spec and this solution folder use the plural "Security Attributes Provider" (flag d-1 in step 3 checkpoint).

## Key features

- **Manage dataspace-level identity attributes** — roles, permissions, security metadata.
- **Provide identity attributes** to other IAA components (Tier 2 Authentication Provider, Authorisation gateways) for access-control decisions.
- **Participant classification** based on assigned identity attributes.
- Authoritative, consistent identity-attribute data across the Simpl ecosystem.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP03A Onboarding of a new data space Participant](../../../../foundations/business-processes/BP03A-onboarding-participant-providers/dynamic-view.md)
- [SA03 Credentials actions by the Governance Authority](../../../../foundations/business-processes/SA03-credentials-actions-governance-authority/dynamic-view.md)


## API

[`api/`](api/README.md) — 3 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `frontend/` (4 files), `iaa-2.11.x/` (2 files), `installation-guide/` (2 files), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source code

- Backend: `code.europa.eu/simpl/simpl-open/development/iaa/security-attributes-provider`
- Frontend: `code.europa.eu/simpl/simpl-open/development/iaa/fe-security-attribute-provider`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
