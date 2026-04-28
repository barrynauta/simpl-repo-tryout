<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP12B — Logging and monitoring</strong><br/>
</p>
</div>

# BP12B – Single node logging & monitoring

## Overview

This business process covers the collection, standardisation, and persistence of logs and metrics, monitoring of the Simpl-Agent, and the visualisation of results. It provides insights into system performance, user activities, and audit trails.

## Main Steps

1.  **Log resource consumption:** Technical logs for billing, audit, and compliance.
2.  **Log agent usage:** Internal logs for troubleshooting and auditing.
3.  **Generate alerts:** Triggered by health check failures or threshold breaches.
4.  **Generate reports:** Insights into system usage and performance.

## Actors

-   **Governance Authority**
-   **Provider**
-   **Consumer**

## Detailed Process Steps

| ID | Step | Description |
| :--- | :--- | :--- |
| **BP12B.01** | Log resource consumption | Captures technical logs for resource usage. |
| **BP12B.02** | Collect & persist metrics | Stores logs in a durable, standardised format. |
| **BP12B.04** | Monitor agent health | Tracks performance and errors of the local agent. |
| **BP12B.08** | Generate alerts | Notifies users when thresholds are exceeded. |
| **BP12B.09** | Generate reports | Creates scheduled or ad-hoc performance reports. |

## Reference Model: Log Types

-   **Business Logs:** Significant business events (e.g., onboarding requests).
-   **Technical Logs:** Application runtime, database queries, and system-level events.
-   **Metrics:** Infrastructure data (CPU, RAM, I/O).
-   **Health Checks:** Real-time component status.

## High-Level Requirements

-   **12B.2:** Log usage of agent components.
-   **12B.3:** Log and store business actions.
-   **12B.8:** Support for threshold-based alerting.
-   **12B.9:** Scheduled reporting on resource consumption.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp12b-single-node-logging-monitoring](https://simpl-programme.ec.europa.eu/book-page/bp12b-single-node-logging-monitoring)
