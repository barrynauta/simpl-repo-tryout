<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Cross-Cutting</a><br/>
        <strong>Agents</strong><br/>
</p>
</div>

# Agents

Master Helm charts that compose the modules of the capability map into a deployable **Simpl-Open Agent**. An agent is a deployment composition, not a service in its own right — each actor type (Provider, Consumer, Governance Authority, Application Provider, Infrastructure Provider) deploys its own agent that bundles only the modules relevant to that actor's role.

These compositions cross every dimension of the capability map (security, governance, data, integration, infrastructure, administration), which is why they live under `cross-cutting/` rather than inside a single dimension.

## Agents

- [consumer-agent/](consumer-agent/README.md) — bundles the modules a Consumer Participant needs (catalogue client, contract consumption, EDC consumer connector, Tier 1/Tier 2 client stack).
- [data-provider-agent/](data-provider-agent/README.md) — bundles the Provider-side modules for sharing data resources (SD-Tooling, EDC provider connector, schema management client).
- [application-provider-agent/](application-provider-agent/README.md) — Provider variant for application/processing services. Currently a placeholder.
- [infrastructure-provider-agent/](infrastructure-provider-agent/README.md) — Provider variant for infrastructure resources. Currently a placeholder.
- [governance-authority-agent/](governance-authority-agent/README.md) — bundles the modules deployed inside the Governance Authority (onboarding, identity provider, EJBCA, signer, federated catalogue, schema management).
- [common-components/](common-components/README.md) — shared Helm chart bundle reused across the agents (Kafka, OpenBao, PostgreSQL).
