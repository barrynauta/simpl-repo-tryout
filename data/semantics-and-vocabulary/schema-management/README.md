<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Data</a><br/>
        <a href="../README.md">Capability: Semantics And Vocabulary</a><br/>
            <strong>Service: Schema Management</strong><br/>
</p>
</div>

# Schema management

Authoritative lifecycle management of self-description schemas (SHACL files) and their synchronisation to Provider and Consumer Nodes.

## Solutions

- [Schema Management Service](schema-management-service/README.md) — the definitive source of truth for schema lifecycle (create, version, publish, revoke) with Management API, Resolver Interface, and event publisher.
- [Schema Synch Service](schema-synch-service/README.md) — distributes schema updates from the Schema Management Service to participant nodes via NFS storage.
