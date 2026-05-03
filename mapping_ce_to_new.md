# Mapping: Code-Europa-EU → New Repo Structure

All repos from code.europa.eu/simpl/simpl-open/development, sorted by team then solution. Status: `placed` = mapped to a path in the new repo; `pending` = not yet placed.

> Note: `sdtooling-validation-api-be` (data1) maps to two separate slots in the new repo (two rows).  
> Note: `agent-iaa/provider-iaa` (IAA) similarly maps to two slots (two rows).  
> Note: items in *italics* in the CE Solution column indicate the exact name as listed in the GitLab group; small spelling differences from the canonical URL are preserved.

| CE Team | CE Solution | New Path | Status |
|---|---|---|---|
| Agents | application-provider | `cross-cutting/agents/application-provider-agent` | placed |
| Agents | common_components | `cross-cutting/agents/common-components` | placed |
| Agents | consumer | `cross-cutting/agents/consumer-agent` | placed |
| Agents | data-provider | `cross-cutting/agents/data-provider-agent` | placed |
| Agents | governance-authority | `cross-cutting/agents/governance-authority-agent` | placed |
| Agents | infrastructure-provider | `cross-cutting/agents/infrastructure-provider-agent` | placed |
| Common-components | kafka | `administration/notification-and-messaging/messaging/kafka` | placed |
| Common-components | openbao | `security/access-control-and-trust/encryption/openbao` | placed |
| Common-components | open-bao-init | `security/access-control-and-trust/encryption/openbao/openbao-init` | placed |
| Common-components | postgres-cluster | `data/supporting-data-services/common/postgres-cluster` | placed |
| Common-components | shared-specs | — | pending |
| Common-components | vault | `security/access-control-and-trust/encryption/vault` | placed |
| Contract-billing | actors | — | pending |
| Contract-billing | billing | — | pending |
| Contract-billing | billing-common | — | pending |
| Contract-billing | common | — | pending |
| Contract-billing | common_logging | `administration/observability/logging/common-logging-java` | placed |
| Contract-billing | common_logging_python | `administration/observability/logging/common-logging-python` | placed |
| Contract-billing | consumer-contract-billing | `cross-cutting/agents/agent-contract-billing/consumer-contract-billing` | placed |
| Contract-billing | contract | — | pending |
| Contract-billing | contract-ui | `governance/contract-management/contract-establishment/contract-manager-ui` | placed |
| Contract-billing | invoicing | — | pending |
| Contract-billing | notification-service | `administration/notification-and-messaging/notification/notification-service` | placed |
| Contract-billing | provider-contract-billing | `cross-cutting/agents/agent-contract-billing/provider-contract-billing` | placed |
| Contract-billing | settlement | — | pending |
| Contract-billing | signing-service | `security/credential-management/signing/signer-service` | placed |
| Contract-billing | simpl-issuance | — | pending |
| Contract-billing | simpl-storage | — | pending |
| Contract-billing | stubs | `cross-cutting/samples/contract-billing-stubs` | placed |
| Contract-billing | vc-issuer-service | `security/credential-management/vc-issuance-verification/vc-issuer` | placed |
| Contract-billing | wallet-service | — | pending |
| data1 | Charts | — | pending |
| data1 | common | — | pending |
| data1 | common-adapter | `integration/resource-sharing/resource-sharing-runtime/common/connector-model-common` | placed |
| data1 | common-tier2 | `security/access-control-and-trust/authentication-provider-federation/common/tier2-catalogue-client` | placed |
| data1 | consumer-data1 | `cross-cutting/agents/agent-resource-handling/consumer-resource-handling` | placed |
| data1 | contract-consumption-be | `integration/resource-discovery/search-engine/contract-consumption-adapter` | placed |
| data1 | EDCConnectorAdapter | `integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter` | placed |
| data1 | provider-data1 | `cross-cutting/agents/agent-resource-handling/provider-resource-handling` | placed |
| data1 | schema-sync-adapter | `data/semantics-and-vocabulary/schema-management/schema-sync-adapter` | placed |
| data1 | sd-schemas-util | `data/semantics-and-vocabulary/schema-management/sd-schema-util` | placed |
| data1 | sdtooling-api-be | `data/semantics-and-vocabulary/schema-management/sd-tooling-api` | placed |
| data1 | sdtooling-sd-schemas | `data/semantics-and-vocabulary/schema-management/sdtooling-sd-schemas` | placed |
| data1 | sdtooling-validation-api-be | `governance/resource-management/metadata-description/validation-backend` | placed |
| data1 | sdtooling-validation-api-be | `integration/resource-discovery/search-engine/validation-backend` | placed |
| data1 | simpl-files | `governance/contract-management/contract-establishment/contract-template-datastore` | placed |
| data1 | simpl-mock-services | — | pending |
| data1 | simpl-vue-components | — | pending |
| data1 | xfsc-advsearch-be | `integration/resource-discovery/search-engine/xfsc-advanced-search` | placed |
| data-services | dataframe-level-anonymisation | `data/data-processing/anonymisation-and-pseudonymisation/dataframe-level-anonymisation` | placed |
| data-services | data-processing | `data/data-processing/anonymisation-and-pseudonymisation/data-processing` | placed |
| data-services | field-level-pseudonimysation | `data/data-processing/anonymisation-and-pseudonymisation/field-level-pseudo-anonymisation` | placed |
| data-services | semaphoreui-deployer-service | `data/data-processing/anonymisation-and-pseudonymisation/semaphoreui-deployer-service` | placed |
| data-services | template-code-location | `data/data-processing/anonymisation-and-pseudonymisation/template-code-location` | placed |
| data-services | util-services | `data/data-processing/anonymisation-and-pseudonymisation/util-services` | placed |
| Gaia-X-EDC | authority-gaia-x-edc | `integration/resource-sharing/resource-sharing-runtime/authority-gaiax-edc` | placed |
| Gaia-X-EDC | connector | `integration/resource-sharing/resource-sharing-runtime/gaia-x-connector` | placed |
| Gaia-X-EDC | consumer-gaia-x-edc | `integration/resource-sharing/resource-sharing-runtime/consumer-gaiax-edc` | placed |
| Gaia-X-EDC | edc-extensions | `integration/resource-sharing/resource-sharing-runtime/edc-extensions` | placed |
| Gaia-X-EDC | EDC MinIO s3 | — | pending |
| Gaia-X-EDC | edelivery | `cross-cutting/samples/edelivery` | placed |
| Gaia-X-EDC | PoC-gaia-edc | `integration/resource-discovery/search-engine/query-mapper-adapter` | placed |
| Gaia-X-EDC | provider-gaia-x-edc | `integration/resource-sharing/resource-sharing-runtime/provider-gaia-x-edc` | placed |
| Gaia-X-EDC | simpl-catalogue-client | `integration/resource-discovery/search-engine/catalogue-client-application` | placed |
| Gaia-X-EDC | simpl-contract-negotiation-mockuop | — | pending |
| Gaia-X-EDC | simpl-edc | `integration/resource-sharing/resource-sharing-runtime/connector` | placed |
| Gaia-X-EDC | simpl-fc-service | `integration/resource-discovery/resource-catalogue/xfsc-federated-catalogue` | placed |
| Gaia-X-EDC | simpl-files | — | pending |
| Gaia-X-EDC | simpl-schema-manager | `data/semantics-and-vocabulary/schema-management/simpl-schema-manager` | placed |
| Gaia-X-EDC | simpl-schema-manager-ui | `data/semantics-and-vocabulary/schema-management/simpl-schema-manager-ui` | placed |
| Gaia-X-EDC | simpl-schema-versioning | `data/semantics-and-vocabulary/schema-management/simpl-schema-versioning` | placed |
| Gaia-X-EDC | simpl-sd-ui | `data/semantics-and-vocabulary/schema-management/simpl-sd-ui` | placed |
| Gaia-X-EDC | simpl-signer | — | pending |
| IAA | Agent (sub-group) | see agent-iaa/* rows below | — |
| IAA | agent-iaa/authority-iaa | `cross-cutting/agents/agent-iaa/authority-iaa` | placed |
| IAA | agent-iaa/consumer-iaa | `cross-cutting/agents/agent-iaa/consumer-iaa` | placed |
| IAA | agent-iaa/participant-iaa | `cross-cutting/agents/agent-iaa/participant-iaa` | placed |
| IAA | agent-iaa/provider-iaa | `cross-cutting/agents/agent-iaa/provider-iaa` | placed |
| IAA | agent-iaa/provider-iaa | `security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider` | placed |
| IAA | authentication provider | — | pending |
| IAA | charts | — | pending |
| IAA | cli | — | pending |
| IAA | common | `security/access-control-and-trust/common/iaa-common` | placed |
| IAA | documentation | — | pending |
| IAA | echo backend | — | pending |
| IAA | echo frontend | — | pending |
| IAA | eIDAS demo keycloack extension | — | pending |
| IAA | eIDAS Demo Node deploy | — | pending |
| IAA | ejbca-preconfig | `cross-cutting/samples/ejbca-preconfig` | placed |
| IAA | fe-authentication-provider | `security/access-control-and-trust/authentication-provider-federation/fe-authentication-provider` | placed |
| IAA | fe-identity-provider | `security/access-control-and-trust/identity-provider-federation/fe-identity-provider` | placed |
| IAA | fe-onboarding | `governance/participant-management/onboarding/fe-onboarding` | placed |
| IAA | fe-openapi-clients | — | pending |
| IAA | fe-security-attribute-provider | `security/access-control-and-trust/security-attribute-provider-federation/fe-security-attribute-provider` | placed |
| IAA | fe-users-and-roles | `governance/participant-management/user-roles/fe-users-roles` | placed |
| IAA | Identity provider | `security/access-control-and-trust/identity-provider-federation/identity-provider` | placed |
| IAA | Keycloake authenticator | `security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider` | placed |
| IAA | microfrontend framework | — | pending |
| Infrastructure | infrastructure-application-deployer | `infrastructure/supporting-infrastructure-services/infrastructure-orchestration/application-deployer` | placed |
| Infrastructure | infrastructure-be | `infrastructure/provisioning/infrastructure-provisioning/infrastructure-be` | placed |
| Infrastructure | infrastructure-crossplane | `infrastructure/provisioning/infrastructure-provisioning/infrastructure-crossplane` | placed |
| Infrastructure | infrastructure-crossplane-dependences | `infrastructure/provisioning/infrastructure-provisioning/infrastructure-crossplane-dependences` | placed |
| Infrastructure | infrastructture-edc | `infrastructure/provisioning/infrastructure-provisioning/infrastructure-edc` | placed |
| Infrastructure | infrastructure-fe | `infrastructure/provisioning/infrastructure-provisioning/infrastructure-fe` | placed |
| Infrastructure | infrastructure-provisioner | `infrastructure/provisioning/infrastructure-provisioning/infrastructure-provisioner` | placed |
| Infrastructure | provider-infrastructure | `infrastructure/provisioning/infrastructure-provisioning/provider-infrastructure` | placed |
| Monitoring | authority-monitoring | `cross-cutting/agents/agent-monitoring/authority-monitoring` | placed |
| Monitoring | consumer-monitoring | `cross-cutting/agents/agent-monitoring/consumer-monitoring` | placed |
| Monitoring | eck-monitoring | `administration/observability/performance-monitoring/eck-monitoring` | placed |
| Monitoring | eck-monitoring-operator | — | pending |
| Monitoring | infrastructure-consumption-monitoring-service | `administration/observability/dashboarding/infrastructure-consumption-monitoring-service` | placed |
| Monitoring | monitoring-proxy | — | pending |
| Monitoring | monitoring-reporting-fe | — | pending |
| Monitoring | provider-monitoring | `cross-cutting/agents/agent-monitoring/provider-monitoring` | placed |
| orchestration-platform | asset-orchestrator | — | pending |
| orchestration-platform | dagster | `data/supporting-data-services/data-orchestration/dagster` | placed |
| orchestration-platform | dagster-dev-local | `data/supporting-data-services/data-orchestration/dagster-dev-local` | placed |
| orchestration-platform | data-analytics-visualisation | `data/data-processing/data-visualisation/data-analytic-visualisation` | placed |
| orchestration-platform | gateway-oauth2-client | `data/supporting-data-services/data-orchestration/gateway-oauth2-client` | placed |
| orchestration-platform | gitea | `data/supporting-data-services/data-orchestration/gitea` | placed |
| orchestration-platform | provider-orchestration-platform | — | pending |
