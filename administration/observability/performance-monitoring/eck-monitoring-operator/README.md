<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Administration</a><br/>
        <a href="../../README.md">Capability: Observability</a><br/>
            <a href="../README.md">Service: Performance monitoring</a><br/>
                <strong>Solution: eck-monitoring-operator</strong><br/>
</p>
</div>

# eck-monitoring-operator

Kubernetes Operator companion to [eck-monitoring](../eck-monitoring/README.md), automating the deployment and lifecycle management of the **ECK Monitoring** stack: collects logs and metrics from Simpl agents, exposes a GUI to visualise the data on dashboards, and triggers alerts when anomalies are detected in the collected data.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Relationship to eck-monitoring

| Solution | Role |
|---|---|
| [eck-monitoring](../eck-monitoring/README.md) | The monitoring stack itself (ECK / Elasticsearch + Kibana + Beats etc.) |
| **eck-monitoring-operator** *(this folder)* | Kubernetes Operator that manages the lifecycle of `eck-monitoring` resources on the cluster |

The two are deliberately split into separate repos: the stack ships its own Helm/manifests; the operator wraps them into custom resources for declarative cluster management.

## Status

Early-stage upstream — the README declares scope (logs, metrics, dashboards, alerting) but the source tree is sparse at the moment. Re-evaluate as content lands.

## Source

- <https://code.europa.eu/simpl/simpl-open/development/monitoring/eck-monitoring-operator>
