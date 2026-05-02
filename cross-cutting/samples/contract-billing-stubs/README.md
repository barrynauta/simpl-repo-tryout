<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Samples</a><br/>
            <strong>contract-billing-stubs</strong><br/>
</p>
</div>

# contract-billing-stubs

Stub/mock backend used to exercise the contract-billing slice without standing up the full Contract Manager / Signer / VC Issuer chain. Helm release name `simpl-stubs`. Bundled by the [`agent-contract-billing/*`](../../agents/agent-contract-billing/README.md) deployment compositions for non-production environments.

Catalogued under cross-cutting/samples/ because it is a runnable test-double, not a participant-facing capability — same shape as the other samples in this folder.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

> **Note on upstream README.** The repo's README and embedded git-remote URL incorrectly say "signer" / point at `contract-billing/signer.git` — copy-paste errors in the upstream. The actual repo path is `contract-billing/stubs`.
