# User Manual

This guide describes how to configure the eIDAS Identity Provider, provided by the eIDAS Demo Keycloak Extension, in your Keycloak instance.

1. [Install `eIDAS Demo Keycloak Extension` SPI](#1-install-eidas-demo-keycloak-extension-spi)
2. [Configure `eIDAS` Identity Provider(s)](#2-configure-eidas-identity-providers)
3. [Configure `SMSSP Response` Identity Provider Mapper on your Identity Provider(s)](#3-configure-smssp-response-identity-provider-mapper-on-your-identity-providers)
4. [Add `Hardcoded User Session Attribute` Identity Provider Mapper to map `idp` claim](#4-add-hardcoded-user-session-attribute-identity-provider-mapper-to-map-idp-claim)
5. [Configuring Terms and Conditions Authenticators](#5-configuring-terms-and-conditions-authenticators)
6. [Configuring Attribute Authenticator Post Login Flow](#6-configuring-attribute-authenticator-post-login-flow)

## 1. Install `eIDAS Demo Keycloak Extension` SPI

1.  Download the `eidas-demo-keycloak-extension-x.x.x.jar` file. For example, using `curl`:
    ```bash
    curl -L -o eidas-demo-keycloak-extension-x.x.x.jar https://code.europa.eu/api/v4/projects/1313/packages/maven/eu/europa/ec/simpl/eidas-demo-keycloak-extension/x.x.x/eidas-demo-keycloak-extension-x.x.x.jar
    ```
2.  Move the downloaded file to the `providers` directory of your Keycloak installation (e.g., `/opt/keycloak/providers`).
3.  Run `kc.sh build` or restart the Keycloak server for the changes to be applied.

## 2. Configure eIDAS Identity Provider(s)

Since version `0.3.x`, the eIDAS Demo Keycloak Extension provides two distinct identity provider types, `eIDAS Demo Natural Person` and `eIDAS Demo Legal Person`, to support the different attribute sets required for natural and legal persons. 
When configuring an identity provider of either type, you will need to specify the mandatory and optional attributes that the user must acknowledge to share with the service provider upon login.

You can configure one or both identity provider types, depending on your use case. For example, if you want to allow both natural and legal persons to authenticate to your service, you can configure one identity provider of each type.

1. In the Keycloak Admin UI, select your realm (e.g. `authority`)
2. Open the `Identity Provider` section to create a new identity provider of type `eIDAS Demo Natural Person` or `eIDAS Demo Legal Person` according to your use case (or edit an existing one)
3. In the Identity Provider settings, configure the following fields:
    * `Client ID` (required): the ID of the service provider that will be used as part of the request from the service provider to the eIDAS connectors
    * `Service Provider Country of Origin` (required): The country code of the Service Provider (ISO 3166-1 alpha-2, e.g., IT for Italy, DE for Germany, or demo values such as CA, CB).
    * `Specific Connector URL` (required): The HTTP URL of the country "specific connector", the user will be redirected here to initiate the eIDAS login flow 
    * `Level of Assurance (LoA)` (required): Indicates the required trust level for electronic identities, from A (highest) through E (lowest). This determines the security and confidence required by the service provider for authentication.
    * `Comparison of LoA` (required): Logic for matching assurance level, with the following options: “minimum” to accept users with LoA equal to or higher than the configured value,“exact”  to accept only users whose LoA exactly matches the configured value.
    * `Provider Type` (required): "public" for public institutions, "private" for private organisations.
    * `Mandatory Attributes` (required): the identity attributes that either the Natural Person or the Legal Person MUST acknowledge to share with the service provider upon login
    * `Optional Attributes`: the identity attributes that either Natural Person or the Legal Person SHOULD acknowledge to share with the service provider upon login
    * `Supported Citizen Countries`: The list of citizen countries supported for eIDAS login. Please note that this is a demo plugin so only some countries are listed as an example.
4. Click `Add` (or `Save`, if updating) to apply the configuration

> ⚠️ Please note that a given combination of Service Provider Country and Citizen Country will only work if your [eIDAS demo node](https://code.europa.eu/simpl/simpl-open/development/iaa/eidas-demo-node-deploy) is correctly configured. 
> For a typical testing configuration, the `Service Provider Country of Origin` would be `CA` (Country A), assuming the citizen would select `CA` as their citizen country during login. 

Refer to the [eIDAS attribute profile](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eID+Profile?preview=/467109280/817168535/eIDAS%20SAML%20Attribute%20Profile%20v1.4.1_final.pdf) documentation for an overview of the eIDAS attributes.

### Mandatory and optional attributes configuration constraints

The following constraints apply when configuring the mandatory and optional attributes:

* Each identity provider type (Natural Person or Legal Person) only allows configuring eIDAS attributes that are relevant for that person type.
* All attributes that are included in the minimum data set for the selected person type must be included in the mandatory attributes (they are selected by default according to the identity provider type).
* No attribute can be included in both the mandatory and optional attributes.

## 3. Configure `SMSSP Response` Identity Provider Mapper on your Identity Provider(s)

The `SMSSP Response` identity provider mapper is responsible for mapping the SMSSP Response received from the eIDAS demo node to a user session note, which can then be mapped to the OIDC `/userinfo` endpoint via a standard Keycloak protocol mapper.

The `SMSSP Response` identity provider mapper needs to be configured for both the `eIDAS Demo Natural Person` and `eIDAS Demo Legal Person` identity providers, if both are configured.

To configure the `SMSSP Response` identity provider mapper, go to the `Identity Providers` tab of your Keycloak realm and perform the following steps for each of your eIDAS Demo identity providers:

1. Select your eIDAS Demo identity provider and go to the `Mappers` tab
2. Click on `Add mapper` and `SMSSP Response` as the mapper type
3. Select a name for your identity provider mapper (e.g., `SMSSP Response Mapper`) and click `Save` (you can leave the other fields with the default values)

This mapper wil map the SMSSP Response to a user session note with specified key (`smssp_response` by default). A protocol mapper can then be used to map the user session note to the OIDC `/userinfo` endpoint. To configure it, go to the `Clients` tab of your Keycloak realm and perform the following steps for your client:

1. Select your client and go to the `Client Scopes` tab
2. Click on the `dedicated` client scope associated with your client (e.g., `your-client-dedicated`)
3. Go to the `Mappers` tab and click on `Add mapper > By configuration` 
4. Select the `User Session Note` mapper type
5. In the `Add mapper` form:
   1. Enter a name for the mapper (e.g., `SMSSP Response Mapperr`)
   2. Enter the user session note name configured in the previous steps (e.g. `smssp_response`) as `User Session Note`
   3. Enter `smssp_response` as the `Token Claim Name`
   4. Set `Claim JSON Type` to `String`
   5. Enable only `Add to user info` (other options can be disabled)
   6. Click `Save`

## 4. Add `Hardcoded User Session Attribute` Identity Provider Mapper to map `idp` claim

IAA Components require the `idp` token claim to identify the Identity Provider used during authentication. This information must be mapped from the eIDAS Demo Identity Provider to the brokered user session, so that it can then be mapped to the user token by a standard Keycloak protocol mapper.

To configure an `Hardcoded User Session Attribute` identity provider mapper, go to the `Identity Providers` tab of your Keycloak realm and perform the following steps for your eIDAS Demo identity provider. Do this for both `eIDAS Demo Natural Person` and `eIDAS Demo Legal Person` if you have both configured:

1. Select your eIDAS Demo identity provider and go to the `Mappers` tab
2. Click on `Add mapper` and `Hardcoded User Session Attribute` as the mapper type
3. Select a name for your identity provider mapper (e.g., `idp session attribute mapper`)
4. Enter the user session attribute name as `User Session Attribute` (for example, `idp`)
5. Enter `eidas` as `User Session Attribute Value`
6. Click `Save` (you can leave the other fields with the default values)

This mapper will set the `eidas` user session note with the specified key (`idp` in the example). A protocol mapper can then be used to map the user session note to the user access token. To configure it, go to the `Clients` tab of your Keycloak realm and perform the following steps for your client:

1. Select your client and go to the `Client Scopes` tab
2. Click on the `dedicated` client scope associated with your client (e.g., `your-client-dedicated`)
3. Go to the `Mappers` tab and click on `Add mapper > By configuration`
4. Select the `User Session Note` mapper type
5. In the `Add mapper` form:
   1. Enter a name for the mapper (e.g., `idp mapper`)
   2. Enter the user session note name configured in the previous steps (e.g. `idp`) as `User Session Note`
   3. Enter `idp` as the `Token Claim Name`
   4. Set `Claim JSON Type` to `String`
   5. Enable only `Add to access token` (other options can be disabled)
   6. Click `Save`

## 5. Configuring Terms and Conditions Authenticators

To enable terms and conditions acceptance during the eIDAS login flow, you need to configure the appropriate authenticators in your Keycloak realm.

1. In the Keycloak Admin UI, select your realm (e.g., `authority`)
2. Go to the `Authentication` section and select the `Flows` tab
3. You'll need to customize the `first broker login` flow. To do that, first create a copy of the Built-in flow if you don't already have a custom one, using the `Duplicate` command.
4. Bind the copied flow as the `First broker login flow` using the `Bind flow` command.
5. Click on the name of your custom `first broker login` flow to edit it.
6. Click the `Add execution` button and select the `Ask the user to accept terms and conditions` authenticator from the list.
7. Drag the newly added execution to the desired position in the flow (typically after the `Review Profile` execution), and set it as `Required`.
8. Click the `Add execution` button and select the `Create user if unique and terms and conditions accepted` authenticator from the list.
9. Drag the newly added execution to replace the existing `Create user if unique` execution, and set it as `Required` (the previous execution must be removed or set as `Disabled`).

## 6. Configuring Attribute Authenticator Post Login Flow

If you need to enable the eIDAS login for Simpl-Open agent internal users (which rely on [Keycloak Authenticator](https://code.europa.eu/simpl/simpl-open/development/iaa/keycloak-authenticator) functionalities), 
you'll need to configure a custom post login flow.  

1. In the Keycloak Admin UI, select your realm (e.g., `authority`)
2. Go to the `Authentication` section and click on `Create flow`
3. In the `Create flow` form, enter a name for your flow (e.g., `Attribute Authenticator Post Login Flow`) and select `Basic flow` as the flow type
4. Enter a meaningful description for your flow and click `Create`
5. Click on the name of the flow you just created to edit it, then click the `Add execution` button and select the `Attribute Authenticator` authenticator from the list
6. Set the `Attribute Authenticator` execution as `Required`
7. Go to the `Identity providers` section and select your eIDAS Demo identity provider(s) (do this for both `eIDAS Demo Natural Person` and `eIDAS Demo Legal Person` if you have both configured)
8. In the `Post login flow` field, select the custom flow you just created (e.g., `Attribute Authenticator Post Login Flow`) and click `Save`