<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Infrastructure</a><br/>
        <a href="../../README.md">Capability: Provisioning</a><br/>
            <a href="../README.md">Service: Infrastructure provisioning</a><br/>
                <strong>Solution: infrastructure-be</strong><br/>
</p>
</div>

# infrastructure-be

Backend service for the infrastructure provisioning capability. Currently consolidates several logical components (the Triggering Module and supporting back-end logic) in a single Java project; per the PSO mapping spreadsheet this repo is flagged as *"Single java project to be split in 2"* once a future split lands — at which point a separate `triggering-module` repository will exist alongside this one.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Components currently bundled

### Triggering Module

Receives infrastructure-provisioning requests originating from the EDC Connector triggering extension and dispatches them — over Kafka — to the [Infrastructure Provisioner](../infrastructure-provisioner/README.md) for execution. Manages lifecycle state for in-flight provisioning requests and surfaces status back to the requesting agent.

**Key features:**

- Listens to provisioning trigger events from the EDC Connector Triggering Extension.
- Validates the request against the consumer's contract and policy decisions.
- Dispatches the resolved provisioning job to the Infrastructure Provisioner via Kafka.
- Tracks per-request lifecycle state in PostgreSQL.
- Reads secrets/credentials from HashiCorp Vault using the `infrastructure-be` secret path.

## Participates in

- [BP08 Consumer consumes an infrastructure resource](../../../../foundations/business-processes/BP08-consume-infrastructure-resource/README.md)

## Architecture

- [doc/architecture.md](doc/architecture.md) — six-view architecture document (originally authored for the Triggering Module; covers the back-end as a whole until the planned split).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-be>
- After the planned split: `infrastructure/triggering-module` will be a separate repository.

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
