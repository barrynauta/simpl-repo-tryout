<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP07 — Establish usage contract</strong><br/>
</p>
</div>

# BP07 - Consumer and Provider establish a usage contract for selected catalogue items

## Overview

This business process describes the establishment of a legally binding usage contract between a **Consumer** and a **Provider** (Data, Application, or Infrastructure). This contract defines rights, limits, and obligations, including pricing, usage limits, data retention policies, and Service Level Agreements (SLAs).

### Scenarios for Contract Establishment

1.  **New resource consumption:** Accessing a new resource for the first time.
2.  **Usage contract expiration:** Creating a new immutable contract when an existing one expires.

## Actors

-   **Consumer**
-   **Provider:** Infrastructure, Application, or Data Provider.

## Prerequisites

-   **Dataspace Configuration:** Governance Authority has configured the catalogue, vocabulary, and schemas (BP02).
-   **Authentication & Authorisation:** End-User is authenticated with necessary roles (BP03B).
-   **Resource Availability:** Resource description is published (BP05) and has been found by the Consumer (BP06).

## Detailed Business Process Steps

| Step ID | Step Name | Description |
| :--- | :--- | :--- |
| **BP07.01** | **Request usage contract offer** | Consumer requests a contract based on a selected resource from the catalogue. |
| **BP07.02** | **Verify access policy** | Provider verifies Consumer's self-description against resource access policies. |
| **BP07.03** | **Verify existence usage contract** | Provider checks if a valid contract already exists for this resource. |
| **BP07.04** | **Provide usage contract** | Provider creates and sends a formal usage contract offer. |
| **BP07.05** | **Review terms and conditions** | Consumer reviews the offer and decides whether to accept. |
| **BP07.06** | **Sign usage contract (Consumer)** | Consumer signs the contract if terms are accepted. |
| **BP07.07** | **Store usage contract (Consumer)** | Consumer securely stores the signed contract for compliance. |
| **BP07.08** | **Validate usage contract** | Provider validates the Consumer's formal agreement. |
| **BP07.09** | **Sign usage contract (Provider)** | Provider signs the contract upon successful validation. |
| **BP07.10** | **Store usage contract (Provider)** | Provider stores the finalised contract in official records. |
| **BP07.11** | **Notify Consumer** | Provider notifies Consumer and makes the signed contract available. |
| **BP07.12** | **Confirm usage contract** | Consumer confirms the final contract against the original request. |

## High-Level Requirements

### 7.1 - Consumer requests a new usage contract offer
Simpl-Open shall support the Consumer to request a contract for a specific resource.

### 7.2 - Provider verifies the request for a usage contract offer
Simpl-Open shall support the Provider to automatically verify the request.

### 7.3 - Provider creates and provides the usage contract offer
Simpl-Open shall support the Provider to automatically generate the offer.

### 7.4 - Consumer reviews the usage contract offer
Simpl-Open shall support the Consumer to review the provided terms.

### 7.5 - Consumer signs, stores and provides the usage contract offer
Simpl-Open shall support the Consumer to sign and return the offer.

### 7.6 - Provider validates the signed usage contract offer
Simpl-Open shall support the Provider to validate the Consumer's signature.

### 7.7 - Provider signs, stores and provides the usage contract
Simpl-Open shall support the Provider to finalize the contract.

### 7.8 - Consumer validates the signed usage contract
Simpl-Open shall support the Consumer to perform a final validation.

## Outcomes

-   **Success:** Usage contract is active. Consumer can now access the resource according to the agreed terms.
-   **Failure:** Process terminated. No contract established.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp07-consumer-and-provider-establish-usage-contract-selected-catalogue-items](https://simpl-programme.ec.europa.eu/book-page/bp07-consumer-and-provider-establish-usage-contract-selected-catalogue-items)
