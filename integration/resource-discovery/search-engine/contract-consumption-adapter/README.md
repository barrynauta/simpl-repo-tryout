<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource Discovery</a><br/>
            <a href="../README.md">Service: Search Engine</a><br/>
                <strong>Solution: Contract Consumption Adapter</strong><br/>
</p>
</div>

# Contract Consumption Adapter

Backend service exposed by the Consumer Agent that lets the catalogue-client frontend initiate Contract Negotiation and Transfer Process workflows from a chosen catalogue entry, and monitor their progress in real time.

Capability-map placement: `integration / resource-discovery / search-engine / contract-consumption-adapter`. Sits beside the [Catalogue Client Application](../catalogue-client-application/README.md) within the same business service.

Provenance: built by Simpl. Java 21 / Maven 3.9+. Source repository: `code.europa.eu/simpl/simpl-open/development/data1/contract-consumption-be`. Licence: EUPL 1.2.

## Key features

- API endpoints to **initiate** and **manage** Contract Negotiation and data Transfer Process workflows.
- Status and **monitoring** APIs to retrieve real-time state of ongoing negotiations and transfers.
- Integration with the **EDC Consumer Connector** (deployed in the same agent) for the technical negotiation/transfer execution.
- Process tracking and auditability — full lifecycle visibility under SIMPL governance.
- Secure access control: only authorised frontend clients or services may initiate or query contractual operations.
- Exposed externally through the **Tier-1 Gateway**.

## Deployment topology

Deployed within the **Consumer Agent**. Calls into the EDC Consumer Connector (same agent) and is consumed by the catalogue-client frontend through the Tier-1 Gateway.

## Participates in

- [BP07 Establish usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/README.md)
- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/README.md)

## Source code

- Simpl repo: <https://code.europa.eu/simpl/simpl-open/development/data1/contract-consumption-be>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
