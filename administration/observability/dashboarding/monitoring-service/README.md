<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Administration</a><br/>
        <a href="../../README.md">Capability: Observability</a><br/>
            <a href="../README.md">Service: Dashboarding</a><br/>
                <strong>Solution: Monitoring Service</strong><br/>
</p>
</div>

# Monitoring Service

Provides observability for all Simpl-Open application components on a node, covering log collection and ingestion, infrastructure metrics, dashboarding, alerting, health checking, application tracing, and reporting. Implemented on the **Elastic Cloud on Kubernetes (ECK)** stack with a Kubernetes operator for stack lifecycle management and a shared logging library used across Java services.

Capability-map placement: `administration / observability / dashboarding / monitoring-service`. This solution implements the **Dashboarding** business service and cross-cuts logging, QoS metrics and alerts, performance monitoring, and reporting within the observability capability.

Provenance: built by Simpl. Source repositories: `monitoring/eck-monitoring` (the deployed Elastic stack — Elasticsearch, Kibana, Beats), `monitoring/eck-monitoring-operator` (custom operator managing the stack lifecycle on Kubernetes), and `contract-billing/common_logging` (shared logback/MDC library used by Java services to emit structured logs into the stack). Licence: EUPL 1.2.

## Key features

- Centralised log aggregation across the agent's microservices (Filebeat → Elasticsearch).
- Infrastructure and application metrics via Metricbeat and Heartbeat.
- Kibana dashboards for visualisation; Alert Manager for QoS alerts.
- Operator-driven lifecycle: rolling upgrades and configuration changes applied through the ECK monitoring operator rather than direct kubectl edits.
- Structured logging from Simpl Java services via the `common_logging` library (MDC propagation for tenant / participant / correlation IDs).

## Sibling solutions in this service

The cloud-consumption ingestion path is now split out:

- [Infrastructure Consumption Monitoring Service](../infrastructure-consumption-monitoring-service/README.md) — scheduled extraction of cloud-provider consumption data (default OVH) published to Kafka for downstream monitoring and billing.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP12B Single-node logging and monitoring](../../../../foundations/business-processes/BP12B-single-node-logging-monitoring/dynamic-view.md)

## Source code

- `code.europa.eu/simpl/simpl-open/development/monitoring/eck-monitoring`
- `code.europa.eu/simpl/simpl-open/development/monitoring/eck-monitoring-operator`
- `code.europa.eu/simpl/simpl-open/development/contract-billing/common_logging`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
