<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP03A — Participant Onboarding</strong><br/>
</p>
</div>

# BP03A – Onboarding of a new data space Participant

## Overview

This business process defines the requirements and steps for transitioning an "Applicant" (an organization) into a "Participant" within a data space. It covers Data, Application, and Infrastructure Providers as well as Consumers.

## Main Steps

1.  **Prepare & Submit Onboarding Request:**
    -   The Applicant submits a request to the Governance Authority, including documentation and identity attributes.
    -   The request specifies roles (Consumer, Provider, or both).
2.  **Review & Validation:**
    -   The Governance Authority verifies the request against predefined criteria.
    -   Automated validation supports document checks and eIDAS attribute verification.
    -   Manual approval or rejection by the Governance Authority.
3.  **Agent Deployment & Key Generation:**
    -   Approved Applicant deploys the **Simpl-Open agent**.
    -   The Applicant generates a public/private key pair.
4.  **Security Credentials (X.509):**
    -   The Governance Authority signs digital security credentials (X.509 certificates) incorporating the Applicant's public key.
5.  **Finalization:**
    -   The Applicant installs the signed credentials into their Simpl-Open Agent.

## Actors

-   **Applicant:** The organization seeking to join the data space.
-   **Governance Authority (GA):** The entity responsible for overseeing the onboarding process.

## Prerequisites

-   **Data Space Configuration (BP02):** The GA must have defined onboarding rules, required attributes, and templates.
-   **Organizational Identity:** Applicants must be recognized organizations.

## High-Level Requirements

-   **3A.1:** System must support role-based requests and store verification documents.
-   **3A.2.4:** Support for automated validation (eIDAS, document consistency).
-   **3A.2.2:** Manual override/review capability for the Governance Authority.

## Outcomes

-   **Success:** Applicant becomes a Participant with active credentials.
-   **Failure:** Request rejected; Applicant notified.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp03a-onboarding-new-data-space-participant-providers-data-application-infrastructure-consumers](https://simpl-programme.ec.europa.eu/book-page/bp03a-onboarding-new-data-space-participant-providers-data-application-infrastructure-consumers)
