<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Infrastructure</a><br/>
        <a href="../../README.md">Capability: Provisioning</a><br/>
            <a href="../README.md">Service: Infrastructure Provisioning</a><br/>
                <strong>Solution: Triggering Module</strong><br/>
</p>
</div>

# Triggering Module

Receives infrastructure-provisioning requests originating from the EDC Connector triggering extension and dispatches them — over Kafka — to the [Infrastructure Provisioner](../infrastructure-provisioner/README.md) for execution. Manages lifecycle state for in-flight provisioning requests and surfaces status back to the requesting agent.

Capability-map placement: `infrastructure / provisioning / infrastructure-provisioning / triggering-module`. Sits alongside the [Deployment Script & Template Management](../deployment-script-and-template-management/README.md) solution and the [Infrastructure Provisioner](../infrastructure-provisioner/README.md) under the same business service.

Provenance: built by Simpl. Currently part of the consolidated `infrastructure/infrastructure-be` repo; the PSO mapping spreadsheet flags this as **"Single java project to be split in 2"** (one sprint of work, parallelisable with feature development) — once the source split lands, the Triggering Module will become a standalone repository at `infrastructure/triggering-module`. Licence: EUPL 1.2.

## Key features

- Listens to provisioning trigger events from the EDC Connector Triggering Extension.
- Validates the request against the consumer's contract and policy decisions.
- Dispatches the resolved provisioning job to the Infrastructure Provisioner via Kafka.
- Tracks per-request lifecycle state in PostgreSQL.
- Reads secrets/credentials from HashiCorp Vault using the `infrastructure-be` secret path.

## Participates in

- [BP08 Consumer consumes an infrastructure resource](../../../../foundations/business-processes/BP08-consume-infrastructure-resource/README.md)

## Source code

- Currently consolidated in: <https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-be>
- After the planned split: `code.europa.eu/simpl/simpl-open/development/infrastructure/triggering-module` (not yet existing)

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
