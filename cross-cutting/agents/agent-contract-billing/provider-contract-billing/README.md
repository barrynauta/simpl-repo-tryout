<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Cross-Cutting</a><br/>
        <a href="../../README.md">Agents</a><br/>
            <a href="../README.md">Agent contract-billing</a><br/>
                <strong>provider-contract-billing</strong><br/>
</p>
</div>

# provider-contract-billing

Provider (data flavour by default; reused across application/infrastructure)-side deployment composition (umbrella Helm/ArgoCD chart) for the contract-billing slice of a Simpl-Open agent. Bundles the contract-billing services the Provider (data flavour by default; reused across application/infrastructure) role needs and is consumed by the [provider (data flavour by default; reused across application/infrastructure)-agent](../../provider (data flavour by default; reused across application/infrastructure)-agent/README.md) master chart.

The contract instance is deployed under `nameOverride: contract-dataprovider` to distinguish it from the counterpart variant.

## Bundled services

- `simpl-contract` → [Contract Manager](../../../../governance/contract-management/contract-establishment/contract-manager/README.md)
- `simpl-signing-service` → [Signer Service](../../../../security/credential-management/signing/signer-service/README.md)
- `simpl-vc-issuer-service` → [VC Issuer](../../../../security/credential-management/vc-issuance-verification/vc-issuer/README.md)
- `simpl-stubs` → [contract-billing-stubs](../../../samples/contract-billing-stubs/README.md)

## ArgoCD environments

The repo ships ArgoCD deployer manifests for four environments: `dev-sandbox-ionos`, `integrated`, `sandbox-cat-dat`, `sandbox-iaa`.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
