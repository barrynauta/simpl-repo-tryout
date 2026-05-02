<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Infrastructure</a><br/>
        <a href="../README.md">Capability: Provisioning</a><br/>
            <strong>Service: Infrastructure Provisioning</strong><br/>
</p>
</div>

# Infrastructure provisioning

Deployment script management and execution, asynchronous provisioning of infrastructure resources via ArgoCD and Crossplane, and access data sharing with consumers.

## Solutions

- [Infrastructure BE](infrastructure-be/README.md) — backend service (currently bundles the Triggering Module logic; planned to split).
- [Infrastructure FE](infrastructure-fe/README.md) — frontend UI for the infrastructure provisioning capability.
- [Infrastructure Crossplane](infrastructure-crossplane/README.md) — Crossplane configuration / packages used by Simpl to declaratively provision cloud resources.
- [Infrastructure Crossplane Dependences](infrastructure-crossplane-dependences/README.md) — Crossplane provider dependencies bundled with the Simpl Crossplane configuration.
- [Infrastructure EDC](infrastructure-edc/README.md) — EDC integration component on the infrastructure provisioning side.
- [Infrastructure Provisioner](infrastructure-provisioner/README.md) — Simpl-Open infrastructure provisioner (Crossplane-driven).
- [Provider Infrastructure](provider-infrastructure/README.md) — provider-side infrastructure component.

