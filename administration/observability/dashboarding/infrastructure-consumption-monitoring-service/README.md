<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Administration</a><br/>
        <a href="../../README.md">Capability: Observability</a><br/>
            <a href="../README.md">Service: Dashboarding</a><br/>
                <strong>Solution: Infrastructure Consumption Monitoring Service</strong><br/>
</p>
</div>

# Infrastructure Consumption Monitoring Service

Scheduled service that pulls infrastructure-consumption data from a cloud provider on a cron interval and publishes it to a dedicated monitoring Kafka topic, where downstream monitoring/billing components can consume it.

Capability-map placement: `administration / observability / dashboarding / infrastructure-consumption-monitoring-service`. Sits beside the [Monitoring Service](../monitoring-service/README.md) under the same business service.

Provenance: built by Simpl. Source repository: `code.europa.eu/simpl/simpl-open/development/monitoring/infrastructure-consumption-monitoring-service`. Licence: EUPL 1.2.

## Key features

- **Scheduled extraction** of consumption data from a cloud provider; cron-driven, with separate schedules per provider and per "current" vs "historical" report.
- **Kafka publication**: writes to a configurable monitoring topic (`spring.kafka.topics.icm`) plus per-provider report topics (e.g. `…ovhReports`).
- **Default provider OVH**, with a mock provider for integration tests (must be disabled in production).
- **Idempotency / replay safety**: stores per-provider processing reports in a dedicated topic so repeated runs do not double-count time ranges.
- **Failed-event retry process** with its own configurable schedule.
- **Vault integration** for credentials.
- **Pluggable** — additional cloud providers can be added (documented in source as "Adding a New Cloud Provider").

## Operational notes

Topic retention must align with the slowest scheduler that produces into a topic — e.g. a monthly scheduler needs a retention longer than one month, otherwise reports are evicted before they are consumed and produce "report not found" errors. The monitoring topic carries data downstream to the consumption-monitoring/reporting layer.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document covering the Kafka-topic shape, the idempotency model, the `@Scheduled`-driven plugin extension point for new cloud providers, and the operational caveats (mock plugin must be disabled in production, retention sizing).

## Participates in

- [BP12B Single-node logging and monitoring](../../../../foundations/business-processes/BP12B-single-node-logging-monitoring/README.md)

## Source code

- Simpl repo: <https://code.europa.eu/simpl/simpl-open/development/monitoring/infrastructure-consumption-monitoring-service>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
