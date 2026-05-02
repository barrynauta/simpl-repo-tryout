<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Security</a><br/>
        <a href="../README.md">Capability: Access Control And Trust</a><br/>
            <strong>Service: Authentication Provider Federation</strong><br/>
</p>
</div>

# Authentication provider federation

Tier 1 and Tier 2 authentication providers for Simpl-Open participant agents. Tier 1 authenticates end-users within a participant's agent (Keycloak + extensions). Tier 2 authenticates participant agents to each other via mTLS with X.509 credentials.

## Solutions

- [Tier 1 Authentication Provider](tier-1-authentication-provider/README.md) — Keycloak-based OIDC identity provider with Simpl-Open custom authenticator plugin.
- [Tier 2 Authentication Provider](tier-2-authentication-provider/README.md) — X.509 mTLS credential holder and validator for agent-to-agent communication.
- [fe-authentication-provider](fe-authentication-provider/README.md) — Angular frontend for credential management, security settings, and Tier 2 connectivity testing across both auth tiers.
