---
id: simpl:schema-synch-service
type: solution
name: Schema Synch Service
owner:
  team: team:edc
dimension: dim:data
capability: cap:semantics-and-vocabulary
business-service: svc:schema-management
status: built
release: r3.0
since: r3.0
deprecated-in: null
replaced-by: null
aliases: []
participates-in:
  - bp:BP05B
realises:
  - cap:semantics-and-vocabulary
covers-nfrs: []
provenance:
  source: built
  upstream: null
  repos: []
  licence: EUPL-1.2
---

<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Semantics And Vocabulary</a><br/>
            <a href="../README.md">Service: Schema Management</a><br/>
                <strong>Solution: Schema Synch Service</strong><br/>
</p>
</div>

# Schema Synch Service

Distributes schema and vocabulary updates from the Schema Management Service to Provider and Consumer Nodes, ensuring that dependent components (SD Tooling, Catalogue Client Application) always have access to the most current schema standards. Implements the Schema Synch Adapter API and the Schema Synch Adapter.

Capability-map placement: `data / semantics-and-vocabulary / schema-management / schema-synch-service`. This solution implements part of the **Schema management** business service.

Provenance: built by Simpl. No standalone source repository identified (described in the architecture spec as part of the SMS ecosystem). Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)

## Source code

No standalone source repository identified. See `gaia-x-edc/simpl-schema-manager` for the broader schema management ecosystem.

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
