<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a> &nbsp;»&nbsp;
<a href="README.md">Foundations</a> &nbsp;»&nbsp;
<strong>Interoperability</strong>
</p>
</div>

# Interoperability

Simpl-Open is built to make European data spaces interoperable — both **inside** a single data space (Provider ↔ Consumer ↔ Governance Authority) and **across** federated data spaces. This page maps every standard, vocabulary, protocol, and governance pattern Simpl-Open uses, organised by the four layers of the **[European Interoperability Framework (EIF)](https://ec.europa.eu/isa2/eif_en/)**.

The four EIF layers, applied to Simpl-Open:

| Layer | Question it answers | Simpl-Open's relationship |
|---|---|---|
| **Legal** | What rules govern who may participate and what they may do? | Licensing of Simpl-Open code; alignment with EU regulations (GDPR, Data Act, eIDAS, etc.) |
| **Organisational** | Who is responsible for what, and how do organisations align processes? | Governance Authority model, role taxonomy, onboarding processes, federation patterns |
| **Semantic** | Do parties mean the same thing when they exchange information? | Shared vocabularies and ontologies (Gaia-X, ODRL, DCAT, SKOS, custom SIMPL namespace) |
| **Technical** | Can systems physically exchange information? | Protocols, formats, APIs, transport, identity and trust mechanisms |

Reference frameworks Simpl-Open aligns with:
- **[Data Spaces Support Centre (DSSC) Blueprint](https://dssc.eu/space/bv15e/766062287/7+Interoperability)** — the canonical European reference for data-space interoperability across all four layers.
- **[IDSA Reference Architecture Model (IDS-RAM 4)](https://docs.internationaldataspaces.org/ids-knowledgebase/ids-ram-4/)** — the architecture for trusted data exchange that the Connector implements.
- **[Gaia-X Trust Framework](https://gaia-x.eu/wp-content/uploads/2022/05/Gaia-x-Trust-Framework-22.04.pdf)** — federated trust model used for self-descriptions.
- **[European Interoperability Framework (EIF)](https://ec.europa.eu/isa2/eif_en/)** — the EU's reference framework for interoperable digital public services.

---

## 1. Legal interoperability

The legal layer covers the licences, regulations, and contractual frameworks that bind participants. Simpl-Open is designed to be deployable inside the EU regulatory perimeter; downstream data-space governance authorities are responsible for layering domain-specific compliance on top.

| Instrument | How Simpl-Open relates |
|------------|------------------------|
| **[EUPL 1.2](https://eupl.eu/)** | Default licence for Simpl-built source code (most modules under `code.europa.eu/simpl/simpl-open/development/`). |
| **Apache 2.0** | Licence inherited from upstream forks (Eclipse XFSC Federated Catalogue, Eclipse Dataspace Connector, Eclipse XFSC TSA Signer, Keycloak, Dagster, Apache Kafka). |
| **[GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)** | Drives the [Anonymisation and Pseudonymisation services](../data/data-processing/anonymisation-and-pseudonymisation/README.md). The user manuals explicitly distinguish GDPR Article 4(5) pseudonymisation (reversible, still personal data) from Recital 26 anonymisation (irreversible, out of GDPR scope). Audit trails and identity-attribute attestation support data-controller/processor obligations. |
| **[Data Governance Act (Reg. 2022/868)](https://eur-lex.europa.eu/eli/reg/2022/868/oj)** | Establishes the legal regime under which data-space intermediation services operate; Simpl-Open implements the structural pattern (data sovereignty, neutral intermediary, voluntary altruism) the DGA presumes. |
| **[Data Act (Reg. 2023/2854)](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)** | Frames the contractual access regime (B2B data-sharing terms) that Simpl's [Contract Manager](../governance/contract-management/contract-establishment/contract-manager/README.md) operationalises through ODRL-encoded contracts. |
| **[eIDAS Regulation (Reg. 910/2014, eIDAS 2.0 Reg. 2024/1183)](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)** | Underpins the digital-identity layer; Simpl integrates with eIDAS-compatible IdPs through the [Tier 1 Authentication Provider](../security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md) and the [eidas-demo-keycloak-extension](../cross-cutting/samples/eidas-demo-keycloak-extension/README.md). The European Digital Identity (EUDI) Wallet roadmap aligns with the planned [Wallet](../security/credential-management/wallet/wallet/README.md) solution. |
| **[NIS2 Directive (Dir. 2022/2555)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)** | Operational-security baseline; the [Monitoring Service](../administration/observability/dashboarding/monitoring-service/README.md) and the planned [CSIRT capability](../security/csirt/README.md) provide the technical instrumentation. |
| **EU Open Source Strategy 2020–2023** | Simpl-Open is a Commission-published open-source product; its multi-vendor, modular, EUPL-default approach implements the strategy's principles. |

---

## 2. Organisational interoperability

The organisational layer covers the **roles, processes, and governance arrangements** that align how participating organisations work together. Simpl-Open's organisational model is largely inherited from DSSC and IDSA, with concrete role and process bindings provided by the Simpl business processes.

### Governance authority model

Every Simpl data space has exactly one **Governance Authority** accountable for the legal-and-operational framework of that space. This single point of accountability is reflected in the deployment topology — the Governance Authority Agent runs `Onboarding`, `Identity Provider`, `Security Attributes Provider`, `Schema Management Service`, `Federated Catalogue`, and `Signer Service`, while Provider and Consumer agents only run their own subset. See [`cross-cutting/agents/governance-authority-agent/`](../cross-cutting/agents/governance-authority-agent/README.md).

### DSSC-aligned actor taxonomy

Per [DSSC Functional Overview](https://dssc.eu/space/BVE/357075035/Functional+Overview+of+Components):

| DSSC concept | Simpl-Open binding |
|---|---|
| **Participant Agent** | The agent compositions in [`cross-cutting/agents/`](../cross-cutting/agents/README.md): Consumer, Data Provider, Application Provider, Infrastructure Provider, Governance Authority. |
| **Shared Services** | Services deployed only on the Governance Authority Agent: Onboarding, Identity Provider, Catalogue, Schema Management. |
| **Control plane** | Implemented in the Connector's Control Plane (DSP contract negotiation) plus [Contract Manager](../governance/contract-management/contract-establishment/contract-manager/README.md), [SD Tooling](../governance/resource-management/metadata-description/sd-tooling/README.md), and the IAA stack. |
| **Data plane** | Implemented in the Connector's Data Plane via the MinIO S3 Object Storage Extension (and roadmap eDelivery extension). See [`integration/data-sharing/`](../integration/data-sharing/README.md). |

### Role taxonomy

The Simpl role table (FTA §4.5) defines the roles that govern who may do what across the data space. The Tier 1 Gateway and Tier 2 Gateway enforce these as RBAC rules; the [Authorisation](../security/access-control-and-trust/authorisation/authorisation/README.md) solution holds the runtime mapping.

| Role | Code | Operated by | Purpose |
|---|---|---|---|
| Catalogue Administrator | `Ro-MU-CA` | Governance Authority | XFSC FC catalogue lifecycle |
| Self-Description Administrator | `Ro-SD-A` | Governance Authority | XFSC FC self-description lifecycle |
| Participant Administrator | `Ro-MU-A` | Provider / Consumer | Per-participant config |
| Participant User Administrator | `Ro-Pa-A` | Provider / Consumer | Per-participant user mgmt |
| SD Publisher | `SD_PUBLISHER` | Provider users | Publish self-descriptions |
| SD Consumer | `SD_CONSUMER` | Consumer users | Search / consume catalogue |
| Infrastructure Admin | `INFRA_ADMIN` | Infrastructure Provider | Manage deployment scripts |
| Infrastructure Deployer | `INFRA_DEPLOYER` | Triggered by EDC | Trigger provisioning |
| Kibana Business User | `KIBANA_BUSINESS_USER` | All participants | Read access to monitoring |
| Kibana Admin | `KIBANA_ADMIN` | Operations | Admin access to monitoring |

### Onboarding and lifecycle processes

Standardised across every Simpl deployment so a participant onboarded in one data space follows the same procedure in another:

- **[BP03A — Onboarding (Provider/Consumer)](business-processes/BP03A-onboarding-participant-providers/README.md)** — applicant request → GA review → Tier 2 credential issuance via [Identity Provider](../security/access-control-and-trust/identity-provider/identity-provider/README.md). Six well-defined steps, audited end-to-end.
- **[BP03B — End-User onboarding](business-processes/BP03B-onboarding-participant-end-user/README.md)** — within an already-onboarded participant, configure end-user identities and roles.
- **[BP03C — End-User role request](business-processes/BP03C-end-user-role-request/README.md)** — self-service role-assignment workflow.
- **[SA03 — Credentials actions by the Governance Authority](business-processes/SA03-credentials-actions-governance-authority/README.md)** — post-onboarding credential lifecycle (revoke, suspend, reactivate, renew, edit identity attributes).
- **[BP01 / BP02 — Defining and configuring a data space](business-processes/BP01-define-dataspace-governance/README.md)** — the meta-process by which a new Simpl data space is brought into existence.

### Service Level Agreements

NFRs in [`foundations/non-functional-requirements/`](non-functional-requirements/README.md) carry measurable thresholds (where the Simpl Requirements site has published them) that bind every deployment regardless of the data-space domain — availability, accessibility, performance, and security baselines.

### Federated governance

Cross-data-space interoperability is one of Simpl-Open's distinguishing architectural goals: as multiple data spaces incorporate Simpl-Open, they become connected through:

- **Federated catalogue queries** routed via the [Query Mapper Adapter](../integration/resource-discovery/resource-catalogue/query-mapper-adapter/README.md).
- **Shared identity-attribute schemas** between Governance Authorities so that an attribute issued in space A can be evaluated in space B.
- **Common contract templates** shared via the [Contract Template Datastore](../governance/contract-management/contract-establishment/contract-template-datastore/README.md) (target design).
- **Federated authentication** through the [Authentication Provider Federation](../security/access-control-and-trust/authentication-provider-federation/README.md) capability.

---

## 3. Semantic interoperability

Shared vocabularies and ontologies that ensure participants interpret exchanged information the same way.

| Standard / vocabulary | Purpose | Where used in Simpl-Open |
|---|---|---|
| **[Gaia-X Trust Framework](https://gaia-x.eu/wp-content/uploads/2022/05/Gaia-x-Trust-Framework-22.04.pdf)** | Self-description structure, trust labels, participant attestation | [SD Tooling](../governance/resource-management/metadata-description/sd-tooling/README.md), [Simpl Catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) |
| **[SHACL (W3C)](https://www.w3.org/TR/shacl/)** | Constraint language for self-description schemas; validation server-side and client-side | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md), [Validation Backend](../integration/resource-discovery/search-engine/validation-backend/README.md) |
| **[ODRL (W3C, Open Digital Rights Language)](https://www.w3.org/TR/odrl-model/)** | Encoding of access and usage policies attached to self-descriptions and contracts | [SD Tooling Policy Creator](../governance/resource-management/metadata-description/sd-tooling/README.md), [Connector Policy Engine](../integration/resource-sharing/resource-sharing-runtime/connector/README.md), [Contract Manager](../governance/contract-management/contract-establishment/contract-manager/README.md) |
| **[DCAT (W3C Data Catalog Vocabulary)](https://www.w3.org/TR/vocab-dcat/) + DCAT-AP** | Catalogue metadata model — datasets, distributions, services, agents | [Simpl Catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md), federated catalogue interoperability |
| **[Dublin Core (DCT)](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)** | Schema metadata properties (`dct:title`, `dct:description`, `dct:creator`, `dct:created`, `dct:isPartOf`) | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) |
| **[OWL (W3C Web Ontology Language)](https://www.w3.org/TR/owl2-overview/)** | Versioning (`owl:versionInfo`) and ontology relationships | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) |
| **[SKOS](https://www.w3.org/TR/skos-reference/)** | Thesauri, controlled vocabularies, taxonomies | Vocabulary Datastore inside [Simpl Catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md); planned [Vocabulary Management](../data/semantics-and-vocabulary/vocabulary-hub/vocabulary-management/README.md) |
| **[PROV-O (W3C Provenance Ontology)](https://www.w3.org/TR/prov-o/)** | Lineage and provenance of self-descriptions and credentials | Implicit in audit trails; explicit alignment a roadmap item |
| **[IDS Information Model](https://github.com/International-Data-Spaces-Association/InformationModel)** | IDSA's data-space-native vocabulary for assets, contracts, transfer processes | Inside the [Connector (Eclipse EDC)](../integration/resource-sharing/resource-sharing-runtime/connector/README.md), inherited from upstream |
| **[W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)** | Credential structure for participant attestations and contract VCs | [VC Issuer](../security/credential-management/vc-issuance-verification/vc-issuer/README.md) (planned), [Wallet](../security/credential-management/wallet/wallet/README.md) (planned) |
| **[W3C Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-1.0/)** | DID-based addressing for participants and assets | Used inside Verifiable Credentials issued by the VC Issuer |
| **Custom SIMPL namespace** | `simpl:Schema`, `simpl:SchemaVersion`, `simpl:status`, `simpl:resourceType`, `simpl:latestVersion`, `simpl:changelog` | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md) — extends the standard vocabularies above with Simpl-specific lifecycle terms |

### Format-level semantics

Beyond vocabularies, Simpl pins to specific serialisation formats so the *shape* of every payload is predictable across implementations:

- **[JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)** — wire format for self-descriptions and verifiable credentials.
- **[Turtle (TTL)](https://www.w3.org/TR/turtle/)** — storage format for SHACL constraints and ontologies in the Schema Management Service and Schema Synch Service.
- **[RDF 1.1](https://www.w3.org/TR/rdf11-concepts/)** — underlying graph data model for all of the above.
- **[SPARQL 1.1](https://www.w3.org/TR/sparql11-overview/)** — query language for the catalogue's RDF triple store (Apache Jena Fuseki / Neo4j with neosemantics).

---

## 4. Technical interoperability

Protocols, APIs, formats, identity, and transport — the standards that let two systems physically exchange information.

### Data-space protocols

| Standard | Implementation | Solution(s) |
|---|---|---|
| **[Data Space Protocol (DSP)](https://docs.internationaldataspaces.org/ids-knowledgebase/v/dataspace-protocol/) / IDSA RAM 4** | Eclipse Dataspace Connector (EDC) fork | [Connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) |
| **DSP Contract Negotiation Protocol** | EDC Control Plane state machine | [Connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md), [Contract Consumption Adapter](../integration/resource-discovery/search-engine/contract-consumption-adapter/README.md) |
| **DSP Transfer Process Protocol** (Consumer Pull, Provider Push) | EDC Data Plane state machine | [Connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) |

### Authentication and identity

| Standard | Implementation | Solution(s) |
|---|---|---|
| **[OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html)** | Keycloak | [Tier 1 Authentication Provider](../security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md) |
| **[OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) + [PKCE (RFC 7636)](https://datatracker.ietf.org/doc/html/rfc7636)** | Keycloak frontend integrations | [Schema Management Service](../data/semantics-and-vocabulary/schema-management/schema-management-service/README.md), [Catalogue Client Application](../integration/resource-discovery/search-engine/catalogue-client-application/README.md), [SD Tooling](../governance/resource-management/metadata-description/sd-tooling/README.md) |
| **[JWT (RFC 7519)](https://datatracker.ietf.org/doc/html/rfc7519) / JOSE** | Tier 1 token format with custom Simpl claims (`participant_id`, `credential_id`, `identity_attributes`, `client-roles`) | [Tier 1 Authentication Provider](../security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md) authenticator plugin |
| **[mTLS](https://datatracker.ietf.org/doc/html/rfc8705) (TLS 1.3 client auth, X.509)** | Agent-to-agent authenticity for all Tier 2 traffic | [Authorisation Tier 2 Gateway](../security/access-control-and-trust/authorisation/authorisation/README.md), [Tier 2 Authentication Provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) |
| **[X.509 (RFC 5280)](https://datatracker.ietf.org/doc/html/rfc5280)** | Tier 2 credentials issued by EJBCA | [Identity Provider](../security/access-control-and-trust/identity-provider/identity-provider/README.md) |
| **[CRL (RFC 5280)](https://datatracker.ietf.org/doc/html/rfc5280) / [OCSP (RFC 6960)](https://datatracker.ietf.org/doc/html/rfc6960)** | Revocation validation in the HTTP client | [simpl-http-client](../cross-cutting/libs/simpl-http-client/README.md) |
| **[PKCS#12 (RFC 7292)](https://datatracker.ietf.org/doc/html/rfc7292)** | SuperAdmin and operator certificate distribution format | [Governance Authority Agent](../cross-cutting/agents/governance-authority-agent/deployment-guide.md) |
| **[eIDAS](https://eur-lex.europa.eu/eli/reg/2024/1183/oj) / EUDI** | Demonstrated through the eIDAS Demo Node SPI | [eidas-demo-keycloak-extension](../cross-cutting/samples/eidas-demo-keycloak-extension/README.md), [eidas-demo-node-deploy](../cross-cutting/samples/eidas-demo-node-deploy/README.md) |

### API-style protocols

| Standard | Implementation | Solution(s) |
|---|---|---|
| **[OpenAPI 3.x](https://spec.openapis.org/oas/latest.html)** | Every REST API in Simpl-Open ships an OpenAPI spec | [API catalogue](api-catalogue.md) — 38 specs |
| **[AsyncAPI 3.0.0](https://www.asyncapi.com/docs/reference/specification/v3.0.0)** | Kafka-topic message contracts | [Notification Service](../administration/notification-and-messaging/notification/notification-service/README.md), Onboarding, Users-Roles, Authentication Provider, Tier 2 Gateway — see [API catalogue](api-catalogue.md) |
| **REST over HTTP/2** | Default API style; HTTP/2 with TLS 1.3 termination at the gateway | All gateway-fronted services |
| **GraphQL** | Dagster orchestration platform's primary programmatic interface | [Orchestration Platform](../data/supporting-data-services/data-orchestration/orchestration-platform/README.md) |
| **[RFC 7807 Problem Details](https://datatracker.ietf.org/doc/html/rfc7807)** | Standard error format for REST endpoints | [Asset Orchestrator](../data/supporting-data-services/data-orchestration/asset-orchestrator/README.md) (explicit; others inherit via Spring Boot defaults) |

### Messaging and storage

| Standard | Implementation | Solution(s) |
|---|---|---|
| **[Apache Kafka protocol](https://kafka.apache.org/protocol)** | Pervasive async coordination bus; SASL-secured (`KAFKA_SASL_ENABLED=true`) | [Notification Service](../administration/notification-and-messaging/notification/notification-service/README.md), [Contract Manager](../governance/contract-management/contract-establishment/contract-manager/README.md), [Triggering Module](../infrastructure/provisioning/infrastructure-provisioning/triggering-module/README.md), [Asset Orchestrator](../data/supporting-data-services/data-orchestration/asset-orchestrator/README.md) |
| **[Amazon S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) (MinIO-compatible)** | Primary data-plane object storage | [Connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) (MinIO S3 extension) |
| **PostgreSQL wire protocol** | Pervasive persistence | All Java services with state |
| **HashiCorp Vault HTTP API** | Secrets and key management; ed25519 transit engine for signing | [Signer Service](../security/credential-management/signing/signer-service/README.md), every agent |

### Deployment and orchestration

| Standard | Implementation | Solution(s) |
|---|---|---|
| **[Kubernetes API](https://kubernetes.io/docs/reference/kubernetes-api/)** | Runtime substrate for every agent | All agent compositions |
| **[OCI Image Format](https://github.com/opencontainers/image-spec)** | Container image distribution; registry at `code.europa.eu:4567/simpl/...` | All deployable services |
| **[Helm Chart API v3](https://helm.sh/docs/topics/charts/)** | Default deployment artefact; charts published to the EU GitLab Helm registry | All agent and component charts |
| **[Crossplane CRDs](https://docs.crossplane.io/)** | Cloud-resource provisioning manifests | [Infrastructure Provisioner](../infrastructure/provisioning/infrastructure-provisioning/infrastructure-provisioner/README.md) |
| **[OpenTofu / Terraform HCL](https://opentofu.org/docs/intro/)** | Alternative provisioning language alongside Crossplane | [Infrastructure Provisioner](../infrastructure/provisioning/infrastructure-provisioning/infrastructure-provisioner/README.md) |
| **[ArgoCD Application CRD](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/)** | GitOps deployment driver for every agent | [`cross-cutting/agents/`](../cross-cutting/agents/README.md) |

### CEF Building Blocks (roadmap)

European Commission Connecting Europe Facility (CEF) Digital Building Blocks slated for future integration (FTA §6.3.1 Technology Roadmap):

| Building block | Status | Solution slot |
|---|---|---|
| **eDelivery** | Roadmap; hook in EDC connector exists; service stub | [`integration/data-sharing/simple-data-transfer/edelivery/`](../integration/data-sharing/README.md) |
| **eSignature** | Roadmap | [`security/credential-management/signing/esignature/`](../security/credential-management/signing/README.md) |
| **eInvoicing** | Roadmap | [`governance/contract-management/billing/einvoicing/`](../governance/contract-management/README.md) |
| **eID** | Roadmap; eIDAS demo extension exists | [`security/access-control-and-trust/identity-provider/eid/`](../security/access-control-and-trust/identity-provider/README.md) |

### Observability and monitoring

| Standard | Implementation | Solution(s) |
|---|---|---|
| **[OpenTelemetry](https://opentelemetry.io/docs/specs/otel/)** | Tracing inside the Connector | [Connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) |
| **Elastic Common Schema (ECS)** | Log shape consumed by ECK; emitted by [Common Logging](../cross-cutting/libs/common-logging-java/README.md) | [Monitoring Service](../administration/observability/dashboarding/monitoring-service/README.md) |
| **[Prometheus exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/)** | Metrics endpoints | All Spring Boot services (via Micrometer) |

---

## See also

- [`api-catalogue.md`](api-catalogue.md) — every imported OpenAPI/AsyncAPI specification, the machine-readable face of technical interoperability.
- [`capability-map.md`](capability-map.md) — the structural map of what Simpl-Open does; many capabilities exist *because* of one of the four EIF layers above.
- [`principles.md`](principles.md) — the high-level architecture commitments that motivate the standard choices on this page.
- [`glossary.md`](glossary.md) — definitions of Simpl-specific terms used across these tables.
- [`business-processes/`](business-processes/README.md) — the operational flows that bind organisational interoperability to actual deployed behaviour.

## Status

This page is reconciled against the FTA spec (§2.5 Connector, §2.7 Capabilities, §4.3.1 ACV Static, §6.3 Technology Choices, §6.5 Federated Catalogue), the imported OpenAPI/AsyncAPI specs, and the source-repo READMEs as of 2026-04-28. Items flagged "roadmap" are not in current Release 3.0 scope; items without an explicit Simpl-Open binding (e.g. PROV-O alignment, CEF blocks) are listed for completeness so future work can pick them up.
