Source: source repo `monitoring/infrastructure-consumption-monitoring-service/README.md`. FTA spec, §6.1.3 TCV Static — Monitoring Service (cloud-consumption ingestion sub-component).

# Infrastructure Consumption Monitoring Service — architecture

## Business view

Cron-driven service that pulls **infrastructure-consumption data** from a cloud provider and publishes it to a dedicated Kafka topic, where downstream monitoring and billing components can consume it. Sits alongside the [Monitoring Service](../../monitoring-service/doc/architecture.md) within the Dashboarding business service but plays a distinct role: rather than collecting logs and metrics from Simpl-Open application components, it collects *resource-usage* data from the underlying cloud provider that hosts the agent.

Default provider is **OVH**; a mock provider is available for integration tests (must be disabled in production by setting its cron to `-`). Adding a new cloud provider is a documented extension point — the service is pluggable.

Capability-map placement: Administration dimension → Observability capability → Dashboarding business service.

**Business processes supported:**
- [BP12B Single-node logging and monitoring](../../../../foundations/business-processes/BP12B-single-node-logging-monitoring/README.md) — usage data feeds the per-node observability stack.
- Indirectly, infrastructure billing flows that depend on consumption data.

## Data view

The service writes to **Kafka** with three classes of topic:

- **Monitoring topic** (`spring.kafka.topics.icm`) — the canonical consumption stream that downstream observability and billing components consume. One per agent / namespace.
- **Per-provider report topics** (e.g. `spring.kafka.topics.icm.ovhReports`, `…testReports`) — track which time ranges have already been processed and sent. One per cloud provider.
- These two are deliberately separated so that idempotency state lives independently of the consumption data itself.

**Idempotency model:** before each scheduled run, the service consults its provider-specific report topic to find the last processed time range. If a report already covers the window, the run is a no-op; otherwise it pulls the missing window from the provider and writes both the consumption data (to the monitoring topic) and a processing-report record (to the report topic). On first-ever startup the service initialises with `initialReportOffsetInMonths` months of historical data.

**Topic retention warning** (operationally critical): retention on each report topic must align with the slowest scheduler that writes to it. A monthly scheduler against a topic with 30-day retention will see its prior reports evicted before its next run, leading the service to re-fetch and re-emit data that downstream consumers may have already processed — surfacing as `"report not found"` errors in logs.

## Application view

### Internal decomposition

Spring Boot service. Three orthogonal concerns:

- **Per-provider connector** — implements the `Connector` interface (`getData()`, `getData(from, to)`, `getName()`, `getTopic()`). Default implementation calls the OVH consumption API.
- **Per-provider model** — implements `Response.process()` (default: JSON-mapper that serialises the response into a string suitable for Kafka).
- **Plugin** — a class annotated with `@Scheduled` that calls `processingEngine.getInfraConsumption(Connector)` on the configured cron expression. Each provider has its own plugin and therefore its own cron (`ovh.schedule`, `ovh.current.schedule`, `mockedPlugin.schedule`, …).

A separate **failed-events retry process** runs on its own cron (`failedEvents.retrySchedule`, suggested `0 */5 * * * *`) and walks an in-memory retry queue. Failures during a fetch (e.g. provider timeout) push the work item onto the queue rather than dropping it; the retry job picks them up later.

**Adding a new cloud provider** (extension procedure from source):

1. New `Connector` implementation supplying `getData`, `getData(from, to)`, `getName`, `getTopic`.
2. New model class implementing `Response.process()`.
3. New `Plugin` class annotated `@Scheduled`, calling `processingEngine.getInfraConsumption(<your Connector>)`.
4. Environment variables for provider-specific config (cron, credentials, endpoint).

### Key integrations

- [Monitoring Service](../../monitoring-service/doc/architecture.md) — sibling solution; consumes from the monitoring topic for visualisation and alerting.
- **Apache Kafka** (`administration/notification-and-messaging/notification/apache-kafka` per the canonical mapping) — the message bus for both data and idempotency-state topics.
- **HashiCorp Vault** — provider credentials (OVH appKey / appSecret / consumerKey, project IDs, etc.) are sourced from Vault rather than from configmaps.
- **Common components** — runs on the agent's shared Kafka, Vault, and observability stack via the [Common Components](../../../../cross-cutting/agents/common-components/README.md) bundle.

## Technical view

- **Framework**: Spring Boot, `@Scheduled` for cron-driven execution.
- **Cron syntax**: standard six-field Spring 5.3+ cron expressions ([reference](https://spring.io/blog/2020/11/10/new-in-spring-5-3-improved-cron-expressions)). Set a provider's schedule to `-` to disable that provider.
- **Cloud client**: REST/HTTP against the cloud provider's consumption API. OVH-specific config: `ovh.host`, `ovh.project_id`, `ovh.appKey`, `ovh.appSecret`, `ovh.consumerKey`.
- **Two OVH schedules** by design — `ovh.schedule` for arbitrary date ranges and `ovh.current.schedule` for the most-recent window. The latter should run no more than hourly (OVH's report update cadence).
- **Deployment**: container, packaged via Helm chart (`charts/values.yaml` carries the env config); deployed alongside the Monitoring Service on each agent.

## Security view

- **Provider credentials in Vault** — never committed; only the Vault path is in chart values.
- **Kafka in `kafka-secure` mode** — the service authenticates to the broker as a per-namespace Kafka principal (e.g. `<namespace>_infrabe`).
- **No public ingress** — the service only consumes (cloud provider's API) and produces (Kafka). There are no public endpoints to attack.
- **Operational guard** — the mock cloud provider plugin **must be disabled in production** (its cron set to `-`); the source explicitly flags this as a manual safety gate.

Threat model: not yet documented.

Secrets management: HashiCorp Vault for provider API credentials; Kafka SASL credentials from the same Vault path.

## Testing

Strategy: the mock cloud provider plugin doubles as the integration-test fixture. CI/CD runs unit tests + SAST (SonarQube) + security tests (Fortify).

PSO validation status: not yet documented.

Requirements traceability: not yet documented.
