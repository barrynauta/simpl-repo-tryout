# Tier 2 Authentication Provider

Manages Tier 2 security credentials (x.509 keypairs) within a participant agent. Validates Tier 2 credentials (ephemeral proof and security credentials) in agent-to-agent communication. Keeps a local copy of the dataspace identity attributes and participant organisation details. Exposes internal APIs for Simpl components to fetch participant and identity attribute information.

Capability-map placement: `security / access-control-and-trust / authentication-provider-federation / tier-2-authentication-provider`. This solution and `tier-1-authentication-provider` together implement the **Authentication provider federation** business service (flag d-2 in step 3 checkpoint).

Provenance: built by Simpl. Source repositories: `iaa/authentication_provider` (backend) and `iaa/fe-authentication-provider` (frontend). Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Source code

- Backend: `code.europa.eu/simpl/simpl-open/development/iaa/authentication_provider`
- Frontend: `code.europa.eu/simpl/simpl-open/development/iaa/fe-authentication-provider`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
