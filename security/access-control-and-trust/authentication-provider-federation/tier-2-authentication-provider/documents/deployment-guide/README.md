# Deployment Guide

This guide provides instructions for deploying the Authentication Provider service using Helm charts in a Kubernetes environment.

## Prerequisites

- A Kubernetes cluster
- Helm - the package manager for Kubernetes. See https://helm.sh/
- kubectl - the Kubernetes command-line tool that allows you to run commands against Kubernetes clusters. See https://kubernetes.io/docs/reference/kubectl/kubectl/

> **⚠️** *Step only needed for the governance authority*

## Deployment Steps

```shell
# 939 is the project_id of this repository
helm repo add authentication-provider-charts https://code.europa.eu/api/v4/projects/939/packages/helm/stable

helm install authentication-provider authentication-provider-charts/authentication-provider \
--version <chart version> \
--values values.yaml
```

> **💡** The latest `2.7.x` chart version can be found in the releases section of the project's repository. Please note that hotfixes may have been released since the last major update. Hotfixes may have been released. [Link to releases](https://code.europa.eu/simpl/simpl-open/development/iaa/authentication_provider/-/releases).

#### Example of values.yaml
```yaml

db:
  cipherSecret: "authenticationprovider-db-cipher-secret" # name of the secret key that will be generated used to encrypt keys  

kafkaConfig:
  spring:
    kafka:
      bootstrap-servers: <your-kafka-url>
      producer:
        properties:
          security.protocol: SASL_PLAINTEXT
          sasl.mechanism: PLAIN
          sasl.jaas.config: org.apache.kafka.common.security.plain.PlainLoginModule required username="${KAFKA_USER:<your-kafka-username>}" password="${KAFKA_PASSWORD:your-kafka-password}";
      admin:
        auto-create: true
  simpl:
    kafka:
      topic:
        prefix: iaa.{{ .Release.Namespace }}.

appConfig:
  spring:
    profiles:
      active: # authority / participant

    datasource:
      url: "jdbc:postgresql://postgresql.{{ .Release.Namespace }}.svc.cluster.local:5432/authenticationprovider"
      username: "authenticationprovider"
      password: "authenticationprovider"
    data:
      redis:
        host: "redis-master.{{ .Release.Namespace }}.svc.cluster.local"
        port: 6379
        username: "default"
        password: "admin" # update this

  security:
    secret:
      location: database # database / vault

  simpl:
    certificate:
      san: <your-tier2-fqdn>
    sync-credentials:
      job:
        cron: 0 0 */6 * * *

  microservice:
    identity-provider:
      url: http://identity-provider.{{ .Release.Namespace }}.svc.cluster.local:8080
    security-attributes-provider:
      url: http://security-attributes-provider.{{ .Release.Namespace }}.svc.cluster.local:8080

  client:
    authority:
      url: "https://<tier2-gateway of the authority>"

  keypair:
    signature-algorithm: "SHA256withECDSA"
    algorithm: "ECDSA"
    key-length: 256
    read-algorithm: "EC"

  management:
    otlp:
      tracing:
        endpoint: <your-otel-endpoint>
```

## Additional Documentation

For more information, please refer to the [documentation repository](https://code.europa.eu/simpl/simpl-open/development/iaa/documentation). Select the correct version based on the release.

For a full overview of configuration properties, please refer to [Properties file](../installation-guide/PROPERTIES.md).