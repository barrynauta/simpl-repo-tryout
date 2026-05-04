<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>Agent composition</strong><br/>
</p>
</div>

# Agent composition

A Simpl-Open **agent** is the deployment unit a participant runs. Each agent is a Helm umbrella that bundles a curated subset of solutions from the capability tree — depending on the participant's role (Consumer, Data Provider, Application Provider, Infrastructure Provider, Governance Authority).

This page collects the per-agent module inventories that are otherwise scattered across the agent READMEs into one cross-cutting view, and shows the layered structure: **role-based top-level agents** ↔ **per-theme sub-agents** (IAA, contract-billing, monitoring, resource-handling, orchestration-platform).

## High-level shape

```
┌───────────────────────────────────────────────────────────────────────────────┐
│  Top-level role-based agents (cross-cutting/agents/<role>-agent/)             │
│  consumer · data-provider · application-provider · infra-provider · authority │
└───────────────────────────────────────────────────────────────────────────────┘
        │ each role-agent bundles per-theme sub-agents + capability solutions
        ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│  Per-theme sub-agents (Helm umbrellas, one per actor variant)                  │
│  agent-iaa/{authority,consumer,participant,provider}-iaa                       │
│  agent-contract-billing/{consumer,provider}-contract-billing                   │
│  agent-monitoring/{authority,consumer,provider}-monitoring                     │
│  agent-resource-handling/{consumer,provider}-resource-handling                 │
└────────────────────────────────────────────────────────────────────────────────┘
        │ each sub-agent deploys solutions from one capability area
        ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│  Solutions (the dimension/capability/business-service/solution leaves)         │
│  e.g. tier-1-authentication-provider, contract-manager, simpl-catalogue, …     │
└────────────────────────────────────────────────────────────────────────────────┘

Plus the shared-infrastructure bundle:
┌────────────────────────────────────────────────────────────────────────────────┐
│  cross-cutting/agents/common-components/                                       │
│  Kafka · OpenBao/Vault · PostgreSQL  — required by every role-agent            │
└────────────────────────────────────────────────────────────────────────────────┘
```

## Role-based agents — modules bundled

Each role-based agent README lists the solutions it composes. The module lists below are extracted from those READMEs; treat them as illustrative — the source of truth is each agent's `Modules composed` section.

### Consumer Agent

Source: [`cross-cutting/agents/consumer-agent/`](../cross-cutting/agents/consumer-agent/README.md)

| Module | Catalogue path |
|---|---|
| Catalogue Client Application | [integration/.../catalogue-client-application](../integration/resource-discovery/search-engine/catalogue-client-application/README.md) |
| Contract Consumption Adapter | [integration/.../contract-consumption-adapter](../integration/resource-discovery/search-engine/contract-consumption-adapter/README.md) |
| Validation Backend | [integration/.../validation-backend](../integration/resource-discovery/search-engine/validation-backend/README.md) |
| Connector (EDC) | [integration/.../connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) |
| EDC Connector Adapter | [integration/.../edc-connector-adapter](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md) |
| Tier 1 Authentication Provider | [security/.../tier-1-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md) |
| Tier 2 Authentication Provider | [security/.../tier-2-authentication-provider](../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md) |
| Authorisation | [security/.../authorisation](../security/access-control-and-trust/authorisation/README.md) |
| Monitoring Service | [administration/.../monitoring-service](../administration/observability/dashboarding/monitoring-service/README.md) |
| Common Components (Kafka + OpenBao + Postgres) | [cross-cutting/agents/common-components](../cross-cutting/agents/common-components/README.md) |

### Data Provider Agent

Source: [`cross-cutting/agents/data-provider-agent/`](../cross-cutting/agents/data-provider-agent/README.md)

| Module | Catalogue path |
|---|---|
| SD-Tooling | [data/.../sd-tooling-api](../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md) |
| Connector (EDC) | [integration/.../connector](../integration/resource-sharing/resource-sharing-runtime/connector/README.md) |
| EDC Connector Adapter | [integration/.../edc-connector-adapter](../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md) |
| Asset Orchestrator | [data/.../asset-orchestrator](../data/supporting-data-services/data-orchestration/asset-orchestrator/README.md) |
| Orchestration Platform | [data/.../orchestration-platform](../data/supporting-data-services/data-orchestration/orchestration-platform/README.md) |
| Anonymisation & Pseudonymisation (optional Dagster code-locations) | [data/.../anonymisation-and-pseudonymisation](../data/data-processing/anonymisation-and-pseudonymisation/README.md) |
| Validation Backend | [integration/.../validation-backend](../integration/resource-discovery/search-engine/validation-backend/README.md) |
| IAA client stack | (via [agent-iaa/provider-iaa](../cross-cutting/agents/agent-iaa/provider-iaa/README.md)) |
| Common Components | [cross-cutting/agents/common-components](../cross-cutting/agents/common-components/README.md) |

### Governance Authority Agent

Source: [`cross-cutting/agents/governance-authority-agent/`](../cross-cutting/agents/governance-authority-agent/README.md)

| Module | Catalogue path |
|---|---|
| Onboarding (FE) | [governance/.../fe-onboarding](../governance/participant-management/onboarding/fe-onboarding/README.md) |
| Users & Roles (FE) | [governance/.../fe-users-roles](../governance/participant-management/user-roles/fe-users-roles/README.md) |
| Identity Provider | [security/.../identity-provider](../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) |
| Security Attributes Provider | [security/.../security-attributes-provider](../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md) |
| Authorisation | [security/.../authorisation](../security/access-control-and-trust/authorisation/README.md) |
| Simpl Catalogue (XFSC FC) | [integration/.../simpl-catalogue](../integration/resource-discovery/resource-catalogue/simpl-catalogue/README.md) |
| Schema Management Service | [data/.../simpl-schema-manager](../data/semantics-and-vocabulary/schema-management/simpl-schema-manager/README.md) |
| Signer Service | [security/.../signer-service](../security/credential-management/signing/signer-service/README.md) |
| Monitoring Service | [administration/.../monitoring-service](../administration/observability/dashboarding/monitoring-service/README.md) |
| EJBCA Preconfig (init-container) | [cross-cutting/samples/ejbca-preconfig](../cross-cutting/samples/ejbca-preconfig/README.md) |
| Common Components | [cross-cutting/agents/common-components](../cross-cutting/agents/common-components/README.md) |

### Application Provider Agent

Source: [`cross-cutting/agents/application-provider-agent/`](../cross-cutting/agents/application-provider-agent/README.md)

> **Composition not yet documented** — the agent README is a placeholder. The expected modules mirror the Data Provider Agent minus data-orchestration-specific bits, plus the application-sharing solutions. Tracked in the Notion FTA-migration audit.

### Infrastructure Provider Agent

Source: [`cross-cutting/agents/infrastructure-provider-agent/`](../cross-cutting/agents/infrastructure-provider-agent/README.md)

> **Composition not yet documented** — the agent README is a placeholder. Expected modules: the infrastructure-provisioning solutions (infrastructure-be, infrastructure-fe, infrastructure-crossplane, infrastructure-provisioner, provider-infrastructure) plus IAA client stack and Common Components. Tracked in the Notion FTA-migration audit.

## Per-theme sub-agents (Helm umbrellas)

These sit under the role-based agents and bundle the solutions for one capability area for one actor variant.

| Sub-agent group | Actor variants | Catalogue path |
|---|---|---|
| **agent-iaa** — IAA client stack per actor (incl. Tier 2 enforcement) | authority-iaa, consumer-iaa, participant-iaa, provider-iaa | [cross-cutting/agents/agent-iaa/](../cross-cutting/agents/agent-iaa/) |
| **agent-contract-billing** — contract-billing client stack | consumer-contract-billing, provider-contract-billing | [cross-cutting/agents/agent-contract-billing/](../cross-cutting/agents/agent-contract-billing/) |
| **agent-monitoring** — monitoring client stack | authority-monitoring, consumer-monitoring, provider-monitoring | [cross-cutting/agents/agent-monitoring/](../cross-cutting/agents/agent-monitoring/) |
| **agent-resource-handling** — resource-handling client stack | consumer-resource-handling, provider-resource-handling | [cross-cutting/agents/agent-resource-handling/](../cross-cutting/agents/agent-resource-handling/) |

## Common-components bundle

Every role-based agent depends on the [common-components](../cross-cutting/agents/common-components/README.md) Helm bundle, which provides:

- **Kafka** — message broker for async coordination ([administration/.../kafka](../administration/notification-and-messaging/messaging/kafka/README.md))
- **OpenBao** / **Vault** — secrets store ([security/.../openbao](../security/access-control-and-trust/encryption/openbao/README.md), [security/.../vault](../security/access-control-and-trust/encryption/vault/README.md))
- **PostgreSQL cluster** — pervasive persistence ([data/.../postgres-cluster](../data/supporting-data-services/common/postgres-cluster/README.md))

## How this view is maintained

This page is derived from the `## Modules composed` section in each role-based agent's README. When an agent's composition changes, update the agent README first; this page is the rollup. Agents whose READMEs lack a Modules-composed section are flagged inline above and tracked as TODOs in the Notion FTA-migration audit.

## Cross-references

- [Capability map](capability-map.md) — the dimension/capability/service tree that solutions sit on.
- [Deployment model](deployment-model.md) — how agents and clusters are arranged.
- [Shared libraries inventory](shared-libraries.md) — the `*-common` libraries consumed across agents and dimensions.
