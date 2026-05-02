<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
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

Shared Java library used across the contract-billing microservices. Centralises cross-cutting concerns — error handling, security, authentication, external communication — to keep the contract-management, signer, and notification services consistent and DRY.

Consumed by [Contract Manager](../../contract-establishment/contract-manager/README.md) and the [Notification Service](../../../../administration/notification-and-messaging/notification/notification-service/README.md). The notification service sits in a different dimension; the dependency is incidental — the library is built for and named after the contract-billing family.

Provenance: built by Simpl. Source repository: `contract-billing/common`. Owner: Contract team. Licence: EUPL 1.2.


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `installation-guide/` (1 file), `upgrade-guide/` (1 file), `user-guide/` (1 file).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/contract-billing/common>
