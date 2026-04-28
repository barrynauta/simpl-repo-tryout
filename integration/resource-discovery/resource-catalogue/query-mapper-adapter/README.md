<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource Discovery</a><br/>
            <a href="../README.md">Service: Resource Catalogue</a><br/>
                <strong>Solution: Query Mapper Adapter</strong><br/>
</p>
</div>

# Query Mapper Adapter

Backend that **maps queries from the Gaia-X EDC** ecosystem into the Simpl-Open Federated Catalogue. Acts as a bridge between EDC-side discovery requests and the GAIA-X Federated Catalogue's query API, registering service offerings for downstream search.

Capability-map placement: `integration / resource-discovery / resource-catalogue / query-mapper-adapter`. Sits beside the [Simpl Catalogue](../simpl-catalogue/README.md) within the same business service.

Provenance: built by Simpl. Java 21 / Maven 3.6+. Source repository: `gaia-x-edc/poc-gaia-edc`. Owner: Catalogue & Connector team. Licence: EUPL 1.2.

## Key features

- Query translation between EDC asset queries and the [Simpl Catalogue](../simpl-catalogue/README.md) API.
- Service-offering registration on the federated catalogue for future searchability.
- Standalone Spring Boot service deployable on Provider/Consumer agents that need EDC ↔ FC bridging.

## Dependencies

- **Federated Catalogue** — `gaia-x-edc/simpl-fc-service` (the [Simpl Catalogue](../simpl-catalogue/README.md)) — the registration and query target.

## Participates in

- [BP06 Consumer searches resources](../../../../foundations/business-processes/BP06-consumer-searches-resources/README.md)


## API

[`api/`](api/README.md) — 1 OpenAPI/AsyncAPI spec imported from the source repository (last imported 2026-04-28).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/poc-gaia-edc>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
