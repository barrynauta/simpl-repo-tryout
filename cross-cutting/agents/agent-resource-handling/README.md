<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Agent resource-handling</strong><br/>
</p>
</div>

# Agent resource-handling

Per-actor-type deployment compositions for the **resource-handling slice** of a Simpl-Open agent — the dataspace participation flow covering contract consumption, EDC connector wiring, schema sync, self-description validation, and federated-catalogue search. Each variant is an umbrella Helm/ArgoCD chart consumed by the master agent Helm chart for that actor.

Same shape as [`agent-iaa/`](../agent-iaa/README.md) and [`agent-contract-billing/`](../agent-contract-billing/README.md): variant-specific deployment compositions consumed by the per-actor master agents.

## Variants

- [consumer-resource-handling](consumer-resource-handling/README.md) — Consumer-side resource-handling composition.
- [provider-resource-handling](provider-resource-handling/README.md) — Provider-side resource-handling composition.

## Bundled services (common to both variants)

| Sub-service in chart | Catalogue location |
|---|---|
| `contract-consumption-be` | [governance/contract-management/contract-establishment/](../../../governance/contract-management/contract-establishment/README.md) |
| `edc-connector-adapter` | [integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/](../../../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md) |
| `schema-sync-adapter` | [data/semantics-and-vocabulary/schema-management/](../../../data/semantics-and-vocabulary/schema-management/README.md) |
| `sd-creation-wizard` (validation) | [governance/resource-management/metadata-description/validation-backend/](../../../governance/resource-management/metadata-description/validation-backend/README.md) |
| `xfsc-advsearch-be` | [integration/resource-discovery/search-engine/xfsc-advanced-search/](../../../integration/resource-discovery/search-engine/xfsc-advanced-search/README.md) |
