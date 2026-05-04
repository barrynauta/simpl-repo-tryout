<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Common Components</strong><br/>
</p>
</div>

# Common Components

Shared Helm chart bundle reused by every agent composition: **Kafka** (message broker), **OpenBao / HashiCorp Vault** (secrets), and **PostgreSQL cluster** (persistence). Each agent depends on this bundle so the same versions and configuration shapes are reused across the whole deployment topology.

Provenance: built by Simpl. Source repository: `agents/common_components`. Backs the individual common-components repos at `common-components/{kafka, openbao, openbao-init, postgres-cluster, vault, shared-specs}`. Licence: EUPL 1.2.

## Sub-bundles

Each sub-bundle has its own capability-aligned folder; this rollup remains because the bundle is published as a single artefact (`agents/common_components`).

- **Kafka** → [administration/notification-and-messaging/messaging/kafka](../../../administration/notification-and-messaging/messaging/kafka/README.md) — message broker used pervasively for async coordination.
- **OpenBao** → [security/access-control-and-trust/encryption/openbao](../../../security/access-control-and-trust/encryption/openbao/README.md) (with companion [openbao-init](../../../security/access-control-and-trust/encryption/openbao/openbao-init/README.md)) — Vault-compatible secrets store; init scripts seed the per-component KV paths.
- **Vault** → [security/access-control-and-trust/encryption/vault](../../../security/access-control-and-trust/encryption/vault/README.md) — HashiCorp Vault realisation of the encryption capability; functionally interchangeable with OpenBao.
- **PostgreSQL** → [data/supporting-data-services/common/postgres-cluster](../../../data/supporting-data-services/common/postgres-cluster/README.md) — pervasive persistence layer.
- **Shared specs** — `common-components/shared-specs` — _Not catalogued. The shared-specs repo is a cross-service spec dump that violates the principle of services owning their own contracts; it is intentionally not given a structural home in the capability map._


## Documentation (imported from source)

[`doc/`](doc/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `iaa-2.11.x/` (2 files), `user-manual/` (3 files).

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/agents/common_components>
- <https://code.europa.eu/simpl/simpl-open/development/common-components/kafka>
- <https://code.europa.eu/simpl/simpl-open/development/common-components/openbao>
- <https://code.europa.eu/simpl/simpl-open/development/common-components/postgres-cluster>
