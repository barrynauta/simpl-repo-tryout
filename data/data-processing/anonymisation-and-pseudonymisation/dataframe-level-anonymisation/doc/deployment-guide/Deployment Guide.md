# Deployment Guide - Dataframe-Level Anonymisation

## Purpose
This guide provides instructions for integrating and releasing the dataframe-level-anonymisation code location within an existing Dagster deployment.
This component is not deployed as a standalone service; instead, it is delivered as a Dagster code location whose Docker image is built via CI/CD and referenced by the Dagster infrastructure.

## Component Description
This component provides the Dagster code-location that implements the anonymisation logic used by the orchestration platform.
It contains the operations and jobs responsible for executing dataframe-level anonymisation workflows, including algorithms such as k-anonymity, l-diversity, and t-closeness. The code-location is deployed as a dedicated container image and loaded by the main Dagster platform, where it becomes part of the available pipeline catalog.
Execution, monitoring, scheduling, and visualization of these anonymisation pipelines are handled directly by the Dagster webserver and daemon components already deployed in the target environment.

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture
  - **Test Environment**: Minimum 2 vCPUs, 4GB RAM per node
  - **Production Environment**: Minimum 4+ vCPUs, 8GB+ RAM per node (recommended: 8 vCPUs, 16GB RAM)
- **Operating System**: Linux-based Kubernetes nodes (Ubuntu 20.04+, CentOS 7+, or compatible)
- **Dagster platform**: An existing Dagster deployment (webserver + daemon + run launcher) in the target cluster — this repository provides a code-location container image that must be loaded by that Dagster instance. The code-location itself is not a full Dagster platform.
- **Network**: 
  - Outbound internet access for image pulls from GitLab Container Registry
  - Ingress controller for external access
  - Open required ports (see section 2.3)
- **Storage**:
  - Dagster metadata DB (PostgreSQL) should use persistent volumes in production.
- **Compute and Scheduling**:
  - The Kubernetes cluster should be able to schedule short-lived run pods with the CPU/memory needed by your anonymisation jobs.
- **Security & Permissions**:
  - Kubernetes: Service account with permissions to create deployments, services, jobs, and pods in the target namespace
  - Container Registry: Pull access to `code.europa.eu:4567/simpl/simpl-open/development/data-services/dataframe-level-anonymisation`
  - Secrets: Access to Kubernetes secrets for database credentials and TLS certificates

---

## 2. Configuration Details

The configuration for this code location is not managed within this repository but is fully handled by the Dagster infrastructure. The Docker image produced by the CI/CD pipeline is referenced in the Dagster values.yaml file, which defines the code location name, repository entry point, environment variables, and Kubernetes resources. As a result, the only action required for deployment is updating the image tag in the values.yaml file used by the Dagster deployment.

An example of the code-location configuration in the vaules.yaml file can be found here → [Config example](/yaml/values-dagster-dataframe-level-anonymisation.yaml).

## 3. Step-by-Step Deployment

Deployment requires no direct actions in this repository. The CI/CD pipeline builds and publishes the Docker image automatically, and the only step needed to roll out a new version is updating the image tag in the Dagster values.yaml file. Once the tag is updated, the Dagster deployment (via Helm or ArgoCD) will pull the new image and refresh the code location accordingly.

## References
- [Dagster Documentation](https://docs.dagster.io/)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)