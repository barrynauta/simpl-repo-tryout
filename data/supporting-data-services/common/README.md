<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Data</a><br/>
        <a href="../README.md">Capability: Supporting data services</a><br/>
            <strong>Common</strong><br/>
</p>
</div>

# Common

Auxiliary shared infrastructure consumed by services across the platform — not deployable as participant-facing capabilities on their own.

## Solutions

- [postgres-cluster](postgres-cluster/README.md) — Helm chart for the shared PostgreSQL cluster used by Keycloak, EJBCA, identity/onboarding/user-roles, catalogue metadata, contract-manager, and other stateful services. Spans multiple dimensions; lives here because the data dimension manages the persistence substrate.
