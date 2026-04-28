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

- [Triggering Module](triggering-module/README.md) — receives provisioning requests from the EDC Connector triggering extension and dispatches jobs to the Infrastructure Provisioner over Kafka.
- [Deployment Script & Template Management](deployment-script-and-template-management/README.md) — backend + frontend for authoring, storing, and versioning deployment scripts (Crossplane / OpenTofu / Terraform) in a Gitea-backed repository.
- [Infrastructure Provisioner](infrastructure-provisioner/README.md) — Crossplane/ArgoCD-based executor that applies deployment scripts on the target Kubernetes cluster.
