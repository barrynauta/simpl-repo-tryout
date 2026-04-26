---
id: simpl:wallet
type: solution
name: Wallet
owner:
  team: team:unassigned
dimension: dim:security
capability: cap:credential-management
business-service: svc:wallet
status: planned
release: null
since: r3.0
deprecated-in: null
replaced-by: null
aliases: []
participates-in:
  - bp:BP05B
  - bp:BP07
  - bp:BP08
realises:
  - cap:credential-management
covers-nfrs: []
provenance:
  source: placeholder
  upstream: XFSC OCM
  repos: []
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
            <a href="../README.md">Service: Wallet</a><br/>
                <strong>Solution: Wallet</strong><br/>
</p>
</div>

# Wallet

A secure digital repository for storing, managing, and presenting verifiable credentials (VCs) issued by the VC Issuer. Enables providers and participants to securely manage and share their credentials, ensuring compliance with contractual requirements while facilitating efficient access to validated information.

Capability-map placement: `security / credential-management / wallet / wallet`. This solution implements the **Wallet** business service.

Provenance: planned — Contract / Catalogue team (no current source repository). Implemented with XFSC Organisation Credential Manager. Licence: Apache 2.0 (XFSC OCM upstream).

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — Apache 2.0.

## Participates in

- [BP05B Provider manages resource descriptions](../../../../foundations/business-processes/BP05B-provider-manages-resource-descriptions/dynamic-view.md)
- [BP07 Consumer and Provider establish a usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/dynamic-view.md)
- [BP08 Consumer consumes an infrastructure resource](../../../../foundations/business-processes/BP08-consume-infrastructure-resource/dynamic-view.md)

## Source code

No current source repository. Planned for the Contract / Catalogue team.

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
