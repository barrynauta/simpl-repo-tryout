---
id: svc:infrastructure-provisioning
type: business-service
name: Infrastructure provisioning
dimension: dim:infrastructure
capability: cap:provisioning
since: r3.0
---

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

- [Infrastructure Provisioner](infrastructure-provisioner/README.md) — Triggering Module (script storage, execution, access management) and Infrastructure Provisioner (ArgoCD + Crossplane), interacting via Kafka.
