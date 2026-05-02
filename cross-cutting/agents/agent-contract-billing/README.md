<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Agent contract-billing</strong><br/>
</p>
</div>

# Agent contract-billing

Per-actor-type deployment compositions for the contract-billing slice of a Simpl-Open agent. Each variant is an umbrella Helm/ArgoCD chart that bundles the contract-billing-related services an actor needs (Contract Manager, Signer, VC Issuer, plus test stubs) and is consumed by the master agent Helm chart for that actor.

Same shape as [`agent-iaa/`](../agent-iaa/README.md): variant-specific deployment compositions consumed by the per-actor master agents.

## Variants

- [consumer-contract-billing](consumer-contract-billing/README.md) — Consumer-side contract-billing composition.
- [provider-contract-billing](provider-contract-billing/README.md) — Provider-side contract-billing composition.

## Bundled services (common to both variants)

| Sub-service in chart | Catalogue location |
|---|---|
| `simpl-contract` | [governance/contract-management/contract-establishment/contract-manager/](../../../governance/contract-management/contract-establishment/contract-manager/README.md) |
| `simpl-signing-service` | [security/credential-management/signing/signer-service/](../../../security/credential-management/signing/signer-service/README.md) |
| `simpl-vc-issuer-service` | [security/credential-management/vc-issuance-verification/vc-issuer/](../../../security/credential-management/vc-issuance-verification/vc-issuer/README.md) |
| `simpl-stubs` | [cross-cutting/samples/contract-billing-stubs/](../../samples/contract-billing-stubs/README.md) |

The two variants differ only in the `nameOverride` of the contract instance (`contract-consumer` vs `contract-dataprovider`) and in their per-environment ArgoCD deployer files.
