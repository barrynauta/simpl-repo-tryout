<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Security</a><br/>
        <a href="../../README.md">Capability: Credential Management</a><br/>
            <a href="../README.md">Service: Signing</a><br/>
                <strong>Solution: Signer Service</strong><br/>
</p>
</div>

# Signer Service

Manages the digital signing of self-descriptions and contracts, ensuring their authenticity, integrity, and non-repudiation. Uses the provider's private key to sign self-descriptions before Catalogue publication, and provides cryptographic signing capabilities for contracts in the credential management workflow.

Capability-map placement: `security / credential-management / signing / signer-service`. This solution implements the **Signing** business service.

Provenance: deployment wrapper (Helm + ArgoCD) over the upstream **Eclipse XFSC TSA Signer** (`gitlab.eclipse.org/eclipse/xfsc/tsa/signer`). The Simpl repository (`gaia-x-edc/simpl-signer`) does not fork the source code — it consumes the upstream container images and adds environment-specific deployment configuration. Licence: Apache 2.0 (TSA Signer upstream).

## Key features

- Pre-built container images consumed from the upstream Eclipse XFSC TSA Signer project; no Simpl-side fork of the signing code itself.
- Helm charts and ArgoCD application manifests for GitOps deployment across SIMPL environments.
- Integration with **HashiCorp Vault** (via Vault Agent Injector) for secrets management; uses the **ed25519 transit engine** for cryptographic operations.
- Support for autoscaling, ingress, Istio service mesh, and Prometheus metrics.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — Apache 2.0.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
- [BP07 Consumer and Provider establish a usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/dynamic-view.md)

## Source code

- Simpl deployment wrapper: <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-signer>
- Upstream signer code: <https://gitlab.eclipse.org/eclipse/xfsc/tsa/signer>
- Container registry: `code.europa.eu:4567/simpl/simpl-open/development/gaia-x-edc/poc-gaia-edc`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
