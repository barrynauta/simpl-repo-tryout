<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP09B — Consume data via application</strong><br/>
</p>
</div>

# BP09B – Consumer receives a data processing service via an application

## Overview

This business process describes the scenario where a **Consumer** processes a data resource using an application provided by a **Data Provider**. This allows for restricted viewing or processing without necessarily transferring the raw data.

### Scenarios

1.  **Scenario 1: Stand-alone application on dedicated infrastructure**
    -   Provider provisions dedicated infrastructure and deploys the application.
    -   Consumer receives access to application endpoints.
2.  **Scenario 2: Shared access to an existing application**
    -   Consumer gains access to an already running shared application.

## Actors

-   **Consumer**
-   **Data Provider**

## Prerequisites

-   **Dataspace Configuration:** GA has configured the catalogue (BP02).
-   **Onboarding:** Both parties are onboarded (BP03A).
-   **Authentication & Authorization:** End-User is authenticated (BP03B).
-   **Usage Contract:** A contract is established for the data resource and application (BP07).

## Detailed Process Steps

| Step ID | Step Name | Description |
| :--- | :--- | :--- |
| **BP09B.01** | **Request data resource** | Consumer initiates the request based on catalogue information. |
| **BP09B.02** | **Consume infrastructure (BP08)** | Infrastructure is provisioned for deployment (Scenario 1). |
| **BP09B.03** | **Deploy application** | Provider deploys the application automatically via scripts. |
| **BP09B.04** | **Provide access** | Provider configures access control and provides credentials. |
| **BP09B.05** | **Access data via application** | Consumer processes the data using the application interface. |

## Outcomes

-   **Data resource is processed:** The Consumer successfully utilizes the processing service.

## High Level Requirements

-   **9B.1:** Simpl provides built-in processing tools.
-   **9B.5:** Support for generating a copy of the dataset intended for processing to ensure integrity.
-   **9B.6:** Automatic provisioning of VMs for application deployment.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp09b-consumer-receives-data-processing-service-data-resource-application](https://simpl-programme.ec.europa.eu/book-page/bp09b-consumer-receives-data-processing-service-data-resource-application)
