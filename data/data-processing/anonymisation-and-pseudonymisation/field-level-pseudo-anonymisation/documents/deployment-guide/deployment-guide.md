# Deployment Guide - Field-Level Pseudo-Anonymisation

## Purpose

This guide provides instructions for integrating and releasing the field-level-pseudo-anonymisation code location within an existing Dagster deployment.
This component is not deployed as a standalone service; instead, it is delivered as a Dagster code location whose Docker image is built via CI/CD and referenced by the Dagster infrastructure.

## Component Description

This component provides the Dagster code-location that implements field-level pseudonymisation logic used by the orchestration platform.
It contains the operations and jobs responsible for executing field-level pseudonymisation workflows, including encryption, decryption, redaction, and PII detection for both structured and unstructured data. The code-location is deployed as a dedicated container image and loaded by the main Dagster platform, where it becomes part of the available pipeline catalog.
Execution, monitoring, scheduling, and visualization of these pseudonymisation pipelines are handled directly by the Dagster webserver and daemon components already deployed in the target environment. The service integrates with OpenBao for secure encryption key management and supports multi-language PII detection using Scrubadub and spaCy.

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture
  - **Test Environment**: Minimum 1 vCPU, 512MB RAM per node
  - **Production Environment**: Minimum 2+ vCPUs, 2GB+ RAM per node (recommended: 4 vCPUs, 4GB RAM for high-throughput workloads)
- **Operating System**: Linux-based Kubernetes nodes (Ubuntu 20.04+, CentOS 7+, or compatible)
- **Dagster platform**: An existing Dagster deployment (webserver + daemon + run launcher) in the target cluster — this repository provides a code-location container image that must be loaded by that Dagster instance. The code-location itself is not a full Dagster platform.
- **Network**: 
  - Outbound internet access for image pulls from GitLab Container Registry
  - Ingress controller for external access
  - Open required ports (gRPC port 4000 for internal cluster communication)
- **Storage**:
  - Dagster metadata DB (PostgreSQL) should use persistent volumes in production.
- **Compute and Scheduling**:
  - The Kubernetes cluster should be able to schedule short-lived run pods with the CPU/memory needed by your pseudonymisation jobs.
- **Security & Permissions**:
  - Kubernetes: Service account with permissions to create deployments, services, jobs, and pods in the target namespace
  - Container Registry: Pull access to `code.europa.eu:4567/simpl/simpl-open/development/data-services/field-level-pseudo-anonymisation`
  - Secrets: Access to Kubernetes secrets for database credentials, Vault tokens, and TLS certificates
  - Vault: Read access to encryption keys stored in OpenBao (AppRole or Kubernetes auth method recommended)

---

## 2. Configuration Details

The configuration for this code location is not managed within this repository but is fully handled by the Dagster infrastructure. The Docker image produced by the CI/CD pipeline is referenced in the Dagster values.yaml file, which defines the code location name, repository entry point, environment variables, and Kubernetes resources. As a result, the only action required for deployment is updating the image tag in the values.yaml file used by the Dagster deployment.

An example of the code-location configuration in the values.yaml file can be found here → [Config example](/yaml/values-dagster-field-level-pseudo-anonymisation.yaml).

### Key Configuration Aspects

The Dagster values.yaml should include:

- **Image reference**: Points to the GitLab container registry with the desired version tag
- **Environment variables**: Database connection details, Vault configuration (VAULT_ADDR, VAULT_TOKEN)
- **Resource limits**: CPU and memory allocation based on expected workload
- **Health probes**: Liveness and readiness checks for the gRPC code server

## 3. Step-by-Step Deployment

Deployment requires no direct actions in this repository. The CI/CD pipeline builds and publishes the Docker image automatically, and the only step needed to roll out a new version is updating the image tag in the Dagster values.yaml file. Once the tag is updated, the Dagster deployment (via Helm or ArgoCD) will pull the new image and refresh the code location accordingly.

### Deployment Process

1. **CI/CD builds the image**: On commit/merge to main branch, GitLab CI builds and pushes the Docker image to the container registry with appropriate tags.
2. **Update Dagster values.yaml**: Modify the image tag in the Dagster deployment's values.yaml to reference the new version.
3. **Apply changes**: Use Helm upgrade or ArgoCD sync to update the Dagster deployment with the new code location image.
4. **Verify in Dagster UI**: Navigate to Workspace → Code Locations and confirm `field-level-pseudo-anonymisation` is loaded successfully with available jobs:
   - `anonymize_pseudonymize_structured_job`
   - `depseudonymize_structured_job`
   - `anonymize_pseudonymize_depseudonymize_structured_job`
   - `anonymize_pseudonymize_unstructured_job`
   - `depseudonymize_unstructured_job`

## References

- [Dagster Documentation](https://docs.dagster.io/)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [OpenBao Documentation](https://openbao.org/docs/)
