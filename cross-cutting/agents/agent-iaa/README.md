<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Agent IAA</strong><br/>
</p>
</div>

# Agent IAA

Per-actor-type configurations of the IAA (Identity, Authentication, Authorisation) stack for Simpl-Open agents. Each entry in this group bundles the IAA components an actor needs (Tier 1 and Tier 2 gateways, Keycloak realm config, identity-attribute mappings) for that actor type.

These configurations are consumed by the corresponding master Helm chart agents under [`cross-cutting/agents/`](../README.md) (e.g. `consumer-agent` consumes `consumer-iaa`).

## Variants

- [authority-iaa](authority-iaa/README.md) — IAA configuration for the Governance Authority.
- [consumer-iaa](consumer-iaa/README.md) — IAA configuration for Consumer participants.
- [participant-iaa](participant-iaa/README.md) — Generic participant-side IAA configuration shared across consumer/provider variants.
- [provider-iaa](provider-iaa/README.md) — IAA configuration for Provider participants (data, application, infrastructure flavours).
