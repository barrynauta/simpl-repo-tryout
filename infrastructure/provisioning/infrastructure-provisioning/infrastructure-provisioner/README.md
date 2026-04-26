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

Manages, validates, and executes Crossplane/OpenTofu deployment scripts to provision compute, storage, and network resources for data space consumers. Comprises a Triggering Module (script management, execution, access sharing) and an Infrastructure Provisioner (ArgoCD + Crossplane). Interactions are asynchronous via Kafka.

Capability-map placement: `infrastructure / provisioning / infrastructure-provisioning / infrastructure-provisioner`. This solution implements the **Infrastructure provisioning** business service.

Provenance: built by Simpl. Source repositories: `infrastructure/infrastructure-crossplane` (primary) and `infrastructure/infrastructure-be` (planned split per Notion). Licence: EUPL 1.2.

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
