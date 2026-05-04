<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Data Provider Agent</strong><br/>
</p>
</div>

# Data Provider Agent

Master Helm chart that deploys a complete **Data Provider** Simpl-Open Agent. Bundles the modules a Provider needs to publish and share data resources: SD-Tooling, EDC Provider Connector, the Asset Orchestrator + Orchestration Platform, the Tier 1 / Tier 2 IAA client stack, monitoring, and shared infrastructure.

Provenance: built by Simpl. Source repository: `agents/data-provider`. Owner: Cross-team. Licence: EUPL 1.2.

## Contents (in source)

- **Master chart** — single-command deployment for a Provider node.
- **`app-values/`** — templated values.yaml files for the Integration environment.
- **`documents/deployment-guide/`** — deployment instructions analogous to the Consumer Agent, with Provider-specific OpenBao secrets and asset-orchestration wiring.

## Modules composed (illustrative)

- [SD-Tooling](../../../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md)
- [Connector (EDC)](../../../integration/resource-sharing/resource-sharing-runtime/connector/README.md)
- [EDC Connector Adapter](../../../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md)
- [Asset Orchestrator](../../../data/supporting-data-services/data-orchestration/asset-orchestrator/README.md)
- [Orchestration Platform](../../../data/supporting-data-services/data-orchestration/orchestration-platform/README.md)
- [Anonymisation and Pseudonymisation](../../../data/data-processing/anonymisation-and-pseudonymisation/README.md) (optional Dagster code-locations)
- [Validation Backend](../../../integration/resource-discovery/search-engine/validation-backend/README.md)
- IAA client stack and shared infrastructure (see [common-components](../common-components/README.md)).

## Documentation

- [deployment-guide.md](deployment-guide.md) — full deployment procedure (ArgoCD and manual paths), prerequisites, OpenBao secrets including Gitea token bootstrap, MinIO secrets for the EDC connector, post-deploy steps, troubleshooting, and a SuperAdmin / ManagementCA cert FAQ. Sourced from `agents/data-provider/documents/deployment-guide/`.


## Documentation (imported from source)

[`doc/`](doc/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `iaa-2.11.x/` (1 file).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/agents/data-provider>
