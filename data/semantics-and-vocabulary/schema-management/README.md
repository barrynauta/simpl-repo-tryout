<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Data</a><br/>
        <a href="../README.md">Capability: Semantics and vocabulary</a><br/>
            <strong>Service: Schema management</strong><br/>
</p>
</div>

# Schema management

Lifecycle management of self-description schemas (SHACL files) and their synchronisation to Provider and Consumer agents. The **Schema Manager** (deployed at the Governance Authority) is the source of truth; the **Sync Adapter** distributes published schemas to participant nodes, where SD-Tooling and the Validation Backend consume them.

Schemas move through a **draft → published → revoked** lifecycle. Lifecycle events are published on Kafka and consumed by the Sync Adapter on each agent, which mirrors the published set into a shared persistent volume in **Turtle (TTL)** format.

## Solutions

- [Schema Sync Adapter](schema-sync-adapter/README.md) — distributes schema lifecycle updates from the Schema Manager to participant nodes.
- [SD Schema Util](sd-schema-util/README.md) — Python tool that generates ontology and SHACL shape files from YAML definitions.
- [SD Tooling API](sd-tooling-api/README.md) — backend API for the SD-Tooling user flow.
- [SD Tooling SD Schemas](sdtooling-sd-schemas/README.md) — repository of authored schemas / shape definitions used by SD-Tooling.
- [Simpl Schema Manager](simpl-schema-manager/README.md) — Schema Manager backend; definitive source of truth for schema lifecycle.
- [Simpl Schema Manager UI](simpl-schema-manager-ui/README.md) — Vue 3 frontend for the Schema Manager.
- [Simpl Schema Versioning](simpl-schema-versioning/README.md) — versioning logic for schema iterations.
- [Simpl SD UI](simpl-sd-ui/README.md) — SD-Tooling frontend used by Provider operators to author, validate, sign, and publish self-descriptions.

## Cross-references

- [SHACL](https://www.w3.org/TR/shacl/) — the W3C constraint language used for all Simpl-Open schemas.
- [Apache Jena Fuseki](../../../foundations/data-architecture/) — the SHACL/RDF store backing schema validation. _(Captured at the data-architecture foundations level rather than as a Schema management solution.)_
- Participating business processes:
  - [BP02 Manage Resource Description Schemas](../../../foundations/business-processes/BP02-configuration-governance-authority/dynamic-view.md)
  - [BP05B Provider manages resource descriptions](../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
  - [BP06 Consumer searches resources](../../../foundations/business-processes/BP06-consumer-searches-resources/dynamic-view.md)
