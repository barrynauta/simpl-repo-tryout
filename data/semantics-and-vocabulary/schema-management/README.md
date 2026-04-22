# Schema management

Authoritative lifecycle management of self-description schemas (SHACL files) and their synchronisation to Provider and Consumer Nodes.

## Solutions

- [Schema Management Service](schema-management-service/README.md) — the definitive source of truth for schema lifecycle (create, version, publish, revoke) with Management API, Resolver Interface, and event publisher.
- [Schema Synch Service](schema-synch-service/README.md) — distributes schema updates from the Schema Management Service to participant nodes via NFS storage.
