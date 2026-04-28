<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP09A — Consume data resource</strong><br/>
</p>
</div>

# BP09A – Consumer consumes a data resource from a Provider

## Overview

This process facilitates secure, transparent, and contractually governed access to a data resource within a data space. It covers the scenario where a Consumer, having established a usage contract, seeks to consume a data resource from a Data Provider.

## Actors

-   **Data Provider:** The entity that provides the data resource and manages access control.
-   **Consumer:** The entity that requests and consumes the data resource based on a usage contract.

## Prerequisites

1.  **Dataspace Configuration:** Governance Authority has configured the catalogue and schemas (BP02).
2.  **Onboarding:** Both parties must have completed onboarding (BP03A).
3.  **Authentication & Authorization:** End-User must possess the appropriate roles (BP03B).
4.  **Resource Discovery:** The Consumer has identified the resource in the catalogue (BP06).
5.  **Usage Contract:** A valid contract is established for the specific resource (BP07).

## Detailed Steps

### 1. Trigger Data Resource Consumption

The process is initiated by the Consumer when they decide to access a data resource for which they have a valid contract.

### 2. BP09A.01: Request Data Resource

-   **Action:** The Consumer sends a request for a specific data resource to the Data Provider.
-   **Basis:** The request aligns with the identified catalogue item and contract.

### 3. BP09A.02: Provide Access to the Data Resource

-   **Action:** The Data Provider processes the request and provides access.
-   **Mechanism:** The Provider applies access control rules and provides credentials or the resource itself (e.g., via S3, file transfer, or direct link).

### 4. BP09A.03: Access the Data Resource

-   **Action:** The Consumer uses the provided credentials or channel to access/download the data.

## Outcomes

-   **Data Resource Consumed:** The Consumer successfully accesses the data in accordance with the established agreements and access policies.

## High Level Requirements

-   **9A.2 (Usage Policy Enforcement):** Policies (e.g., time limits, purpose) are enforced during consumption.
-   **9A.5 (Real-Time Support):** Support for (near) real-time data access across data spaces.
-   **9A.6 (Subscription Management):** Consumers can manage or terminate subscriptions at any time.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp09a-consumer-consumes-data-resource-provider](https://simpl-programme.ec.europa.eu/book-page/bp09a-consumer-consumes-data-resource-provider)
