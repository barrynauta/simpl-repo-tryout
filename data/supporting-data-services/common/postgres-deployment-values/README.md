<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Supporting data services</a><br/>
            <a href="../README.md">Service: Common</a><br/>
                <strong>Solution: postgres-deployment-values</strong><br/>
</p>
</div>

# postgres-deployment-values

Three Helm `values.yaml` overrides for the upstream **Bitnami PostgreSQL** chart, customised for the Postgres instances backing the EDC/catalogue stack. The chart itself is pulled from `bitnami/postgresql` at deploy time — only the per-consumer values are catalogued here.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Contents

The upstream `postgres/` folder ships three values files; each pins the image, resources, persistence, and security context for one Postgres instance:

| Values file | Backs | Catalogue placement |
|---|---|---|
| `values-fc-service.yaml` | Federated Catalogue (fc-service) Postgres | [xfsc-federated-catalogue](../../../../integration/resource-discovery/resource-catalogue/xfsc-federated-catalogue/README.md) |
| `values-edc-provider.yaml` | EDC connector (provider side) Postgres | [provider-gaia-x-edc](../../../../integration/resource-sharing/resource-sharing-runtime/provider-gaia-x-edc/README.md) |
| `values-edc-consumer.yaml` | EDC connector (consumer side) Postgres | [consumer-gaiax-edc](../../../../integration/resource-sharing/resource-sharing-runtime/consumer-gaiax-edc/README.md) |

Deployment is operator-driven — three `helm install` invocations against `bitnami/postgresql --version 16.0.1`, each with one of the values files. See the upstream `postgres/README.md` for the exact commands.

## Naming notes (upstream)

The upstream repo is named `simpl-files` and its top-level README states the purpose is *"to store commonly used helm charts"*. Both labels are misleading:

- The repo doesn't ship any chart — only Helm values overrides.
- A separate `data1/simpl-files` exists and legitimately serves files (NGINX hosting contract templates, catalogued at [contract-template-datastore](../../../../governance/contract-management/contract-establishment/contract-template-datastore/README.md)). The two repos share a name but do unrelated things.

Worth flagging upstream as a rename + README-fix candidate.

## Source

- <https://code.europa.eu/simpl/simpl-open/development/gaia-x-edc/simpl-files>
