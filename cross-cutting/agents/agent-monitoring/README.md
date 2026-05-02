<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Agents</a><br/>
            <strong>Agent monitoring</strong><br/>
</p>
</div>

# Agent monitoring

Per-actor-type deployment compositions for the **monitoring/observability slice** of a Simpl-Open agent. Each variant is a thin Helm/ArgoCD wrapper that deploys the shared `eck-monitoring` chart (Elastic / Filebeat / Metricbeat / Heartbeat) with actor-specific namespace tags and resource sizing.

Same shape as [`agent-iaa/`](../agent-iaa/README.md), [`agent-contract-billing/`](../agent-contract-billing/README.md), and [`agent-resource-handling/`](../agent-resource-handling/README.md).

## Variants

- [authority-monitoring](authority-monitoring/README.md) — Governance Authority monitoring composition.
- [consumer-monitoring](consumer-monitoring/README.md) — Consumer monitoring composition.
- [provider-monitoring](provider-monitoring/README.md) — Provider monitoring composition.

## Bundled chart

| Sub-service in chart | Catalogue location |
|---|---|
| `eck-monitoring` | [administration/observability/logging/eck-monitoring/](../../../administration/observability/logging/eck-monitoring/README.md) and [administration/observability/performance-monitoring/eck-monitoring/](../../../administration/observability/performance-monitoring/eck-monitoring/README.md) |

The three variants differ only in their namespace tags and per-environment ArgoCD deployer files. The actual observability stack (Elastic Operator + Elasticsearch + Kibana + Logstash + Filebeat + Metricbeat + Heartbeat) lives under the [administration/observability](../../../administration/observability/README.md) capability.
