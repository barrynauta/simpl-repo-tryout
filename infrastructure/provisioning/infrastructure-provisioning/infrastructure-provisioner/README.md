# Infrastructure Provisioner

Manages, validates, and executes Crossplane/OpenTofu deployment scripts to provision compute, storage, and network resources for data space consumers. Comprises a Triggering Module (script management, execution, access sharing) and an Infrastructure Provisioner (ArgoCD + Crossplane). Interactions are asynchronous via Kafka.

Capability-map placement: `infrastructure / provisioning / infrastructure-provisioning / infrastructure-provisioner`. This solution implements the **Infrastructure provisioning** business service.

Provenance: built by Simpl. Source repositories: `infrastructure/infrastructure-crossplane` (primary) and `infrastructure/infrastructure-be` (planned split per Notion). Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Source code

- `code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-crossplane`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
