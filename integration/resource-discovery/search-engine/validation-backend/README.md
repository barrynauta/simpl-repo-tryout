<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource Discovery</a><br/>
            <a href="../README.md">Service: Search Engine</a><br/>
                <strong>Solution: Validation Backend</strong><br/>
</p>
</div>

# Validation Backend

API service that performs **syntactic and structural validation** of self-descriptions against their schemas before publication to the federated catalogue, and validates the resource-address parameters that identify the source (Provider Agent) and destination (Consumer Agent) sides of a data exchange.

Capability-map placement: `integration / resource-discovery / search-engine / validation-backend`. Sits beside the [Catalogue Client Application](../catalogue-client-application/README.md) and the [Contract Consumption Adapter](../contract-consumption-adapter/README.md) within the same business service.

Provenance: built by Simpl. Java 21 / Maven 3.9+. Source repository: `code.europa.eu/simpl/simpl-open/development/data1/sdtooling-validation-api-be`. Licence: EUPL 1.2.

## Key features

- API endpoints for **syntactic validation** of self-descriptions against the configured schemas.
- Validation of **internal parameters** in the self-description, including the Resource Address fields that identify the shared resource on both source and destination sides.
- **Structured error reporting** with detailed validation outcomes for troubleshooting and audit.
- Modular validation logic: extensible for future schema evolutions or domain-specific rules.

## Deployment topology

Deployed on **both the Provider Agent and the Consumer Agent**.
- **Provider Agent**: invoked by SD-Tooling to validate a self-description before catalogue registration and publication.
- **Consumer Agent**: validates the **Destination Address** in the self-description — the endpoint where a transferred asset will be delivered.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/README.md)
- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/README.md)


## API

[`api/`](api/README.md) — 1 OpenAPI/AsyncAPI spec imported from the source repository (last imported 2026-04-28).

## Source code

- Simpl repo: <https://code.europa.eu/simpl/simpl-open/development/data1/sdtooling-validation-api-be>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
