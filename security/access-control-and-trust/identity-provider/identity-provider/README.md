<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access Control And Trust</a><br/>
            <a href="../README.md">Service: Identity Provider</a><br/>
                <strong>Solution: Identity Provider</strong><br/>
</p>
</div>

# Identity Provider

Deployed inside the Governance Authority Agent. Generates and renews Tier 2 x.509 credentials for newly onboarded participants; manages the full credential lifecycle (issue, suspend, revoke, renew, edit identity attributes).

Capability-map placement: `security / access-control-and-trust / identity-provider / identity-provider`. This solution implements the **Identity provider** business service.

Provenance: built by Simpl. Source repositories: `iaa/identity-provider` (backend) and `iaa/fe-identity-provider` (frontend). Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP03A Onboarding of a new data space Participant](../../../../foundations/business-processes/BP03A-onboarding-participant-providers/dynamic-view.md)
- [SA03 Credentials actions by the Governance Authority](../../../../foundations/business-processes/SA03-credentials-actions-governance-authority/dynamic-view.md)

## Source code

- Backend: `code.europa.eu/simpl/simpl-open/development/iaa/identity-provider`
- Frontend: `code.europa.eu/simpl/simpl-open/development/iaa/fe-identity-provider`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
