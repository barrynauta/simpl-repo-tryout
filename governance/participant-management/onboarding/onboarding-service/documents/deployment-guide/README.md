# Deployment Guide

This guide provides instructions for deploying the Onboarding service using Helm charts in a Kubernetes environment.

## Prerequisites

- A Kubernetes cluster
- Helm - the package manager for Kubernetes. See https://helm.sh/
- kubectl - the Kubernetes command-line tool that allows you to run commands against Kubernetes clusters. See https://kubernetes.io/docs/reference/kubectl/kubectl/

> **⚠️** *Step only needed for the governance authority*

## Deployment Steps

```shell
# 770 is the project_id of this repository
helm repo add onboarding-charts https://code.europa.eu/api/v4/projects/770/packages/helm/stable

helm install onboarding onboarding-charts/onboarding \
--version <chart version> \
--values values.yaml

```

> **💡** The latest `2.8.x` chart version can be found in the releases section of the project's repository. Please note that hotfixes may have been released since the last major update. Hotfixes may have been released. [Link to releases](https://code.europa.eu/simpl/simpl-open/development/iaa/users-roles/-/releases).

#### Kafka Configuration
To configure kafka, you need to update your values.yaml with the entry `kafkaConfig`.

- The value `kafkaConfig.spring.kafka` can be built following the spring documentation for the standard kafka configuration
- The value `kafkaConfig.simpl.kafka.topic.prefix` is used to differentiate the topics for the kafka inbox/outbox pattern. Don't change it.

#### eIDAS Configuration
To configure eIDAS, you need to update the `appConfig` entry of your values.yaml with an `eidas` entry.

- The value `appConfig.eidas.enabled` is used to enable/disable the eIDAS integration (default: `false`)
- The value `appConfig.eidas.attributes-file-path` is used to provide the path to the eIDAS attributes configuration file (default: `classpath:eidas/eidasAttributes.json`)
- The value `appConfig.eidas.integration.type` is used to define the implementation of eIDAS integration
- The value `appConfig.eidas.integration.properties.user-info-endpoint` is used to define keycloak userinfo endpoint to retrieve smssp_response with eIDAS document

Make sure to enable eIDAS in the [onboarding frontend](https://code.europa.eu/simpl/simpl-open/development/iaa/fe-onboarding/-/tree/develop/documents/deployment-guide) as well.

##### eIDAS Attributes Configuration File

> ⚠️ *The eIDAS attributes from the configuration file are referenced by eIDAS validation rules via the `uri` field. The file is loaded regardless of the `appConfig.eidas.enabled` flag to ensure that existing eIDAS validation rules are fully readable even if the eIDAS integration is later disabled.*

The eIDAS attributes configuration file is a JSON file containing an array of objects representing the available eIDAS attributes. Each object should contain the following fields:
- `friendlyName`: A user-friendly name for the attribute (e.g., "BirthName")
- `humanReadableName`: A human-readable name for the attribute (e.g., "Names at Birth")
- `personType`: The type of person the attribute applies to (e.g., "NATURAL_PERSON" or "LEGAL_PERSON")
- `category`: The category of the attribute (e.g., "MANDATORY_MINIMUM_DATA_SET", "OPTIONAL_MINIMUM_DATA_SET", "COMMON", "SECTOR_SPECIFIC")
- `uri`: The URI of the attribute (e.g., "http://eidas.europa.eu/attributes/naturalperson/BirthName")

##### Customizing eIDAS integration

The integration provided by the current implementation only supports the [eIDAS Demo node](https://code.europa.eu/simpl/simpl-open/development/iaa/eidas-demo-node-deploy).
To integrate with a different eIDAS node or to implement a custom logic for fetching/parsing the eIDAS assertion, you can develop your own implementation of the eIDAS integration by performing the following steps.

Modify the onboarding application by:
1. implementing a new [EidasAssertionFetcher](../../src/main/java/eu/europa/ec/simpl/onboarding/services/EidasAssertionFetcher.java) that fetches the eIDAS assertion data fom the user session
2. implementing a new [EidasAssertionParser](../../src/main/java/eu/europa/ec/simpl/onboarding/services/EidasAssertionParser.java) that parses the eIDAS assertion of the user based on the format that the member state has defined
3. annotate the implementation classes with `@ConditionalOnProperty(value = "eidas.integration.type", havingValue = "NAME_OF_CUSTOM_INTEGRATION")`
4. configure the `eidas.integration.type` property of the onboarding application  (see the [eIDAS Configuration](#eidas-configuration))
5. configure a map of properties under `eidas.integration.properties` to insert the properties that can be used by the custom implementations to fetch and parse the assertions

As reference, you can check the existing implementation for the eIDAS integration with Keycloak, which uses the `/userinfo` endpoint to fetch the eIDAS assertion and relies on a specific format of the assertion that is provided by the Keycloak eIDAS integration,
see [EidasAssertionDemoFetcherImpl](../../src/main/java/eu/europa/ec/simpl/onboarding/services/impl/EidasAssertionDemoFetcherImpl.java) and [EidasAssertionDemoParserImpl](../../src/main/java/eu/europa/ec/simpl/onboarding/services/impl/EidasAssertionDemoParserImpl.java).

##### Configure keycloak service account
To allow the onboarding service to delete users in keycloak when an onboarding request is rejected, you need to configure a keycloak service account with the appropriate permissions and provide its credentials in the `appConfig.keycloak` section of your values.yaml.
Below the explaonation of the fields:
- `keycloak.url`: the keycloak url
- `keycloak.realm`: the keycloak realm
- `keycloak.service-account.client-id`: the keycloak service account client id
- `keycloak.service-account.client-secret`: the keycloak service account client secret

#### Example of values.yaml
```yaml
hostT1: < participant or authority backend > # example: t1.authority.dev.simpl-europe.eu or t1.participant1.dev.simpl-europe.eu
authorityHostT2: < authority tier-2 url >  # example: t2.authority.dev.simpl-europe.eu
db:
  url: "jdbc:postgresql://postgresql.{{ .Release.Namespace }}.svc.cluster.local:5432/onboarding"
  username: "onboarding"
  password: "onboarding"

microservices:
  identityProviderUrl: http://identity-provider.{{ .Release.Namespace }}.svc.cluster.local:8080
  usersRolesUrl: http://users-roles.{{ .Release.Namespace }}.svc.cluster.local:8080
  securityAttributesProviderUrl: http://security-attributes-provider.{{ .Release.Namespace }}.svc.cluster.local:8080

appConfig:
  scheduled-tasks:
    rejection-of-stale-onboarding-requests:
      cron: "*/5 * * * * *"
    evaluate-not-executed-validation-rules:
      cron: "*/5 * * * * *"
      rules-per-execution: 20
    evaluate-rule-execution-results:
      cron: "15,45 * * * * *"
      onboarding-request-per-execution: 20
    delete-rejected-onboarding-requests:
      cron: "*/5 * * * * *"
      retention-time: 10d
    handle-stuck-onboarding-requests:
      cron: "*/5 * * * * *"
      retention-time: 10m
  management:
   tracing:
     sampling:
       probability: [MANAGEMENT_TRACING_SAMPLING_PROBABILITY]
   otlp:
     tracing:
       endpoint: [MANAGEMENT_OTLP_TRACING_ENDPOINT]
  email-service:
    onboarding-request-url:
      applicant-url-template: https://fe.{{ .Release.Namespace }}.dev.simpl-europe.eu/onboarding/application/additional-request
      notary-url-template: https://fe.{{ .Release.Namespace }}.dev.simpl-europe.eu/onboarding/administration/{id}
  eidas:
    enabled: true
    integration:
      type: [EIDAS_ASSERTION_IMPLEMENTATION_TYPE]
      properties:
        user-info-endpoint: {{tier1-gateway-url}}/auth/realms/${keycloak.realm}/protocol/openid-connect/userinfo
  keycloak:
    url: <your-keycloak-url>
    realm: <your-keycloak-realm>
    service-account:
      client-id: <your-keycloak-service-account-client-id>
      client-secret: <your-keycloak-service-account-client-secret>

kafkaConfig:
  spring:
    kafka:
      bootstrap-servers: <your-kafka-url>
      producer:
        properties:
          security.protocol: SASL_PLAINTEXT
          sasl.mechanism: PLAIN
          sasl.jaas.config: org.apache.kafka.common.security.plain.PlainLoginModule required username="${KAFKA_USER:admin}" password="${KAFKA_PASSWORD:admin-location}";
      admin:
        auto-create: true
  simpl:
    kafka:
      topic:
        prefix: iaa.{{ .Release.Namespace }}.


```

## Additional Documentation

For more information, please refer to the [documentation repository](https://code.europa.eu/simpl/simpl-open/development/iaa/documentation). Select the correct version based on the release.

For a full overview of configuration properties, please refer to [Properties file](../installation-guide/PROPERTIES.md).
