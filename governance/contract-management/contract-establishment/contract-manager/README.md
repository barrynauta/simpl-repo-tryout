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
