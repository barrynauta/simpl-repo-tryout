<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Governance</a><br/>
        <a href="../../README.md">Capability: Participant management</a><br/>
            <a href="../README.md">Service: Onboarding</a><br/>
                <strong>Solution: fe-onboarding</strong><br/>
</p>
</div>

# fe-onboarding

Frontend (Angular) for the **Onboarding** business service. UI used by applicants to submit onboarding requests and by the Governance Authority to review, approve, or reject them.

> **Scope note.** This folder represents the frontend solution. Most documentation under `doc/` and `api/` was originally bundled with the backend repository (`iaa/onboarding`) and is preserved here for reference until a dedicated backend solution folder is added — see [Source code](#source-code) below for the upstream backend repository.

## Underlying business process

Core Governance Authority workflow: applicants (providers and consumers) request new Tier 1 credentials, submit their onboarding request with required documents, and the Governance Authority approves, requests revision, or rejects. On approval, the backend triggers Tier 2 credential creation via the Identity Provider.

Capability-map placement: `governance / participant-management / onboarding / fe-onboarding`. This solution implements the frontend half of the **Onboarding** business service.

Provenance: built by Simpl. Source repository (this folder, frontend): `iaa/fe-onboarding`. Backend lives upstream at `iaa/onboarding` (Java 21 / Maven 3.9+) — no dedicated catalogue folder yet. Licence: EUPL 1.2.

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


## API

[`api/`](api/README.md) — 3 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).


## Documentation (imported from source)

[`doc/`](doc/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `frontend/` (4 files), `iaa-2.11.x/` (6 files), `installation-guide/` (2 files), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source code

- Frontend (this folder): <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-onboarding>
- Backend (upstream — no dedicated catalogue folder yet): `code.europa.eu/simpl/simpl-open/development/iaa/onboarding`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
