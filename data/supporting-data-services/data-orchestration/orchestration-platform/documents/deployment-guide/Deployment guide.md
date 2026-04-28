# Deployment Guide

## Purpose
This guide provides step-by-step instructions and best practices for deploying the Dagster orchestration platform into production or controlled environments. It covers environment requirements, configuration, deployment workflows, scaling, monitoring, security, and recovery procedures for Kubernetes deployments using Helm and ArgoCD.

## Component Description
The component is a Dagster orchestration platform deployment that enables data pipeline orchestration and management. It includes multiple code locations for custom Dagster code jobs (like field-level pseudo-anonymisation, dataframe-level anonymisation, and others). The platform provides a web UI for pipeline visualization, monitoring, and execution control.

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture
  - **Test Environment**: Minimum 2 vCPUs, 4GB RAM per node
  - **Production Environment**: Minimum 4+ vCPUs, 8GB+ RAM per node (recommended: 8 vCPUs, 16GB RAM)
- **Operating System**: Linux-based Kubernetes nodes (Ubuntu 20.04+, CentOS 7+, or compatible)
- **Network**: 
  - Outbound internet access for image pulls from GitLab Container Registry
  - Ingress controller for external access
  - Open required ports (see section 2.3)
- **Storage**:
  - PostgreSQL requires persistent volume (production environment only)
  - Code locations may require persistent volumes for data processing (Optional)
- **Security & Permissions**:
  - Kubernetes: Service account with permissions to create deployments, services, jobs, and pods in the target namespace
  - Container Registry: Pull access to `code.europa.eu:4567/simpl/simpl-open/development/data-services`
  - Secrets: Access to Kubernetes secrets for database credentials and TLS certificates

---

## 2. Configuration Details

### 2.1 Environment Variables
Environment variables are configured in the Helm values.yaml file:

- **Dagster Webserver**:
  - `DAGSTER_ENVIRONMENT`: Environment identifier (e.g., "test", "production")
  - `LOG_LEVEL`: Logging verbosity (DEBUG for test, INFO for production)

- **Code Locations**:
  - Database credentials inherited from secrets (see section 2.4)
  - Custom environment variables can be added per code location in values.yaml

### 2.2 Config Files
Configuration is managed through three main files:

#### A. Helm Chart (`charts/Chart.yaml`)
Defines Dagster chart version and dependencies:
```yaml
apiVersion: v2
name: dagster
description: "Local wrapper chart for Dagster, for ArgoCD"
type: application
version: ${PROJECT_RELEASE_VERSION}
appVersion: ${PROJECT_RELEASE_VERSION}

dependencies:
  - name: dagster
    version: 1.11.11
    repository: "https://dagster-io.github.io/helm"
```

#### B. Values File (`charts/values.yaml`)
Contains all deployment-specific configuration including:
- **Code Location Deployments**: Configuration for each Dagster code location (image, resources, health checks)
- **Database Configuration**: PostgreSQL settings, persistence, and resource limits
- **Webserver Configuration**: UI settings, environment variables, and resource allocation
- **Ingress Configuration**: TLS, routing rules, and nginx annotations
- **Run Launcher**: Kubernetes job launcher configuration for pipeline execution
- **Security Settings**: Service accounts, security contexts, and RBAC

Key configuration sections:
```yaml
dagster:
  dagster-user-deployments:
    deployments:
      - name: <code-location-name>
        image:
          repository: code.europa.eu:4567/simpl/...
          tag: <version>
        resources:
          requests:
            cpu: 100m
            memory: 256Mi
          limits:
            cpu: 500m
            memory: 512Mi
  
  postgresql:
    enabled: true
    auth:
      existingSecret: postgres-secret
  
  dagsterWebserver:
    env:
      - name: DAGSTER_ENVIRONMENT
        value: "test"
      - name: LOG_LEVEL
        value: "DEBUG"
  
  ingress:
    enabled: true
    dagsterWebserver:
      host: <your-hostname>
      tls:
        enabled: true
        secretName: dagster-tls
```

#### C. ArgoCD Manifest (`argo/manifest.yaml`)
Defines GitOps deployment configuration:
```yaml
project: data2
destination:
  server: https://kubernetes.default.svc
  namespace: dataorchestrator
sources:
  - repoURL: >-
      https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/dagster.git
    targetRevision: develop
    ref: values
  - repoURL: https://code.europa.eu/api/v4/projects/1304/packages/helm/stable
    targetRevision: 0.0.1-SNAPSHOT.25.b80f193d
    helm:
      valueFiles:
        - $values/charts/values.yaml
    chart: dagster
```

This configuration:
- Deploys to the `dataorchestrator` namespace
- References both the Helm chart from GitLab package registry and values from Git repository
- Uses the `develop` branch for values
- Enables multi-source application pattern (Helm chart + values from Git)

### 2.3 Network Configuration
Required ports and endpoints:

| Service | Port | Protocol | Purpose |
|---------|------|----------|---------|
| Dagster Webserver | 80/443 | HTTP/HTTPS | Web UI and API access |
| Code Locations | 4000 | TCP | Internal gRPC communication |
| PostgreSQL | 5432 | TCP | Database connection |

**Ingress Configuration**:
- Host: `dagit-ui-test2.dataorchestrator.sandbx-cat-dat.simpl-europe.eu` (test environment)
- TLS enabled with cert-manager automatic certificate management
- Nginx ingress with custom timeouts and body size limits

### 2.4 Secrets Management

#### OpenBao/Vault Configuration (Recommended)
The deployment uses Bank-Vaults operator to inject secrets from OpenBao/Vault directly into pods. Secrets must be configured in OpenBao before deployment.

**Required secrets in OpenBao**:

1. **PostgreSQL Database Credentials**:
   ```sh
   vault kv put dev/data/dagster-postgres \
     password="YOUR_POSTGRES_PASSWORD"
   ```

2. **OAuth2 Proxy Secrets** (for Keycloak authentication):
   ```sh
   vault kv put dev/data/dagster-oauth2 \
     client-secret="YOUR_KEYCLOAK_CLIENT_SECRET" \
     cookie-secret="YOUR_COOKIE_SECRET"
   ```
   
   Note: To generate a secure cookie-secret:
   ```sh
   python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'
   ```

3. **Code Location Database Credentials** (if different from main database):
   ```sh
   vault kv put dev/data/dagster-code-location-db \
     username="YOUR_DB_USERNAME" \
     password="YOUR_DB_PASSWORD" \
     host="YOUR_DB_HOST" \
     database="YOUR_DB_NAME"
   ```

**Verify secrets**:
```sh
# List all Dagster secrets
vault kv list dev/data/ | grep dagster

# Read a specific secret (without showing values)
vault kv get dev/data/dagster-postgres
```

**How it works**:
- Pods have `vault.security.banzaicloud.io` annotations in values.yaml
- Bank-Vaults operator intercepts pod creation
- Secrets are injected as environment variables using `vault:` syntax
- Example: `password: "vault:dev/data/dagster-postgres#password"`

#### Alternative: Manual Kubernetes Secrets (Not Recommended)
If not using OpenBao/Vault, you can manually create Kubernetes secrets:

1. **Database Credentials** (`postgres-secret`):
   ```sh
   kubectl create secret generic postgres-secret \
     --from-literal=postgres-password=<password> \
     -n <namespace>
   ```

2. **OAuth2 Proxy Secrets**:
   ```sh
   kubectl create secret generic oauth2-proxy-secret \
     --from-literal=client-secret=<keycloak-client-secret> \
     --from-literal=cookie-secret=<cookie-secret> \
     -n <namespace>
   ```

3. **TLS Certificate** (`dagster-tls`):
   - Automatically managed by cert-manager with cluster issuer `dev-prod`
   - Or manually create with:
   ```sh
   kubectl create secret tls dagster-tls \
     --cert=path/to/tls.crt \
     --key=path/to/tls.key \
     -n <namespace>
   ```

4. **GitLab Container Registry Pull Secret** (optional, if not using public registry):
   ```sh
   kubectl create secret docker-registry gitlab-registry \
     --docker-server=code.europa.eu:4567 \
     --docker-username=<username> \
     --docker-password=<token> \
     -n <namespace>
   ```

---

## 3. Step-by-Step Deployment

### A. Manual Deployment with Helm

1. **Clone the repository**:
   ```sh
   git clone https://code.europa.eu/simpl/simpl-open/development/orchestration-platform/dagster.git
   cd dagster
   ```

2. **Configure secrets in OpenBao/Vault**:
   ```sh
   # PostgreSQL password
   vault kv put dev/data/dagster-postgres \
     password="YOUR_POSTGRES_PASSWORD"
   
   # OAuth2 Proxy secrets
   vault kv put dev/data/dagster-oauth2 \
     client-secret="YOUR_KEYCLOAK_CLIENT_SECRET" \
     cookie-secret="$(python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())')"
   
   # Verify secrets are saved
   vault kv get dev/data/dagster-postgres
   vault kv get dev/data/dagster-oauth2
   ```

3. **Review and customize values** in `charts/values.yaml`:
   - Update image tags for code locations
   - Adjust resource limits based on environment
   - Configure ingress hostname
   - Set appropriate environment variables

3. **Add Dagster Helm repository**:
   ```sh
   helm repo add dagster https://dagster-io.github.io/helm
   helm repo update
   ```

4. **Update chart dependencies**:
   ```sh
   cd charts
   helm dependency update
   ```

5. **Deploy with Helm**:
   ```sh
   # Create namespace if it doesn't exist
   kubectl create namespace dagster
   
   # Install or upgrade the release
   helm upgrade --install dagster . \
     --namespace dagster \
     --values values.yaml \
     --timeout 10m
   ```

6. **Verify deployment**:
   ```sh
   # Check pod status
   kubectl get pods -n dagster
   
   # Check services
   kubectl get svc -n dagster
   
   # Check ingress
   kubectl get ingress -n dagster
   
   # View logs
   kubectl logs -n dagster -l app=dagster-webserver
   ```

7. **Check startup status**:
   - Access the web UI: `https://dagit-ui-test2.dataorchestrator.sandbx-cat-dat.simpl-europe.eu`
   - Verify all code locations are loaded and healthy
   - Check that scheduled runs and sensors are active (if configured)

### B. GitOps Deployment with ArgoCD

1. **Configure secrets in OpenBao/Vault** (prerequisite):
   ```sh
   # PostgreSQL password
   vault kv put dev/data/dagster-postgres \
     password="YOUR_POSTGRES_PASSWORD"
   
   # OAuth2 Proxy secrets
   vault kv put dev/data/dagster-oauth2 \
     client-secret="YOUR_KEYCLOAK_CLIENT_SECRET" \
     cookie-secret="$(python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())')"
   
   # Verify secrets
   vault kv get dev/data/dagster-postgres
   vault kv get dev/data/dagster-oauth2
   ```

2. **Configure ArgoCD application**:
   - The application manifest is provided in `argo/manifest.yaml`
   - This references both the Helm chart from GitLab package registry and values from Git

3. **Deploy via ArgoCD CLI**:
   ```sh
   # Apply the ArgoCD application manifest
   kubectl apply -f argo/manifest.yaml -n argocd
   
   # Sync the application
   argocd app sync dagster
   
   # Watch deployment progress
   argocd app wait dagster --health
   ```

3. **Deploy via ArgoCD UI**:
   - Navigate to ArgoCD web interface
   - Click "New App" or "Create Application"
   - Use the configuration from `argo/manifest.yaml`:
     - **Application Name**: dagster
     - **Project**: data2
     - **Sync Policy**: Automatic (optional)
     - **Repository URL**: `https://code.europa.eu/api/v4/projects/1304/packages/helm/stable`
     - **Chart**: dagster
     - **Target Revision**: As specified in manifest
     - **Values Files**: `$values/charts/values.yaml`
     - **Values Repository**: Git repository URL
     - **Destination Cluster**: In-cluster
     - **Namespace**: dataorchestrator

4. **Verify deployment**:
   ```sh
   # Check ArgoCD application status
   argocd app get dagster
   
   # Check Kubernetes resources
   kubectl get all -n dataorchestrator -l app.kubernetes.io/instance=dagster
   
   # View ArgoCD sync logs
   argocd app logs dagster
   ```

5. **Enable auto-sync** (optional):
   ```sh
   argocd app set dagster --sync-policy automated --auto-prune --self-heal
   ```

### C. Updating Code Location Images

Code location images are managed by GitLab CI/CD. To update:

1. **Automatic Update** (via CI/CD):
   - GitLab CI/CD pipeline automatically updates image tags in values.yaml
   - Changes are committed to the repository
   - ArgoCD detects changes and syncs automatically (if auto-sync is enabled)

2. **Manual Update**:
   ```sh
   # Edit values.yaml to update image tag
   vi charts/values.yaml
   
   # Commit and push changes
   git add charts/values.yaml
   git commit -m "Update image tag for <code-location-name>"
   git push
   
   # If using ArgoCD, sync the application
   argocd app sync dagster
   ```

### D. Managing Code Locations

To add a new code location:

1. **Add deployment configuration** in `charts/values.yaml` under `dagster.dagster-user-deployments.deployments`:
   ```yaml
   - name: new-code-location
     location_name: new_code_location
     enabled: true
     enableSubchart: true
     codeServerArgs:
       - "--host"
       - "0.0.0.0"
       - "--port"
       - "4000"
       - "--python-file"
       - "src/new_code_location/repository.py"
     image:
       pullPolicy: IfNotPresent
       repository: code.europa.eu:4567/simpl/simpl-open/development/data-services/new-code-location
       tag: 0.0.1
     port: 4000
     resources:
       requests:
         cpu: 100m
         memory: 256Mi
       limits:
         cpu: 500m
         memory: 512Mi
   ```

2. **Deploy the updated configuration**:
   ```sh
   helm upgrade dagster ./charts --namespace dagster --values charts/values.yaml
   ```

To disable a code location:

1. Set `enabled: false` in the deployment configuration
2. Redeploy with Helm or sync with ArgoCD

---

## 4. Scaling and Monitoring

### 4.1 Scaling

**Horizontal Scaling - Code Locations**:
- Not typically needed as each code location runs as a single deployment
- For high-availability, consider running multiple instances with a load balancer
- Dagster itself manages parallelism within pipelines

**Horizontal Scaling - Webserver**:
```yaml
# In values.yaml
dagster:
  dagsterWebserver:
    replicaCount: 3  # Run multiple replicas
```

**Horizontal Scaling - Daemon**:
- The Dagster daemon should typically run as a single instance
- Multiple instances can lead to duplicate job execution

**Vertical Scaling**:
Adjust resource limits in `values.yaml`:
```yaml
resources:
  requests:
    cpu: 200m      # Increase from 100m
    memory: 512Mi  # Increase from 256Mi
  limits:
    cpu: 1000m     # Increase from 500m
    memory: 2Gi    # Increase from 512Mi
```


**Run Concurrency**:
Adjust maximum concurrent runs in `values.yaml`:
```yaml
dagster:
  dagsterDaemon:
    runCoordinator:
      config:
        queuedRunCoordinator:
          maxConcurrentRuns: 10  # Increase from 5
```


**Horizontal Pod Autoscaler (HPA)**:
The structure for the HPA configuration stored in the /templates/hpa.yaml file.
The exact values can be set up in `values.yaml`:
```yaml
# In values.yaml
hpa:
  webserver:
    enabled: true # --> boolean flag to enable/disable HPA
    minReplicas: 2 # --> minimum number of the pods
    maxReplicas: 7 # --> maximum number of the pods
    cpuTarget: 70 # --> CPU target, maximum usage per pod
    memoryTarget: 75 # --> Memory target, maximum usage per pod
```

### 4.2 Monitoring

**Built-in Monitoring**:
- Access Dagster web UI for pipeline runs, schedules, and sensors
- View run logs directly in the UI
- Monitor resource usage per run

**Kubernetes Monitoring**:
```sh
# Monitor pod resources
kubectl top pods -n dagster

# Monitor pod status
kubectl get pods -n dagster -w

# View pod events
kubectl get events -n dagster --sort-by='.lastTimestamp'
```

**Log Aggregation**:
- Integrate with ELK stack, Loki, or cloud-native logging
- Logs are emitted to stdout/stderr for easy collection
- Configure log level via `LOG_LEVEL` environment variable

**Health Checks**:
- Liveness probes ensure pods are restarted if unhealthy
- Readiness probes ensure traffic is only sent to ready pods
- Startup probes handle slow-starting containers

## 5. CI/CD Integration

### 5.1 GitLab CI/CD Pipeline
The project uses GitLab CI/CD to:
- Build and push code location images
- Update image tags in values.yaml

### 5.2 Pipeline Variables
Configure in `pipeline.variables.sh`:
```bash
PROJECT_VERSION_NUMBER="0.0.1"
```

### 5.3 Automated Deployment Flow
1. Developer commits code changes in a Data Service
2. GitLab CI builds Docker images
3. Images are pushed to container registry
4. CI updates values.yaml with new image tags
5. ArgoCD detects changes and syncs
6. New code locations are deployed

---

## References
- [Dagster Documentation](https://docs.dagster.io/)
- [Dagster Helm Chart](https://github.com/dagster-io/dagster/tree/master/helm)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)

