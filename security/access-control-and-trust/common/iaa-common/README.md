<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access control and trust</a><br/>
            <a href="../README.md">Service: Common</a><br/>
                <strong>Solution: iaa-common</strong><br/>
</p>
</div>

# iaa-common

Shared Java library module used across multiple IAA services. Provides reusable components, shared models, and utilities, plus the `simpl-api-iaa` submodule that centralises every OpenAPI and AsyncAPI specification used by the IAA ecosystem.

## Purpose

The `common` project is a shared Java library consumed by the runtime services in this capability. It packages cross-cutting code (models, utilities, error handling, security helpers) so each IAA service depends on a single curated baseline rather than re-inventing the same primitives.

The `simpl-api-iaa` submodule stores and exposes all OpenAPI and AsyncAPI specifications used by the IAA service ecosystem. It serves as a static-resource module that can be packaged and deployed independently — useful for documentation portals, contract validation in CI, and consumer SDK generation.

## Used by

Every runtime service under [`access-control-and-trust/`](../../README.md) — including the [Tier 1 Authentication Provider](../../authentication-provider-federation/tier-1-authentication-provider/README.md), [Tier 2 Authentication Provider](../../authentication-provider-federation/tier-2-authentication-provider/README.md), [Identity Provider](../../identity-provider-federation/identity-provider/README.md), and [Security Attributes Provider](../../security-attribute-provider-federation/security-attributes-provider/README.md).

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
