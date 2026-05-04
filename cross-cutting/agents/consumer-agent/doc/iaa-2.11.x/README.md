# IAA Installation documentation `2.11.x`

## Prerequisites

- A Kubernetes cluster
- Helm - the package manager for Kubernetes. See https://helm.sh/
- kubectl - the Kubernetes command-line tool that allows you to run commands against Kubernetes clusters. See https://kubernetes.io/docs/reference/kubectl/kubectl/

## Deployment of the components

To deploy an actor (for example, data provider or governance authority), follow this order:

- [Redis](#redis)
- [Postgresql](#postgresql)
- [Keycloak](#keycloak)
- [EJBCA](#ejbca) - *(⚠️ only deployed by the governance authority)*
- [Onboarding](#onboarding) - *(⚠️ only deployed by the governance authority)*
- [Security Attributes Provider](#security-attributes-provider) - *(⚠️ only deployed by the governance authority)*
- [Tier 1 Gateway](#tier-1-gateway)
- [Users Roles](#users-roles)
- [Identity Provider](#identity-provider) - *(⚠️ only deployed by the governance authority)*
- [Frontend](#frontend)
- [Tier 2 Gateway](#tier-2-gateway)
- [Authentication Provider](#authentication-provider)
- [Tier 2 Proxy](#tier-2-proxy)

Other information:
- [Agent initialization](#agent-initialization)
  - [Governance Authority init via Kubernetes](#governance-authority-init-via-kubernetes)
  - [Participant onboarding and initialization via Kubernetes](#participant-onboarding-and-initialization-via-kubernetes)
- [Checklist of healthy environment](#checklist-of-healthy-environment)
- [Business logging](#business-logging) configuration
- [Onboard a Participant into the dataspace](user-manual/ONBOARD.md)
- [Workflow for Managing Identity Attributes](user-manual/IDENTITY-ATTR.md)

> **💡** Tips: You can append `--kubeconfig <config file>` to any command without changing your local kubecofing file, where `<config file>` is the path to your custom kubeconfig. Append `-n <namespace_name>` to any command to install the charts in the selected namespace. Look also at [kubectx](https://github.com/ahmetb/kubectx)

> **💡** Tips: Create a new namespace with a name of your choice: `kubectl create namespace <namespace_name>`

Add the following chart repositories before starting:
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add keyfactor https://keyfactor.github.io/ejbca-community-helm/
```

## Redis

```bash
helm install redis bitnami/redis --version 19.6.0 --values < values path >
```
#### Example values.yaml

```yaml
auth:
  # Defaults to a random 10-character alphanumeric string if not set
  password: "admin"
```

## Postgresql

To install Postgresql chart, update the *initdb script* in `values-authority.yaml` or `values-participant.yaml` reasonably.
```bash
helm install postgresql bitnami/postgresql \
--version 15.2.5 \
--values < authority or participant postgres values path >
```
You can check that the initialization of the database has been successful by looking at the pod log or by connecting to it using an SQL client.

#### Example of values-authority.yaml

```yaml
primary:
  initdb:
    scripts:
      init.sql: |
        CREATE USER ejbca WITH PASSWORD 'ejbca2123' CREATEDB;
        CREATE DATABASE ejbca OWNER ejbca;
        CREATE USER keycloak WITH PASSWORD 'keycloak' CREATEDB;
        CREATE DATABASE keycloak OWNER keycloak;
        CREATE USER securityattributesprovider WITH PASSWORD 'securityattributesprovider' CREATEDB;
        CREATE DATABASE securityattributesprovider OWNER securityattributesprovider;
        CREATE USER onboarding WITH PASSWORD 'onboarding' CREATEDB;
        CREATE DATABASE onboarding OWNER onboarding;
        CREATE USER usersroles WITH PASSWORD 'usersroles' CREATEDB;
        CREATE DATABASE usersroles OWNER usersroles;
        CREATE USER identityprovider WITH PASSWORD 'identityprovider' CREATEDB;
        CREATE DATABASE identityprovider OWNER identityprovider;
        CREATE USER authenticationprovider WITH PASSWORD 'authenticationprovider' CREATEDB;
        CREATE DATABASE authenticationprovider OWNER authenticationprovider;

```

#### Example of values-participant.yaml

```yaml
primary:
  initdb:
    scripts:
      init.sql: |
        CREATE USER keycloak WITH PASSWORD 'keycloak' CREATEDB;
        CREATE DATABASE keycloak OWNER keycloak;
        CREATE USER usersroles WITH PASSWORD 'usersroles' CREATEDB;
        CREATE DATABASE usersroles OWNER usersroles;
        CREATE USER authenticationprovider WITH PASSWORD 'authenticationprovider' CREATEDB;
        CREATE DATABASE authenticationprovider OWNER authenticationprovider;
```

> **⚠️** The configuration examples use the users and passwords mentioned above. If you change them, ensure that your configuration reflects those changes accordingly.

## Keycloak

The `import-realm` init container allows you to download and copy from `code.europa.eu` the exported realm to a volume for an authority or participant. The exported realm contains pre-configured users for initialisation and demo purposes.

```bash
helm install keycloak bitnami/keycloak \
--version 25.2.0 \
--values < authority or participant keycloak values path >
```

#### Example of values.yaml



```yaml
image:
    repository: keycloak/keycloak
    tag: 26.4

defaultInitContainers:
  prepareWriteDirs:
    enabled: false
args:
  - start
  - --import-realm
  - --verbose
  - --proxy-headers
  - xforwarded

containerSecurityContext:
  runAsUser: 1000
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: false

apiUrl: "<authority or participant endpoint>" # example: https://participant.be.aruba-simpl.cloud
                                              # example: https://authority.be.aruba-simpl.cloud
extraEnvVars:
  - name: KC_HOSTNAME_ADMIN
    value: "< apiUrl as above >/auth" # update
  - name: KC_HOSTNAME
    value: "< apiUrl as above >/auth" # update
  - name: USERS_ROLES_BASE_URL
    value: "http://users-roles.{{ .Release.Namespace }}.svc.cluster.local:8080" # update
  - name: AUTHENTICATION_PROVIDER_BASE_URL
    value: "http://authentication-provider.{{ .Release.Namespace }}.svc.cluster.local:8080" # update
  - name: KEYCLOAK_BASE_URL
    value: "< apiUrl as above >/auth" # update
  - name: REALM
    value: "<authority or participant>" # set this
    value: "authority" # update
  - name: KEYCLOAK_ADMIN
    value: "admin"
  - name: KEYCLOAK_ADMIN_PASSWORD
    value: "admin"
  - name: KC_DB
    value: "postgres"
  - name: KC_DB_URL_HOST
    value: "postgresql.{{ .Release.Namespace }}.svc.cluster.local"
  - name: KC_DB_URL_PORT
    value: "5432"
  - name: KC_DB_URL_DATABASE
    value: "keycloak"
  - name: KC_DB_USERNAME
    value: "keycloak"
  - name: KC_DB_PASSWORD
    value: "keycloak"
  - name: KC_BOOTSTRAP_ADMIN_USERNAME
    value: "admin"
  - name: KC_BOOTSTRAP_ADMIN_PASSWORD
    value: "admin"

auth:
  adminUser: "user" # update
  adminPassword: "admin" # update

postgresql:
  enabled: false

externalDatabase:
  annotations: {}
  database: keycloak
  existingSecret: ""
  existingSecretDatabaseKey: ""
  existingSecretHostKey: ""
  existingSecretPasswordKey: ""
  existingSecretPortKey: ""
  existingSecretUserKey: ""
  host: "postgresql.{{ .Release.Namespace }}.svc.cluster.local" # update
  password: keycloak
  port: 5432
  user: keycloak

extraVolumes:
  - name: spi-volume
    emptyDir: {}
  - name: realm-volume
    emptyDir: {}

extraVolumeMounts:
  - name: spi-volume
    mountPath: /opt/keycloak/providers/keycloak-authenticator.jar
    subPath: keycloak-authenticator.jar
  - name: realm-volume
    mountPath: /opt/keycloak/data/import/realm.json
    subPath: realm.json

initContainers:
  - name: init-spi
    image: curlimages/curl
    command: ["/bin/sh", "-c"]
    env:
      - name: ARTIFACT
        value: keycloak-authenticator
      - name: URL
        value: https://code.europa.eu/api/v4/projects/915/packages/maven/com/aruba/simpl/keycloak-authenticator/2.4.0/keycloak-authenticator-2.4.0.jar
      # Uncomment the following lines to install eIDAS Demo Extension SPI
      # - name: EIDAS_EXTENSION_ARTIFACT
      #   value: keycloak-eidas-demo-authenticator
      # - name: EIDAS_EXTENSION_URL
      #   value: https://code.europa.eu/api/v4/projects/1313/packages/maven/eu/europa/ec/simpl/eidas-demo-keycloak-extension/0.0.1/eidas-demo-keycloak-extension-0.0.1.jar

    args:
      - |
        curl -o /custom-spi/${ARTIFACT}.jar ${URL};
      # Uncomment the following line to install eIDAS Demo Extension SPI
      #  curl -o /custom-spi/${EIDAS_EXTENSION_ARTIFACT}.jar ${EIDAS_EXTENSION_URL};
    volumeMounts:
      - name: spi-volume
        mountPath: /custom-spi

  - name: import-realm
    image: nginx:latest
    command: ["/bin/sh", "-c"]
    env:
      - name: REDIRECT_URIS
        # Adjust the array values accordingly, list all the needed frontend endpoints of other components
        value: |
          [ "https://fe.{{ .Release.Namespace }}.dev.simpl-europe.eu/*" ]
      - name: REALM_NAME
        value: realm
      - name: URL
        # uncomment below if you are deploying an authority
        # value: https://code.europa.eu/simpl/simpl-open/development/iaa/charts/-/raw/develop/samples/keycloak-realms/2.1.0/authority-realm-export.json?ref_type=heads
        # uncomment below if you are deploying a participant
        # value: https://code.europa.eu/simpl/simpl-open/development/iaa/charts/-/raw/develop/samples/keycloak-realms/2.1.0/participant-realm-export.json?ref_type=heads
    args:
      - |
        curl ${URL} | envsubst '$REDIRECT_URIS' > /config/${REALM_NAME}.json;
    volumeMounts:
      - name: realm-volume
        mountPath: /config
```

## EJBCA

> **⚠️** *Step only needed for the governance authority*

Before installing EJBCA, update the values in `values.yaml` reasonably to interact with the Postgresql instance.

```bash
helm install ejbca keyfactor/ejbca-community-helm --version 1.0.7 --values < ejbca values path >
```
Then follow the instructions here to configure EJBCA and continue with the deployment.

### EJBCA Configuration

The EJBCA configuration can be performed manually by following the instructions [here](./EJBCA.md) or automatically by means of an initialization container available in the `ejbca-preconfig` repository [here](https://code.europa.eu/simpl/simpl-open/development/iaa/ejbca-preconfig).

Configure EJBCA with one of the methods described above and continue with the deployment.

> **⚠️** To reinitialize EJBCA after using `ejbca-preconfig`, you don't need to delete the entire Kubernetes namespace. Instead, you can reset the environment by dropping the EJBCA database and deleting the related Kubernetes secret.

#### Example of values.yaml without `ejbca-preconfig`

```yaml
hostname: &ejbcaHostname ejbca-community-helm.<namespace>.svc.cluster.local # update this
fullnameOverride: ejbca-community-helm
ejbca:
  useEphemeralH2Database: false
  env:
    HTTPSERVER_HOSTNAME: *ejbcaHostname
    TLS_SETUP_ENABLED: "true"
    DATABASE_JDBC_URL: jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/ejbca # update this
    DATABASE_USER: "ejbca"
    DATABASE_PASSWORD: "ejbca2123"
nginx:
  host: *ejbcaHostname

# The following allows to not use a NodePort and have multiple istances of EJBCA on the same cluster
services:
  directHttp:
    type: ClusterIP
```

<!-- helm repo add <repo name> https://code.europa.eu/api/v4/projects/<project_id>/packages/helm/<channel> -->


## Onboarding
> **⚠️** *Step only needed for the governance authority*

### Deployment

**You can find information about deployment in the [deployment guide](https://code.europa.eu/simpl/simpl-open/development/iaa/onboarding/-/blob/v2.10.1/documents/deployment-guide/README.md?ref_type=tags).**


## Security Attributes Provider
> **⚠️** *Step only needed for the governance authority*

### Deployment

**You can find information about deployment in the [deployment guide](https://code.europa.eu/simpl/simpl-open/development/iaa/security-attributes-provider/-/blob/v2.10.1/documents/deployment-guide/README.md?ref_type=tags).**

## Tier 1 Gateway

### Deployment

**You can find information about deployment in the [deployment guide](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-gateway/-/blob/v2.10.1/documents/deployment-guide/README.md?ref_type=tags).**

## Users Roles

### Prerequisites

- *simpl-cloud-gateway* up and running
- *security-attributes-provider* up and running

### Deployment

**You can find information about deployment in the [deployment guide](https://code.europa.eu/simpl/simpl-open/development/iaa/users-roles/-/blob/v2.10.1/documents/deployment-guide/README.md?ref_type=tags).**

## Identity Provider
> **⚠️** *Step only needed for the governance authority*

### Prerequisites

- Possess EJBCA SuperAdmin credentials (i.e. PKCS#12 certificate - also named TrustStore - and password)
- Possess ManagementCA (also named TrustStore and its password), it can be downloaded from EJBCA Admin dashboard, as explained [here](./EJBCA.md#download-the-managementca-certificate).
- Deployed and running users-roles, security-attributes-provider, onboarding

### Deployment

**You can find information about deployment in the [deployment guide](https://code.europa.eu/simpl/simpl-open/development/iaa/identity-provider/-/blob/v2.9.1/documents/deployment-guide/README.md?ref_type=tags).**

## Frontend

For information on deploying micro-frontends, please refer to the dedicated guides for each individual micro-frontend listed below

#### Authority

- [onboarding](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-onboarding/-/blob/v2.10.1/documents/deployment-guide/README.md)
- [identity-provider](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-identity-provider/-/blob/v2.8.4/documents/deployment-guide/README.md)
- [security-attributes-provider](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-security-attribute-provider/-/blob/v2.8.1/documents/deployment-guide/README.md)
- [users-and-roles](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-users-and-roles/-/blob/v2.10.0/documents/deployment-guide/README.md)
- [authentication-provider](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-authentication-provider/-/blob/v2.8.5/documents/deployment-guide/README.md)

#### Participant

- [users-and-roles](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-users-and-roles/-/blob/v2.9.0/documents/deployment-guide/README.md)
- [authentication-provider](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-authentication-provider/-/blob/v2.9.0/documents/deployment-guide/README.md)

## Tier 2 Gateway

This microservice is a gateway for inbound Tier 2 API operation between agents and work only in https on mTLS.

### Prerequisites

- All the previous microservices up and runnning
- **⚠️** Only for the authority - init the authority as described [here](#authority-init).
- **⚠️** Only for the participant - obtain a credential from the authority by following this guide [here](user-manual/ONBOARD.md), and then install it on the participant. (Alternatively, you can use the `simpl-cli` for onboarding instead of the traditional UI. ollow the steps outlined [here](#participant-init) for CLI-based onboarding).

### Deployment

**You can find information about deployment in the [deployment guide](https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-gateway/-/blob/v2.9.0/documents/deployment-guide/README.md?ref_type=tags).️**

## Authentication Provider

### Prerequisites

- Users Roles up and running

### Deployment

**You can find information about deployment in the [deployment guide](https://code.europa.eu/simpl/simpl-open/development/iaa/authentication-provider/-/blob/v2.9.0/documents/deployment-guide/README.md?ref_type=tags).**

## Agent initialization

### Governance Authority init via APIs

In order to initialise the authority and obtain a valid certificate for mTLS communication with other participants, the following requests must be performed:

```bash
kubectl port-forward svc/authentication-provider 8080:8080
kubectl port-forward svc/identity-provider 8090:8080

export AUTHORITY_AUTH_PROVIDER=localhost:8080
export AUTHORITY_IDENTITY_PROVIDER=localhost:8090

# Generating keypair...
curl -X POST "$AUTHORITY_AUTH_PROVIDER/v1/keypairs/generate"

# Generating CSR...
curl -X POST "$AUTHORITY_AUTH_PROVIDER/v1/csr/generate" \
--header 'Content-Type: application/json' \
--data-raw '{
  "commonName": "<tier2 hostname>",
  "country": "<country>",
  "organization": "<organization name>",
  "organizationalUnit": "<organizational unit name>"
}' > csr.pem

# Creating Authority participant
PARTICIPANT_ID=$(curl -X POST "$AUTHORITY_IDENTITY_PROVIDER/v1/participants" \
--header 'Content-Type: application/json' \
--data-raw '{
  "organization": "<organization name>",
  "participantType": "GOVERNANCE_AUTHORITY"
}' | sed -E 's/^"(.*)"$/\1/')

# Uploading CSR ..
curl -X POST "$AUTHORITY_IDENTITY_PROVIDER/v1/participants/$PARTICIPANT_ID/csr" \
-F "csr=@/path/to/csr.pem"

# Downloading credentials ...
curl "$AUTHORITY_IDENTITY_PROVIDER/v1/credentials/$PARTICIPANT_ID/download" \
-o cert.pem

# Uploading credentials ...
curl -X POST "$AUTHORITY_AUTH_PROVIDER/v1/credentials" \
-F "credential=@/path/to/cert.pem"
```

### Governance Authority init via Kubernetes

*Prerequisite*: make sure you have the latest Keycloak configuration with the `cli` client configured

The authority initialization can be carried out in by deploying a kubernetes job as described in the SIMPL CLI [documentation](https://code.europa.eu/simpl/simpl-open/development/iaa/cli/-/tree/v2.2.1?#authority-initialization) in a fully automated way.

An example of the appropriate `values.yml` file can be found [here](https://code.europa.eu/simpl/simpl-open/development/iaa/cli/-/tree/v2.2.1?#example-of-values-for-authority-initialization)

### Participant onboarding and initialization via Kubernetes

> **⚠️**The initialisation of participants via Kubernetes is intended for use only in development or testing environments. In real-world scenarios, participants can only be onboarded via the UI.

*Prerequisite*: make sure you have the latest Keycloak configuration with the `cli` client configured

The participant onboarding and initialization can be carried out in by deploying a kubernetes job as described in the SIMPL CLI [documentation](https://code.europa.eu/simpl/simpl-open/development/iaa/cli/-/tree/v2.2.1?#participant-agent-initialization) in a fully automated way.

An example of the appropriate `values.yml` file can be found [here](https://code.europa.eu/simpl/simpl-open/development/iaa/cli/-/tree/v2.2.1?#example-of-values-for-participant-initialization)

## Checklist of healthy environment

Once deployment and initialisation of authority have been completed, participants should be able to be onboarded in the dataspace and communicate with each other.

Ensure the following components are correctly configured:
- tier2-gateway: Refer to the [Known behaviour](#known-behaviour) section for details,

## Business logging

Business logging can be enabled by adding `logging.business` values under `appConfig.external-routes` configuration. This applies to both the `tier1-gateway` and `tier2-gateway` components. The following are example:

```yaml
appConfig:
  external-routes:
    # ...
    logging:
      business:
        - method: POST
          path: /some/path/*
          config:
            message: This is an example of a message
            operations:
              - EXAMPLE_OPERATION_1
              - EXAMPLE_OPERATION_2
```

Business logging rules can be configured to match specific criteria, such as the presence of a particular header or query parameter. For example:

```yaml
appConfig:
  external-routes:
    # ...
    logging:
      business:
        - method: GET
          path: /some/path/*
          query: # Replace with 'header' to match against a header instead of a query parameter.
            - name: query1
          config:
            message: This is an example of a message
            operations:
              - EXAMPLE_OPERATION_1
              - EXAMPLE_OPERATION_2
```

If a specific value is provided, the rule will match only when the given header or query parameter contains that exact value. For example:

```yaml
appConfig:
  external-routes:
    # ...
    logging:
      business:
        - method: GET
          path: /some/path/*
          query: # Replace with 'header' to match against a header instead of a query parameter.
            - name: query1
              value: value1
          config:
            message: This is an example of a message
            operations:
              - EXAMPLE_OPERATION_1
              - EXAMPLE_OPERATION_2
```

A full configuration for business logging is as follows:

```yaml
appConfig:
  external-routes:
    # ...
    logging:
      business:
        - method: GET
          path: /some/path/*
          query: # multiple query params are in AND
            - name: name
              value: value # If not specified, the rule will match if the query param is present.
              # Specify either `value` (a single value) or `values` (a list of values).
              # Use `values` to define several acceptable options; these are evaluated with OR logic.
              # values:
              #   - a
              #   - b
          header: # multiple headers are in AND
            - name: name
              value: value # If not specified, the rule will match if the header is present.
              # Specify either `value` (a single value) or `values` (a list of values).
              # Use `values` to define several acceptable options; these are evaluated with OR logic.
              # values:
              #   - c
              #   - d
          config:
            message: "This is an example of a message"
            operations: # At least one is mandatory
              - EXAMPLE_OPERATION_1
              - EXAMPLE_OPERATION_2
```


## Tier 2 Proxy

For deployment/installation information, please refer to the [running-the-proxy-on-kubernetes](https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-proxy/-/tree/v1.2.1?ref_type=tags#running-the-proxy-on-kubernetes) section of the README in the tier2-proxy [repository](https://code.europa.eu/simpl/simpl-open/development/iaa/tier2-proxy).

### Known behaviour

Upon startup, the tier2-proxy try to find the installed certificate from authentication provider component.

This scenario can be traced to two main consequences:
- Missing certificate: the authority was not properly initialized, or a participant was not fully onboarded. The solution is to complete the missing steps and finally restart the proxy.
- Certificate retrieval failure: the tier2-proxy failed to retrieve a valid certificate from the authentication provider. The most common cause for this is the tier2-gateway starting up and requesting the certificate before the authentication provider is fully operational. Restarting the tier2-proxy after the authentication provider was confirmed to be up and running can resolve the issue.
