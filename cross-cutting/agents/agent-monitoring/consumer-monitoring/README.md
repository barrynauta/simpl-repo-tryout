<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Cross-Cutting</a><br/>
        <a href="../../README.md">Agents</a><br/>
            <a href="../README.md">Agent monitoring</a><br/>
                <strong>consumer-monitoring</strong><br/>
</p>
</div>

# consumer-monitoring

Consumer-side deployment composition (umbrella Helm/ArgoCD chart) for the monitoring slice of a Simpl-Open agent. Bundles the shared `eck-monitoring` chart with consumer-specific namespace tags. Consumed by the [consumer-agent](../../consumer-agent/README.md) master chart.

## Bundled chart

- `eck-monitoring` → [administration/observability/logging/eck-monitoring](../../../../administration/observability/logging/eck-monitoring/README.md) (Elastic / Filebeat / Metricbeat / Heartbeat stack)

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).
