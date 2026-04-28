# Installation Guide

## Overview
This guide will help you install and run **simpl-contract** on a fresh system. 
Follow the steps for your operating system and refer to troubleshooting if you encounter issues.

---

## Prerequisites

- **Java**: JDK 21 or higher
- **Maven**: 3.9.x or higher
- **Git**: Latest stable version
- **Operating System**: Windows, macOS, or Linux
- **Internet Connection**: Required for downloading dependencies

> **Note:** Ensure your `JAVA_HOME` and `MAVEN_HOME` environment variables are set correctly.

---

## Step-by-Step Installation

### 1. Clone the Repository

```
git clone https://code.europa.eu/simpl/simpl-open/development/contract-billing/contract.git
cd contract-billing
```

### 2. Build the Project

#### Windows
Run:
```
#build_and_release.bat
```

#### macOS/Linux
Run:
```
chmod +x #build_and_release.bat
./#build_and_release.bat
```

_Alternatively, use Maven directly:_
```
mvn clean install
```

### 3. Run the Application

Refer to the documentation or run the generated JAR/WAR file as per your deployment needs.

---

### 4. Verify Installation

To verify the application is running correctly, call the `/status` endpoint:

```
curl http://localhost:<port>/status
```

Replace `<port>` with the actual port number configured for the application.

---

## Example Output

After a successful build, you should see output similar to:
```
[INFO] BUILD SUCCESS
```

---

## Troubleshooting

- **Java not found**: Ensure Java is installed and `JAVA_HOME` is set.
- **Maven not found**: Install Maven and add it to your PATH.
- **Permission denied (macOS/Linux)**: Run `chmod +x #build_and_release.bat`.
- **Dependency download errors**: Check your internet connection and proxy settings.

---

## Automated Options

- Use the provided `#build_and_release.bat` script for automated build and release.
- For Dockerized deployments, check for a `Dockerfile` or related scripts in the repository.

---

## Version Information

- **simpl-contract**: v1.0.0 or higher
- **Java**: 21+
- **Maven**: 3.9+

---

## 5. Configuration details

- **Environment Variables**: Set via Docker/Kubernetes manifests or `.env` files.
- **Config Files**: Mount configuration files as volumes or use Kubernetes ConfigMaps/Secrets.
- **Secrets Management**: Vault variables and values

### 5.1 HashiCorp Vault integration
1) create a Vault role for the application
2) create your Vault secrets engine
3) create a new Vault secret for **simpl-contract** application named *{{ .Release.Namespace }}-{{ .Release.Name }}*
4) edit your Helm *values.yaml* file and configure:
    - *vault.secretEngine*
    - *vault.role*
    - *vault.service*
5) add the following keys for the required component credentials:

| Parameter name             | Description                                                                        | Default value | Allowed values / range | Minimum version | Status |
|----------------------------|------------------------------------------------------------------------------------|---------------|------------------------|------------------|--------|
| API_KEY                    | API key used to authenticate requests to the application API                       | apikey        | Non-empty string       | 1.0.0            | Active |
| DBPASSWORD                 | Password used to authenticate with the application database                        | pass123       | Non-empty string       | 1.0.0            | Active |
| KAFKA_CLIENT_PASSWORDS     | Password used by Kafka clients to authenticate with the Kafka broker               | pass123       | Non-empty string       | 1.0.0            | Active |
| SIGNER_API_KEY             | API key used to authorize requests to the signing service                          | apikey        | Non-empty string       | 1.0.0            | Active |
| VC_ISSUER_API_KEY          | API key used to authorize requests to vc-issuer service (Verifiable Credentials)   | apikey        | Non-empty string       | 1.0.0            | Active |


### 5.2 Kafka variables

All Kafka-related variables, including dedicated topics for contract processing:
sign-contract-request: ${TOPIC_SIGN_CONTRACT_REQUEST}
sign-contract-request-dlt: ${TOPIC_SIGN_CONTRACT_REQUEST_DLT}
sign-contract-response: ${TOPIC_SIGN_CONTRACT_RESPONSE}
sign-contract-response-dlt: ${TOPIC_SIGN_CONTRACT_RESPONSE_DLT}
status-update: ${TOPIC_STATUS_UPDATE}
status-update-dlt: ${TOPIC_STATUS_UPDATE_DLT}
search-contract-request: ${TOPIC_SEARCH_CONTRACT_REQUEST}
search-contract-request-dlt: ${TOPIC_SEARCH_CONTRACT_REQUEST_DLT}
search-contract-response: ${TOPIC_SEARCH_CONTRACT_RESPONSE}
search-contract-response-dlt: ${TOPIC_SEARCH_CONTRACT_RESPONSE_DLT}
create-contract-request: ${TOPIC_CREATE_CONTRACT_REQUEST}
create-contract-request-dlt: ${TOPIC_CREATE_CONTRACT_REQUEST_DLT}
create-contract-response: ${TOPIC_CREATE_CONTRACT_RESPONSE}
create-contract-response-dlt: ${TOPIC_CREATE_CONTRACT_RESPONSE_DLT}
verification-request: ${TOPIC_VERIFICATION_REQUEST}
verification-request-dlt: ${TOPIC_VERIFICATION_REQUEST_DLT}
verification-response: ${TOPIC_VERIFICATION_RESPONSE}
verification-response-dlt: ${TOPIC_VERIFICATION_RESPONSE_DLT}

### 5.3 Environment variables

1. Database url and user
2. Vault variables and values
3. To deploy consumer deployment.mode should be CONSUMER, and deployment.vault.hashicorp.role should be "contract-consumer".
   To deploy provider deployment.mode should be PROVIDER, and deployment.vault.hashicorp.role should be "contract-provider".
4. otel (Open Telemetry) endpoint
5. file folder for storing contract negotiation files
6. api-key

---