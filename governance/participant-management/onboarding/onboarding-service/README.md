<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Governance</a><br/>
        <a href="../../README.md">Capability: Participant Management</a><br/>
            <a href="../README.md">Service: Onboarding</a><br/>
                <strong>Solution: Onboarding</strong><br/>
</p>
</div>

# Onboarding

Core Governance Authority component that manages participant onboarding requests. Applicants (providers and consumers) request new Tier 1 credentials, submit their onboarding request with required documents, and the Governance Authority approves, requests revision, or rejects. On approval, the Onboarding component triggers Tier 2 credential creation via the Identity Provider.

Capability-map placement: `governance / participant-management / onboarding / onboarding-service`. This solution implements the **Onboarding** business service.

Provenance: built by Simpl. Source repositories: `iaa/onboarding` (backend, Java 21 / Maven 3.9+) and `iaa/fe-onboarding` (frontend). Licence: EUPL 1.2.

## Key features

- **Onboard new dataspace participants**: applicant fills an onboarding template; the participant's onboarding manager generates a key pair and requests a Certificate Signing Request (CSR) from the Governance Authority; the applicant attaches the CSR to the form and submits.
- **Approve / reject onboarding requests**: the Governance Authority reviews the request and decides — approval, revision, or rejection. On approval the GA acts as Certification Authority, signs the certificate, and the agent installs it.
- **Logging and auditing**: every onboarding action is logged for audit purposes.
- **Notifications**: status-change emails to applicants, agents, and stakeholders (submitted, approved, rejected, ready).
- Backed by Postgres for state, Helm 3.19 for deployment.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP03A Onboarding of a new data space Participant](../../../../foundations/business-processes/BP03A-onboarding-participant-providers/dynamic-view.md)

## Source code

- Backend: `code.europa.eu/simpl/simpl-open/development/iaa/onboarding`
- Frontend: `code.europa.eu/simpl/simpl-open/development/iaa/fe-onboarding`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
