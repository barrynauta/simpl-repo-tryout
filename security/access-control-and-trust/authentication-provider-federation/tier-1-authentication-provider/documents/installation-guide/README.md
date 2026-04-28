# Installation Guide

The Keycloak Authenticator is delivered as a deployable JAR file.
During the build process, the project produces an artifact located in the target/deploy directory.
This file represents the Keycloak provider and must be added to the Keycloak installation so that it can be loaded at startup.

### Build Instructions

You can follow these instructions to build the project manually:
From the project root:

``` bash
mvn package
```

The deployment artifact will be generated at:

    /target/deploy/<jar-name>.jar

Copy this file into your Keycloak container:

    /opt/bitnami/keycloak/providers/

Restart Keycloak afterwards.

---

## Provider Deployment

To install the component, the generated JAR must be placed inside the Keycloak providers directory.
A typical deployment places it under:

```
  /opt/keycloak/providers
```


(or the equivalent directory depending on the specific Keycloak distribution).

Once the file is present, Keycloak will detect and load the custom SPI module during its next startup.

## Required Configuration

The authenticator relies on external Simpl backend services.
The following environment variables must be defined in the Keycloak runtime environment:

- **AUTHENTICATION_PROVIDER_BASE_URL** - Defines the base URL of the Simpl Authentication Provider service (API Tier 1 V2).
- **USERS_ROLES_BASE_URL** - Defines the base URL of the Simpl Users & Roles service (API v1).

Both variables may be provided as plain URLs or as JSON maps when supporting multiple realms.


### Required Environment Variables

| Variable                           | Description                          | Example                                                             |
|------------------------------------|--------------------------------------|---------------------------------------------------------------------|
| `USERS_ROLES_BASE_URL`             | Base URL for Users & Roles service   | `http://users-roles.ns.svc.cluster.local:8080/tier1/v2`             |
| `AUTHENTICATION_PROVIDER_BASE_URL` | Base URL for Authentication Provider | `http://authentication-provider.ns.svc.cluster.local:8080/tier1/v2` |

### Optional Environment Variables

| Variable                          | Description                                                   | Default                               |
|----------------------------------|---------------------------------------------------------------|---------------------------------------|
| `ROLES_USER_SESSION_NOTE`         | Session note key for roles                                   | `DS_ROLES`                            |
| `ATTRIBUTES_USER_SESSION_NOTE`    | Session note key for attributes                              | `DS_ATTRIBUTES`                       |
| `CREDENTIAL_ID_USER_SESSION_NOTE` | Credential ID note key                                       | `DS_CREDENTIAL_ID`                    |
| `PARTICIPANT_ID_USER_SESSION_NOTE`| Participant ID note key                                      | `DS_PARTICIPANT_ID`                   |
| `CLIENT_ROLES_IGNORE_CLIENTS`     | Comma-separated list of clients whose roles should be ignored| `account, realm-management`           |
| `REALM_ROLES_IGNORE_ROLES`        | Realm roles to ignore                                        | `offline_access, uma_authorization`   |

### Multi‑Realm Support

You may pass JSON maps for services instead of `AUTHENTICATION_PROVIDER_BASE_URL` and `USERS_ROLES_BASE_URL`:

    AUTHENTICATION_PROVIDER_URLS_MAP={"authority":"https://auth-provider-authority/tier1/v2","participant":"https://auth-provider-participant/tier1/v2"}
    USERS_ROLES_URLS_MAP={"authority":"https://users-roles-authority/tier1/v2","participant":"https://users-roles-participant/tier1/v2"}

---
