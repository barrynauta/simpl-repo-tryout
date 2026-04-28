<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Infrastructure</a><br/>
        <a href="../../README.md">Capability: Provisioning</a><br/>
            <a href="../README.md">Service: Infrastructure Provisioning</a><br/>
                <strong>Solution: Deployment Script & Template Management</strong><br/>
</p>
</div>

# Deployment Script & Template Management

Backend + frontend application that lets an Infrastructure Provider author, store, version, and validate the deployment scripts and templates that the [Infrastructure Provisioner](../infrastructure-provisioner/README.md) will later execute (Crossplane / OpenTofu / Terraform). Templates are pushed into a Git-backed repository (Gitea) so changes are reviewable and auditable.

Capability-map placement: `infrastructure / provisioning / infrastructure-provisioning / deployment-script-and-template-management`. Sits alongside the [Triggering Module](../triggering-module/README.md) and the [Infrastructure Provisioner](../infrastructure-provisioner/README.md) under the same business service.

Provenance: built by Simpl. Backend currently consolidated in `infrastructure/infrastructure-be` (planned split per the PSO mapping); frontend in `infrastructure/infrastructure-fe`. Java 21 + Spring (backend), Angular (frontend). Licence: EUPL 1.2.

## Key features

- **Script Management API** ([OpenAPI spec](https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-be/-/blob/main/openapi/infrastructure-provisioning-api.yaml)) — CRUD over deployment scripts.
- **Script Management UI** — operations on deployment scripts, served by the `infrastructure-fe` Angular frontend.
- **Gitea integration** for storing scripts and templates with version control; the integration secrets (`gitea.url`, `gitea.user`, `gitea.password`, `gitea.token`) are sourced from Vault.
- **HashiCorp Vault / OpenBao integration** (KV-v2 engine, `infrastructure-be` secret path) for all runtime configuration: database, Kafka, mail, Gitea credentials. The only env var required to start is `VAULT_TOKEN`.
- **Kafka** for asynchronous coordination with the Triggering Module and the Infrastructure Provisioner.
- PostgreSQL 16 for persistence (Flyway-managed schema).

## Participates in

- [SA04 Provider manages deployment scripts](../../../../foundations/business-processes/SA04-provider-manages-deployment-scripts/README.md)
- [BP08 Consumer consumes an infrastructure resource](../../../../foundations/business-processes/BP08-consume-infrastructure-resource/README.md)

## Source code

- Backend: <https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-be>
- Frontend: <https://code.europa.eu/simpl/simpl-open/development/infrastructure/infrastructure-fe>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
