# User Manual

This guide describes how to configure Keycloak both for the participant and the authority:

1. Install `Keycloak Authenticator` SPI
2. Delete obsolete mapper, client and client scopes
3. Create `dsRole` and `dsCredentialId` client scopes and enable them for the client in use
4. Enable `Direct access grants` authentication flow and enable the `Keycloak Authenticator` SPI for such flow

## 1. Install `Keycloak Authenticator` SPI

1.  Download the `keycloak-authenticator-x.x.x.jar` file. For example, using `curl`:
    ```bash
    curl -L -o keycloak-authenticator-x.x.x.jar https://code.europa.eu/api/v4/projects/915/packages/maven/com/aruba/simpl/keycloak-authenticator/x.x.x/keycloak-authenticator-x.x.x.jar
    ```
2.  Move the downloaded file to the `providers` directory of your Keycloak installation (e.g., `/opt/keycloak/providers`).
3.  Run `kc.sh build` or restart the Keycloak server for the changes to be applied.

## 2. Delete obsolete mapper and client scopes

1. In the Keycloak Admin UI, select your realm (e.g. `participant` or `authority`)
2. Open the `Clients` section and click on the client in use (e.g. `frontend-cli`)
3. On the `Client scopes` tab, click `frontend-cli-dedicated` (or the entry dedicated to the client in use)
4. In the `Mappers` tab, delete the `client-roles` (if present) mapper using the three dots to the right of the corresponding line
5. Open the `Clients` section and delete the `authenticator-client` (if present) using the three dots to the right of the corresponding line
5. Open the `Client scopes` section of your realm
6. Delete the following scopes (if present) using the three dots to the right of each line :
    * `dataspace-attribute`
    * `dsPublicKey` (this will be later replaced with another scope named `dsCredentialId`)

## 3. Create `dsRole` and `dsCredentialId` client scopes and enable them for the client in use

### Create `dsRole` client scope

1. In the Keycloak Admin UI, select your realm (e.g. `participant` or `authority`)
2. Open the `Client Scopes` section and click `Create client scope`
3. Fill out the form as follow:
    * In the `Name` field enter `dsRoles`
    * Disable `Display on consent screen `
4. Click `Save`
5. In the `Mappers` tab, click `Configure a new mapper` and select `User Session Note` mapper
6. Fill out the form as follow:
    * In the `Name` field enter `dsRoles`
    * In the `User Session Note` field enter `DS_ROLES`
    * In the `Token Claim Name` field enter `client-roles`
    * In the `Claim JSON Type` field select `JSON`
    * Disable all switches except `Add to access token`
7. Click `Save`

### Create `dsCredentialId` client scope

1. In the Keycloak Admin UI, select your realm (e.g. `participant` or `authority`)
2. Open the `Client Scopes` section and click `Create client scope`
3. Fill out the form as follow:
    * In the `Name` field enter `dsCredentialId`
    * Disable `Display on consent screen `
4. Click `Save`
5. In the `Mappers` tab, click `Configure a new mapper` and select `User Session Note` mapper
6. Fill out the form as follow:
    * In the `Name` field enter `dsCredentialId`
    * In the `User Session Note` field enter `DS_CREDENTIAL_ID`
    * In the `Token Claim Name` field enter `credential_id`
    * In the `Claim JSON Type` field select `String`
    * Disable all switches except `Add to access token`
7. Click `Save`

### Enable created scopes for the client in use

1. In the Keycloak Admin UI, select your realm (e.g. `participant` or `authority`)
2. Open the `Clients` section and click on the client in use (e.g. `frontend-cli`) and open the `Client scopes` tab
3. Use the `Add client scope` button to add the `dsRoles` client scope to the client. Select `Default` as `Assigned Type`
4. Use the `Add client scope` button to add the `dsCredentialId` client scope to the client. Select `Default` as `Assigned Type`

## 4. Enable `Direct access grants` authentication flow and enable the `Keycloak Authenticator` SPI for such flow

⚠️ This is configuration is enabled for development and testing purpuses and may be removed in the future

### Enable `Direct access grants` authentication flow for your client 

1. In the Keycloak Admin UI, select your realm (e.g. `participant` or `authority`)
2. Open the `Clients` section and click on the client in use (e.g. `frontend-cli`)
3. On the `Settings` tab, enabled `Direct access grants` authentication flow

### Enable the `Keycloak Authenticator` SPI for the `Direct access grants` authentication flow

1. In the Keycloak Admin UI, select your realm (e.g. `participant` or `authority`) and open the `Authentication` section
2. Duplicate the `direct grant (Built-in)` authentication flow by clicking the three dots to the right and choosing `Duplicate`. Give it a meaningful name, such as `custom direct grant`
3. Click on `Add step` and choose `Attribute Authenticator`. Click `Add`
4. Move the `Attribute Authenticator` step just below the existing `Password` step
5. Set the `Attribute Authenticator` step as `Required`
6. Go back to `Authentication` and bind the new `custom direct grant` authentication flow by clicking the three dots to the right and choosing `Bind flow`. Select `Direct grant flow` as binding type and click `Save`
7. The `custom direct grant` flow should be bound to the `Direct grant flow`, as shown in the `Used by` column
