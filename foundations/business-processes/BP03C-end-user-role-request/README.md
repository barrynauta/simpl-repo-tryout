<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP03C — Role Request</strong><br/>
</p>
</div>

# BP03C - End-User Role Request

## Overview

This business process covers the procedure for requesting roles by End-Users of Simpl-Open. It applies when a federated user logs in for the first time without assigned roles, or when a local user needs additional roles.

## Main Steps

1.  **Request role:** End-User submits a request to the Participant's Tier 1 User and Roles Manager.
2.  **Review role request:** The Manager reviews and either approves or rejects the request.

## Actors

The process involves the **Participant**, which can be an *End-User* or *Representative* of:
-   **Consumer**
-   **Provider**
-   **Governance Authority**

## Prerequisites & Assumptions

### Assumptions

-   The Participant has installed the Simpl-Open agent.
-   Default users and roles are available.

### Prerequisites

-   **Governance Authority Agent:** Configured and ready (BP02).
-   **Participant's User and Roles:** Module configured; Tier 1 users can log in (BP03B).

## Detailed Process Steps

### 1. Trigger Onboarding

The Participant's End-User logs into Simpl-Open and initiates the individual onboarding request.

### 2. BP03C.01 - Request Role

The End-User fills out a form specifying the requested roles and submits it for review.

### 3. BP03C.02 - Review Role Request

The **Participant's Tier 1 User Roles Manager** reviews the request to ensure:
-   The role matches declared responsibilities.
-   The request follows the **principle of least privilege**.

### 4. BP03C.03/04 - Notification

-   **Rejected:** User is notified of the rejection.
-   **Accepted:** User is notified of approval and the assigned role.

## Outcomes

-   **Success:** Requested roles are assigned to the End-User.
-   **Failure:** Roles are not assigned due to rejection.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp03c-end-user-role-request](https://simpl-programme.ec.europa.eu/book-page/bp03c-end-user-role-request)
