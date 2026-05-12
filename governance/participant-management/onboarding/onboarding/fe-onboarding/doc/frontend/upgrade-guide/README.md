# Upgrade guide

## Upgrade from 2.11.x to 2.12.x

The 2.12.x release contains some updates to the **Keycloak Configuration**. Specifically, you need to set up the ***onboarding*** realm.
Refer to the `Onboarding Realm` document of [Tier1-authentication](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-authentication) to configure the onboparding realm.

The additional Keycloak configuration for eIDAS is no longer required.

The EIDAS_IDP variable is no longer required.

The onboarding scope is no longer required.

All the Notary functionalities are moved to the [***fe-identity-provider*** component](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-identity-provider).

All the Onboarding Templates Management functionalities are moved to the [***fe-identity-provider*** component](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-identity-provider).

## Upgrade from 2.10.x to 2.11.x

The 2.10.x release contains some updates to the **Keycloak Configuration**. Specifically, you need to activate [User Registration](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-authentication#enable-user-registration). It is highly recommended to configure a secure [Password Policy](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-authentication#configure-password-policy).

## Upgrade from 2.9.x to 2.10.x

The 2.10.x release contains some updates to the **eIDAS Configuration**. The upgrade from 2.9.x to 2.10.x follows the instructions in the [Deployment Guide](../deployment-guide/README.md).

## Upgrade from 2.8.x to 2.9.x

The 2.9.x release contains the **eIDAS Configuration**. The upgrade from 2.8.x to 2.9.x follows the instructions in the [Deployment Guide](../deployment-guide/README.md).

## Upgrade from 2.7.x to 2.8.x

The 2.8.x release does not require any configuration changes. The upgrade from 2.7.x to 2.8.x requires no special actions.

## Upgrade from 2.6.x to 2.7.x

To perform the upgrade, uninstall the **simpl-fe** component (version **2.6.0**) and install the new **2.7.0** release, following the instructions in the [Deployment Guide](../deployment-guide/README.md).
