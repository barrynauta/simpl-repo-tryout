<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Semantics And Vocabulary</a><br/>
            <a href="../README.md">Service: Schema Management</a><br/>
                <strong>Solution: Schema Management Service</strong><br/>
</p>
</div>

# Schema Management Service

The authoritative source of truth and lifecycle manager for all schemas and vocabularies within the Simpl-Open data space. Enables the Governance Authority to define, version, publish, and revoke the structure of self-descriptions for datasets, applications, and infrastructure resources. Exposes a Management API, a public Resolver Interface, and an event publisher that notifies downstream services of schema lifecycle changes.

Capability-map placement: `data / semantics-and-vocabulary / schema-management / schema-management-service`. This solution implements the **Schema management** business service.

Provenance: built by Simpl. Source repositories: `gaia-x-edc/simpl-schema-manager` (backend) + `gaia-x-edc/simpl-schema-manager-ui` (frontend). Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [api/](api/README.md) — API specifications.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP02 Manage Resource Description Schemas](../../../../foundations/business-processes/BP02-configuration-governance-authority/dynamic-view.md)
- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
- [BP06 Consumer searches resources](../../../../foundations/business-processes/BP06-consumer-searches-resources/dynamic-view.md)

## Source code

- `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-schema-manager`
- `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-schema-manager-ui`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
