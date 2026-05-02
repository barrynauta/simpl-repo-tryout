<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Administration</a><br/>
        <a href="../../README.md">Capability: Observability</a><br/>
            <a href="../README.md">Service: Performance monitoring</a><br/>
                <strong>Solution: eck-monitoring</strong><br/>
</p>
</div>

# eck-monitoring

Elastic Cloud on Kubernetes (ECK) monitoring deployment for Simpl-Open. Manages the Elasticsearch + Kibana cluster on Kubernetes, providing the storage backend for both the metrics pipeline (Metricbeat, Heartbeat, Prometheus) and the centralised logging stack (ELK + Filebeat).

This folder is the **canonical home** for ECK monitoring under the Performance monitoring service. It is also referenced from the [Logging](../../logging/eck-monitoring/README.md) service since the same Elasticsearch cluster backs both data streams.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
