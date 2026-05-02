<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access control and trust</a><br/>
            <a href="../README.md">Service: Encryption</a><br/>
                <strong>Solution: vault</strong><br/>
</p>
</div>

# vault

Helm chart deploying HashiCorp Vault as the cryptographic secret/key store. Used by every service that holds a Tier 2 X.509 credential or any secret it cannot keep in plaintext config. Bundled by [Common Components](../../../../cross-cutting/agents/common-components/README.md) into every agent deployment.

See also [openbao](../openbao/README.md) — the OSS-licensed Vault fork; the two are alternative realisations of the same encryption capability.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
