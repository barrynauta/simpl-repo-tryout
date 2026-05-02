<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Consumer Agent</strong><br/>
</p>
</div>

# Consumer Agent

Master Helm chart that deploys a complete **Consumer** Simpl-Open Agent in a single command. Bundles the modules needed by a Consumer Participant: catalogue client (search), contract consumption back-end, EDC Consumer Connector, Tier 1 / Tier 2 IAA client stack, monitoring, and shared infrastructure (OpenBao, Postgres, Kafka).

Provenance: built by Simpl. Source repository: `agents/consumer`. Owner: Cross-team. Licence: EUPL 1.2.

## Contents (in source)

- **Master chart** — single-command deployment.
- **`app-values/`** — templated values.yaml files for the Integration environment.
- **`documents/deployment-guide/`** — step-by-step deployment via ArgoCD or manual `helm install`, including OpenBao secret setup for EDC, DNS prerequisites, onboarding follow-up steps, and tier2-proxy status checks.

## Modules composed (illustrative, not exhaustive)

- [Catalogue Client Application](../../../integration/resource-discovery/search-engine/catalogue-client-application/README.md)
- [Contract Consumption Adapter](../../../integration/resource-discovery/search-engine/contract-consumption-adapter/README.md)
- [Validation Backend](../../../integration/resource-discovery/search-engine/validation-backend/README.md)
- [Connector (EDC)](../../../integration/resource-sharing/resource-sharing-runtime/connector/README.md)
- [EDC Connector Adapter](../../../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md)
- [Tier 1 Authentication Provider](../../../security/access-control-and-trust/authentication-provider-federation/tier-1-authentication-provider/README.md)
- [Tier 2 Authentication Provider](../../../security/access-control-and-trust/authentication-provider-federation/tier-2-authentication-provider/README.md)
- [Authorisation](../../../security/access-control-and-trust/authorisation/README.md)
- [Monitoring Service](../../../administration/observability/dashboarding/monitoring-service/README.md)
- [Common Components](../common-components/README.md)

## Documentation

- [deployment-guide.md](deployment-guide.md) — full deployment procedure (ArgoCD and manual paths), prerequisites, OpenBao secrets, post-deploy steps, and troubleshooting. Sourced from `agents/consumer/documents/deployment-guide/`.


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `iaa-2.11.x/` (1 file).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/agents/consumer>
