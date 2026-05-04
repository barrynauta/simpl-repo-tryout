<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Supporting data services</a><br/>
            <a href="../README.md">Service: Common</a><br/>
                <strong>Solution: data-services-common</strong><br/>
</p>
</div>

# data-services-common

Shared Java/Spring Boot library consumed by the data-dimension microservices (advanced search, schema management, schema synchronisation, SD authoring, contract consumption, etc.). Provides cross-cutting building blocks — logging filters, exception handling, model classes, JSON utilities, validators, Spring config, Feign client scaffolding, Bearer-token filters — so each downstream service depends on a single curated baseline rather than re-implementing the same primitives.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Used by

Imported as a Maven dependency (`simpl-data1-common`) by:

- [xfsc-advanced-search](../../../../integration/resource-discovery/search-engine/xfsc-advanced-search/README.md)
- [sd-tooling-api](../../../semantics-and-vocabulary/schema-management/sd-tooling-api/README.md)
- [sd-tooling-validation-api](../../../semantics-and-vocabulary/schema-management/sd-tooling-validation-api/README.md)
- [schema-sync-adapter](../../../semantics-and-vocabulary/schema-management/schema-sync-adapter/README.md)
- contract-consumption-be (and several other data-team microservices)

## Modularisation note

This library aggregates multiple unrelated concerns into a single jar — HTTP/Feign plumbing, JWT auth filters, exception types, domain models (ODRL, self-description), schema-sync clients, and self-description utilities. That breadth violates the modularity principle Simpl applies to its own runtime services. The library is catalogued here so every CE repo has a home, but it is a candidate for being **split into smaller, properly-scoped modules** during a future hardening pass — at which point each split would get its own catalogue entry under the appropriate capability and this aggregator entry would be retired.

## Source

- <https://code.europa.eu/simpl/simpl-open/development/data1/common>
