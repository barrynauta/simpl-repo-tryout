# Repository mapping — catalogue ↔ Simpl-Open development repos

This page maps each *solution folder* in this catalogue to the repository or repositories that implement it on `code.europa.eu/simpl/simpl-open/development`. The mapping is the source of truth used to generate `CANONICAL.md` and `.canonical.yaml` files in each solution folder of `simpl-repo-tryout`.

## Source of truth

- **Catalogue side:** the 18 folders in this repository that contain a `.simpl/manifest.yaml` file (i.e., the documented Simpl-Open solutions).
- **Repository side:** the spreadsheet `Repository_reorganisation_-_mapping_as-is_and_to-be_BN.xlsx`, first tab `Repository mapping AS IS-TO PSO`, columns *Group (Capability)*, *Sub-group-L1 (Business service)*, *Sub-group-L2 (App service)*, *Repository*, and *Mapping to current repository*.

## How to read

- The catalogue uses a `dimension/capability/business-service/solution/` hierarchy. The xlsx uses `capability/business-service/app-service/repository/` — there is no dimension level, and many names differ. The mapping below was reconciled by hand.
- Each catalogue solution maps to **one or more repositories** in the xlsx. When the count is greater than one, all canonical URLs are listed; the solution as a whole has no single URL.
- Where a catalogue solution has *no* xlsx counterpart, it is flagged explicitly. This usually means the solution is documented but not yet developed, or the xlsx and catalogue have not yet agreed on a name.

## Numbers

- xlsx rows (= individual repositories): **79**
- xlsx distinct solutions (capability+bsvc+asvc tuples): **35** (22 rows sit at bsvc level only — libs, samples, utils, external-dependencies)
- xlsx repositories without a canonical URL in column 7: **1** (`policy-template-datastore`, row 52)
- Catalogue solution folders (with `.simpl/manifest.yaml`): **18**
- Catalogue solutions whose path matches an xlsx tuple directly (modulo the catalogue's dimension prefix): **2** (`onboarding-service`, `monitoring-service`)
- Catalogue solutions reconciled by manual rename in this table: **15**
- Catalogue solutions with no xlsx counterpart: **1** (`schema-sync-service`)

## Multi-repo solutions

Of the 18 catalogue solutions, **15 map to more than one xlsx repository** — typically a `*-backend` and `*-frontend` pair, sometimes with adapters or alternative tier implementations. The CANONICAL files generated from this mapping must list all URLs for these solutions; pointing at only one would mis-represent the implementation.

Solutions with multi-repo mapping (counts):
- `data/supporting-data-services/data-orchestration/orchestration-platform` — 4 repos
- `infrastructure/provisioning/infrastructure-provisioning/infrastructure-provisioner` — 4 repos
- `integration/resource-discovery/search-engine/catalogue-client-application` — 4 repos
- `administration/observability/dashboarding/monitoring-service` — 3 repos
- `security/access-control-and-trust/authorisation/authorisation` — 3 repos
- `governance/contract-management/contract-establishment/contract-manager` — 2 repos
- `integration/resource-discovery/resource-catalogue/simpl-catalogue` — 2 repos
- `integration/resource-sharing/resource-sharing-runtime/connector` — 2 repos
- `security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider` — 2 repos
- `security/access-control-and-trust/identity-provider-federation/identity-provider` — 2 repos
- `security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider` — 2 repos

## Mapping table

### `administration/notification-and-messaging/notification/notification-service`

_Sits at bsvc level in xlsx (no asvc). Single repo `notification-service`._

- **xlsx tuple:** `notification-and-messaging` / `notification` (no app-service level)
- **Repositories (1):**
  - `notification-service` → <https://code.europa.eu/simpl/simpl-open/development/contract-billing/notification-service>

### `administration/observability/dashboarding/monitoring-service`

_Direct path match (modulo dimension prefix)._

- **xlsx tuple:** `observability` / `dashboarding` / `monitoring-service`
- **Repositories (3):**
  - `monitoring` → <https://code.europa.eu/simpl/simpl-open/development/monitoring/eck-monitoring>
  - `monitoring-operator` → <https://code.europa.eu/simpl/simpl-open/development/monitoring/eck-monitoring-operator>
  - `infrastructure-consumption-monitoring-service` → <https://code.europa.eu/simpl/simpl-open/development/monitoring/infrastructure-consumption-monitoring-service>

### `data/semantics-and-vocabulary/schema-management/schema-sync-service`

_**No xlsx entry.** Refer to the per-solution canonical files instead._

- **xlsx counterpart:** none.
- **Canonical URL:** none.

### `data/supporting-data-services/data-orchestration/orchestration-platform`

_Solution renamed: catalogue uses `orchestration-platform`, xlsx uses `data-orchestration-service`._

- **xlsx tuple:** `supporting-data-services` / `data-orchestration` / `data-orchestration-service`
- **Repositories (4):**
  - `orchestration-engine` → <https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/dagster>
  - `orchestration-management-frontend` → <Not yet existing>
  - `code-location` → <https://code.europa.eu/simpl/simpl-open/development/data-services>
  - `asset-orchestrator` → <Not yet existing>

### `governance/contract-management/contract-establishment/contract-manager`

_Solution renamed: catalogue uses `contract-manager`, xlsx uses `contract-service`. Note: xlsx has a sibling asvc `contract-template-datastore-service` not represented in catalogue._

- **xlsx tuple:** `contract-management` / `contract-establishment` / `contract-service`
- **Repositories (2):**
  - `contract-manager-backend` → <https://code.europa.eu/simpl/simpl-open/development/contract-billing/contract>
  - `contract-manager-orchestrator` → <https://code.europa.eu/simpl/simpl-open/development/contract-billing/contract>

### `infrastructure/provisioning/infrastructure-provisioning/infrastructure-provisioner`

_Solution renamed: catalogue uses `infrastructure-provisioner`, xlsx uses `infrastructure-provisioning-service`. The catalogue has since restructured infrastructure-provisioning into multiple peer solutions (infrastructure-be, infrastructure-fe, infrastructure-crossplane, infrastructure-provisioner, provider-infrastructure)._

- **xlsx tuple:** `provisioning` / `infrastructure-provisioning` / `infrastructure-provisioning-service`
- **Repositories (4):**
  - `triggering-module` → <https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-be>
  - `infrastructure-provisioner` → <https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-crossplane>

### `integration/resource-discovery/resource-catalogue/simpl-catalogue`

_Solution renamed: catalogue uses `simpl-catalogue`, xlsx uses `catalogue-service`._

- **xlsx tuple:** `resource-discovery` / `resource-catalogue` / `catalogue-service`
- **Repositories (2):**
  - `catalogue` → <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-fc-service>
  - `query-mapper-adapter` → <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/poc-gaia-edc>

### `integration/resource-discovery/search-engine/catalogue-client-application`

_Solution renamed: catalogue uses `catalogue-client-application`, xlsx uses `catalogue-client-service`._

- **xlsx tuple:** `resource-discovery` / `search-engine` / `catalogue-client-service`
- **Repositories (4):**
  - `catalogue-client-application-backend` → <https://code.europa.eu/simpl/simpl-open/development/data1/xfsc-advsearch-be>
  - `catalogue-client-application-frontend` → <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-catalogue-client>
  - `contract-consumption-adapter` → <https://code.europa.eu/simpl/simpl-open/development/data1/contract-consumption-be>
  - `validation-backend` → <https://code.europa.eu/simpl/simpl-open/development/data1/sdtooling-validation-api-be>

### `integration/resource-sharing/resource-sharing-runtime/connector`

_**Capability mismatch.** Catalogue places this under `integration/resource-sharing/`; xlsx places it under `data-sharing/`. Both refer to the same EDC connector implementation._

- **xlsx tuple:** `data-sharing` / `data-sharing-runtime` / `connector-service`
- **Repositories (2):**
  - `connector` → <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-edc>
  - `edc-connector-adapter` → <https://code.europa.eu/simpl/simpl-open/development/data1/edcconnectoradapter>

### `security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider`

_Capability renamed: `access-control-and-trust` → `access-control-trust` (no `and`). Solution renamed: `tier-1-...` → `tier1-...`._

- **xlsx tuple:** `access-control-trust` / `authentication-provider-federation` / `tier1-authentication-service`
- **Repositories (1):**
  - `keycloak-authenticator` → <https://code.europa.eu/simpl/simpl-open/development/iaa/keycloak-authenticator>

### `security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider`

_Capability renamed (no `and`); solution renamed `tier-2-...` → `tier2-...`._

- **xlsx tuple:** `access-control-trust` / `authentication-provider-federation` / `tier2-authentication-service`
- **Repositories (2):**
  - `tier2-authentication-provider-backend` → <https://code.europa.eu/simpl/simpl-open/development/iaa/authentication_provider>
  - `tier2-authentication-provider-frontend` → <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-authentication-provider>

### `security/access-control-and-trust/authorisation/authorisation`

_Capability renamed (no `and`); solution renamed `authorisation` → `authorisation-service`._

- **xlsx tuple:** `access-control-trust` / `authorisation` / `authorisation-service`
- **Repositories (3):**
  - `autorisation-tier-1` → <https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-gateway>
  - `autorisation-tier-2` → <https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-gateway>
  - `tier2-proxy` → <https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-proxy>

### `security/access-control-and-trust/identity-provider-federation/identity-provider`

_Capability renamed (no `and`); solution renamed `identity-provider` → `identity-provider-service`._

- **xlsx tuple:** `access-control-trust` / `identity-provider-federation` / `identity-provider-service`
- **Repositories (2):**
  - `identity-provider-backend` → <https://code.europa.eu/simpl/simpl-open/development/iaa/identity-provider>
  - `identity-provider-frontend` → <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-identity-provider>

### `security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider`

_**Business-service mismatch.** Catalogue has its own bsvc `security-attribute-provider-federation`; xlsx places the same solution under `identity-provider-federation/identity-attributes-service`. Same component._

- **xlsx tuple:** `access-control-trust` / `identity-provider-federation` / `identity-attributes-service`
- **Repositories (2):**
  - `identity-attributes-provider-backend` → <https://code.europa.eu/simpl/simpl-open/development/iaa/security-attributes-provider>
  - `identity-attributes-provider-frontend` → <https://code.europa.eu/simpl/simpl-open/development/iaa/fe-security-attribute-provider>

## What is *not* in this mapping

After reconciliation, **18 xlsx categories remain without a catalogue solution folder** (11 asvc-level, 7 bsvc-level). They are listed here for awareness only — they do not generate `CANONICAL` files because there is nowhere to put them. Several of these correspond to capabilities marked as "Not yet implemented" in the catalogue (signing, wallet, vc-issuance, vocabulary-management); others are cross-cutting groups already documented under `cross-cutting/` (libs, samples, utils, tests) but at a folder layer that doesn't carry `.simpl/manifest.yaml`.

**xlsx solutions (asvc-level) without a catalogue folder:**

- `contract-management/contract-establishment/contract-template-datastore-service` — 2 repo(s)
- `credential-management/signing/signer-service` — 1 repo(s)
- `credential-management/vc-issuance/issuer-service` — 1 repo(s)
- `credential-management/wallet/wallet-service` — 1 repo(s)
- `policy-management/policy-administration-point/policy-template-datastore-service` — 1 repo(s)
- `semantics-vocabulary/vocabulary-management/vocabulary-management-service` — 2 repo(s)
- `sovereign-x-devsecops//contract-billing` — 1 repo(s)
- `sovereign-x-devsecops//data1` — 1 repo(s)
- `sovereign-x-devsecops//iaa` — 2 repo(s)
- `supporting-infrastructure-services/infrastructure-orchestation/infrastructure-connector-service` — 1 repo(s)
- `supporting-services/samples/microfrontend-framework` — 4 repo(s)

**xlsx bsvc-level groupings without a catalogue folder** (cross-cutting / supporting / external):

- `access-control-trust/common` — 2 repo(s): java-common, js-commons
- `external-dependencies` — 3 repo(s): kafka, openbao, postgresql
- `observability/logging` — 1 repo(s): logger
- `supporting-services/libs` — 5 repo(s): simpl-http-client, participant-fe-components
- `supporting-services/samples` — 4 repo(s): sd-schemas, eidas-demo-keycloak-extension, echo-backend, echo-frontend
- `supporting-services/tests` — 2 repo(s): iaa-api-tests, iaa-ui-tests
- `supporting-services/utils` — 3 repo(s): ejbca-preconfig, iaa-cli, sd-schemas-util

## Updating this mapping

- When the xlsx is updated, re-run the analysis script and regenerate this file.
- When a new solution folder is added to the catalogue (i.e., a new `.simpl/manifest.yaml`), add a row to the `MAPPING` table in the analysis script and regenerate.
- The CANONICAL files in `simpl-repo-tryout` are derived from this table — regenerate them only after this table has been updated and reviewed.

_Generated 2026-05-01._