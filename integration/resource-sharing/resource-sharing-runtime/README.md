<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Integration</a><br/>
        <a href="../README.md">Capability: Resource Sharing</a><br/>
            <strong>Service: Resource Sharing Runtime</strong><br/>
</p>
</div>

# Resource sharing runtime

Data Space Protocol (DSP) contract negotiation and data exchange runtime. Manages assets, policies, contract negotiation, and data transfers between providers and consumers.

## Solutions

- [Connector](connector/README.md) — Eclipse EDC fork implementing DSP; includes Control Plane, Data Plane, Policy Engine, Triggering Extension, and S3 Extension.
- [EDC Connector Adapter](edc-connector-adapter/README.md) — abstraction layer between the EDC Connector and the SD-Tooling / Contract Consumption components, decoupling business logic from the specific connector implementation.
- [Gaia-X Connector](gaia-x-connector/README.md) — upstream Gaia-X EDC fork that the Simpl Connector solution builds on.
- [EDC Extensions](edc-extensions/README.md) — Simpl-built EDC extension packages (S3, triggering, IAA glue, etc.) that plug into the Gaia-X Connector and its deployment variants.
- [Authority Gaia-X EDC](authority-gaiax-edc/README.md) — Governance-Authority deployment variant of the Gaia-X EDC connector.
- [Provider Gaia-X EDC](provider-gaia-x-edc/README.md) — Provider-side deployment variant of the Gaia-X EDC connector.
- [Consumer Gaia-X EDC](consumer-gaiax-edc/README.md) — Consumer-side deployment variant of the Gaia-X EDC connector.

- [Common](common/README.md) — shared libraries (e.g. `connector-model-common`) consumed across the resource-sharing-runtime services. Not deployable on their own.

