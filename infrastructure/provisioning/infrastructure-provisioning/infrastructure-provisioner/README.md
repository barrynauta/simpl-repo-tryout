<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Infrastructure</a><br/>
        <a href="../../README.md">Capability: Provisioning</a><br/>
            <a href="../README.md">Service: Infrastructure Provisioning</a><br/>
                <strong>Solution: Infrastructure Provisioner</strong><br/>
</p>
</div>

# Infrastructure Provisioner

Executes Crossplane / OpenTofu / Terraform deployment scripts to provision compute, storage, and network resources for data-space consumers. Receives provisioning jobs over Kafka from the [Triggering Module](../triggering-module/README.md) and applies them through ArgoCD + Crossplane on the target Kubernetes cluster.

Capability-map placement: `infrastructure / provisioning / infrastructure-provisioning / infrastructure-provisioner`. Sits alongside the [Triggering Module](../triggering-module/README.md) and the [Deployment Script & Template Management](../deployment-script-and-template-management/README.md) solutions within the same business service.

Provenance: built by Simpl. Source repository: `infrastructure/infrastructure-crossplane`. Licence: EUPL 1.2.

Note: the consolidated `infrastructure/infrastructure-be` repository (referenced in earlier mapping versions) covers the **Triggering Module** and **Deployment Script & Template Management** roles, not the executor — that lives in `infrastructure-crossplane`. The PSO mapping flags `infrastructure-be` as a single Java project to be split into 2.

## Key features

- Consumes provisioning jobs from Kafka (produced by the Triggering Module).
- Applies Crossplane manifests via ArgoCD on the target cluster, with rollout progress reported back over Kafka.
- Supports OpenTofu and Terraform script formats alongside Crossplane primitives.
- Reports provisioning success/failure events back to the Triggering Module for state reconciliation.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP08 Consumer consumes an infrastructure resource](../../../../foundations/business-processes/BP08-consume-infrastructure-resource/dynamic-view.md)
- [BP09B Consumer receives a data processing service](../../../../foundations/business-processes/BP09B-consume-data-via-application/dynamic-view.md)

## Source code

- `code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-crossplane`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
