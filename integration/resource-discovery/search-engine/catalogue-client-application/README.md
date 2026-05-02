<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource Discovery</a><br/>
            <a href="../README.md">Service: Search Engine</a><br/>
                <strong>Solution: Catalogue Client Application</strong><br/>
</p>
</div>

# Catalogue Client Application

Web application that lets a Consumer **search and browse** the Simpl-Open Federated Catalogue, then drive Contract Negotiation and Transfer Process from a chosen offering. Quick search hits the catalogue directly; advanced search renders a schema-driven form against the active SHACL schema.

Capability-map placement: `integration / resource-discovery / search-engine / catalogue-client-application`. This solution implements the **Search engine** business service.

Provenance: built by Simpl. The catalogue client (Astro + Keycloak) lives at `gaia-x-edc/simpl-catalogue-client`; the advanced-search backend at `data1/xfsc-advsearch-be`. Two adapters — [Contract Consumption Adapter](../contract-consumption-adapter/README.md) and [Validation Backend](../validation-backend/README.md) — are now separate sibling solutions under the same business service. Licence: EUPL 1.2.

## Key features

- **Authentication** with Keycloak via the **Tier-1 Gateway**.
- **Quick search** (free-text against catalogue index).
- **Advanced search** — schema-driven form built dynamically from the active SHACL schema.
- **Contract negotiation kick-off** — once a result is selected, the UI triggers Contract Negotiation via the Contract Consumption Adapter and surfaces transfer status.

## Frontend configuration

Tier-1 gateway base URLs for the dependent services (no trailing slashes):

| Variable | Purpose |
|----------|---------|
| `PUBLIC_AUTH_KEYCLOAK_SERVER_URL` / `_REALM` / `_CLIENT_ID` | Keycloak (Tier 1) |
| `PUBLIC_SEARCH_API_URL` (+ `_API_VERSION`) | xfsc-advsearch-be — advanced-search schemas + quick/advanced search gateways |
| `PUBLIC_CONTRACT_CONSUMPTION_API_URL` (+ `_API_VERSION`) | contract-consumption-be |

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [api/README.md](api/README.md) — API index (two backend APIs).
- [api/advanced-search.openapi.yaml](api/advanced-search.openapi.yaml) — Advanced search backend API specification (stub).
- [api/contract-consumption.openapi.yaml](api/contract-consumption.openapi.yaml) — Contract Consumption Adapter API specification (stub).
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP06 Consumer searches resources](../../../../foundations/business-processes/BP06-consumer-searches-resources/dynamic-view.md)
- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/dynamic-view.md)
- [BP09B Consumer receives a data processing service](../../../../foundations/business-processes/BP09B-consume-data-via-application/dynamic-view.md)


## Documentation (imported from source)

[`documents/`](doc/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `installation-guide/` (1 file), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source code

- Advanced search backend: `code.europa.eu/simpl/simpl-open/development/data1/xfsc-advsearch-be`
- Catalogue client frontend: `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-catalogue-client`
- Contract consumption backend: `code.europa.eu/simpl/simpl-open/development/data1/contract-consumption-be`
- Validation API backend: `code.europa.eu/simpl/simpl-open/development/data1/sdtooling-validation-api-be`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
