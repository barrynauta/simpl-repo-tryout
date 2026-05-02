 # Deployment Guide

## Purpose
This guide provides step-by-step instructions and best practices for deploying the `schema-sync-adapter` project into production or controlled environments, including cloud, on-premises, containers, and Kubernetes. It covers environment requirements, configuration, deployment workflows, scaling, monitoring, security, and recovery procedures.

## Component Description
The component allows integration with the Gaia-X Data Space Connector ecosystem.

## Prerequisites
- Postgresql DB server
- Kafka broker
- Gaia-X Schema manager service proxed by the local agent Tier2 Proxy service
- Shared PVC where <username>/data/schemas will be created and updated
- Tier2 routing to receive notifications from the Schema Manager (cross agent)
- OpenBao Vault

---

## 1. Environment Requirements

- **Infrastructure**: x86_64 architecture, minimum 2 vCPUs, 4GB RAM (production: 4+ vCPUs, 8GB+ RAM recommended).
- **Operating System**: Linux (Ubuntu 20.04+, CentOS 7+, or compatible). Windows containers are not supported.
- **Network**: Outbound internet access for image pulls and updates. Open required ports (see below).
- **Security & Permissions**:
    - Docker/Kubernetes: User must have permissions to manage containers and images

---

## 2. Configuration Details

- **Environment Variables**: Set via Docker/Kubernetes manifests or `.env` files.
- **Config Files**: Mount configuration files as volumes or use Kubernetes ConfigMaps
- **Secrets Management**: No secrets required.

### 2.1 OpenBao Vault integration
1) create a Vault role for the application
2) create your Vault secrets engine
3) create two new Vault secrets for consumer and for dataprovider participant named *{{ .Release.Namespace }}-{{ .Release.Name }}*
4) edit your Helm *values.yaml* file and configure:
    - *vault.secretEngine*
    - *vault.role*
    - *vault.service*
5) adding the following vault entries

**Vault entries for the consumer participant**:

```
	# schema-manager keycloak client id
	AUTH_CLIENT_ID
	# schema-manager credentials for the keycloak client (to be used if auth.grant-type=client_credentials)
	AUTH_CLIENT_SECRET
	# schema-manager credentials for the keycloak user with role GA_SCHEMA_ADMIN (to be used if auth.grant-type=password)
	AUTH_USERNAME
	AUTH_PASSWORD
	
	# schema-sync-adapter kafka credentials
	KAFKA_AUTH_USERNAME
	KAFKA_AUTH_PASSWORD
	
	# schema-sync-adapter PostgreSQL DB credentials
	SPRING_DATASOURCE_MAIN_USERNAME
	SPRING_DATASOURCE_MAIN_PASSWORD
```

**Vault entries for the dataprovider participant**:

```
	# schema-manager keycloak client id
	AUTH_CLIENT_ID
	# schema-manager credentials for the keycloak client (to be used if auth.grant-type=client_credentials)
	AUTH_CLIENT_SECRET
	# schema-manager credentials for the keycloak user with role GA_SCHEMA_ADMIN (to be used if auth.grant-type=password)
	AUTH_USERNAME
	AUTH_PASSWORD
	
	# schema-sync-adapter kafka credentials
	KAFKA_AUTH_USERNAME
	KAFKA_AUTH_PASSWORD
	
	# schema-sync-adapter PostgreSQL DB credentials
	SPRING_DATASOURCE_MAIN_USERNAME
	SPRING_DATASOURCE_MAIN_PASSWORD
```

### 2.2 Postgresql DB server
As administrative user create the database, the application user role with privileges.
Use this script as example setting <schema_name>, <role_name>, <role_password>:

```
	CREATE ROLE <role_name> WITH LOGIN PASSWORD '<role_password>';
    CREATE DATABASE <schema_name> OWNER <role_name>;
    GRANT ALL PRIVILEGES ON DATABASE <schema_name> TO <role_name>; 
```

In the Helm values.yaml file configure <host>, <schema_name>.

```
	postgres:
  	  url: "jdbc:postgresql://<host>:5432/<schema_name>?ssl=false"
```

### 2.3 Kafka broker
In your Helm values.yaml file configure <host>, <port>.
You must also change consumer.groupId and topic.processSchemaEvent prefix 'dataprovider01' with an unique one
if the same kafka broker is shared beween providers and consumers agents.

```
kafka:
  bootstrapServers: "<host>:<port>"
  consumer:
    groupId: "dataprovider01.schema-sync-adapter"
  topic:
    processSchemaEvent: "dataprovider01.schema-sync-adapter.process-schema-event"
```


### 2.4 Schema manager service
In your Helm values.yaml file, configure <schema_manager_service_url> with the url to the Schema Manager service.
If the Schema Manager service is exposed by the tier2 gateway you have to use the Tier2 proxy service.

```
schemaManager:
  serviceUrl: "<schema_manager_service_url>"
```

### 2.5 PVC configuration
In application values.yaml file we already configured the values to the shared PVC as expected by other participant services (sd-tooling, xfsc-adv-search).

```
schemaVolumeClaim: nfs-storage-pvc
schemaPvcMountPath: /home/simpluser/data
```

> **⚠️ Warning**: Modifying these values may cause malfunctions if they are not aligned with those expected by other services. Ensure consistency across all components that share this persistent volume (sd-tooling, xfsc-adv-search, etc.) before making any changes.

### 2.6 Tier2 routing configuration
Add these rules to the Tier2 routing configuration to expose the service out of the participant agent
in order to receive notifications events from the Schema Manager:
	
```
abac:
  - method: POST
    path: "/schema-sync-adapter/**"
    disable-ephemeral-proof-check: true

spring-route-definitions:
    - id: schema-sync-adapter
        uri: http://schema-sync-adapter:8080
        predicates:
        - Path=/schema-sync-adapter/**
        filters:
        - StripPrefix=1
```


### 2.7 Authentication Client Configuration
In your Helm values.yaml file, configure the authentication client parameters for accessing the Schema Manager service.

The authentication supports two grant types:
- **client_credentials**: requires `AUTH_CLIENT_ID` and `AUTH_CLIENT_SECRET` from the vault.
- **password**: requires `AUTH_CLIENT_ID`, `AUTH_USERNAME`, and `AUTH_PASSWORD` from the vault.

Set `<auth.serviceUrl>` (base URL), `<auth.servicePath>` (token endpoint path), and the required fields according to your grant type and authentication provider (e.g., Keycloak):

**Configuration for `client_credentials` grant type**:

```yaml
auth:
  serviceUrl: "<auth_service_url>"
  servicePath: "<auth_service_path>"
  grantType: "client_credentials"
```

**Configuration for `password` grant type**:

```yaml
auth:
  serviceUrl: "<auth_service_url>"
  servicePath: "<auth_service_path>"
  grantType: "password"
```

### 2.8 Webhook Registration Configuration
The schema-sync-adapter automatically registers with the Schema Manager to receive event notifications.
Configure the **targetUrl** (the participant TIER2 URL of schema-sync-adapter service) parameter in your Helm `values.yaml` file:

```yaml
webhook:
  registration:
    # tier2 url to the schema-sync-adapter service to be used to compose the registered uri in the schema manager webhook (ending with the route context name)
    targetUrl: https://example.simpl-europe.eu/schema-sync-adapter
```
 
The Schema Manager will send event notifications (schema published/revoked) to this URL. This must be the external URL accessible from the Schema Manager (typically through Tier2 routing).


## 3. Step-by-Step Deployment

### A. Docker
1. **Build the image** (if not using a published one):
   ```sh
   docker build -t schema-sync-adapter:latest .
   ```
2. **Run the container**:
   ```sh
   docker run -d --name schema-sync-adapter \
     -p 8080:8080 \
     schema-sync-adapter:latest
   ```

### B. Kubernetes (using Helm charts)
1. **Configure values** in `charts/values.yaml` (or override via CLI)
      
2. **Deploy with Helm**:
   ```sh
   helm install schema-sync-adapter ./charts
   ```
3. **Setup with ArgoCD**:
    - Create an ArgoCD application pointing to your Helm chart repository
    - Configure sync options to use the Helm chart values
    - Set the target namespace and cluster for deployment
    - Enable automated sync if desired for continuous deployment

4. **Verify deployment**:
   ```sh
   kubectl get pods -l app=schema-sync-adapter
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
