<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Cross-Cutting</a><br/>
        <a href="../../README.md">Agents</a><br/>
            <a href="../README.md">Agent resource-handling</a><br/>
                <strong>provider-resource-handling</strong><br/>
</p>
</div>

# provider-resource-handling

Provider (data flavour)-side deployment composition (umbrella Helm/ArgoCD chart) for the resource-handling slice of a Simpl-Open agent. Consumed by the [provider (data flavour)-agent](../../provider (data flavour)-agent/README.md) master chart.

## Bundled services

- `contract-consumption-be` → contract-consumption backend
- `edc-connector-adapter` → [edc-connector-adapter](../../../../integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md)
- `schema-sync-adapter` → schema-sync adapter
- `sd-creation-wizard` (deployed as `sd-validation`) → [validation-backend](../../../../governance/resource-management/metadata-description/validation-backend/README.md)
- `xfsc-advsearch-be` → [xfsc-advanced-search](../../../../integration/resource-discovery/search-engine/xfsc-advanced-search/README.md)

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
