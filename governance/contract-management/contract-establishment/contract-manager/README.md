<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Governance</a><br/>
        <a href="../../README.md">Capability: Contract Management</a><br/>
            <a href="../README.md">Service: Contract Establishment</a><br/>
                <strong>Solution: Contract Manager</strong><br/>
</p>
</div>

# Contract Manager

Orchestrates contract validation, issuance, and storage. Coordinates with the VC Issuer, Signer, and Wallet to integrate contract validation, issuance, and storage functionalities. Also stores contracts for billing and record-keeping purposes, centralising key contract-related data. Interactions between the Orchestrator and Backend are asynchronous via a Message Broker (Kafka).

Capability-map placement: `governance / contract-management / contract-establishment / contract-manager`. This solution implements the **Contract establishment** business service.

Provenance: built by Simpl. Source repository: `contract-billing/contract`. Licence: EUPL 1.2.

Note: the architecture spec describes a planned split into Contract Manager Orchestrator and Contract Manager Backend (referenced in Notion); the current implementation consolidates these as a single solution folder per the step 3 mapping decision.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP07 Consumer and Provider establish a usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/dynamic-view.md)

## Source code

- `code.europa.eu/simpl/simpl-open/development/contract-billing/contract`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
