<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Semantics and vocabulary</a><br/>
            <a href="../README.md">Service: Schema management</a><br/>
                <strong>Solution: Schema Sync Adapter</strong><br/>
</p>
</div>

# Schema Sync Adapter

Participant-side process that keeps each Provider and Consumer node aligned with the schemas published by the [Schema Manager](../simpl-schema-manager/README.md). The adapter realises the **Schema Sync** flow — distributing schema lifecycle updates from the Governance Authority to local agent storage so dependent components can read schemas without calling the Schema Manager API on every operation.

## How it works

- **Initial full sync** at startup — pulls every published schema from the Schema Manager and writes them to a configured shared persistent volume in **Turtle (TTL)** format.
- **Event subscription** — registers with the Schema Manager to receive lifecycle notifications (publication, revocation) and processes them in real time.
- **Incremental updates** — on each event the local TTL files are added, replaced (new version), or removed (revocation) so the persistent volume always mirrors the Schema Manager's published set.
- Other components ([SD Tooling API](../sd-tooling-api/README.md), [Catalogue Client Application](../../../../integration/resource-discovery/search-engine/catalogue-client-application/README.md), [Validation Backend](../../../../integration/resource-discovery/search-engine/validation-backend/README.md)) read schemas from the shared volume on each agent rather than calling the Schema Manager API on every operation.

## Key features

- Initial full synchronisation of all published schemas at startup.
- TTL storage on a shared persistent volume.
- Real-time handling of publication events.
- Removal of revoked schemas.
- Continuous synchronisation between Schema Manager and local persistent storage.
- Logging, audit trail, and error handling for traceability.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [doc/deployment-guide/](doc/deployment-guide/) — deployment instructions.
- [doc/installation-guide/](doc/installation-guide/) — installation procedure.
- [doc/upgrade-guide/](doc/upgrade-guide/) — upgrade procedure.
- [api/](api/README.md) — 2 OpenAPI specs (Tier 1 + Tier 2).
- [CANONICAL.md](CANONICAL.md) — canonical source location for this repository.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/data1/schema-sync-adapter>

Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
