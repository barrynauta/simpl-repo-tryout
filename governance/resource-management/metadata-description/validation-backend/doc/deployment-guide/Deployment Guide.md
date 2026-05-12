# Deployment Guide

## Purpose
This guide provides step-by-step instructions and best practices for deploying the `validation-api-be` project into production or controlled environments, including cloud, on-premises, containers, and Kubernetes. It covers environment requirements, configuration, deployment workflows, scaling, monitoring, security, and recovery procedures.

## Component Description
The component enables validation for self-describing data (SD) tools, ensuring that data adheres to defined schemas and policies.

## Prerequisites
- No outside dependencies required.

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture, minimum 2 vCPUs, 4GB RAM (production: 4+ vCPUs, 8GB+ RAM recommended).
- **Operating System**: Linux (Ubuntu 20.04+, CentOS 7+, or compatible). Windows containers are not supported.
- **Network**: Outbound internet access for image pulls and updates. Open required ports (see below).
- **Security & Permissions**:
    - Docker/Kubernetes: User must have permissions to manage containers and images.
    - Secrets: No secrets required.

---

## 2. Configuration Details

- **Environment Variables**: Set via Docker/Kubernetes manifests or `.env` files.
- **Config Files**: Mount configuration files as volumes or use Kubernetes ConfigMaps/Secrets.
- **Secrets Management**: No secrets required.

---

## 3. Step-by-Step Deployment

### A. Docker
1. **Build the image** (if not using a published one):
   ```sh
   docker build -t validation-api-be:latest .
   ```
2. **Run the container**:
   ```sh
   docker run -d --name validation-api-be \
     -p 8080:8080 \
     validation-api-be:latest
   ```

### B. Kubernetes (using Helm charts)
1. **Configure values** in `charts/values.yaml` (or override via CLI):
    - Required Helm variables to configure:
      ```yaml
      # Logging configuration
      log4j.config: <value>
      
      # OpenAPI configuration
      openapiConfig.servers: <value>
      
      # OpenTelemetry configuration
      openTelemetry.otlpExporter.endpoint: <value>
      openTelemetry.otlpExporter.protocol: <value>
      openTelemetry.propagators: <value>
      openTelemetry.environment: <value>
      openTelemetry.disabled: <value>
      ```
2. **Deploy with Helm**:
   ```sh
   helm install validation-api-be ./charts
   ```
3. **Setup with ArgoCD**:
    - Create an ArgoCD application pointing to your Helm chart repository
    - Configure sync options to use the Helm chart values
    - Set the target namespace and cluster for deployment
    - Enable automated sync if desired for continuous deployment

4. **Verify deployment**:
   ```sh
   kubectl get pods -l app=validation-api-be
   kubectl logs <pod-name>
   ```

5. **Check startup status**:
    - Verify the service is running correctly by calling the `/status` endpoint

### C. Cloud Platforms
- Use managed Kubernetes (EKS, AKS, GKE) or container services (ECS, ACI) as above.
- Ensure cloud firewalls/security groups allow required ports.

---

## 4. Scaling and Monitoring

- **Scaling**:
    - Docker: Run multiple containers behind a load balancer (e.g., NGINX, HAProxy).
    - Kubernetes: Set `replicaCount` in Helm values or use Horizontal Pod Autoscaler.
- **Monitoring**:
    - Integrate with Prometheus, Grafana, or cloud-native monitoring.
    - Expose health endpoints and configure liveness/readiness probes in Kubernetes.

---

## 5. Security Best Practices

- **Network**: This component should only be accessible from trusted networks or as internal cluster service.
- **Updates**: Regularly update base images and dependencies.

---

## 6. Rollback and Recovery

- **Docker**: Stop and remove the faulty container, then redeploy the previous image tag.
- **Kubernetes**: Use `helm rollback` or `kubectl rollout undo` to revert to a previous release.
- **Backups**: Regularly back up configuration, secrets, and persistent data.
- **Logs**: Aggregate logs for troubleshooting (e.g., ELK stack, cloud logging).

---

## References
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
