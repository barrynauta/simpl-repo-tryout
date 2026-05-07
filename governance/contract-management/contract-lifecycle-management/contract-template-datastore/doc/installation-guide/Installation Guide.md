# Installation Guide

## Prerequisites
- Operating system: Windows, macOS, Linux
- Docker installed
- Access to shell/terminal

## Installation Steps
1. Clone the repository:
   ```sh
   git clone https://code.europa.eu/simpl/simpl-open/development/data1/simpl-files
   ```
2. Build and start the nginx server using Docker (Dockerfile is already provided):
   ```sh
   docker build -t simpl-nginx .
   docker run -d -p 80:80 -v $(pwd)/files:/usr/share/nginx/html:ro simpl-nginx
   ```
   On Windows, use:
   ```bat
   docker run -d -p 80:80 -v %cd%\files:/usr/share/nginx/html:ro simpl-nginx
   ```

## Configuration
### Configuration Parameters
##### Deployment Configuration
###### This section defines the deployment baseline for the application instance.
---------------
| Parameter name | Description            | Default value | Allowed values/range | Minimum version | Status |
| -------------- | ---------------------- | ------------- | -------------------- | --------------- | ------ |
| replicaCount   | Number of pod replicas | 1             | integer ≥ 1          | 1.2.0           | Active |


##### Service Configuration
###### This section defines Kubernetes service exposure.
---------------
| Parameter name | Description                     | Default value | Allowed values/range              | Minimum version | Status |
| -------------- | ------------------------------- | ------------- | --------------------------------- | --------------- | ------ |
| service.type   | Kubernetes service type         | ClusterIP     | ClusterIP, NodePort, LoadBalancer | 1.2.0           | Active |
| service.port   | Service port exposed internally | 80            | integer (1–65535)                 | 1.2.0           | Active |

##### Resource Configuration
###### This section defines Kubernetes resource allocation (CPU and memory requests/limits).
---------------
| Parameter name            | Description    | Default value | Allowed values/range     | Minimum version | Status |
| ------------------------- | -------------- | ------------- | ------------------------ | --------------- | ------ |
| resources.limits.cpu      | CPU limit      | 500m          | Kubernetes CPU format    | 1.2.0           | Active |
| resources.limits.memory   | Memory limit   | 512Mi         | Kubernetes memory format | 1.2.0           | Active |
| resources.requests.cpu    | CPU request    | 200m          | Kubernetes CPU format    | 1.2.0           | Active |
| resources.requests.memory | Memory request | 128Mi         | Kubernetes memory format | 1.2.0           | Active |

##### Ingress Configuration
###### This section defines ingress exposure and TLS settings.
---------------
| Parameter name        | Description                     | Default value             | Allowed values/range         | Minimum version | Status |
| --------------------- | ------------------------------- | ------------------------- | ---------------------------- | --------------- | ------ |
| ingress.hostname      | Public hostname used by ingress | files.dev.simpl-europe.eu | valid DNS hostname           | 1.2.0           | Active |
| ingress.secretName    | TLS secret name                 | simpl-tls-files           | valid Kubernetes secret name | 1.2.0           | Active |
| ingress.clusterIssuer | Cluster issuer name             | dev-prod                  | string                       | 1.2.0           | Active |
| ingress.ingressClass  | Ingress class                   | nginx                     | string                       | 1.2.0           | Active |



## Troubleshooting
- Port 80 busy: Change the port with `-p <other>:80`
- Docker not running: Make sure Docker is running

## Compatible Versions
- Tested with Docker >= 20.10

## Automated Options
- Use the `build-docker-be-local.bat` script for local build on Windows
