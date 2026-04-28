<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource Sharing</a><br/>
            <a href="../README.md">Service: Resource Sharing Runtime</a><br/>
                <strong>Solution: EDC Connector Adapter</strong><br/>
</p>
</div>

# EDC Connector Adapter

Abstraction layer between the EDC Connector and the upper-layer Simpl-Open components — primarily **SD-Tooling** (asset & policy registration) and **Contract Consumption** (Contract Negotiation and Transfer Process initiation). Decouples the business logic of those modules from the specific EDC implementation, enabling alternative connector technologies to be plugged in later without changing the consumers.

Capability-map placement: `integration / resource-sharing / resource-sharing-runtime / edc-connector-adapter`. This solution sits alongside the [Connector](../connector/README.md) (the EDC fork) within the same business service.

Provenance: built by Simpl. Java/Maven service deployed as an internal component on both the Consumer Agent and the Provider Agent. Source repository: `code.europa.eu/simpl/simpl-open/development/data1/edcconnectoradapter`. Licence: EUPL 1.2.

## Key features

- Unified, connector-agnostic API surface for upper-layer components.
- API methods for asset and policy registration on the EDC Connector, consumed by SD-Tooling.
- API methods for initiating Contract Negotiation and Transfer Process operations, consumed by Contract Consumption.
- Translation/orchestration between Simpl-Open business calls and the EDC protocol endpoints.
- Centralised error handling, logging, and response normalisation.
- Extensibility mechanism for future connector implementations beyond EDC.

## Deployment topology

- **Provider Agent**: mediates between the SD-Tooling component and the EDC Provider Connector — handles asset registration and publication operations.
- **Consumer Agent**: mediates between the Contract Consumption back-end and the EDC Consumer Connector — coordinates negotiation and data-transfer initiation.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/README.md)
- [BP07 Establish usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/README.md)
- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/README.md)


## API

[`api/`](api/README.md) — 2 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `installation-guide/` (1 file), `upgrade-guide/` (1 file).

## Source code

- Simpl repo: <https://code.europa.eu/simpl/simpl-open/development/data1/edcconnectoradapter>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
