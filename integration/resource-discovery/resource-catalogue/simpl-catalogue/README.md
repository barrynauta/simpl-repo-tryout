<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource Discovery</a><br/>
            <a href="../README.md">Service: Resource Catalogue</a><br/>
                <strong>Solution: Simpl Catalogue</strong><br/>
</p>
</div>

# Simpl Catalogue

Central publication point on the Governance Authority for signed self-descriptions of data, application and infrastructure offerings. The Catalogue supports both quick and advanced (schema-driven) search, enforces policy-aware filtering at query time, and validates self-descriptions for syntax, semantics and quality before storage.

Capability-map placement: `integration / resource-discovery / resource-catalogue / simpl-catalogue`. This solution implements the **Resource catalogue** business service and contributes to the **Search engine** business service under the same capability.

Provenance: forked from the upstream **XFSC Federated Catalogue** (Eclipse project, Apache 2.0). The Simpl fork lives at `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-fc-service`. LICENSE in this folder mirrors the upstream Apache 2.0 licence; it is not EUPL.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document (business, data, application, technical, security, testing).
- [doc/api.md](doc/api.md) — GAIA-X Federated Catalogue REST API endpoints, callers, and upstream OpenAPI link.
- [LICENSE](LICENSE) — Apache 2.0 (upstream XFSC licence).

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
- [BP06 Consumer searches resources](../../../../foundations/business-processes/BP06-consumer-searches-resources/dynamic-view.md)
- [BP09A Consumer consumes a data resource](../../../../foundations/business-processes/BP09A-consume-data-resource/dynamic-view.md)
- [BP09B Consumer receives a data processing service](../../../../foundations/business-processes/BP09B-consume-data-via-application/dynamic-view.md)


## API

[`api/`](api/README.md) — 2 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).

## Source code

- Simpl fork: <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-fc-service>
- Upstream: <https://gitlab.eclipse.org/eclipse/xfsc/cat>

## Roadmap

Roadmap items for the Catalogue live in the Simpl Notion "Roadmap items overview" page. Per repository rules, roadmap is not duplicated per-service — see the link in `references.md` once step 7 populates it.
