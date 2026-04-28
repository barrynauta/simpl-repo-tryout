<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>SA01 — Data orchestration</strong><br/>
</p>
</div>

# SA01 - Data Orchestration Used by a Participant

## Overview

This supporting activity enables Participants (Providers and Consumers) to design, execute, and monitor repeatable data processing workflows within the data space.

## Workflow Model

-   **Service:** A modular, reusable unit of work (e.g., data transformation).
-   **Workflow:** A structured sequence of services defining orchestration logic and data flow.

## Triggering Mechanisms

-   **During Consumption:** Triggered by a resource request.
-   **Source Data Change:** Triggered by modifications to a dataset.
-   **Schedule:** Runs on a predefined time (e.g., daily).
-   **Manual:** Initiated via the User Interface.

## Detailed Steps

### SA01.01: Create a Workflow
-   Define logical sequence and select input sources.
-   Configure the triggering mechanism.

### SA01.02: Update a Workflow
-   Modify sequence, sources, or triggers.
-   Tracking via versioning for rollbacks.

### SA01.04: Execute a Workflow
-   Manual or automatic trigger.
-   Logging of results for each step.

### SA01.05: Monitor a Workflow Execution
-   Real-time status tracking (Running, Completed, Failed).
-   Access to logs and history.

## Outcomes

-   **Workflow established:** Participants can automate complex data handling tasks within the data space.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/sa01-data-orchestration-used-participant](https://simpl-programme.ec.europa.eu/book-page/sa01-data-orchestration-used-participant)
