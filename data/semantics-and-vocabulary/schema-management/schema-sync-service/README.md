<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Semantics And Vocabulary</a><br/>
            <a href="../README.md">Service: Schema Management</a><br/>
                <strong>Solution: Schema Sync Service</strong><br/>
</p>
</div>

# Schema Sync Service

## How it works

- **Initial full sync** at startup — pulls every published schema from the Schema Manager and writes them to a configured shared persistent volume in **Turtle (TTL)** format.
- **Event subscription** — registers with the Schema Manager to receive lifecycle notifications (publication, revocation) and processes them in real time.
- **Incremental updates** — on each event the local TTL files are added, replaced (new version), or removed (revocation) so the persistent volume always mirrors the Schema Manager's published set.
- Other components (SD Tooling, Catalogue Client, Validation Backend) read schemas from the shared volume on each agent rather than calling the Schema Manager API on every operation.

## Key features

- Initial full synchronisation of all published schemas at startup.
- TTL storage on a shared persistent volume.
- Real-time handling of publication events.
- Removal of revoked schemas.
- Continuous synchronisation between Schema Manager and local persistent storage.
- Logging, audit trail, and error handling for traceability.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)


## API

[`api/`](api/README.md) — 2 OpenAPI/AsyncAPI specs imported from the source repository (last imported 2026-04-28).


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `installation-guide/` (1 file), `upgrade-guide/` (1 file).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/data1/schema-sync-adapter>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
