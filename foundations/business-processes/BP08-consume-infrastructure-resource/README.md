<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP08 — Consume infrastructure resource</strong><br/>
</p>
</div>

# BP08 – Consumer consumes an infrastructure resource from a Provider

## Overview

This business process covers the situation where a **Consumer** has a usage contract for a certain infrastructure resource and seeks to consume it from an **Infrastructure Provider**. The goal is to facilitate secure, transparent, and contractually governed access within a data space.

## Main Steps

1.  **Request infrastructure resource:** The Consumer requests the resource from the Provider.
2.  **Provision infrastructure resource:** The Provider provisions and configures the resource on a dedicated environment.
3.  **Provide access to infrastructure resource:** The Provider applies access control rules and provides credentials.

## Actors

-   **Infrastructure Provider**
-   **Consumer**

## Assumptions & Prerequisites

### Assumptions

-   The Infrastructure Provider has services available and running.
-   The Consumer understands the available resources and how to use them.

### Prerequisites

-   **Data space is configured:** Governance Authority has configured the catalogue (BP02).
-   **Onboarding complete:** Both parties are onboarded (BP03A).
-   **Authenticated & Authorised:** The End-User has appropriate permissions (BP03B).
-   **Resource description present:** The resource is published in the catalogue (BP05) and found by the Consumer (BP06).

## Detailed Process Steps

### 1. Trigger infrastructure resource consumption

The Consumer initiates the process.

### 2. BP08.01 Request infrastructure resource

The Consumer sends a request for the infrastructure resource to the Provider.

### 3. BP08.02 Provision infrastructure resource

The Provider provisions and configures the resource for a dedicated environment specific to the Consumer.

### 4. BP08.03 Post configuration

If deployment scripts include post-configuration (e.g., deploying apps, loading datasets), the Provider executes these actions.

### 5. BP08.04 Provide access to the infrastructure resource

The Provider configures usage and access policies (duration, limitations) based on the usage contract and delivers access credentials.

### 6. BP08.05 Access the infrastructure resource

The Consumer consumes the resource until it is decommissioned.

### 7. BP08.06 Remediate errors and notify Consumer

If errors occur during provisioning, both parties are notified. The Provider reviews, solves, and monitors the process until remediation is complete.

## Outcome

-   **Infrastructure resource is consumed:** The Consumer has access based on contract details, including access policies and decommissioning terms.

## High Level Requirements

### 8.1 - Requesting a resource (app/data/infrastructure)

SIMPL shall have a mechanism to allow consumers to request resources through the platform.

### 8.2 - Using infrastructure from a provider - Consumer Monitoring

Simpl shall provide monitoring capabilities to ensure the Consumer can track resource usage and performance.

### 8.3 - Using infrastructure from a provider - Connectivity

SIMPL shall support the establishment of necessary communication channels between the Consumer and the Provider's infrastructure.

### 8.4 - Mechanisms to configure and provision infrastructure resources

Simpl shall provide mechanisms to automatically configure and provision resources based on predefined scripts or templates.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp08-consumer-consumes-infrastructure-resource-provider](https://simpl-programme.ec.europa.eu/book-page/bp08-consumer-consumes-infrastructure-resource-provider)
