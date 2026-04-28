<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP02 — Configure Governance Authority</strong><br/>
</p>
</div>

# BP02 - Configuration of data space Governance Authority

## Overview

This business process involves the comprehensive configuration of a data space to ensure it is functional, secure, and interoperable. It follows the initial definition of governance (BP01) and sets the technical stage for participant onboarding and resource sharing. The configuration covers identity and trust mechanisms, vocabulary management, and resource description schemas.

## Actors

-   **Governance Authority (GA):** The primary entity responsible for the data space.
-   **Governance Authority Representative:** The authenticated individual performing the configuration steps.

## Prerequisites

-   **Governance Defined (BP01):** Roles and permissions must be established.
-   **GA Agent Installed:** The Simpl-Open agent must be deployed with valid cryptographic keys and security credentials (e.g., X.509).
-   **Default Attributes:** Built-in identity attributes must be available in the system.

## Configuration Sub-Processes

### BP02A — Configure ID/Trust Security Solution

Focuses on securing communication and establishing the trust framework for onboarding.
-   **Define Identity Attributes:** Creation of custom attributes to supplement built-in ones.
-   **Onboarding Templates:** Setting up procedures for different participant types, including required documentation and validation rules.
-   **Security Settings:** Defining encryption standards and token policies.

### BP02B — Manage Vocabularies

Ensures semantic interoperability by governing the lifecycle of data space vocabularies.
-   **Lifecycle Management:** Creating, validating, publishing, and deprecating vocabularies (e.g., RDF Schema, OWL).
-   **Validation:** Ensuring syntactic and semantic correctness before publication.
-   **Versioning:** Managing iterations based on stakeholder feedback or domain evolution.

### BP02C — Manage Resource Description Schemas

Standardizes how resources (data, applications, infrastructure) are described in the catalogue.
-   **Schema Definition:** Defining mandatory and recommended metadata properties for each resource type.
-   **Validation & Publication:** Ensuring resource descriptions adhere to the established vocabularies and structure.
-   **Notification:** Informing Providers of schema updates or revocations to ensure catalogue consistency.

## Outcomes

-   **Governance Authority Ready:** The GA is technically capable of overseeing the data space.
-   **Trust Framework Active:** Onboarding templates and security policies are live.
-   **Catalogue Initialized:** Validated vocabularies and schemas are available for Providers to use when publishing resources.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp02b-setup-idtrust-catalogues-and-vocabulary](https://simpl-programme.ec.europa.eu/book-page/bp02b-setup-idtrust-catalogues-and-vocabulary)
