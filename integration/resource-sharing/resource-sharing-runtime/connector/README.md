# Connector

Eclipse EDC-based Dataspace Protocol connector. Registers resources (datasets, applications, infrastructure) as assets in the data space, associates policies and contracts with each asset, and manages contractual relationships between providers and consumers. Implements both the control plane (contract negotiation) and the data plane (data transfer). Also includes extensions for infrastructure triggering and S3 object storage transfer.

Capability-map placement: `integration / resource-sharing / resource-sharing-runtime / connector`. This solution implements the **Resource sharing runtime** business service.

Provenance: forked from the upstream **Eclipse Dataspace Connector (EDC)** (Apache 2.0). The Simpl fork lives at `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-edc`. Licence: Apache 2.0 (Eclipse EDC upstream). See licence notes — the Simpl-specific extensions (Triggering Extension, S3 Extension, Asset Orchestrator) may carry separate provenance.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [api/README.md](api/README.md) — API index (three APIs).
- [api/management.openapi.yaml](api/management.openapi.yaml) — Management API specification (stub).
- [api/control-plane.openapi.yaml](api/control-plane.openapi.yaml) — Dataspace Protocol (DSP) API specification (stub).
- [api/data-plane.openapi.yaml](api/data-plane.openapi.yaml) — Data Plane API specification (stub).
- [LICENSE](LICENSE) — Apache 2.0 (Eclipse EDC upstream).

## Source code

- Simpl fork: `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-edc`
- Upstream Eclipse EDC: `https://github.com/eclipse-edc/Connector`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
