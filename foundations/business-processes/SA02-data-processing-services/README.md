<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>SA02 — Data processing services</strong><br/>
</p>
</div>

# SA02 – Data processing services used by a Participant

## Overview

This supporting activity provides functional containers for data processing services offered through Simpl. It covers the full data lifecycle—from preparation to analysis—enabling governed interaction with datasets.

## Services Provided

-   **Data Pseudonymisation:** Reversible transformation that allows re-identification only when justified.
-   **Data Anonymisation:** Irreversible transformation ensuring no link to original subjects remains.

## Actors

-   **Participant:** Either a Provider or a Consumer.

## Prerequisites

1.  **Participant Onboarded:** Completion of BP03A.
2.  **End-User Authenticated:** Appropriate roles/permissions (BP03B).

## Detailed Steps

### 1. Trigger Data Processing Services
The Participant selects a service based on operational needs.

### 2. SA02.01: Data Pseudonymisation
-   Participant evaluates dataset and applies technique.
-   Can be configured at execution or via saved templates.

### 3. SA02.02: Data Anonymisation
-   Participant applies irreversible transformation.
-   Technical support is provided, but expert judgment is required for risk management.

## High-Level Requirements

-   **2.1:** Service for dataset pseudonymisation.
-   **2.2:** Service for dataset anonymisation.

## Touches

-   [`../../data/data-processing/anonymisation-and-pseudonymisation/dataframe-level-anonymisation/`](../../data/data-processing/anonymisation-and-pseudonymisation/dataframe-level-anonymisation/README.md)
-   [`../../data/data-processing/anonymisation-and-pseudonymisation/field-level-pseudo-anonymisation/`](../../data/data-processing/anonymisation-and-pseudonymisation/field-level-pseudo-anonymisation/README.md)

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/sa02-data-processing-services-used-participant](https://simpl-programme.ec.europa.eu/book-page/sa02-data-processing-services-used-participant)
