<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource Sharing</a><br/>
            <a href="../README.md">Service: Resource Sharing Runtime</a><br/>
                <strong>Solution: Connector</strong><br/>
</p>
</div>

# Connector

Eclipse EDC-based Dataspace Protocol connector — the **SIMPL EDC**. Registers resources (datasets, applications, infrastructure) as assets in the data space, associates policies and contracts with each asset, and manages contractual relationships between providers and consumers. Implements both the **control plane** (contract negotiation, DSP) and the **data plane** (data transfer). Customised for the European SIMPL programme to secure data exchange between participants.

Capability-map placement: `integration / resource-sharing / resource-sharing-runtime / connector`. This solution implements the **Resource sharing runtime** business service.

Provenance: forked from the upstream **Eclipse Dataspace Connector (EDC)** (Apache 2.0). The Simpl fork lives at `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-edc`. Java 17+, Maven 3.6+. Licence: Apache 2.0 (Eclipse EDC upstream). The Simpl-specific extensions below may carry separate provenance.

## Simpl extensions to upstream EDC

The fork extends the Eclipse EDC framework with:

- **MinIO S3 Extension** — native MinIO S3 support for data transfers (Gaia-X implementation).
- **Infrastructure provisioning capabilities** — bridges to the [Triggering Module](../../../../infrastructure/provisioning/infrastructure-provisioning/triggering-module/README.md) over Kafka.
- **Contract management extensions** — enhanced contract lifecycle hooks integrating with the [Contract Manager](../../../../governance/contract-management/contract-establishment/contract-manager/README.md).
- **Enhanced policy constraints and validation** — additional ODRL constraint types beyond stock EDC.
- **OpenTelemetry integration** for observability — traces and metrics flow into the [Monitoring Service](../../../../administration/observability/dashboarding/monitoring-service/README.md).
- **eDelivery extension** — triggers eDelivery transfer.

## Backing services

- **PostgreSQL** — connector state and policies.
- **HashiCorp Vault** — secrets and credentials.
- **MinIO S3** — primary object storage for transfers.

## Companion solution

The [EDC Connector Adapter](../edc-connector-adapter/README.md) is the abstraction layer above this connector — SD-Tooling and Contract Consumption services call the adapter rather than the EDC API directly so a future replacement of EDC stays transparent to those services.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [api/README.md](api/README.md) — API index (three APIs).
- [api/management.openapi.yaml](api/management.openapi.yaml) — Management API specification (stub).
- [api/control-plane.openapi.yaml](api/control-plane.openapi.yaml) — Dataspace Protocol (DSP) API specification (stub).
- [api/data-plane.openapi.yaml](api/data-plane.openapi.yaml) — Data Plane API specification (stub).
- [LICENSE](LICENSE) — Apache 2.0 (Eclipse EDC upstream).

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
- [BP07 Consumer and Provider establish a usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/dynamic-view.md)
- [BP08 Consumer consumes an infrastructure resource](../../../../foundations/business-processes/BP08-consume-infrastructure-resource/dynamic-view.md)
- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/dynamic-view.md)
- [BP09B Consumer receives a data processing service](../../../../foundations/business-processes/BP09B-consume-data-via-application/dynamic-view.md)

## Source code

- Simpl fork: `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-edc`
- Upstream Eclipse EDC: `https://github.com/eclipse-edc/Connector`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
