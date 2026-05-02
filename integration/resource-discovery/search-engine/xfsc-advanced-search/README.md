<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Integration</a><br/>
        <a href="../../README.md">Capability: Resource discovery</a><br/>
            <a href="../README.md">Service: Search engine</a><br/>
                <strong>Solution: xfsc-advanced-search</strong><br/>
</p>
</div>

# xfsc-advanced-search

REST microservice providing the **Advanced Search API** for the federated catalogue — searches and retrieves self-descriptions, supporting both keyword-based and advanced (schema-field) queries. Deployed on both the Provider and Consumer agents.

## How it fits

- Exposed behind the **Tier 1 Gateway**.
- Communicates with [Query Mapper Adapter](../query-mapper-adapter/README.md) via the **Tier 2 Gateway** to translate search criteria onto the federated-catalogue data model.
- Logging and auditability of search requests for traceability and governance compliance.
- Bundled into [`agent-resource-handling/{consumer,provider}-resource-handling`](../../../../cross-cutting/agents/agent-resource-handling/README.md) deployments.

## Source code

Java 21 / Maven. Spring Boot.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
