<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP03B — End-User Onboarding</strong><br/>
</p>
</div>

# BP03B – Onboarding of a new data space - Participant End-User

## Overview

This business process covers the configuration of the **User and Roles** module within **Simpl-Open**. It details how a Participant (Consumer, Provider, or Governance Authority) manages end-users and their access permissions within their Simpl-Open Agent.

## Main Steps

1.  **Configure Roles:** Managing roles available in the Participant's Simpl-Open Agent.
2.  **Configure Identity Provider Federation:** (Optional) Linking external IDPs (e.g., EU Login, eIDAS, or private corporate IDPs).
3.  **Manage End Users:** Creating and managing users and assigning them roles.

## Actors

-   **Participant:** End-User or Representative of a Consumer, Provider, or Governance Authority.
-   **Tier 1 User Roles Manager:** The specific role responsible for performing these configurations.

## Prerequisites & Assumptions

-   **Assumption:** The Simpl-Open agent is installed with default users and roles available.
-   **Prerequisite 1:** Governance Authority must be configured (BP02).
-   **Prerequisite 2:** Participant onboarding must be completed (BP03A).

## Detailed Process Steps

### BP03B.01: Configure Roles

The Tier 1 User Roles Manager configures roles by mapping Identity Attributes to specific user roles.
-   **Role Creation:** Define new roles.
-   **Role Update:** Modify attributes of existing roles.
-   **Role Cancellation:** Delete roles.

### BP03B.02: Configure Identity Provider Federation

Allows users to log in using existing organizational credentials.
-   **Scope:** Supports external IDPs like eIDAS, EU Login, or private IDPs.

### BP03B.03: Manage End User

Management of the actual user accounts within the Agent.
-   **Account Creation:** New user registration and initial role assignment.
-   **Account Update:** Modifying user attributes or roles.
-   **Account Cancellation:** Deleting users.

## High-Level Requirements

| ID | Requirement | Description |
| :--- | :--- | :--- |
| **3B.1** | **Access Control - End Users to Agent** | Simpl shall support Role-based Access Control (RBAC). |
| **3B.2** | **Access Control - Roles Management** | Simpl shall support the management of end users and their associated roles. |
| **3B.3** | **Manage Users and Permissions** | Simpl shall provide support for the registration and permission management of new participants. |
| **3B.4** | **Federated Authentication** | Simpl shall support authentication systems from trusted service providers. |

## Outcomes

-   **Configured User and Roles Module:** The Participant's Agent is ready for Tier 1 users to log in and perform operations.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp03b-onboarding-new-data-space-participant-end-user](https://simpl-programme.ec.europa.eu/book-page/bp03b-onboarding-new-data-space-participant-end-user)
