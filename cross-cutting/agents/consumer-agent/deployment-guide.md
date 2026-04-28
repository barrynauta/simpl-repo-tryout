# Consumer Agent — Deployment Guide

> Source: [agents/consumer/documents/deployment-guide/README.md](https://code.europa.eu/simpl/simpl-open/development/agents/consumer/-/blob/main/documents/deployment-guide/README.md). This file mirrors that guide; refer to source for screenshots and any later updates.

## Description

The Consumer agent is deployed via a **master Helm chart**. Applying the chart to a Kubernetes cluster produces an ArgoCD application that materialises every Consumer-side module (catalogue client, contract consumption back-end, EDC consumer connector, IAA Tier 1/Tier 2 client stack, monitoring) as separate apps.

The repository contains:
- the master Helm chart (deploys with one command),
- templates of `values.yaml` files for the Integration environment under `app-values/`.

## Prerequisites

### Tools

See the shared list at the [common_components deployment guide → Tools](https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/deployment-guide/README.md#tools).

### DNS entries

| Entry name | FQDN pattern |
|------------|--------------|
| catalogue-ui | `catalogue-ui.<namespaceTag>.<domainSuffix>` |
| redis-commander | `redis-commander.<namespaceTag>.<domainSuffix>` |
| simpl-fe-authentication-provider | `participant.fe.<namespaceTag>.<domainSuffix>/participant-utility` |
| simpl-fe-users-roles | `participant.fe.<namespaceTag>.<domainSuffix>/users-roles` |
| simpl-ingress | `participant.be.<namespaceTag>.<domainSuffix>` |
| tier2-gateway | `tls.participant.<namespaceTag>.<domainSuffix>` |

## Deployment

### Preliminary tasks

#### OpenBao setup

OpenBao is reachable at `https://secrets.<commonNamespaceTag>.<domainSuffix>`. The root token lives in the `common` namespace, secret `secrets-root-token`, key `token`.

Read the OpenBao usage primer first: [Using_OpenBao.md (source)](https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/user-manual/Using_OpenBao.md).

##### Secret for EDC

Edit the key `<consumerNamespaceTag>-simpl-edc` (the prefix is your consumer namespace) and provide your MinIO endpoint and keys:

| Variable | Example | Description |
|----------|---------|-------------|
| `fr_gxfs_s3_access_key` | `minioacckey` | MinIO access key |
| `fr_gxfs_s3_endpoint` | `https://minio.address.eu` | MinIO API address |
| `fr_gxfs_s3_secret_key` | `minioseckey` | MinIO secret key |

All other secrets are seeded automatically.

### Deployment via ArgoCD

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: consumer01-deployer            # name of the deploying app in ArgoCD
  namespace: argocd                    # your ArgoCD namespace
spec:
  project: default
  source:
    repoURL: https://code.europa.eu/api/v4/projects/903/packages/helm/stable
    path: '""'
    targetRevision: 3.0.2              # package version
    helm:
      values: |
        values:
          branch: v3.0.2               # release branch for values
        project: default
        namespaceTag:
          consumer: consumer01         # this agent's identifier
          authority: authority01       # GA identifier
          common: common01             # common-components identifier
        domainSuffix: example.com      # FQDN suffix
        resourcePreset: default        # set to "low" to disable resource requests
        argocd:
          appname: consumer01
          namespace: argocd
        cluster:
          address: https://kubernetes.default.svc
          namespace: consumer01
          commonToolsNamespace: common01
          issuer: dev-prod
        secrets:
          secretEngine: example        # OpenBao secret engine
          role: example-role           # OpenBao access role
        monitoring:
          enabled: true
    chart: consumer
  destination:
    server: https://kubernetes.default.svc
    namespace: consumer01
```

### Manual deployment

Unpack the released chart locally, edit `values.yaml` (same fields as the ArgoCD example above), then from the chart folder run:

```
helm install consumer .
```

The trailing `.` is required — it points at the current folder.

### Verification

Pod creation can take up to **30 minutes** depending on configuration. Check ArgoCD until all expected apps are healthy. (See source guide for the reference screenshot.)

## Additional steps

### Onboarding

After deployment, the participant must be onboarded manually. Procedure: [iaa/documentation → ONBOARD.md](https://code.europa.eu/simpl/simpl-open/development/iaa/documentation/-/blob/main/versioned_docs/2.9.x/user-manual/ONBOARD.md).

### Tier 2 proxy

Until the agent is fully initialised the `tier2-proxy` will not be functional — expected behaviour.

### Monitoring

Filebeat sidecars ship with the release. Disable by setting `monitoring.enabled: false`.

## Troubleshooting

- ArgoCD up and reachable from the cluster.
- Target namespace exists.
- Inspect the ArgoCD application logs and Helm error output for the specific failing app.
