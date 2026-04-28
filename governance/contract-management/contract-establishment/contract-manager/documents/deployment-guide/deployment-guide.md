# Deployment Guide

## Purpose
This guide provides step-by-step instructions and best practices for deploying the `simpl-contract` project into production 
or controlled environments, including cloud, on-premises, containers, and Kubernetes. 
It covers environment requirements, configuration, deployment workflows, scaling, monitoring, security, 
and recovery procedures.

## Component Description
This component provides following functionalities:
- Functionality extending the participants contract management to store, consult or update (as appropriate) the signed
  contracts established via DataSpace connectors interaction between consumer and provider participants at contract
  negotiation and signature.
- Functionality extending the participants contract management additional negotiation steps in the contract
  establishment.
- Functionality reporting on and enforcing resources usage defined in contracts, including the trigger of contract
  closure, decommissioning of resources trigger. Monitoring functionality expected to contribute to this trigger
  and usage reporting.

## Prerequisites
- Kafka server
- Vault (to connect to the vault service provider class is used and vault instance should allow that)
- Postgres database
- update env values in charts/values.yaml (see section: Environment variables)

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture, minimum 2 vCPUs, 4GB RAM (production: 4+ vCPUs, 8GB+ RAM recommended).
- **Operating System**: Linux (Ubuntu 20.04+, CentOS 7+, or compatible). Windows containers are not supported.
- **Network**: Outbound internet access for image pulls and updates. Open required ports (see below).
- **Security & Permissions**:
    - Docker/Kubernetes: User must have permissions to manage containers and images.
    - Secrets: Vault variables and values

---

## 2. Step-by-Step Deployment

### A. Docker
1. **Build the image** (if not using a published one):
   ```sh
   docker build -t simpl-contract:latest .
   ```
2. **Run the container**:
   ```sh
   docker run -d --name simpl-contract \
     -p 8080:8080 \
     simpl-contract:latest
   ```

### B. Kubernetes (using Helm charts)
1. **Configure values** in `charts/values.yaml` (or override via CLI):
2. **Deploy with Helm**:
   ```sh
   helm install simpl-contract ./charts
   ```
3. **Setup with ArgoCD**:
    - Create an ArgoCD application pointing to your Helm chart repository
    - Configure sync options to use the Helm chart values
    - Set the target namespace and cluster for deployment
    - Enable automated sync if desired for continuous deployment

4. **Verify deployment**:
   ```sh
   kubectl get pods -l app=simpl-contract
   kubectl logs <pod-name>
   ```

5. **Check startup status**:
    - Verify the service is running correctly by calling the `/status` endpoint

### C. Cloud Platforms
- Use managed Kubernetes (EKS, AKS, GKE) or container services (ECS, ACI) as above.
- Ensure cloud firewalls/security groups allow required ports.

---

## 3. Scaling and Monitoring

- **Scaling**:
    - Docker: Run multiple containers behind a load balancer (e.g., NGINX, HAProxy).
    - Kubernetes: Set `replicaCount` in Helm values or use Horizontal Pod Autoscaler.
- **Monitoring**:
    - Integrate with Prometheus, Grafana, or cloud-native monitoring.
    - Expose health endpoints and configure liveness/readiness probes in Kubernetes.

---

## 4. Security Best Practices

- **Network**: This component should only be accessible from trusted networks or as internal cluster service.
- **Updates**: Regularly update base images and dependencies.

---

## 5. Rollback and Recovery

- **Docker**: Stop and remove the faulty container, then redeploy the previous image tag.
- **Kubernetes**: Use `helm rollback` or `kubectl rollout undo` to revert to a previous release.
- **Backups**: Regularly back up configuration, secrets, and persistent data.
- **Logs**: Aggregate logs for troubleshooting (e.g., ELK stack, cloud logging).

---

## References
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
