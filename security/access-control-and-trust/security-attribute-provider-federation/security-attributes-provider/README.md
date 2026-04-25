# Security Attributes Provider

Deployed in the Governance Authority Agent. Registers and manages participant security identity attributes; invoked by Onboarding on participant approval to associate security identity attributes to the participant; supports ABAC enforcement across agents.

Capability-map placement: `security / access-control-and-trust / security-attribute-provider-federation / security-attributes-provider`. This solution implements the **Security attribute provider federation** business service.

Provenance: built by Simpl. Source repositories: `iaa/security-attributes-provider` (backend) and `iaa/fe-security-attribute-provider` (frontend). Licence: EUPL 1.2.

Note on naming: the capability in the capmap uses the singular `security-attribute-provider-federation`; the architecture spec and this solution folder use the plural "Security Attributes Provider" (flag d-1 in step 3 checkpoint).

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP03A Onboarding of a new data space Participant](../../../../foundations/business-processes/BP03A-onboarding-participant-providers/dynamic-view.md)
- [SA03 Credentials actions by the Governance Authority](../../../../foundations/business-processes/SA03-credentials-actions-governance-authority/dynamic-view.md)

## Source code

- Backend: `code.europa.eu/simpl/simpl-open/development/iaa/security-attributes-provider`
- Frontend: `code.europa.eu/simpl/simpl-open/development/iaa/fe-security-attribute-provider`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
