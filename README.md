# Simpl-Open Documentation Catalogue

Architecture documentation for the Simpl-Open data space platform, structured as a navigable capability map. Each solution folder contains a six-view architecture document, installation guides, API references, and a licence file.

This is a **documentation** repository. Source code lives in the Simpl-Open development namespace on code.europa.eu.

---

## Capability map

### [Administration](administration/README.md)

- [Notification and messaging](administration/notification-and-messaging/README.md)
  - [Notification](administration/notification-and-messaging/notification/README.md) — [Notification Service](administration/notification-and-messaging/notification/notification-service/README.md)
- [Observability](administration/observability/README.md)
  - [Dashboarding](administration/observability/dashboarding/README.md) — [Monitoring Service](administration/observability/dashboarding/monitoring-service/README.md)

### [Data](data/README.md)

- [Semantics and vocabulary](data/semantics-and-vocabulary/README.md)
  - [Schema management](data/semantics-and-vocabulary/schema-management/README.md) — [Schema Management Service](data/semantics-and-vocabulary/schema-management/schema-management-service/README.md), [Schema Synch Service](data/semantics-and-vocabulary/schema-management/schema-synch-service/README.md)
  - [Vocabulary hub](data/semantics-and-vocabulary/vocabulary-hub/README.md) — [Vocabulary Management](data/semantics-and-vocabulary/vocabulary-hub/vocabulary-management/README.md)
- [Supporting data services](data/supporting-data-services/README.md)
  - [Data orchestration](data/supporting-data-services/data-orchestration/README.md) — [Orchestration Platform](data/supporting-data-services/data-orchestration/orchestration-platform/README.md)

### [Governance](governance/README.md)

- [Contract management](governance/contract-management/README.md)
  - [Contract establishment](governance/contract-management/contract-establishment/README.md) — [Contract Manager](governance/contract-management/contract-establishment/contract-manager/README.md), [Contract Template Datastore](governance/contract-management/contract-establishment/contract-template-datastore/README.md)
- [Participant management](governance/participant-management/README.md)
  - [Onboarding](governance/participant-management/onboarding/README.md) — [Onboarding](governance/participant-management/onboarding/onboarding/README.md)
  - [User roles](governance/participant-management/user-roles/README.md) — [Users & Roles](governance/participant-management/user-roles/users-roles/README.md)
- [Policy management](governance/policy-management/README.md)
  - [Policy administration point](governance/policy-management/policy-administration-point/README.md) — [Policy Template Datastore](governance/policy-management/policy-administration-point/policy-template-datastore/README.md)
- [Resource management](governance/resource-management/README.md)
  - [Metadata description](governance/resource-management/metadata-description/README.md) — [SD Tooling](governance/resource-management/metadata-description/sd-tooling/README.md)

### [Infrastructure](infrastructure/README.md)

- [Provisioning](infrastructure/provisioning/README.md)
  - [Infrastructure provisioning](infrastructure/provisioning/infrastructure-provisioning/README.md) — [Infrastructure Provisioner](infrastructure/provisioning/infrastructure-provisioning/infrastructure-provisioner/README.md)

### [Integration](integration/README.md)

- [Resource discovery](integration/resource-discovery/README.md)
  - [Resource catalogue](integration/resource-discovery/resource-catalogue/README.md) — [Simpl Catalogue](integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md)
  - [Search engine](integration/resource-discovery/search-engine/README.md) — [Catalogue Client Application](integration/resource-discovery/search-engine/catalogue-client-application/README.md)
- [Resource sharing](integration/resource-sharing/README.md)
  - [Resource sharing runtime](integration/resource-sharing/resource-sharing-runtime/README.md) — [Connector](integration/resource-sharing/resource-sharing-runtime/connector/README.md)

### [Security](security/README.md)

- [Access control and trust](security/access-control-and-trust/README.md)
  - [Authentication provider federation](security/access-control-and-trust/authentication-provider-federation/README.md) — [Tier 1 Authentication Provider](security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md), [Tier 2 Authentication Provider](security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md)
  - [Authorisation](security/access-control-and-trust/authorisation/README.md) — [Authorisation](security/access-control-and-trust/authorisation/authorisation/README.md)
  - [Identity provider](security/access-control-and-trust/identity-provider/README.md) — [Identity Provider](security/access-control-and-trust/identity-provider/identity-provider/README.md)
  - [Security attribute provider federation](security/access-control-and-trust/security-attribute-provider-federation/README.md) — [Security Attributes Provider](security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md)
- [Credential management](security/credential-management/README.md)
  - [Signing](security/credential-management/signing/README.md) — [Signer Service](security/credential-management/signing/signer-service/README.md)
  - [VC issuance and verification](security/credential-management/vc-issuance-verification/README.md) — [VC Issuer](security/credential-management/vc-issuance-verification/vc-issuer/README.md)
  - [Wallet](security/credential-management/wallet/README.md) — [Wallet](security/credential-management/wallet/wallet/README.md)

---

## Top-level documents

**[foundations/](foundations/README.md) — canonical entry point for understanding what Simpl is and should do** (capability map, business processes, non-functional requirements), separate from the implementation tree below.

- [foundations/capability-map.md](foundations/capability-map.md) — Level 1 and Level 2 capability map with narrative, deployment model, and Release 3.0 scope
- [foundations/business-processes/](foundations/business-processes/README.md) — business process catalogue: 13 BPs and 4 scenario architectures
- [foundations/non-functional-requirements/](foundations/non-functional-requirements/README.md) — non-functional requirements catalogue: 15 NFRs with measurable thresholds

---

- [definition-of-done.md](definition-of-done.md) — definition of done for solution documentation
- [references.md](references.md) — all external links
- [interoperability/README.md](interoperability/README.md) — technical and semantic interoperability index
- [api-catalogue/README.md](api-catalogue/README.md) — all APIs grouped by service
- [testing/README.md](testing/README.md) — aggregate testing status

## Source and provenance

Architecture content is extracted from `functional-and-technical-architecture-specifications.md`. Per-solution provenance is noted in each solution's README and `doc/architecture.md`.
