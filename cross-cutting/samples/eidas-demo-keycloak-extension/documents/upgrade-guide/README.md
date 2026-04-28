# Upgrade guide

## Upgrading to v0.3.x

> ⚠️ Version 0.3.x introduced specialized eIDAS Identity Providers for Natural and Legal Persons as required by [SIMPL-22683](https://jira.simplprogramme.eu/browse/SIMPL-22683). 
> This implies that any existing identity provider of type `eidas-demo` must be deleted and recreated as either `eidas-demo-natural-person` or `eidas-demo-legal-person` (or both) depending on the use case.
> Please take note of your existing identity provider configuration before proceeding with the upgrade, because you will not be able to access it after the upgrade.

### Configure new identity provider(s) of type `eidas-demo-natural-person` and/or `eidas-demo-legal-person`

In order to upgrade to version 0.3.x, you will need to delete any existing identity provider of type `eidas-demo` and recreate it as either `eidas-demo-natural-person` or `eidas-demo-legal-person` depending on your use case, as explained in the [user manual](../user-manual/README.md#2-configure-eidas-identity-providers) instructions.

1. In the Keycloak Admin UI, select your realm (e.g. `authority`)
2. Open the `Identity Provider` section and open the existing `eidas-demo` identity provider (if any)
3. Take note of the existing configuration, as you will need to reapply it to the new identity provider(s)
4. Delete the existing `eidas-demo` identity provider
5. Create a new identity provider of type `eidas-demo-natural-person` and/or `eidas-demo-legal-person` according to your use case, and reapply the configuration following the [user manual](../user-manual/README.md#2-configure-eidas-identity-providers) instructions.

### Replace `SMSSP Response` Protocol Mapper with the `SMSSP Response` Identity Provider Mapper

In order to upgrade to version 0.3.x, you will need to replace the existing `SMSSP Response` protocol mapper with the new `SMSSP Response` identity provider mapper.

To remove it, go to the `Clients` tab of your Keycloak realm and perform the following steps:

1. Select your client and go to the `Client Scopes` tab
2. Click on the `dedicated` client scope associated with your client (e.g., `your-client-dedicated`)
3. Select any existing `SMSSP Response` protocol mapper and click on the `Delete` action to remove it

Then, configure the new `SMSSP Response` identity provider mapper (and related user session note protocol mapper) as explained in the [user manual](../user-manual/README.md#3-configure-smssp-response-identity-provider-mapper-on-your-identity-providers) instructions.

️️

## Upgrading to v0.2.x

Add the `SMSSP Response` protocol mapper to your configuration, as explained in the [user manual](../user-manual/README.md) instructions.