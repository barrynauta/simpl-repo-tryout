<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP05B — Manage resource descriptions</strong><br/>
</p>
</div>

# BP05B - Provider Manages Resource Descriptions

## Overview

This business process covers the management of resource descriptions in the data space catalogue by both a **Provider** and the **Governance Authority**. It includes creating new descriptions, updating versions, and revoking existing ones.

### Main Steps

-   **Create a new resource description:** Provider creates, signs, and submits a description for publication.
-   **Create a new version:** Provider updates an existing description (descriptions are immutable).
-   **Request revocation:** Provider requests the removal of a description.
-   **Publish:** Governance Authority validates and publishes the description.
-   **Revoke:** Governance Authority removes the description and informs Consumers.

## Actors

-   **Governance Authority**
-   **Provider**

## Assumptions

-   Creation/updates always use the latest schema version.
-   Existing usage contracts remain unaffected by new versions or revocations.
-   Revoked resources cannot be used for *new* contracts but remain inspectable for existing ones.

## Prerequisites

-   **Data space configured:** Vocabulary, schemas, and contract templates must be set up (BP02).
-   **Provider onboarded:** Successful completion of BP03A.
-   **Contract clauses available:** At least one set of clauses must be stored (BP05A).

## Detailed Process Steps

| ID | Step | Description |
| :--- | :--- | :--- |
| **BP05B.01** | **Create new description** | Provider selects resource type (data, app, infra) and enters common metadata. |
| **BP05B.02** | **Add type-specific metadata** | Provider adds metadata specific to the selected resource type. |
| **BP05B.03** | **Add policy/contract metadata** | Provider configures access/usage policies and contract-related metadata. |
| **BP05B.04** | **Sign and submit** | Provider signs the description with credentials and submits to the GA. |
| **BP05B.05** | **Validate description** | GA performs syntactic, semantic, and quality rule validations. |
| **BP05B.06** | **Remediate issues** | If validation fails, Provider must fix issues and resubmit. |
| **BP05B.07** | **Publish description** | Validated descriptions are published in the catalogue. |
| **BP05B.11** | **Revoke previous version** | GA revokes the old version once the new one is valid. |
| **BP05B.13** | **Request revocation** | Provider initiates the revocation of a published description. |
| **BP05B.14** | **Revoke description** | GA removes the description from the catalogue. |

## Outcomes

-   **Resource description managed:** The catalogue is updated with the latest version or the resource is revoked.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp05b-provider-manages-resource-descriptions](https://simpl-programme.ec.europa.eu/book-page/bp05b-provider-manages-resource-descriptions)
