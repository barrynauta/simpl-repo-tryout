<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP12B — Single node logging &amp; monitoring</strong><br/>
</p>
</div>

# BP12B – Single node logging & monitoring

> **See also: [Dynamic view](./dynamic-view.md)** — sequence diagram showing how
> this business process executes at runtime, with links to each participating
> solution.

## Overview

This business process covers the collection, standardisation, and persistence of
logs and metrics, the monitoring of the Simpl-Agent, and the visualisation and
reporting of data. The logs include gathering metrics like performance data,
error logs, and usage statistics. Furthermore, visualisations and reports
provide insights into system performance and user activities. This workflow is
applicable to all _Participants_ — _Consumers_, _Providers_, and the
_Governance Authority_.

It includes the following main steps:

- **Log consumption of a resource (infra/data/app)** — during consumption of an infrastructure / data / application resource, the Simpl-Open agent generates technical logs used for billing, audit, policy enforcement, regulation compliance, etc.
- **Log usage of Simpl-Open agent components** — while running, Simpl-Open agent components generate technical and business logs used for audit and troubleshooting.
- **Generate alerts** — alerts are generated when health checks fail or predefined thresholds are exceeded.
- **Generate reports** — logged data is compiled into reports providing insights (e.g. system performance, user activities, issues encountered).

## Actors

- _Governance Authority_
- _Provider_
- _Consumer_

> In the diagrams, they are described collectively as _Participant_.

## Assumptions

- The Simpl-Open agent is configured to capture technical logs that allow following the consumption of (infrastructure / data / application) resources.
- The Simpl-Open agent is configured to capture technical logs that allow following the usage of the agent components.
- The Simpl-Open agent is configured to capture technical logs that allow following the infrastructure and service health.
- The Simpl-Open agent is configured to capture business logs for significant events or actions (related to steps within a business process or other functional use cases).
- A solution is in place to persist the technical and business logs.
- A solution is in place for monitoring, alerting and visualising the technical and business logs.

## Prerequisites

- **Data space is configured** — the _Governance Authority_ has configured the data space catalogue with the corresponding vocabulary and schemas (BP02).
- **Participant onboarded** — the _Participant_ has successfully completed the onboarding business process (BP03A).

![BP12B figure 1](./media/BP12B-figure-1.png)
*BP12B figure 1 — overview diagram*

![BP12B figure 2](./media/BP12B-figure-2.png)
*BP12B figure 2 — detailed diagram*

## Process steps

### Trigger — single node logging & monitoring

While using Simpl-Open, the agent of the _Participant_ initiates the single node
logging and monitoring.

### BP12B.01 Log the consumption of a resource (infra/data/app)

During the consumption of a (infrastructure / data / application) resource, the
Simpl-Open agent of the _Participant_ generates technical logs that will be used
for various reasons (billing, audit, policy enforcement, regulation compliance,
infrastructure metrics, service health, etc.). This is generally done with a
push-based mechanism, but can also be done with a pull-based mechanism for the
purpose of monitoring infrastructure metrics and service health.

### BP12B.02 Collect and persist infrastructure metrics and technical logs

The Simpl-Open agent of the _Participant_ converts the collected technical logs
and infrastructure metrics into a consistent format to facilitate analysis and
integration with other monitoring tools. The collected and standardised
technical logs and metrics are persisted in a durable, accessible location for
future analysis and access.

### BP12B.03 Monitor consumption of a resource (infra/data/app)

The _Participant_ monitors the consumption of resources through a dashboard to
enforce policies and regulations compliance.

### BP12B.04 Monitor usage and health of Simpl-Open agent

The _Participant_ monitors the Simpl-Open agent usage and health through a
dashboard to ensure it is functioning correctly, tracking the usage, its
performance, and any errors or warnings.

### BP12B.05 Log the usage of Simpl-Open agent components

While they are running, the components of the Simpl-Open agent of the
_Participant_ generate both technical logs and business logs that will be used
for audit and troubleshooting. The business logs are generated for pre-defined
significant events or actions (related to steps within a business process or
other functional use cases).

### BP12B.06 Collect and persist business logs

The Simpl-Open agent of the _Participant_ converts the collected business logs
into a consistent format to facilitate analysis and integration with other
monitoring tools. The collected and standardised business logs are persisted in
a durable, accessible location for future analysis and access.

### BP12B.07 Monitor business actions

The _Participant_ monitors the business actions through a dashboard.

### BP12B.08 Generate alerts

The _Participant_ defines alerts and assigns target users to receive the alerts
when they occur. The Simpl-Open agent of the _Participant_ generates alerts when
health checks fail or predefined thresholds are exceeded, and shares them with
the assigned target users.

### BP12B.09 Generate reports

The _Participant_ defines and schedules reports based on the logged data to
support monitoring and follow-up. The Simpl-Open agent generates the pre-defined
reports according to the schedule. The _Participant_ also defines and generates
custom ad-hoc reports based on the logged data to support analysis and
follow-up of specific issues.

## High-level requirements

| ID | Title | Local copy |
|----|-------|------------|
| 12B.1 | A Consumer and Provider log the consumption of infrastructure resources. | [12b1-…](./12b1-consumer-and-provider-log-consumption-infrastructure-resources.md) |
| 12B.2 | A Participant logs the usage of Simpl-Open agent components. | [12b2-…](./12b2-participant-logs-usage-simpl-open-agent-components.md) |
| 12B.3 | A Participant logs business actions. | [12b3-…](./12b3-participant-logs-business-actions.md) |
| 12B.4 | A Consumer and Provider log the consumption of data and application resources. | [12b4-…](./12b4-consumer-and-provider-log-consumption-data-and-application-resources.md) |
| 12B.5 | A Participant checks the health of the application components of their Simpl-Open agent. | [12b5-…](./12b5-participant-checks-health-application-components-their-simpl-open-agent.md) |
| 12B.6 | A Participant stores logs and metrics. | [12b6-…](./12b6-participant-stores-logs-and-metrics.md) |
| 12B.7 | A Participant monitors their Simpl-Open agent usage, consumption of resources, and business actions. | [12b7-…](./12b7-participant-monitors-their-simpl-open-agent-usage-consumption-resources-and-business.md) |
| 12B.8 | A Participant generates alerts on their Simpl-Open agent usage, consumption of resources, and business actions. | [12b8-…](./12b8-participant-generates-alerts-their-simpl-open-agent-usage-consumption-resources-and.md) |
| 12B.9 | A Participant reports on their Simpl-Open agent usage, consumption of resources, and business actions. | [12b9-…](./12b9-participant-reports-their-simpl-open-agent-usage-consumption-resources-and-business.md) |

Detail pages on the public site:

- 12B.1 → [12b1-consumer-and-provider-log-consumption-infrastructure-resources](https://simpl-programme.ec.europa.eu/book-page/12b1-consumer-and-provider-log-consumption-infrastructure-resources)
- 12B.2 → [12b2-participant-logs-usage-simpl-open-agent-components](https://simpl-programme.ec.europa.eu/book-page/12b2-participant-logs-usage-simpl-open-agent-components)
- 12B.3 → [12b3-participant-logs-business-actions](https://simpl-programme.ec.europa.eu/book-page/12b3-participant-logs-business-actions)
- 12B.4 → [12b4-consumer-and-provider-log-consumption-data-and-application-resources](https://simpl-programme.ec.europa.eu/book-page/12b4-consumer-and-provider-log-consumption-data-and-application-resources)
- 12B.5 → [12b5-participant-checks-health-application-components-their-simpl-open-agent](https://simpl-programme.ec.europa.eu/book-page/12b5-participant-checks-health-application-components-their-simpl-open-agent)
- 12B.6 → [12b6-participant-stores-logs-and-metrics](https://simpl-programme.ec.europa.eu/book-page/12b6-participant-stores-logs-and-metrics)
- 12B.7 → [127-monitoring-business-actions](https://simpl-programme.ec.europa.eu/book-page/127-monitoring-business-actions) *(note: source-site slug differs)*
- 12B.8 → [12b8-participant-generates-alerts-their-simpl-open-agent-usage-consumption-resources-and](https://simpl-programme.ec.europa.eu/book-page/12b8-participant-generates-alerts-their-simpl-open-agent-usage-consumption-resources-and)
- 12B.9 → [12b9-make-all-logged-information-retrievable-real-time-reporting-module](https://simpl-programme.ec.europa.eu/book-page/12b9-make-all-logged-information-retrievable-real-time-reporting-module) *(note: source-site slug differs)*

## Source page metadata

- **Author:** Rick Marinus Johannes Santbergen
- **Published:** 23 June 2025
- **Status on source site:** Proposed
- **Snapshot taken:** 28 April 2026

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp12b-single-node-logging-monitoring](https://simpl-programme.ec.europa.eu/book-page/bp12b-single-node-logging-monitoring)

## Touches

- (auto-inferred — verify) [`../../../cross-cutting/`](../../../cross-cutting/README.md)
