Source: source repo `infrastructure/infrastructure-be` (README.md, OpenAPI at `openapi/infrastructure-provisioning-api.yaml`). FTA spec, §4.3.1 (ACV Static — Infrastructure Provisioning Service), §4.3.2 (ACV Dynamic — BP 08), §6.1.2 (TCV Static — Infrastructure Provisioning Service).

# Triggering Module — architecture

> **Implementation note (PSO mapping):** the Triggering Module currently shares a Java codebase with the [Deployment Script & Template Management](../../deployment-script-and-template-management/doc/architecture.md) backend in the source repo `infrastructure-be`. The PSO mapping spreadsheet flags it as **"Single java project to be split in 2"** (one sprint of work, parallelisable with feature development). When the split lands, the Triggering Module's API endpoints, schedulers, and Connector-triggering integration will move to a dedicated `triggering-module` repo.

## Business view

The Triggering Module is the **inbound coordinator** of the infrastructure-provisioning pipeline. It receives provisioning requests from the **Connector's Triggering Extension** at contract finalisation, validates them against the Provider's local script catalogue, and dispatches the resolved provisioning job to the [Infrastructure Provisioner](../../infrastructure-provisioner/doc/architecture.md) over Kafka. After provisioning completes, it manages access-data sharing back to the Consumer.

Capability-map placement: Infrastructure dimension → Provisioning capability → Infrastructure provisioning business service.

**Business process — BP 08 (Consumer consumes an infrastructure resource):** on contract finalisation the EDC Connector's Triggering Extension publishes a `(DeploymentScriptID, consumerEmail)` event. The Triggering Module looks up the script by ID, validates its hash against the stored one, and submits the provisioning job. Once provisioning completes, the Access Management submodule retrieves credentials/endpoints from the Infrastructure Provisioner and delivers them to the consumer (typically by email).

![ACV Static view — Infrastructure Provisioning Service](./media/image49.jpeg)
![ACV Dynamic — BP 08](./media/image65.jpeg)

## Data view

The Triggering Module reads from the shared **Infrastructure Provider Storage** (PostgreSQL) maintained by the Deployment Script & Template Management backend:

- **Script metadata + integrity hash** — looked up by `DeploymentScriptID` at trigger time.
- **In-flight request state** — per-request lifecycle records (queued → running → succeeded/failed) plus the consumer email captured from the triggering event.

It also writes Kafka messages onto the provisioning topic for the Infrastructure Provisioner and consumes status events back from the same topic.

## Application view

### Internal decomposition

Three submodules, all currently inside the `infrastructure-be` Spring Boot application:

- **Script Execution submodule** —
  - `Retrieve Deployment Script` from the Gitea-backed repository.
  - `Validate Deployment Script` — recomputes the script hash and compares against the value stored at upload time (integrity check; rejects if mismatched).
  - `Trigger Execution` — produces a Kafka message onto the provisioning topic for the Infrastructure Provisioner.
- **Access Management submodule** —
  - `Retrieve and Share Access Data` — collects access credentials and endpoints from the Infrastructure Provisioner and dispatches them to the consumer over the configured channel (email via Spring Mail by default).
- **Provisioning API** — small REST surface exposed externally:
  - `POST /api/infrastructureProvisioning/v1/scripts/trigger` — RBAC role `INFRA_DEPLOYER`. Trigger endpoint consumed by the Connector Triggering Extension or the consumer's tooling. Configured as a **Tier 1 business log** with operation `TRIGGER_REQUEST`.
  - `GET /api/infrastructureProvisioning/v1/status` — public-URL status probe.

### Key integrations

- [Connector](../../../../../integration/resource-sharing/resource-sharing-runtime/connector/doc/architecture.md) — Triggering Extension is the upstream caller.
- [Infrastructure Provisioner](../../infrastructure-provisioner/doc/architecture.md) — async target of triggered provisioning jobs over Kafka.
- [Deployment Script & Template Management](../../deployment-script-and-template-management/doc/architecture.md) — sibling solution; owns the script catalogue and Gitea repository this module reads from.
- [Authorisation](../../../../../security/access-control-and-trust/authorisation/authorisation/doc/architecture.md) — Tier 1 Gateway routes inbound calls; the trigger endpoint is RBAC-gated to `INFRA_DEPLOYER`.
- [Notification Service](../../../../../administration/notification-and-messaging/notification/notification-service/doc/architecture.md) — alternative channel for access-data delivery (Spring Mail used today; Notification Service is the strategic target).

## Technical view

- **Source repo (current)**: `infrastructure/infrastructure-be` — shared with Deployment Script & Template Management backend.
- **Source repo (target after split)**: `infrastructure/triggering-module` (not yet existing).
- **Language / runtime**: Java 21+, Maven 3.9+, Spring Boot.
- **Persistence**: PostgreSQL 16 (shared with Deployment Script & Template Management).
- **Messaging**: Apache Kafka with SASL (`KAFKA_SASL_ENABLED=true`).
- **Secrets**: HashiCorp Vault (KV v2 engine, secret path `secret/infrastructure-be`); the only environment variable required to start is `VAULT_TOKEN`. All other config is sourced from Vault.
- **Mail**: Spring Mail for access-data delivery (`SPRING_MAIL_USERNAME` / `SPRING_MAIL_PASSWORD`).

## Security view

- **RBAC** at Tier 1: trigger endpoint requires the `INFRA_DEPLOYER` role; full provisioning admin requires `INFRA_ADMIN`.
- **Hash integrity check** before execution — if the on-disk script hash differs from the hash stored at upload time, the request is rejected. This is the primary defence against post-upload script tampering.
- **Kafka SASL** secures the Triggering Module ↔ Infrastructure Provisioner channel against unauthorised producers.
- **Access-data sensitivity** — credentials and endpoints flow through this module on their way to the consumer; the `secret/infrastructure-be` Vault path holds the SMTP credentials needed to deliver them.

Threat model: not yet documented.

Secrets management: HashiCorp Vault, KV v2 engine, secret path `secret/infrastructure-be`. Only `VAULT_TOKEN` is configured outside Vault.

## Testing

Strategy: Spring Boot integration tests (Docker-Compose-based local stack: API + scripts-db Postgres + Zookeeper/Kafka + Vault + Gitea). CI/CD runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
