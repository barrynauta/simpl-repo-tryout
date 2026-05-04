<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Governance</a><br/>
        <a href="../../README.md">Capability: Contract management</a><br/>
            <a href="../README.md">Common</a><br/>
                <strong>Solution: contract-billing-common</strong><br/>
</p>
</div>

# Contract Billing Common

Shared Java library used across the contract-billing microservices. Centralises cross-cutting concerns — error handling, security/authentication, external HTTP communication — so the contract-management, signer, and notification services share one curated baseline rather than re-implementing the same primitives.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Used by

Imported as a Maven dependency by:

- [Contract Manager](../../contract-establishment/contract-manager/README.md)
- [Notification Service](../../../../administration/notification-and-messaging/notification/notification-service/README.md)

The notification service sits in a different dimension; the dependency is incidental — the library is built for and named after the contract-billing family.

## Modularisation note

This library bundles five small but distinct concerns into a single jar: `exceptions/` (error types and a global handler), `security/` (API-key auth filter and secret-client config), `service/` (a shared HTTP client), `transfer/` (error DTOs), and `utils/` (error codes, log utilities). The scope is narrower than other Simpl shared libraries — but the same modularity principle applies: a finer-grained split (separate auth, error-handling, and HTTP-client modules) would let consumers depend only on what they actually use. Catalogued here so every CE repo has a home; flagged as a candidate for upstream modularisation during a future hardening pass, at which point each split would get its own catalogue entry under the appropriate capability.

## Documentation (imported from source)

[`doc/`](doc/) — user-facing documentation imported verbatim from the source repository: `installation-guide/` (1 file), `upgrade-guide/` (1 file), `user-guide/` (1 file).

## Source

- <https://code.europa.eu/simpl/simpl-open/development/contract-billing/common>
