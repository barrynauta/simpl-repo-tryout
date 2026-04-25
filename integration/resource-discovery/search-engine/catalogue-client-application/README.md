# Catalogue Client Application

Frontend and backend for searching and browsing the Simpl-Open catalogue. Supports quick search and schema-driven advanced search. Includes a Validation Backend (syntax validation of self-descriptions before publication) and a Contract Consumption Adapter (contract negotiation initiation).

Capability-map placement: `integration / resource-discovery / search-engine / catalogue-client-application`. This solution implements the **Search engine** business service.

Provenance: built by Simpl. Source repositories: `data1/xfsc-advsearch-be` (advanced search backend), `gaia-x-edc/simpl-catalogue-client` (catalogue client frontend), `data1/contract-consumption-be` (contract consumption adapter), `data1/sdtooling-validation-api-be` (validation backend). Licence: EUPL 1.2.

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

## Source code

- Advanced search backend: `code.europa.eu/simpl/simpl-open/development/data1/xfsc-advsearch-be`
- Catalogue client frontend: `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-catalogue-client`
- Contract consumption backend: `code.europa.eu/simpl/simpl-open/development/data1/contract-consumption-be`
- Validation API backend: `code.europa.eu/simpl/simpl-open/development/data1/sdtooling-validation-api-be`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
