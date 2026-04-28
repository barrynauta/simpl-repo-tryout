# Data Provider Agent — Deployment Guide

> Source: [agents/data-provider/documents/deployment-guide/README.md](https://code.europa.eu/simpl/simpl-open/development/agents/data-provider/-/blob/main/documents/deployment-guide/README.md). This file mirrors that guide; refer to source for screenshots and any later updates.

## Description

The Data Provider agent is deployed via a master Helm chart. Applying the chart to a Kubernetes cluster materialises every Provider-side module (SD-Tooling, EDC Provider Connector, Asset Orchestrator, IAA client stack, monitoring, plus the **infrastructure-provisioning crossplane stack** if enabled) as ArgoCD apps.

The repository contains:
- the master Helm chart (one-command deployment),
- templates of `values.yaml` files for the Integration environment under `app-values/`.

## Prerequisites

### Tools

See the shared list at the [common_components deployment guide → Tools](https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/deployment-guide/README.md#tools).

### DNS entries

If you don't run external-dns, add these manually:

| Entry name | FQDN pattern |
|------------|--------------|
| catalogue-ui | `catalogue-ui.<namespaceTag>.<domainSuffix>` |
| gitea-http | `gitea.crossplane.<namespaceTag>.<domainSuffix>` |
| infrastructure-argo-cd-server | `argoui.crossplane.<namespaceTag>.<domainSuffix>` |
| infrastructure-argo-workflows-server | `argoworkflows.crossplane.<namespaceTag>.<domainSuffix>` |
| infrastructure-be | `infrastructure-be.<namespaceTag>.<domainSuffix>` |
| infrastructure-fe-frontend | `infrastructure-fe.<namespaceTag>.<domainSuffix>` |
| redis-commander | `redis-commander.<namespaceTag>.<domainSuffix>` |
| sd-ui | `sd-ui.<namespaceTag>.<domainSuffix>` |
| simpl-fe-authentication-provider | `participant.fe.<namespaceTag>.<domainSuffix>/participant-utility` |
| simpl-fe-users-roles | `participant.fe.<namespaceTag>.<domainSuffix>/users-roles` |
| simpl-files | `files.<namespaceTag>.<domainSuffix>` |
| simpl-ingress | `participant.be.<namespaceTag>.<domainSuffix>` |
| tier2-gateway | `tls.participant.<namespaceTag>.<domainSuffix>` |

## Deployment

### Preliminary tasks

#### OpenBao setup

OpenBao at `https://secrets.<commonNamespaceTag>.<domainSuffix>`; root token in the `common` namespace, secret `secrets-root-token`, key `token`. Read [Using_OpenBao.md](https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/user-manual/Using_OpenBao.md) before editing secrets.

##### Secret for Infrastructure-be

Edit the OpenBao key `<dataproviderNamespaceTag>-infrastructure-be`. The Gitea token can only be requested **after** the provider is deployed — once you've changed values in this secret, restart the `infrastructure-be` pod.

To obtain `gitea.token`, run (replace the bracketed values):

```bash
curl -X POST "https://gitea.crossplane.(namespaceTag).(domainSuffix)/api/v1/users/(gitea.username)/tokens" \
  -u (gitea.username):(gitea.password) \
  -H "Content-Type: application/json" \
  -d '{"name": "token-name", "scopes": ["all"]}'
```

The response's `sha1` field is the value to put under `gitea.token`:

| Variable | Description |
|----------|-------------|
| `gitea.token` | Gitea API token (from the response above) |

##### Secret for simpl-edc

Edit `<dataproviderNamespaceTag>-simpl-edc` and provide MinIO endpoint + keys:

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
  name: dataprovider01-deployer
spec:
  project: default
  source:
    repoURL: https://code.europa.eu/api/v4/projects/904/packages/helm/stable
    path: '""'
    targetRevision: 3.0.8
    helm:
      values: |
        values:
          branch: v3.0.8
        project: default
        namespaceTag:
          dataprovider: dataprovider01
          authority: authority01
          common: common01
        domainSuffix: example.com
        resourcePreset: default
        argocd:
          appname: dataprovider01
          namespace: argocd
        cluster:
          address: https://kubernetes.default.svc
          namespace: dataprovider01
          commonToolsNamespace: common01
          issuer: dev-prod
        secrets:
          role: example-role
          secretEngine: example
        crossplane:
          enabled: true                # only one instance per cluster
          kafka:
            username: dataprovider01_infrabe   # convention: <namespace>_infrabe
            password: pass             # from common01-kafka-credentials OpenBao secret, key dataprovider01_infrabe
          gitea:
            username: gitops_test
            password: pass             # any value — set it to whatever you want
        monitoring:
          enabled: true
    chart: data-provider
  destination:
    server: https://kubernetes.default.svc
    namespace: dataprovider01
```

### Manual deployment

Unpack the release locally, edit `values.yaml` (same fields as above), then from the chart folder:

```
helm install data-provider .
```

The trailing `.` is required.

### Verification

Pod creation can take up to **30 minutes**. Watch ArgoCD until all expected apps are healthy. (See source guide for reference screenshots.)

## Additional steps

### Onboarding

After deployment, the participant must be onboarded manually: [iaa/documentation → ONBOARD.md](https://code.europa.eu/simpl/simpl-open/development/iaa/documentation/-/blob/main/versioned_docs/2.9.x/user-manual/ONBOARD.md).

### Tier 2 proxy

Until the agent is fully initialised the `tier2-proxy` will not be functional — expected behaviour.

### Monitoring

Filebeat sidecars ship with the release. Disable with `monitoring.enabled: false`.

## Troubleshooting

- ArgoCD reachable from the cluster.
- Target namespace exists.
- Inspect ArgoCD application logs and Helm error output for the failing app.

## FAQ

**How do I install the SuperAdmin certificate in my browser?**
Download in PKCS#12 (`*.p12`) format and follow your browser's import procedure (e.g. [Firefox](https://docs.keyfactor.com/ejbca-cloud/latest/import-certificate-to-mozilla-firefox)). Restart if the cert isn't recognised immediately.

**What is the ManagementCA certificate and how do I get it?**
The ManagementCA cert is the truststore for secure communications. Download from the EJBCA Admin Dashboard under *CA Structure & CRL*; save in JKS format with the chosen password kept securely.
