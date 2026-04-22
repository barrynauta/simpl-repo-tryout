# Schema Management Service — API specifications

The SMS exposes two distinct interfaces:

| Specification | Description |
|--------------|-------------|
| [schema-management-api.openapi.yaml](schema-management-api.openapi.yaml) | Management API — private, authenticated RESTful interface for schema lifecycle management (create versions, publish, revoke) |
| [resolver-interface.openapi.yaml](resolver-interface.openapi.yaml) | Resolver Interface — public, read-only interface for retrieving raw RDF schema content at stable URIs |

The SMS also publishes lifecycle events (SchemaPublished, SchemaRevoked) via webhooks to subscribed services; this channel is defined in the AsyncAPI contract maintained in the source repository.

Full specifications: Status: stub files — see source repositories for runtime documentation.
