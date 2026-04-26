---
id: simpl:signer-service
type: solution
name: Signer Service
owner:
  team: team:edc
dimension: dim:security
capability: cap:credential-management
business-service: svc:signing
status: built
release: r3.0
since: r3.0
deprecated-in: null
replaced-by: null
aliases: []
participates-in:
  - bp:BP05B
  - bp:BP07
realises:
  - cap:credential-management
covers-nfrs: []
provenance:
  source: fork
  upstream: XFSC OCM
  repos:
    - code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-signer
  licence: Apache-2.0
---

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

Provenance: built by Simpl on XFSC Organisation Credential Manager. Source repository: `gaia-x-edc/simpl-signer`. Licence: Apache 2.0 (XFSC OCM upstream).

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — Apache 2.0.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
- [BP07 Consumer and Provider establish a usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/dynamic-view.md)

## Source code

- `code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-signer`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
