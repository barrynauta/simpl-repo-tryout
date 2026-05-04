<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Administration</a><br/>
        <a href="../../README.md">Capability: Observability</a><br/>
            <a href="../README.md">Service: Performance monitoring</a><br/>
                <strong>Solution: monitoring-proxy</strong><br/>
</p>
</div>

# monitoring-proxy

NGINX-based reverse proxy fronting the Simpl monitoring stack. Provides request routing, ingress termination, and a single entry point for downstream consumers (UIs, agents, exporters) to reach the underlying [eck-monitoring](../eck-monitoring/README.md) services.

The production code lives at the canonical location — see [CANONICAL.md](CANONICAL.md). Machine-readable form: [`.canonical.yaml`](.canonical.yaml).

## Status

Early-stage. Upstream contains NGINX configuration files; recently updated. Functionality and the precise role in the Tier 1 / Tier 2 routing topology will firm up as the monitoring stack matures.

## Source

- <https://code.europa.eu/simpl/simpl-open/development/monitoring/monitoring-proxy>
