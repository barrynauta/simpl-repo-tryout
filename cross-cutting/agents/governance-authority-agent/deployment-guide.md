# Governance Authority Agent — Deployment Guide

> Source: [agents/governance-authority/documents/deployment-guide/README.md](https://code.europa.eu/simpl/simpl-open/development/agents/governance-authority/-/blob/main/documents/deployment-guide/README.md). This file mirrors that guide; refer to source for screenshots and any later updates.

## Description

The Governance Authority agent is deployed via a master Helm chart that, when applied to a Kubernetes cluster, materialises every GA module (Onboarding, Identity Provider, EJBCA, Federated Catalogue, Schema Management, Signer, IAA Tier 1/Tier 2 stack, monitoring) as ArgoCD apps.

The repository contains:
- the master Helm chart (one-command deployment),
- templates of `values.yaml` files for the Integration environment under `app-values/`.

## Prerequisites

### Common components first

The Governance Authority installation **requires the common-components** stack to already be deployed: see [Common components install](https://code.europa.eu/simpl/simpl-open/documentation/installation-guide/-/blob/main/README.md#set-up-common-components).

### Tools

See the shared list at the [common_components deployment guide → Tools](https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/deployment-guide/README.md#tools).

### DNS entries

| Entry name | FQDN pattern |
|------------|--------------|
| schema-manager-ui | `schema-manager-fe.<namespaceTag>.<domainSuffix>` |
| redis-commander | `redis-commander.<namespaceTag>.<domainSuffix>` |
| simpl-fe-authentication-provider | `authority.fe.<namespaceTag>.<domainSuffix>/participant-utility` |
| simpl-fe-identity-provider | `authority.fe.<namespaceTag>.<domainSuffix>/identity-provider` |
| simpl-fe-onboarding | `authority.fe.<namespaceTag>.<domainSuffix>/onboarding` |
| simpl-fe-sap | `authority.fe.<namespaceTag>.<domainSuffix>/sap` |
| simpl-fe-users-roles | `authority.fe.<namespaceTag>.<domainSuffix>/users-roles` |
| simpl-ingress | `authority.be.<namespaceTag>.<domainSuffix>` |
| tier2-gateway | `tls.authority.<namespaceTag>.<domainSuffix>` |
| simpl-schema-manager-ingress | `schema-manager-be.<namespaceTag>.<domainSuffix>` |

## Deployment

### Deployment via ArgoCD

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: authority01-deployer
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://code.europa.eu/api/v4/projects/902/packages/helm/stable
    path: '""'
    targetRevision: 3.0.4
    helm:
      values: |
        values:
          branch: v3.0.4
        project: default
        namespaceTag:
          authority: authority01
          common: common01
        domainSuffix: example.com
        resourcePreset: default
        argocd:
          appname: authority01
          namespace: argocd
        cluster:
          address: https://kubernetes.default.svc
          namespace: authority01
          commonToolsNamespace: common
          issuer: dev-int-dns01
        secrets:
          role: example-role
          secretEngine: example
        monitoring:
          enabled: true
    chart: authority
  destination:
    server: https://kubernetes.default.svc
    namespace: authority01
```

### Manual deployment

Unpack the release locally, edit `values.yaml`, then from the chart folder:

```
helm install authority .
```

The trailing `.` is required.

Pod creation can take up to **30 minutes**. Watch ArgoCD until all expected apps are healthy.

## Additional steps

### Initialization

After deployment, the authority must be initialised manually via APIs: [iaa/documentation → governance-authority-init-via-apis](https://code.europa.eu/simpl/simpl-open/development/iaa/documentation/-/tree/main/versioned_docs/2.9.x#governance-authority-init-via-apis).

### Tier 2 proxy

Until the agent is fully initialised the `tier2-proxy` will not be functional — expected behaviour.

### Monitoring

Filebeat sidecars ship with the release. Disable with `monitoring.enabled: false`.

## Troubleshooting

- ArgoCD reachable from the cluster.
- Target namespace exists.
- Inspect ArgoCD application logs and Helm error output for the failing app.

### Identity Provider failure (cluster-performance race)

A known intermittent failure mode — usually triggered by cluster performance — leaves the Identity Provider unable to create its bootstrap secret, and the Tier 2 gateway fails as a consequence. Recovery procedure:

1. **Check the IdP pod's events** (Rancher → workload → events). Symptom: missing/automatic secret never created.
2. **Drop and recreate the affected Postgres databases.** Access procedure: [POSTGRESQL_ADMINISTRATION.md](https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/user-manual/POSTGRESQL_ADMINISTRATION.md). Log in as `admin@<domainSuffix>` with the password from OpenBao key `<commonNamespaceTag>-pgadmin-credentials/password`. Inside pgAdmin, log in to the Postgres server itself with the password from key `postgres` of the same secret.
3. **Drop these two DBs**: `<authorityNamespaceTag>_ejbca` and `<authorityNamespaceTag>_identityprovider`.
4. **In the `common` namespace**, restart the `pg-operator-<commonNamespaceTag>` deployment. Verify the deleted databases are recreated.
5. **In the `authority` namespace**, delete the `identity_provider` deployment and the `ejbca-community-helm` deployment.
6. After full ArgoCD re-sync of the authority namespace, the previously missing secret should now exist.
7. Restart the `tier2-gateway` deployment. All pods should now be healthy.

(Source guide includes step-by-step screenshots.)

## FAQ

**What is the Governance Authority Agent?**
The data-space participant accountable for creating, developing, operating, maintaining and enforcing the governance framework for a particular data space.

**What's the prerequisite for installation?**
[Common components installed](https://code.europa.eu/simpl/simpl-open/documentation/installation-guide/-/blob/main/README.md#set-up-common-components).

**What OpenBao tasks are needed during installation?**
[Using_OpenBao.md](https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/user-manual/Using_OpenBao.md).
