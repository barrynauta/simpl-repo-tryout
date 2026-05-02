<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a> &nbsp;»&nbsp;
<a href="README.md">Foundations</a> &nbsp;»&nbsp;
<strong>API catalogue</strong>
</p>
</div>

# API catalogue

Single index of every OpenAPI and AsyncAPI specification imported into this documentation catalogue from the Simpl-Open implementation source. For each solution that exposes APIs, the spec files live in `<solution>/api/` and are linked from the solution's own README.

Last imported from `code.europa.eu/simpl/simpl-open/development/...` on **2026-04-28**.

---

## Summary

| Metric | Count |
|--------|-------|
| Total specifications | **42** |
| OpenAPI 3.x | 36 |
| AsyncAPI 3.x | 6 |
| Tier 1 (human-user / browser-facing) | 11 |
| Tier 2 (agent-to-agent, mTLS) | 4 |
| Solutions exposing APIs | 21 |

---

## Browse by dimension

The capability map is the canonical organising structure of this catalogue; APIs follow it.

### administration

**[notification-service](../administration/notification-and-messaging/notification/notification-service/README.md)** — `notification-and-messaging / notification`  →  [api/](../administration/notification-and-messaging/notification/notification-service/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`asyncapi-v1.yaml`](../administration/notification-and-messaging/notification/notification-service/api/asyncapi-v1.yaml) | asyncapi 3.0.0 | Notification Service API | `1.0.0` | — | 1 channels |
| [`asyncapi.yaml`](../administration/notification-and-messaging/notification/notification-service/api/asyncapi.yaml) | asyncapi 3.0.0 | Notification Service API | `1.0.0` | — | 1 channels |


### data

**[simpl-schema-manager](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md)** — `semantics-and-vocabulary / schema-management`  →  [api/](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`resolver-interface.openapi.yaml`](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/api/resolver-interface.openapi.yaml) | openapi 3.0.3 | Schema Management Service — Resolver Interface | `0.0.0-stub` | — |  |
| [`schema-management-api.openapi.yaml`](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/api/schema-management-api.openapi.yaml) | openapi 3.0.3 | Schema Management Service — Management API | `0.0.0-stub` | — |  |
| [`schema_openapi.yaml`](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/api/schema_openapi.yaml) | openapi 3.0.1 | Schema Management API | `1.0.0` | — | 9 paths |

**[schema-sync-adapter](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/README.md)** — `semantics-and-vocabulary / schema-management`  →  [api/](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi-schema-sync-adapter-tier2-v1.yaml`](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/api/openapi-schema-sync-adapter-tier2-v1.yaml) | openapi 3.0.1 | Schema Sync Adapter API | `1.0` | Tier 2 | 1 paths |
| [`openapi-schema-sync-adapter-v1.yaml`](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/api/openapi-schema-sync-adapter-v1.yaml) | openapi 3.0.1 | Schema Sync Adapter API | `1.0` | — | 1 paths |

**[asset-orchestrator](../data/supporting-data-services/data-orchestration/asset-orchestrator/README.md)** — `supporting-data-services / data-orchestration`  →  [api/](../data/supporting-data-services/data-orchestration/asset-orchestrator/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi-asset-orchestrator-v1.yaml`](../data/supporting-data-services/data-orchestration/asset-orchestrator/api/openapi-asset-orchestrator-v1.yaml) | openapi 3.0.1 | Asset Orchestrator API | `1.0.0` | — | 6 paths |


### governance

**[contract-manager](../governance/contract-management/contract-establishment/contract-manager/README.md)** — `contract-management / contract-establishment`  →  [api/](../governance/contract-management/contract-establishment/contract-manager/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi3-v1.yaml`](../governance/contract-management/contract-establishment/contract-manager/api/openapi3-v1.yaml) | openapi 3.0.3 | Contract Manager | `1.1` | — | 8 paths |

**[onboarding-service](../governance/participant-management/onboarding/fe-onboarding/README.md)** — `participant-management / onboarding`  →  [api/](../governance/participant-management/onboarding/fe-onboarding/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`asyncapi-v1.yaml`](../governance/participant-management/onboarding/fe-onboarding/api/asyncapi-v1.yaml) | asyncapi 3.0.0 | Onboarding Async API | `1.3.0` | — | 1 channels |
| [`onboarding-tier1-v2.yaml`](../governance/participant-management/onboarding/fe-onboarding/api/onboarding-tier1-v2.yaml) | openapi 3.0.1 | Onboarding Tier 1 | `2.0.1` | Tier 1 | 2 paths |
| [`onboarding-v1.yaml`](../governance/participant-management/onboarding/fe-onboarding/api/onboarding-v1.yaml) | openapi 3.0.1 | Onboarding | `1.6.0` | — | 25 paths |

**[users-roles](../governance/participant-management/user-roles/fe-users-roles/README.md)** — `participant-management / user-roles`  →  [api/](../governance/participant-management/user-roles/fe-users-roles/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`asyncapi-v1.yaml`](../governance/participant-management/user-roles/fe-users-roles/api/asyncapi-v1.yaml) | asyncapi 3.0.0 | Users and Roles Async API | `1.3.0` | — | 3 channels |
| [`usersroles-tier1-v2.yaml`](../governance/participant-management/user-roles/fe-users-roles/api/usersroles-tier1-v2.yaml) | openapi 3.0.1 | User and Roles Tier 1 | `2.0.0` | Tier 1 | 12 paths |
| [`usersroles-v1.yaml`](../governance/participant-management/user-roles/fe-users-roles/api/usersroles-v1.yaml) | openapi 3.0.1 | User and Roles | `1.5.0` | — | 9 paths |


| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|


### infrastructure


| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|


### integration

**[query-mapper-adapter](../integration/resource-discovery/search-engine/query-mapper-adapter/README.md)** — `resource-discovery / resource-catalogue`  →  [api/](../integration/resource-discovery/search-engine/query-mapper-adapter/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`adapter_openapi.yaml`](../integration/resource-discovery/search-engine/query-mapper-adapter/api/adapter_openapi.yaml) | openapi 3.0.1 | Query Mapper Adapter API | `1.0.0` | — | 5 paths |

**[simpl-catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md)** — `resource-discovery / resource-catalogue`  →  [api/](../integration/resource-discovery/resource-catalogue/simpl-catalogue/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`fc_openapi-itb.yaml`](../integration/resource-discovery/resource-catalogue/simpl-catalogue/api/fc_openapi-itb.yaml) | openapi 3.0.1 | Eclipse XFSC Federated Catalogue | `1.0.0` | — | 21 paths |
| [`fc_openapi.yaml`](../integration/resource-discovery/resource-catalogue/simpl-catalogue/api/fc_openapi.yaml) | openapi 3.0.1 | Eclipse XFSC Federated Catalogue | `1.0.0` | — | 21 paths |

**[catalogue-client-application](../integration/resource-discovery/search-engine/catalogue-client-application/README.md)** — `resource-discovery / search-engine`  →  [api/](../integration/resource-discovery/search-engine/catalogue-client-application/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi-xfscadvsearch-tier1-v1.yaml`](../integration/resource-discovery/search-engine/catalogue-client-application/api/openapi-xfscadvsearch-tier1-v1.yaml) | openapi 3.0.1 | Catalog Search API | `1.0` | Tier 1 | 3 paths |
| [`openapi-xfscadvsearch-tier1-v2.yaml`](../integration/resource-discovery/search-engine/catalogue-client-application/api/openapi-xfscadvsearch-tier1-v2.yaml) | openapi 3.0.1 | Catalog Search API | `1.0` | Tier 1 | 3 paths |

**[contract-consumption-adapter](../integration/resource-discovery/search-engine/contract-consumption-adapter/README.md)** — `resource-discovery / search-engine`  →  [api/](../integration/resource-discovery/search-engine/contract-consumption-adapter/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi-contract-consumption-be-tier1-v1.yaml`](../integration/resource-discovery/search-engine/contract-consumption-adapter/api/openapi-contract-consumption-be-tier1-v1.yaml) | openapi 3.0.1 | Contract Consumption API | `1.0` | Tier 1 | 8 paths |

**[validation-backend](../integration/resource-discovery/search-engine/validation-backend/README.md)** — `resource-discovery / search-engine`  →  [api/](../integration/resource-discovery/search-engine/validation-backend/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi-validation-v1.yaml`](../integration/resource-discovery/search-engine/validation-backend/api/openapi-validation-v1.yaml) | openapi 3.0.1 | Validation Service API | `1.0` | — | 2 paths |

**[edc-connector-adapter](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md)** — `resource-sharing / resource-sharing-runtime`  →  [api/](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi-edc-connector-adapter-v1.yaml`](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/api/openapi-edc-connector-adapter-v1.yaml) | openapi 3.0.1 | EDC Connector Adapter API | `1.0` | — | 8 paths |
| [`openapi-edc-connector-adapter-v2.yaml`](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/api/openapi-edc-connector-adapter-v2.yaml) | openapi 3.0.1 | EDC Connector Adapter API | `1.0` | — | 1 paths |


### security

**[tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md)** — `access-control-and-trust / authentication-provider-federation`  →  [api/](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`asyncapi-v1.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/asyncapi-v1.yaml) | asyncapi 3.0.0 | Authentication Provider Async API | `1.3.0` | — | 2 channels |
| [`authenticationprovider-tier1-v2.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-tier1-v2.yaml) | openapi 3.0.1 | Authentication Provider Tier 1 | `2.0.0` | Tier 1 | 24 paths |
| [`authenticationprovider-tier2-v2.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-tier2-v2.yaml) | openapi 3.0.1 | Authentication Provider Tier 2 | `2.0.0` | Tier 2 | 2 paths |
| [`authenticationprovider-v1.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-v1.yaml) | openapi 3.0.1 | Authentication Provider | `1.5.0` | — | 16 paths |

**[authorisation](../security/access-control-and-trust/authorisation/README.md)** — `access-control-and-trust / authorisation`  →  [api/](../security/access-control-and-trust/authorisation/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`asyncapi-v1.yaml`](../security/access-control-and-trust/authorisation/api/asyncapi-v1.yaml) | asyncapi 3.0.0 | Tier 2 Gateway Async API | `1.3.0` | — | 1 channels |
| [`tier1gateway-v1.yaml`](../security/access-control-and-trust/authorisation/api/tier1gateway-v1.yaml) | openapi 3.0.1 | Tier 1 Gateway | `1.5.0` | — | 1 paths |

**[identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md)** — `access-control-and-trust / identity-provider`  →  [api/](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`identityprovider-tier1-v2.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-tier1-v2.yaml) | openapi 3.0.1 | Identity Provider Tier 1 | `2.0.0` | Tier 1 | 8 paths |
| [`identityprovider-tier2-v2.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-tier2-v2.yaml) | openapi 3.0.1 | Identity Provider Tier 2 | `2.0.0` | Tier 2 | 8 paths |
| [`identityprovider-v1.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-v1.yaml) | openapi 3.0.1 | Identity Provider | `1.5.0` | — | 11 paths |

**[security-attributes-provider](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md)** — `access-control-and-trust / security-attribute-provider-federation`  →  [api/](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`securityattributesprovider-tier1-v2.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-tier1-v2.yaml) | openapi 3.0.1 | Security Attributes Provider Tier 1 | `2.0.0` | Tier 1 | 4 paths |
| [`securityattributesprovider-tier2-v2.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-tier2-v2.yaml) | openapi 3.0.1 | Security Attributes Provider Tier 2 | `2.0.0` | Tier 2 | 4 paths |
| [`securityattributesprovider-v1.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-v1.yaml) | openapi 3.0.1 | Security Attributes Provider | `1.5.0` | — | 9 paths |

**[signer-service](../security/credential-management/signing/signer-service/README.md)** — `credential-management / signing`  →  [api/](../security/credential-management/signing/signer-service/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi3-v1.yaml`](../security/credential-management/signing/signer-service/api/openapi3-v1.yaml) | openapi 3.0.3 | Signing service | `1.1` | — | 3 paths |

**[vc-issuer](../security/credential-management/vc-issuance-verification/vc-issuer/README.md)** — `credential-management / vc-issuance-verification`  →  [api/](../security/credential-management/vc-issuance-verification/vc-issuer/api/README.md)

| File | Kind | Title | API version | Tier | Endpoints |
|------|------|-------|------|------|----------|
| [`openapi3-v1.yaml`](../security/credential-management/vc-issuance-verification/vc-issuer/api/openapi3-v1.yaml) | openapi 3.0.3 | Verifiable Credentials issuer service | `1.1` | — | 3 paths |


---

## Browse by kind

### OpenAPI specifications

REST API contracts. View locally with [editor.swagger.io](https://editor.swagger.io/) or `npx redoc-cli serve <file>.yaml`.

| Solution | File | Title | Tier | Paths |
|----------|------|-------|------|-------|
| [simpl-schema-manager](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md) | [`resolver-interface.openapi.yaml`](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/api/resolver-interface.openapi.yaml) | Schema Management Service — Resolver Interface | — | — |
| [simpl-schema-manager](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md) | [`schema-management-api.openapi.yaml`](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/api/schema-management-api.openapi.yaml) | Schema Management Service — Management API | — | — |
| [simpl-schema-manager](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md) | [`schema_openapi.yaml`](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/api/schema_openapi.yaml) | Schema Management API | — | 9 |
| [schema-sync-adapter](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/README.md) | [`openapi-schema-sync-adapter-tier2-v1.yaml`](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/api/openapi-schema-sync-adapter-tier2-v1.yaml) | Schema Sync Adapter API | Tier 2 | 1 |
| [schema-sync-adapter](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/README.md) | [`openapi-schema-sync-adapter-v1.yaml`](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/api/openapi-schema-sync-adapter-v1.yaml) | Schema Sync Adapter API | — | 1 |
| [asset-orchestrator](../data/supporting-data-services/data-orchestration/asset-orchestrator/README.md) | [`openapi-asset-orchestrator-v1.yaml`](../data/supporting-data-services/data-orchestration/asset-orchestrator/api/openapi-asset-orchestrator-v1.yaml) | Asset Orchestrator API | — | 6 |
| [contract-manager](../governance/contract-management/contract-establishment/contract-manager/README.md) | [`openapi3-v1.yaml`](../governance/contract-management/contract-establishment/contract-manager/api/openapi3-v1.yaml) | Contract Manager | — | 8 |
| [onboarding-service](../governance/participant-management/onboarding/fe-onboarding/README.md) | [`onboarding-tier1-v2.yaml`](../governance/participant-management/onboarding/fe-onboarding/api/onboarding-tier1-v2.yaml) | Onboarding Tier 1 | Tier 1 | 2 |
| [onboarding-service](../governance/participant-management/onboarding/fe-onboarding/README.md) | [`onboarding-v1.yaml`](../governance/participant-management/onboarding/fe-onboarding/api/onboarding-v1.yaml) | Onboarding | — | 25 |
| [users-roles](../governance/participant-management/user-roles/fe-users-roles/README.md) | [`usersroles-tier1-v2.yaml`](../governance/participant-management/user-roles/fe-users-roles/api/usersroles-tier1-v2.yaml) | User and Roles Tier 1 | Tier 1 | 12 |
| [users-roles](../governance/participant-management/user-roles/fe-users-roles/README.md) | [`usersroles-v1.yaml`](../governance/participant-management/user-roles/fe-users-roles/api/usersroles-v1.yaml) | User and Roles | — | 9 |
| [query-mapper-adapter](../integration/resource-discovery/search-engine/query-mapper-adapter/README.md) | [`adapter_openapi.yaml`](../integration/resource-discovery/search-engine/query-mapper-adapter/api/adapter_openapi.yaml) | Query Mapper Adapter API | — | 5 |
| [simpl-catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) | [`fc_openapi-itb.yaml`](../integration/resource-discovery/resource-catalogue/simpl-catalogue/api/fc_openapi-itb.yaml) | Eclipse XFSC Federated Catalogue | — | 21 |
| [simpl-catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) | [`fc_openapi.yaml`](../integration/resource-discovery/resource-catalogue/simpl-catalogue/api/fc_openapi.yaml) | Eclipse XFSC Federated Catalogue | — | 21 |
| [catalogue-client-application](../integration/resource-discovery/search-engine/catalogue-client-application/README.md) | [`openapi-xfscadvsearch-tier1-v1.yaml`](../integration/resource-discovery/search-engine/catalogue-client-application/api/openapi-xfscadvsearch-tier1-v1.yaml) | Catalog Search API | Tier 1 | 3 |
| [catalogue-client-application](../integration/resource-discovery/search-engine/catalogue-client-application/README.md) | [`openapi-xfscadvsearch-tier1-v2.yaml`](../integration/resource-discovery/search-engine/catalogue-client-application/api/openapi-xfscadvsearch-tier1-v2.yaml) | Catalog Search API | Tier 1 | 3 |
| [contract-consumption-adapter](../integration/resource-discovery/search-engine/contract-consumption-adapter/README.md) | [`openapi-contract-consumption-be-tier1-v1.yaml`](../integration/resource-discovery/search-engine/contract-consumption-adapter/api/openapi-contract-consumption-be-tier1-v1.yaml) | Contract Consumption API | Tier 1 | 8 |
| [validation-backend](../integration/resource-discovery/search-engine/validation-backend/README.md) | [`openapi-validation-v1.yaml`](../integration/resource-discovery/search-engine/validation-backend/api/openapi-validation-v1.yaml) | Validation Service API | — | 2 |
| [edc-connector-adapter](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md) | [`openapi-edc-connector-adapter-v1.yaml`](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/api/openapi-edc-connector-adapter-v1.yaml) | EDC Connector Adapter API | — | 8 |
| [edc-connector-adapter](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md) | [`openapi-edc-connector-adapter-v2.yaml`](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/api/openapi-edc-connector-adapter-v2.yaml) | EDC Connector Adapter API | — | 1 |
| [tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) | [`authenticationprovider-tier1-v2.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-tier1-v2.yaml) | Authentication Provider Tier 1 | Tier 1 | 24 |
| [tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) | [`authenticationprovider-tier2-v2.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-tier2-v2.yaml) | Authentication Provider Tier 2 | Tier 2 | 2 |
| [tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) | [`authenticationprovider-v1.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-v1.yaml) | Authentication Provider | — | 16 |
| [authorisation](../security/access-control-and-trust/authorisation/README.md) | [`tier1gateway-v1.yaml`](../security/access-control-and-trust/authorisation/api/tier1gateway-v1.yaml) | Tier 1 Gateway | — | 1 |
| [identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) | [`identityprovider-tier1-v2.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-tier1-v2.yaml) | Identity Provider Tier 1 | Tier 1 | 8 |
| [identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) | [`identityprovider-tier2-v2.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-tier2-v2.yaml) | Identity Provider Tier 2 | Tier 2 | 8 |
| [identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) | [`identityprovider-v1.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-v1.yaml) | Identity Provider | — | 11 |
| [security-attributes-provider](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md) | [`securityattributesprovider-tier1-v2.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-tier1-v2.yaml) | Security Attributes Provider Tier 1 | Tier 1 | 4 |
| [security-attributes-provider](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md) | [`securityattributesprovider-tier2-v2.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-tier2-v2.yaml) | Security Attributes Provider Tier 2 | Tier 2 | 4 |
| [security-attributes-provider](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md) | [`securityattributesprovider-v1.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-v1.yaml) | Security Attributes Provider | — | 9 |
| [signer-service](../security/credential-management/signing/signer-service/README.md) | [`openapi3-v1.yaml`](../security/credential-management/signing/signer-service/api/openapi3-v1.yaml) | Signing service | — | 3 |
| [vc-issuer](../security/credential-management/vc-issuance-verification/vc-issuer/README.md) | [`openapi3-v1.yaml`](../security/credential-management/vc-issuance-verification/vc-issuer/api/openapi3-v1.yaml) | Verifiable Credentials issuer service | — | 3 |

### AsyncAPI specifications

Kafka-topic message contracts (publishers / subscribers / payload schemas). View with [studio.asyncapi.com](https://studio.asyncapi.com/).

| Solution | File | Title | Channels |
|----------|------|-------|----------|
| [notification-service](../administration/notification-and-messaging/notification/notification-service/README.md) | [`asyncapi-v1.yaml`](../administration/notification-and-messaging/notification/notification-service/api/asyncapi-v1.yaml) | Notification Service API | 1 |
| [notification-service](../administration/notification-and-messaging/notification/notification-service/README.md) | [`asyncapi.yaml`](../administration/notification-and-messaging/notification/notification-service/api/asyncapi.yaml) | Notification Service API | 1 |
| [onboarding-service](../governance/participant-management/onboarding/fe-onboarding/README.md) | [`asyncapi-v1.yaml`](../governance/participant-management/onboarding/fe-onboarding/api/asyncapi-v1.yaml) | Onboarding Async API | 1 |
| [users-roles](../governance/participant-management/user-roles/fe-users-roles/README.md) | [`asyncapi-v1.yaml`](../governance/participant-management/user-roles/fe-users-roles/api/asyncapi-v1.yaml) | Users and Roles Async API | 3 |
| [tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) | [`asyncapi-v1.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/asyncapi-v1.yaml) | Authentication Provider Async API | 2 |
| [authorisation](../security/access-control-and-trust/authorisation/README.md) | [`asyncapi-v1.yaml`](../security/access-control-and-trust/authorisation/api/asyncapi-v1.yaml) | Tier 2 Gateway Async API | 1 |

---

## Browse by tier

The IAA two-tier architecture means most services expose distinct API surfaces depending on the caller:

- **Tier 1** APIs are reached through the Tier 1 Gateway by human users and their browsers. Authentication is by Keycloak JWT; authorisation is RBAC.
- **Tier 2** APIs are reached through the Tier 2 Gateway by other agents. Authentication is by x.509 client certificate (mTLS); authorisation is ABAC against identity attributes.
- Specs without a tier suffix are typically internal-only (called from inside the same agent) or pre-date the explicit Tier 1 / Tier 2 split.

### Tier 1 — human/browser facing

| Solution | File | Title |
|----------|------|-------|
| [onboarding-service](../governance/participant-management/onboarding/fe-onboarding/README.md) | [`onboarding-tier1-v2.yaml`](../governance/participant-management/onboarding/fe-onboarding/api/onboarding-tier1-v2.yaml) | Onboarding Tier 1 |
| [users-roles](../governance/participant-management/user-roles/fe-users-roles/README.md) | [`usersroles-tier1-v2.yaml`](../governance/participant-management/user-roles/fe-users-roles/api/usersroles-tier1-v2.yaml) | User and Roles Tier 1 |
| [catalogue-client-application](../integration/resource-discovery/search-engine/catalogue-client-application/README.md) | [`openapi-xfscadvsearch-tier1-v1.yaml`](../integration/resource-discovery/search-engine/catalogue-client-application/api/openapi-xfscadvsearch-tier1-v1.yaml) | Catalog Search API |
| [catalogue-client-application](../integration/resource-discovery/search-engine/catalogue-client-application/README.md) | [`openapi-xfscadvsearch-tier1-v2.yaml`](../integration/resource-discovery/search-engine/catalogue-client-application/api/openapi-xfscadvsearch-tier1-v2.yaml) | Catalog Search API |
| [contract-consumption-adapter](../integration/resource-discovery/search-engine/contract-consumption-adapter/README.md) | [`openapi-contract-consumption-be-tier1-v1.yaml`](../integration/resource-discovery/search-engine/contract-consumption-adapter/api/openapi-contract-consumption-be-tier1-v1.yaml) | Contract Consumption API |
| [tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) | [`authenticationprovider-tier1-v2.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-tier1-v2.yaml) | Authentication Provider Tier 1 |
| [identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) | [`identityprovider-tier1-v2.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-tier1-v2.yaml) | Identity Provider Tier 1 |
| [security-attributes-provider](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md) | [`securityattributesprovider-tier1-v2.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-tier1-v2.yaml) | Security Attributes Provider Tier 1 |

### Tier 2 — agent-to-agent (mTLS)

| Solution | File | Title |
|----------|------|-------|
| [schema-sync-adapter](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/README.md) | [`openapi-schema-sync-adapter-tier2-v1.yaml`](../data/semantics-and-vocabulary/schema-management/schema-sync-adapter/api/openapi-schema-sync-adapter-tier2-v1.yaml) | Schema Sync Adapter API |
| [tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) | [`authenticationprovider-tier2-v2.yaml`](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/api/authenticationprovider-tier2-v2.yaml) | Authentication Provider Tier 2 |
| [identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) | [`identityprovider-tier2-v2.yaml`](../security/access-control-and-trust/identity-provider-federation/identity-provider/api/identityprovider-tier2-v2.yaml) | Identity Provider Tier 2 |
| [security-attributes-provider](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md) | [`securityattributesprovider-tier2-v2.yaml`](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/api/securityattributesprovider-tier2-v2.yaml) | Security Attributes Provider Tier 2 |

---

## Notes

- **Solutions with no API spec here:** the [Connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) is a fork of upstream Eclipse EDC; its three API surfaces (Management, DSP, Data Plane) are inherited from upstream and not redefined in the Simpl repository — see [the Connector's `api/README.md`](../integration/resource-sharing/resource-sharing-runtime/connector/api/README.md) for upstream links. The [Tier 1 Authentication Provider](../security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md) wraps upstream Keycloak; its OpenID Connect endpoints come from Keycloak directly. Planned solutions (`vc-issuer`, `wallet`, `policy-template-datastore`, `vocabulary-management`) have no source repository yet.
- **Source-of-truth path** for each spec is recorded in the parent solution's `README.md` under "Source code". When the source code repository is restructured per the PSO mapping, this catalogue should be re-imported.
- **Generic / shared specs** like `applicationinfo-v1.yaml` (a 4 KB health endpoint shared across IAA components) and the aggregated copies under `iaa/common/.../static/openapi/` are intentionally **not** imported — only canonical per-solution specs.
- **Re-importing**: the catalogue can be regenerated by re-running the API extraction script. Filenames preserve their source naming exactly so changes are diff-friendly.
