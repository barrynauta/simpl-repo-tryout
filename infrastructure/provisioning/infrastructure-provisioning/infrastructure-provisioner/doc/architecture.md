Source: source repo `infrastructure/infrastructure-crossplane`. FTA spec, §4.3.1 (ACV Static — Infrastructure Provisioning Service), §4.3.2 (ACV Dynamic — BP 08), §6.1.2 (TCV Static — Infrastructure Provisioning Service), §6.5.2 (Infrastructure Provisioning).

> **Scope of this document.** Earlier editions described the Triggering Module + Deployment-Script Management + Infrastructure Provisioner as one combined service. With the recent solution-folder split they are now three sibling solutions, each with its own architecture document. This document scopes specifically to the **Crossplane/ArgoCD executor**. For the inbound coordinator and the script catalogue, see [Triggering Module](../../triggering-module/doc/architecture.md) and [Deployment Script & Template Management](../../deployment-script-and-template-management/doc/architecture.md) respectively.

# Infrastructure Provisioner — architecture

## Business view

The Infrastructure Provisioner is the **executor** in the infrastructure-provisioning pipeline. It receives provisioning jobs over Kafka from the [Triggering Module](../../triggering-module/doc/architecture.md), then applies them — through ArgoCD + Crossplane — on the target Kubernetes cluster. After provisioning completes it produces the access data (credentials, endpoints) that flows back through the Triggering Module to the consumer. It also handles **decommissioning** at contract end.

Capability-map placement: Infrastructure dimension → Provisioning capability → Infrastructure provisioning business service.

**Business process — BP 08 (Consumer consumes an infrastructure resource):** triggered by the Triggering Module on contract finalisation; runs Provisioning → Post-configuration (apps + datasets) → Share Access Data. At contract end, runs Pre-decommissioning (notifications, backups) → Access Revocation.

![ACV Static view — Infrastructure Provisioning Service](./media/image49.jpeg)
![ACV Dynamic — BP 08](./media/image65.jpeg)

## Data view

This component holds **no first-party persistent data**. Its inputs are:

- The **deployment-script content** retrieved from the [Deployment Script & Template Management](../../deployment-script-and-template-management/doc/architecture.md) Gitea repository (Crossplane manifests, OpenTofu/Terraform configs).
- The **provisioning request** (DeploymentScriptID, consumer email, parameter values) received over Kafka from the Triggering Module.

Its outputs are:
- **Access data** (credentials, endpoints, post-configuration results) sent back over Kafka to the Triggering Module for delivery to the consumer.
- **ArgoCD/Crossplane state** in the target cluster — the live infrastructure resources themselves.

Data model diagrams (showing the shared Infrastructure Provider Storage owned by the script-management side):
- CDM: `./media/image100.png` (§5.2.1).
- LDM: `./media/image109.png` (§5.2.2).
- PDM: `./media/image117.png` (§5.2.3).

![CDM — Infrastructure Provider Storage conceptual data model](./media/image100.png)

## Application view

### Internal decomposition

- **Provisioning sub-component**:
  - `Execute Deployment Script` — applies the Crossplane / OpenTofu / Terraform script via ArgoCD on the target cluster.
  - `Set Policies` — applies the policies bundled with the deployment.
  - `Create Access Information` — generates / collects credentials and endpoints exposed by the provisioned resources.
  - `Post Configuration` — deploys ancillary applications and loads datasets into the freshly provisioned infrastructure where the script defines this.
  - `Share Access Data` — emits the access-data event back over Kafka.
- **Decommissioning sub-component**:
  - `Pre-decommissioning` — notifications, backups (where defined by the script).
  - `Access Revocation` — removes credentials and tears down the provisioned resources via ArgoCD.

This service is **not exposed via a public API**. The only way to drive it is the Kafka topic produced by the Triggering Module; that asymmetry is intentional and load-bearing for the security view.

### Key integrations

- [Triggering Module](../../triggering-module/doc/architecture.md) — sole upstream caller; sends provisioning jobs and consumes the access-data response, both over Kafka.
- [Deployment Script & Template Management](../../deployment-script-and-template-management/doc/architecture.md) — sibling solution; the Gitea repository it owns is the source of every script this component runs.
- **ArgoCD** (under [Infrastructure → Supporting Infrastructure Services → Infrastructure Orchestration](../../../../supporting-infrastructure-services/README.md)) — the GitOps deployment engine that applies Crossplane manifests on the target cluster.
- **Crossplane** — the Kubernetes-native control-plane primitive that turns the manifests into actual cloud resources.

## Technical view

- **Source repo**: `infrastructure/infrastructure-crossplane`.
- **Executor stack**: ArgoCD + Crossplane on the target Kubernetes cluster. Supports OpenTofu and Terraform script formats alongside Crossplane primitives.
- **Inbound channel**: Kafka topic shared with the Triggering Module.
- **Outbound channel**: Kafka topic for status / access-data events (consumed by the Triggering Module's Access Management submodule).

Deployment: deployed in Infrastructure Provider Agents. Crossplane is deployed as a single instance per cluster (the Provider Agent's Helm values flag `crossplane.enabled: true` and the [Data Provider Agent deployment guide](../../../../../cross-cutting/agents/data-provider-agent/deployment-guide.md) explicitly notes "only one instance per cluster").

![TCV Static view — Infrastructure Provisioning Service](./media/image141.jpeg)

## Security view

- **No public ingress** — this component is reachable only via the Kafka topic produced by the Triggering Module. Direct external requests cannot start a provisioning run.
- **Script integrity** is checked **upstream** by the Triggering Module before the job arrives here; if the on-disk script hash differs from the stored hash, the Triggering Module refuses to dispatch.
- **Access-data sensitivity** — credentials produced by `Create Access Information` are written onto the Kafka topic; SASL authentication on the topic restricts which services can consume them.
- **ArgoCD permissions** scope what this executor can do on the target cluster; over-broad permissions would let a compromised Crossplane manifest escalate to cluster admin.

Threat model: not yet documented.

Secrets management: ArgoCD service-account tokens for the target cluster; Vault for any credential material the deployment scripts themselves need at runtime.

## Testing

Strategy: integration tests against a kind/k3d cluster with a stub Triggering Module producing onto the Kafka topic; assertion is the Crossplane resources land on the cluster and the access-data response surfaces back. CI/CD runs unit tests, SAST (SonarQube), and security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
