<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Integration</a><br/>
        <a href="../README.md">Capability: Resource Discovery</a><br/>
            <strong>Service: Search Engine</strong><br/>
</p>
</div>

# Search engine

Consumer and provider-side search interface for discovering resources in the Catalogue. Supports quick search and advanced search using schema-defined fields, with policy-filtered query forwarding to the Catalogue.

## Solutions

- [Catalogue Client Application](catalogue-client-application/README.md) — search frontend and backend (Java + Angular) covering quick and advanced search.
- [Contract Consumption Adapter](contract-consumption-adapter/README.md) — Consumer-side backend that initiates and tracks Contract Negotiation and Transfer Process workflows from the catalogue UI.
- [Validation Backend](validation-backend/README.md) — syntactic validation of self-descriptions and resource-address parameters before catalogue publication and during data-exchange setup.
- [Query Mapper Adapter](query-mapper-adapter/README.md) — bridges Gaia-X EDC asset queries into the Simpl Federated Catalogue and registers service offerings for downstream search.
- [xfsc-advanced-search](xfsc-advanced-search/README.md) — REST microservice for keyword and advanced search over federated-catalogue self-descriptions; deployed on both Consumer and Provider agents.

The EDC abstraction used by these clients lives at [`integration/resource-sharing/resource-sharing-runtime/edc-connector-adapter/`](../../resource-sharing/resource-sharing-runtime/edc-connector-adapter/README.md).
