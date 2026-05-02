<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Access control and trust</a><br/>
            <a href="../README.md">Service: Encryption</a><br/>
                <strong>Solution: openbao</strong><br/>
</p>
</div>

# openbao

Helm chart deploying [OpenBao](https://openbao.org/) — the OSS-licensed Vault fork — as the cryptographic secret/key store. Functionally interchangeable with [vault](../vault/README.md). Companion init job: [openbao-init/](openbao-init/README.md). Bundled by [Common Components](../../../../cross-cutting/agents/common-components/README.md) into every agent deployment.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
