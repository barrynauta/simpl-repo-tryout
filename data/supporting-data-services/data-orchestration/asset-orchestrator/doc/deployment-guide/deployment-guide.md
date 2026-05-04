# Deployment Guide

## Purpose
This guide provides step-by-step instructions and best practices for deploying the `asset-orchestrator` service into production or controlled environments, including cloud, on-premises, containers, and Kubernetes. It covers environment requirements, configuration, deployment workflows, scaling, monitoring, security, and recovery procedures.

## Component Description
The Asset Orchestrator service provides a REST API for managing catalog assets, Dagster workflows, and their associations. It enables CRUD operations on catalog assets and workflows, validates YAML configurations with Dagster, manages active workflow associations, and executes workflows dynamically with placeholder replacement. The service integrates with Dagster GraphQL API for workflow orchestration, PostgreSQL for data persistence, HashiCorp Vault for secrets management, and OpenTelemetry for observability.

## Prerequisites
- PostgreSQL database (version 13+) with schema `asset-orchestrator` created
- Dagster deployment with GraphQL API accessible
- HashiCorp Vault instance with Kubernetes authentication configured
- NFS or cloud storage for persistent data (optional)

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture
  - **Test Environment**: Minimum 1 vCPU, 512MB RAM per node
  - **Production Environment**: Minimum 2 vCPUs, 2GB RAM per node (recommended: 4 vCPUs, 4GB RAM for high-throughput workloads)
- **Operating System**: Linux-based Kubernetes nodes (Ubuntu 20.04+, CentOS 7+, or compatible). Windows containers are not supported.
- **Network**: 
  - Outbound internet access for image pulls from container registry
  - Ingress controller for external access (optional)
  - Open required ports (HTTP 8080 for API access)
  - Access to PostgreSQL database (port 5432)
  - Access to Dagster GraphQL API (port 3000)
  - Access to HashiCorp Vault (port 8200)
  - Access to OpenTelemetry Collector (port 4318)
- **Storage**:
  - PostgreSQL database with persistent volumes in production
  - Optional: Persistent volumes for application logs and temporary files
- **Security & Permissions**:
  - Kubernetes: Service account with permissions to create deployments, services, and pods in the target namespace
  - Container Registry: Pull access to the asset-orchestrator image repository
  - Database: Credentials with read/write access to the `asset-orchestrator` schema
  - Vault: Kubernetes authentication method configured with appropriate policies

---

## 2. Configuration Details

- **Environment Variables**: Set via Kubernetes manifests, ConfigMaps, or Helm values.
- **Config Files**: Application configuration is managed through `application.yml` (bundled in container) and overridden via environment variables.
- **Secrets Management**: All secrets are managed through HashiCorp Vault and injected via Vault Agent.

### 2.1 HashiCorp Vault Setup

The service requires Vault to be configured with the following:

1. **Enable Kubernetes authentication**:
   ```bash
   vault auth enable kubernetes
   
   vault write auth/kubernetes/config \
       kubernetes_host="https://kubernetes.default.svc:443"
   ```

2. **Create policy for asset-orchestrator**:
   ```bash
   vault policy write asset-orchestrator-policy - <<EOF
   path "asset-orchestrator/data/database" {
     capabilities = ["read"]
   }
   path "asset-orchestrator/data/otel" {
     capabilities = ["read"]
   }
   EOF
   ```

3. **Create Kubernetes role**:
   ```bash
   vault write auth/kubernetes/role/asset-orchestrator \
       bound_service_account_names=asset-orchestrator \
       bound_service_account_namespaces=dataorchestrator \
       policies=asset-orchestrator-policy \
       ttl=24h
   ```

4. **Store secrets in Vault**:
   ```bash
   # Database credentials
   vault kv put asset-orchestrator/database \
       username="postgres_user" \
       password="secure_password"
   
   # OpenTelemetry API key (optional)
   vault kv put asset-orchestrator/otel \
       apiKey="your_otel_api_key"
   ```

### 2.2 Database Setup

Create the PostgreSQL database and schema:

```sql
CREATE DATABASE orchestration_platform;

\c orchestration_platform

CREATE SCHEMA IF NOT EXISTS "asset-orchestrator";
```

The service uses Flyway for database migrations, which will automatically create the required tables on startup.

### 2.3 Helm Values Configuration

Required Helm variables to configure in `chart/values.yaml`:

```yaml
# Image configuration
image:
  repository: <your-registry>/asset-orchestrator
  tag: "1.0.0"
  pullPolicy: IfNotPresent

# Resource limits
resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 500m
    memory: 512Mi

# Database configuration
database:
  host: pg-cluster.common.svc.cluster.local
  port: 5432
  name: orchestration_platform

# HashiCorp Vault configuration
vault:
  enabled: true
  address: "http://vault.default.svc.cluster.local:8200"
  authPath: "auth/kubernetes"
  role: "asset-orchestrator"

# Dagster GraphQL configuration
dagster:
  graphql:
    url: http://dagster-dagster-webserver.dataorchestrator.svc.cluster.local:3000/dagster/graphql
    timeout: 30000
    maxRetries: 3

# OpenTelemetry configuration (optional)
opentelemetry:
  endpoint: http://otel-collector.common.svc.cluster.local:4318
  serviceName: asset-orchestrator
  tracesExporter: otlp
  metricsExporter: otlp
```

---

## 3. Step-by-Step Deployment

### A. Docker

1. **Build the image** (if not using a published one):
   ```sh
   docker build -t asset-orchestrator:latest .
   ```

2. **Run the container**:
   ```sh
   docker run -d --name asset-orchestrator \
     -p 8080:8080 \
     -e DB_HOST=postgres \
     -e DB_PORT=5432 \
     -e DB_NAME=orchestration_platform \
     -e DB_USER=postgres \
     -e DB_PWD=postgres \
     -e DAGSTER_GRAPHQL_URL=http://dagster:3000/dagster/graphql \
     asset-orchestrator:latest
   ```

3. **Verify deployment**:
   ```sh
   curl http://localhost:8080/v1/swagger-ui.html
   ```

### B. Kubernetes (using Helm charts)

1. **Add Helm repository** (if using a Helm registry):
   ```sh
   helm repo add asset-orchestrator <your-helm-repo-url>
   helm repo update
   ```

2. **Configure values** in `chart/values.yaml` or create an override file:
   ```yaml
   # values-production.yaml
   image:
     repository: code.europa.eu:4567/simpl/data-orchestrator/asset-orchestrator
     tag: "1.0.0"
   
   replicaCount: 3
   
   resources:
     limits:
       cpu: 1000m
       memory: 1Gi
     requests:
       cpu: 500m
       memory: 512Mi
   
   database:
     host: pg-cluster.common.svc.cluster.local
     port: 5432
     name: orchestration_platform
   ```

3. **Deploy with Helm**:
   ```sh
   helm install asset-orchestrator ./chart \
     --namespace dataorchestrator \
     --create-namespace \
     -f values-production.yaml
   ```

4. **Setup with ArgoCD**:
   - Create an ArgoCD application manifest:
     ```yaml
     apiVersion: argoproj.io/v1alpha1
     kind: Application
     metadata:
       name: asset-orchestrator
       namespace: argocd
     spec:
       project: default
       source:
         repoURL: https://code.europa.eu/simpl/data-orchestrator/asset-orchestrator.git
         targetRevision: main
         path: chart
         helm:
           valueFiles:
             - values.yaml
       destination:
         server: https://kubernetes.default.svc
         namespace: dataorchestrator
       syncPolicy:
         automated:
           prune: true
           selfHeal: true
     ```
   - Apply the manifest:
     ```sh
     kubectl apply -f argocd-application.yaml
     ```

5. **Verify deployment**:
   ```sh
   kubectl get pods -n dataorchestrator -l app.kubernetes.io/name=asset-orchestrator
   kubectl logs -n dataorchestrator -l app.kubernetes.io/name=asset-orchestrator
   ```

6. **Check health status**:
   ```sh
   kubectl port-forward -n dataorchestrator svc/asset-orchestrator 8080:8080
   curl http://localhost:8080/actuator/health
   ```

### C. Cloud Platforms

- **AWS EKS**: Use managed Kubernetes with Application Load Balancer for ingress
- **Azure AKS**: Use Azure Application Gateway or NGINX Ingress Controller
- **Google GKE**: Use Google Cloud Load Balancer with Ingress
- **Container Services**: Deploy to ECS, ACI, or Cloud Run with environment variables configured

Ensure cloud firewalls/security groups allow required ports:
- Inbound: 8080 (HTTP API)
- Outbound: 5432 (PostgreSQL), 3000 (Dagster), 8200 (Vault), 4318 (OTEL)

---

## 4. Scaling and Monitoring

### Scaling

- **Horizontal Scaling**:
  ```yaml
  # Enable HPA in values.yaml
  autoscaling:
    enabled: true
    minReplicas: 2
    maxReplicas: 10
    targetCPUUtilizationPercentage: 80
  ```

- **Manual Scaling**:
  ```sh
  kubectl scale deployment asset-orchestrator -n dataorchestrator --replicas=5
  ```

### Monitoring

- **Health Endpoints**:
  - Liveness: `/actuator/health/liveness`
  - Readiness: `/actuator/health/readiness`
  - Metrics: `/actuator/prometheus`

- **OpenTelemetry Integration**:
  - Traces exported to OTLP collector
  - Metrics exported via Prometheus endpoint
  - Service name: `asset-orchestrator`

- **Logging**:
  - Structured JSON logging (configurable log level)
  - Integration with ELK stack or cloud logging services

- **Dashboards**:
  - Import Grafana dashboards for Spring Boot applications
  - Monitor JVM metrics, HTTP requests, database connections

---

## 5. Security Best Practices

- **Network Security**:
  - Restrict inbound traffic to port 8080 only from trusted sources
  - Use NetworkPolicies in Kubernetes to limit pod-to-pod communication
  - Enable TLS/HTTPS for production deployments

- **Authentication & Authorization**:
  - API endpoints are currently unprotected (consider integration with OAuth2/JWT)
  - Vault authentication uses Kubernetes ServiceAccount tokens

- **Secret Management**:
  - All secrets stored in HashiCorp Vault
  - No secrets hardcoded in container images or manifests
  - Vault Agent injects secrets as Kubernetes Secrets

- **Container Security**:
  - Run as non-root user (UID 1001)
  - Use minimal base images (Alpine JRE)
  - Scan images for vulnerabilities with Trivy or similar tools

- **Updates**:
  - Regularly update base images and dependencies
  - Monitor CVE databases for security vulnerabilities
  - Apply security patches promptly

---

## 6. Rollback and Recovery

### Rollback Procedures

- **Helm Rollback**:
  ```sh
  # List release history
  helm history asset-orchestrator -n dataorchestrator
  
  # Rollback to previous version
  helm rollback asset-orchestrator -n dataorchestrator
  
  # Rollback to specific revision
  helm rollback asset-orchestrator 3 -n dataorchestrator
  ```

- **Kubernetes Rollout Undo**:
  ```sh
  kubectl rollout undo deployment/asset-orchestrator -n dataorchestrator
  kubectl rollout status deployment/asset-orchestrator -n dataorchestrator
  ```

- **ArgoCD Rollback**:
  - Navigate to the application in ArgoCD UI
  - Click "History" tab
  - Select previous revision and click "Rollback"

### Backup and Recovery

- **Database Backups**:
  ```sh
  # Backup PostgreSQL schema
  pg_dump -h pg-cluster.common.svc.cluster.local \
          -U postgres \
          -n asset-orchestrator \
          orchestration_platform > backup.sql
  
  # Restore from backup
  psql -h pg-cluster.common.svc.cluster.local \
       -U postgres \
       orchestration_platform < backup.sql
  ```

- **Configuration Backups**:
  - Store Helm values files in version control
  - Backup Vault secrets regularly
  - Export ConfigMaps and Secrets from Kubernetes

- **Disaster Recovery**:
  - Document all external dependencies (database, Dagster, Vault)
  - Maintain runbooks for common failure scenarios
  - Test recovery procedures regularly

### Troubleshooting

- **Pod Crashes**:
  ```sh
  kubectl describe pod <pod-name> -n dataorchestrator
  kubectl logs <pod-name> -n dataorchestrator --previous
  ```

- **Database Connection Issues**:
  - Verify database credentials in Vault
  - Check network connectivity: `kubectl exec -it <pod-name> -- nc -zv <db-host> 5432`
  - Review Flyway migration logs

- **Vault Authentication Failures**:
  - Verify ServiceAccount exists: `kubectl get sa asset-orchestrator -n dataorchestrator`
  - Check Vault role binding: `vault read auth/kubernetes/role/asset-orchestrator`
  - Review Vault Agent logs in pod annotations

- **Dagster API Errors**:
  - Verify Dagster webserver is running
  - Test GraphQL endpoint: `curl http://dagster:3000/dagster/graphql`
  - Check network policies and service mesh configuration

---

## 7. API Documentation

Once deployed, the API documentation is available at:
- Swagger UI: `http://<service-url>/v1/swagger-ui.html`
- OpenAPI JSON: `http://<service-url>/v1/api-docs`
- OpenAPI Specification: See `openapi/openapi-asset-orchestrator-v1.yaml`

### API Overview

The Asset Orchestrator API provides REST endpoints for managing workflow definitions and their execution. The API follows REST best practices and RFC 7807 Problem Details for error responses.

**Base URL**: `/v1`

### Main Endpoints

#### 1. Workflow Definitions (`/v1/workflowDefinitions`)

**Purpose**: Create and manage associations between catalog resources and workflows with YAML configuration templates.

- **POST `/v1/workflowDefinitions`**: Create a workflow definition
  - Associates a catalog resource (by `assetId`) with a workflow
  - Accepts YAML configuration with variable placeholders (e.g., `${APP_URL}`)
  - Request body:
    ```json
    {
      "assetId": "asset-001",
      "repositoryName": "my_repository",
      "codeLocation": "user_code",
      "jobName": "data_pipeline",
      "yamlConfiguration": {
        "ops": {
          "process_data": {
            "config": {
              "url": "${APP_URL}",
              "api_key": "${API_KEY}"
            }
          }
        }
      }
    }
    ```
  - Response (201 Created):
    ```json
    {
      "id": 1,
      "assetId": 1,
      "workflowId": 1,
      "associationTitle": "Data Processing Pipeline",
      "isActive": true,
      "yamlConfiguration": "ops:\n  process_data:\n    config:\n      url: ${APP_URL}"
    }
    ```
  - Errors: 400 (validation error), 404 (resource not found), 500 (internal error)

#### 2. Workflow Configuration (`/v1/workflows`)

**Purpose**: Retrieve available workflows, default configurations, and validate workflow configurations.

- **GET `/v1/workflows`**: Get available workflows
  - Retrieves all workflows from the orchestration engine that can be associated with resources
  - No request body required
  - Response (200 OK):
    ```json
    {
      "codeLocations": [
        {
          "id": "location-1",
          "name": "user_code",
          "loadStatus": "LOADED",
          "locationDetails": {
            "repositories": [
              {
                "id": "repo-1",
                "name": "my_repository",
                "jobs": [
                  {
                    "id": "job-1",
                    "name": "data_pipeline"
                  }
                ]
              }
            ]
          }
        }
      ],
      "total": 1
    }
    ```
  - Errors: 500 (internal error), 502 (WorkflowEngine communication error)

- **POST `/v1/workflows/defaultConfig`**: Get workflow default configuration
  - Retrieves the default configuration schema for a workflow
  - Used when creating a workflow definition to pre-populate configuration values
  - Request body:
    ```json
    {
      "repositoryName": "my_repository",
      "codeLocation": "user_code",
      "jobName": "data_pipeline"
    }
    ```
  - Response (200 OK):
    ```json
    {
      "jobName": "data_pipeline",
      "repositoryName": "my_repository",
      "codeLocation": "user_code",
      "defaultYamlConfig": "ops:\n  process_data:\n    config:\n      url: \"https://default.com\"",
      "success": true
    }
    ```
  - Errors: 400 (invalid input), 404 (workflow not found), 500 (internal error), 502 (WorkflowEngine error)

- **POST `/v1/workflows/validateConfig`**: Validate workflow configuration
  - Validates a workflow configuration against its schema before creating a workflow definition
  - Request body:
    ```json
    {
      "repositoryName": "my_repository",
      "codeLocation": "user_code",
      "jobName": "data_pipeline",
      "yamlConfiguration": {
        "ops": {
          "process_data": {
            "config": {
              "url": "${APP_URL}",
              "api_key": "${API_KEY}"
            }
          }
        }
      }
    }
    ```
  - Response (200 OK) - Valid configuration:
    ```json
    {
      "jobName": "data_pipeline",
      "isValid": true,
      "errors": []
    }
    ```
  - Response (200 OK) - Invalid configuration:
    ```json
    {
      "jobName": "data_pipeline",
      "isValid": false,
      "errors": [
        {
          "message": "Field \"url\" is required but not provided",
          "path": ["ops", "process_data", "config", "url"],
          "reason": "MISSING_REQUIRED_FIELD",
          "errorType": "FIELD_NOT_DEFINED",
          "fieldName": "url",
          "fieldNames": [],
          "valueRep": null
        }
      ]
    }
    ```
  - Errors: 400 (validation error), 500 (internal error), 502 (WorkflowEngine error)

### Error Handling

All error responses follow **RFC 7807 Problem Details** standard with BelGIF guidelines:

```json
{
  "type": "urn:problem-type:simpl:validationError",
  "title": "Validation Error",
  "status": 400,
  "detail": "Validation failed for one or more fields",
  "instance": "/v1/workflowDefinitions",
  "timestamp": "2024-12-03T10:15:30.123Z",
  "errors": {
    "assetId": "must not be blank",
    "yamlConfiguration": "Invalid YAML syntax"
  }
}
```

**Error Types**:
- `urn:problem-type:simpl:badRequest` (400)
- `urn:problem-type:simpl:validationError` (400)
- `urn:problem-type:simpl:resourceNotFound` (404)
- `urn:problem-type:simpl:internalServerError` (500)
- `urn:problem-type:simpl:externalServiceError` (502)

### Authentication

Currently, the API does not require authentication. For production deployments, consider integrating with OAuth2/JWT or API Gateway authentication mechanisms.

### Rate Limiting

No rate limiting is currently enforced. Consider implementing rate limiting at the ingress/API gateway level for production environments.

---

## References

- [Spring Boot Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
- [HashiCorp Vault Documentation](https://developer.hashicorp.com/vault/docs)
- [Dagster Documentation](https://docs.dagster.io/)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
