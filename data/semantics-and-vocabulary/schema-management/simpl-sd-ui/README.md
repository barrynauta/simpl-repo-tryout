<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Semantics and vocabulary</a><br/>
            <a href="../README.md">Service: Schema management</a><br/>
                <strong>Solution: simpl-sd-ui</strong><br/>
</p>
</div>

# simpl-sd-ui

SD-Tooling frontend — Astro 4 + Vue 3 UI used by Provider operators to author, validate, sign, and publish self-descriptions. The submit flow chains three backends: sdtooling-api-be (validation + enrichment) → simpl-signer (JWS signing) → simpl-fc-service (publish). Schemas are loaded from the [Schema Manager](../simpl-schema-manager/README.md). Production-grade: versioned to 1.10.0 (April 2026), monthly releases, Helm charts shipped, Cypress E2E coverage. In production it sits behind the Tier-1 gateway with Keycloak auth.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

This solution is the UI counterpart of [sd-tooling-api](../sd-tooling-api/README.md) (backend).
