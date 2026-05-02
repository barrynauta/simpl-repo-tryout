<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Security</a><br/>
        <a href="../README.md">Capability: Access Control And Trust</a><br/>
            <strong>Service: Identity provider federation</strong><br/>
</p>
</div>

# Identity provider federation

Governance Authority–managed identity federation service. Issues and manages Tier 2 X.509 credentials for participant agents; acts as Certificate Authority for the data space.

> **Naming note.** The capability map (FTA §2.8) lists this service as "Identity provider"; the surrounding architecture text refers to "Identity Provider Federation" as the operational concept. The folder is named `identity-provider-federation` for consistency with the sibling `-federation` services (Authentication provider federation, Security attribute provider federation).

## Solutions

- [Identity Provider](identity-provider/README.md) — EJBCA-based CA for Tier 2 credential issuance, renewal, and revocation; integrated with the Onboarding workflow.
- [fe-identity-provider](fe-identity-provider/README.md) — Angular frontend for participant and credential management; UI counterpart to the Identity Provider backend.
