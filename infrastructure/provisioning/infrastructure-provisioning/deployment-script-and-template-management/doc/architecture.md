Source: source repos `infrastructure/infrastructure-be` (README.md + OpenAPI `openapi/infrastructure-provisioning-api.yaml`) and `infrastructure/infrastructure-fe` (Angular frontend). FTA spec, §4.3.1 (ACV Static — Infrastructure Provisioning Service), §6.1.2 (TCV Static — Infrastructure Provisioning Service).

# Deployment Script & Template Management — architecture

> **Implementation note (PSO mapping):** this solution's backend currently shares a Java codebase with the [Triggering Module](../../triggering-module/doc/architecture.md) in the source repo `infrastructure-be`. The PSO mapping spreadsheet flags it as **"Single java project to be split in 2"**; when the split lands, the script-management API and UI plumbing here will move to a dedicated repo (`deployment-script-and-template-management-backend`). The frontend (`infrastructure-fe`) is already independent.

## Business view

Provider-facing application that lets an Infrastructure Provider author, store, version, validate, and manage the **deployment scripts and templates** that the [Infrastructure Provisioner](../../infrastructure-provisioner/doc/architecture.md) executes when a Consumer triggers provisioning. Scripts are pushed into a Git-backed repository (Gitea) so changes are reviewable and auditable; metadata and integrity hashes are persisted in PostgreSQL.

Capability-map placement: Infrastructure dimension → Provisioning capability → Infrastructure provisioning business service.

**Business processes supported:**
- [SA04 Provider manages deployment scripts](../../../../../foundations/business-processes/SA04-provider-manages-deployment-scripts/README.md) — the primary scenario this solution supports.
- [BP08 Consumer consumes an infrastructure resource](../../../../../foundations/business-processes/BP08-consume-infrastructure-resource/README.md) — provides the script catalogue against which the [Triggering Module](../../triggering-module/doc/architecture.md) resolves consumer-triggered provisioning requests.

![UI screenshots — Infrastructure Deployment Script Management UI](./media/image78.png)

## Data view

**Infrastructure Provider Storage** (shared with the Triggering Module):

- **Database** (PostgreSQL 16) — script metadata: name, version, owner, integrity hash, lifecycle status (DRAFT / PUBLISHED / INVALIDATED), references to the Gitea revision.
- **Repository** (Gitea) — the actual script bodies, versioned in Git so the entire change history is preserved and reviewable. Each upload creates a commit; a script's "current version" is the latest commit on its branch.

Data classification: deployment scripts may contain sensitive infrastructure configuration (cloud-account IDs, role ARNs, image references). Treat them as confidential and protect the Gitea repository accordingly.

## Application view

### Internal decomposition

**Backend — Script Storage Management submodule** (currently inside `infrastructure-be`):
- `Add Script` — uploads a script body to the Gitea repository AND writes its integrity hash to PostgreSQL. Performs **security checks** on upload to prevent obvious malicious payloads.
- `Update Script` — creates a new Git revision, updates the metadata row.
- `Remove / Invalidate Script` — soft-delete that flips lifecycle status to INVALIDATED while preserving the Git history; the Triggering Module will refuse to execute INVALIDATED scripts.

**Backend — REST API** (subset of `infrastructureProvisioning/v1/**`, RBAC-gated to `INFRA_ADMIN`):
- Script CRUD endpoints.
- Template CRUD endpoints (deployment templates that bundle parameter sets for repeated provisioning patterns).
- The OpenAPI spec lives at `openapi/infrastructure-provisioning-api.yaml`; Swagger UI at `http://<host>/swagger-ui/index.html`.

**Frontend — Script Management UI** (`infrastructure-fe`):
- **Angular** application served by the Tier 1 Gateway.
- Lets Infrastructure Provider users browse the script catalogue, upload/edit scripts, manage templates, and observe provisioning runs (status pulled via the Triggering Module's status endpoints).

### Key integrations

- [Triggering Module](../../triggering-module/doc/architecture.md) — sibling solution; reads from the same PostgreSQL + Gitea storage to resolve consumer-triggered provisioning requests.
- [Infrastructure Provisioner](../../infrastructure-provisioner/doc/architecture.md) — eventual executor of every script managed here (via the Triggering Module).
- [Authorisation](../../../../../security/access-control-and-trust/authorisation/authorisation/doc/architecture.md) — all UI traffic and CRUD-API traffic passes through the Tier 1 Gateway; CRUD endpoints require the `INFRA_ADMIN` role.
- **Gitea** (under [common-components](../../../../../cross-cutting/agents/common-components/README.md)) — the Git-backed script repository.
- **PostgreSQL** (common-components) — script metadata and lifecycle status.

## Technical view

- **Backend source repo (current)**: `infrastructure/infrastructure-be` — shared with Triggering Module.
- **Backend source repo (target after split)**: `infrastructure/deployment-script-and-template-management-backend` (not yet existing).
- **Frontend source repo**: `infrastructure/infrastructure-fe` — Angular.
- **Language / runtime (backend)**: Java 21+, Maven 3.9+, Spring Boot.
- **Persistence**: PostgreSQL 16 with **Flyway-managed schema migrations** (`SPRING_FLYWAY_*` env vars).
- **Repository**: Gitea (`GITEA_URL`, `GITEA_USER`, `GITEA_PASSWORD`).
- **Secrets**: HashiCorp Vault (KV v2, secret path `secret/infrastructure-be`); only `VAULT_TOKEN` is set outside Vault.

**Local development stack** (`docker-compose.yaml` in source):
- API container (Spring Boot)
- `scripts-db` (PostgreSQL)
- Zookeeper + Kafka
- Vault
- Gitea

After local startup, Swagger UI is available at `http://localhost:8080/swagger-ui/index.html`.

Production deployment uses Helm charts (`charts/`) — see the [Data Provider Agent deployment guide](../../../../../cross-cutting/agents/data-provider-agent/deployment-guide.md) for the values needed (especially the OpenBao `secret/infrastructure-be` path and the Gitea token bootstrap procedure).

## Security view

- **RBAC**: all CRUD endpoints require the `INFRA_ADMIN` role; the trigger endpoint (in the sibling Triggering Module) requires `INFRA_DEPLOYER`.
- **Add Script security checks** prevent obviously malicious payloads from being persisted.
- **Hash-on-upload** writes a script's integrity hash to PostgreSQL; the Triggering Module re-validates it before execution. A divergence between the on-disk hash and the stored hash is treated as tampering and the execution is refused.
- **Gitea token bootstrap** is the most operationally sensitive step: the token can only be created *after* the Provider Agent has come up; `infrastructure-be` must then be restarted to pick up the new value. The Data Provider Agent deployment guide documents the procedure step-by-step.
- **Vault auth via `VAULT_TOKEN`** — supplied to the pod by Kubernetes secret injection; never present in source or chart values.

Threat model: not yet documented.

Secrets management: HashiCorp Vault, KV v2 engine, secret path `secret/infrastructure-be`. The Gitea token has its own bootstrap procedure (see deployment guide).

## Testing

Strategy: Spring Boot integration tests against the docker-compose stack; OpenAPI contract tests via Swagger Editor. CI/CD runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
