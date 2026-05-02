# Upgrade guide

## Upgrade to v2.12.x

To enable and configure the keycloak user removal feature, see the [deployment guide](../deployment-guide/README.md#configure-keycloak-service-account).

To configure the new `onboarding` realm, see the `ONBOARDING-REALM.md` guide in the [Tier 1 Authentication documentation](https://code.europa.eu/simpl/simpl-open/development/iaa/tier1-authentication).

## Upgrade to v2.10.x

To enable and configure the new eIDAS feature, see the [deployment guide](../deployment-guide/README.md#eidas-configuration).

**Note:** To use eIDAS functionalities, keycloak eIDAS plugin installation is required: [keycloak-eidas-plugin-guide](https://code.europa.eu/simpl/simpl-open/development/iaa/eidas-demo-keycloak-extension/-/blob/main/README.md?ref_type=heads)

**Important:** The eIDAS assertion implementation is a beta type and at this moment it can be used only in a no production environment

**Update** appConfig entry with eidas configuration:

```yaml
appConfig:
  eidas:
    enabled: true
    integration:
      type: [EIDAS_ASSERTION_IMPLEMENTATION_TYPE]
      properties:
        user-info-endpoint: {{tier1-gateway-url}}/auth/realms/authority/protocol/openid-connect/userinfo
```

**Upgrade** the version via helm upgrade:

```bash
helm upgrade onboarding onboarding-charts/onboarding \
--version 2.10.0 \
--values values.yaml
```

## Upgrade to v2.9.x

To enable and configure the new eIDAS feature, see the [deployment guide](../deployment-guide/README.md#eidas-configuration).

**Upgrade** the version via helm upgrade:

```bash
helm upgrade onboarding onboarding-charts/onboarding \
--version 2.9.0 \
--values values.yaml
```

## Upgrade to v2.8.x

**Update** appConfig entry with the email service configuration:

```yaml
appConfig:
  email-service:
    onboarding-request-url:
      applicant-url-template: {{tier1-gateway-url}}/onboarding/application/additional-request
      notary-url-template: {{tier1-gateway-url}}/onboarding/administration/{id}
```

**Upgrade** the version via helm upgrade:

```bash
helm upgrade onboarding onboarding-charts/onboarding \
--version 2.8.1 \
--values values.yaml
```

## Upgrade up to version 2.7
For upgrades prior to version 2.7, please refer to the 'UPGRADING.md' file in the appropriate version of the 'version_docs' (https://code.europa.eu/simpl/simpl-open/development/iaa/documentation/-/tree/main/versioned_docs) folder within the central documentation repository.