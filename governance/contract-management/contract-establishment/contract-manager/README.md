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

Orchestrates contract validation, issuance, and storage between data-space participants. Coordinates with the VC Issuer, Signer, and Wallet to integrate contract validation, issuance, and storage functionalities. Also stores contracts for billing and record-keeping purposes, centralising key contract-related data. Interactions between the Orchestrator and the Backend are asynchronous via a message broker (Kafka).

Capability-map placement: `governance / contract-management / contract-establishment / contract-manager`. This solution implements the **Contract establishment** business service.

Provenance: built by Simpl. Source repository: `contract-billing/contract`. Java 21 / Maven 3.9+. Licence: EUPL 1.2.

Note: the architecture spec describes a planned split into Contract Manager Orchestrator and Contract Manager Backend; per the current to-be mapping the two pieces share this solution folder. The PSO mapping spreadsheet lists them as separate app-services (`contract-manager-backend`, `contract-manager-orchestrator`) — keep that distinction in mind when the split actually lands in source.

## Key features

- **Contract storage and lifecycle**: stores, consults, and updates signed contracts established via the dataspace connectors during contract negotiation and signature.
- **Extended negotiation**: extends the participant contract-management with additional negotiation steps in the contract-establishment flow.
- **Usage reporting and enforcement**: reports on resource usage as defined in contracts, and triggers contract-closure and resource-decommissioning when usage thresholds or contract end-conditions are met. Monitoring contributes inputs to these triggers.
- **Asynchronous orchestration**: Orchestrator ↔ Backend communicate over Kafka; persistent state in PostgreSQL; secrets via HashiCorp Vault; signing/verification through the EDC Connector and credential-management services.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP07 Consumer and Provider establish a usage contract](../../../../foundations/business-processes/BP07-establish-usage-contract/dynamic-view.md)


## API

[`api/`](api/README.md) — 1 OpenAPI/AsyncAPI spec imported from the source repository (last imported 2026-04-28).


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `installation-guide/` (1 file), `upgrade-guide/` (1 file), `user-guide/` (1 file).

## Source code

- `code.europa.eu/simpl/simpl-open/development/contract-billing/contract`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
