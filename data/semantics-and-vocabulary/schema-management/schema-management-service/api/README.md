<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../../README.md">🏠 Home</a><br/>
    <a href="../../../../README.md">Dimension: Data</a><br/>
        <a href="../../../README.md">Capability: Semantics And Vocabulary</a><br/>
            <a href="../../README.md">Service: Schema Management</a><br/>
                <a href="../README.md">Solution: Schema Management Service</a><br/>
                    <strong>API: API Documentation</strong><br/>
</p>
</div>

# Schema Management Service — API specifications

The SMS exposes two distinct interfaces:

| Specification | Description |
|--------------|-------------|
| [schema-management-api.openapi.yaml](schema-management-api.openapi.yaml) | Management API — private, authenticated RESTful interface for schema lifecycle management (create versions, publish, revoke) |
| [resolver-interface.openapi.yaml](resolver-interface.openapi.yaml) | Resolver Interface — public, read-only interface for retrieving raw RDF schema content at stable URIs |

The SMS also publishes lifecycle events (SchemaPublished, SchemaRevoked) via webhooks to subscribed services; this channel is defined in the AsyncAPI contract maintained in the source repository.

Full specifications: Status: stub files — see source repositories for runtime documentation.
