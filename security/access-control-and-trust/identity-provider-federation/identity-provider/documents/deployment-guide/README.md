# Deployment Guide

This guide provides instructions for deploying the Identity Provider service using Helm charts in a Kubernetes environment.

## Prerequisites

- A Kubernetes cluster
- Helm - the package manager for Kubernetes. See https://helm.sh/
- kubectl - the Kubernetes command-line tool that allows you to run commands against Kubernetes clusters. See https://kubernetes.io/docs/reference/kubectl/kubectl/

> **⚠️** *Step only needed for the governance authority*

## Deployment Steps

```shell
# 913 is the project_id of this repository
helm repo add identity-provider-charts https://code.europa.eu/api/v4/projects/913/packages/helm/stable

helm install identity-provider identity-provider-charts/identity-provider \
--version <chart version> \ 
--values values.yaml
```

> **💡** The latest `2.7.x` chart version can be found in the releases section of the project's repository. Please note that hotfixes may have been released since the last major update. Hotfixes may have been released. [Link to releases](https://code.europa.eu/simpl/simpl-open/development/iaa/identity-provider/-/releases).

#### Example of values.yaml
```yaml
ejbca:
  keystore:
  # uncomment the following line if your are not using ejbca-preconfig
  # base64: "<base64 of the keystore>" # SuperAdmin .p12 
  truststore:
  # uncomment the following line if your are not using ejbca-preconfig
  # base64: "<base64 of the truststore>" # ManagementCA

appConfig:
  spring:
    datasource:
      url: jdbc:postgresql://postgresql.{{ .Release.Namespace }}.svc.cluster.local:5432/identityprovider
      username: identityprovider
      password: identityprovider
    ssl:
      bundle:
        jks:
          ejbca:
            key:
              alias: "superadmin"
            keystore:
              # if your are using ejbca-preconfig the following password should match 
              # the MANAGEMENT_END_ENTITY_PASSWORD provided to the script
              password: "<password of the keystore>"
            truststore:
              # this password typically matches the default password defined by EJBCA (changeit)
              password: "<password of the truststore>"
  simpl:
    automatic-renewal:
      default-duration-before-renewal: 20d
      job:
        cron: "0 0 2 * * ?"
        max-fetch-size: 100


  microservice:
    security-attributes-provider:
      url: "http://security-attributes-provider.{{ .Release.Namespace }}.svc.cluster.local:8080"

  ejbca:
    url: "https://ejbca-community-helm.{{ .Release.Namespace }}.svc.cluster.local:30443"
    profile-name: "<End Entity Certificate Profile>" # update this field, example "Onboarding TLS Profile"
    end-entity-name: "<EndEntity Profile>" # update this field, example "Onboarding End Entity"
    ca-name: "<SubCA>" # update this field, example "OnBoardingCA"

  management:
    otlp:
      tracing:
        endpoint: <otlp-endpoint> # put your tracing endpoint

```

## Additional Documentation

For more information, please refer to the [documentation repository](https://code.europa.eu/simpl/simpl-open/development/iaa/documentation). Select the correct version based on the release.

For a full overview of configuration properties, please refer to [Properties file](../installation-guide/PROPERTIES.md).