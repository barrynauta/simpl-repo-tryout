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

Provides observability for all Simpl-Open application components on a node, covering log collection, log ingestion, infrastructure metrics, dashboarding, alerting, health checking, application tracing, and reporting. Implemented on the Elastic Cloud on Kubernetes (ECK) stack with a custom infrastructure consumption monitoring service and a shared logging library.

Capability-map placement: `administration / observability / dashboarding / monitoring-service`. This solution implements the **Dashboarding** business service and cross-cuts logging, QoS metrics and alerts, performance monitoring, and reporting within the observability capability.

Provenance: built by Simpl. Source repositories: `monitoring/eck-monitoring`, `monitoring/eck-monitoring-operator`, `monitoring/infrastructure-consumption-monitoring-service`, `contract-billing/common_logging`. Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP12B Single-node logging and monitoring](../../../../foundations/business-processes/BP12B-single-node-logging-monitoring/dynamic-view.md)

## Source code

- `code.europa.eu/simpl/simpl-open/development/monitoring/eck-monitoring`
- `code.europa.eu/simpl/simpl-open/development/monitoring/eck-monitoring-operator`
- `code.europa.eu/simpl/simpl-open/development/monitoring/infrastructure-consumption-monitoring-service`
- `code.europa.eu/simpl/simpl-open/development/contract-billing/common_logging`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
