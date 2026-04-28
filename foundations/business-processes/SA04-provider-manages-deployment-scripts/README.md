<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>SA04 — Deployment script management</strong><br/>
</p>
</div>

# SA04 - Provider Manages Deployment Scripts

## Overview

This activity covers the management of deployment scripts used for provisioning infrastructure and post-configuration of resources. It supports the metadata management in BP05B.

## Core Functionality

-   **Provisioning:** Setting up dedicated environments for Consumers.
-   **Post-Configuration:** Deploying applications or loading data automatically.
-   **VM Templates:** Parameters for automatic VM provisioning across cloud providers.

## Actors

-   **Infrastructure Provider**

## Detailed Steps

### 1. Manage VM Templates

-   **SA04.01: Create Template:** Define hardware, OS, and post-provisioning blocks. Automatically generates a deployment script.
-   **SA04.02: Update Template:** Modifies building blocks and updates related scripts.
-   **SA04.03: Delete Template:** Removes the template and its linked script.

### 2. Manage Deployment Scripts

-   **SA04.04: Create Script:** Upload manual instruction files for infrastructure creation.
-   **SA04.05: Update Script:** Modify existing configuration items.
-   **SA04.06: Delete Script:** Removes the script from the catalogue.

## Outcomes

-   **Scripts Managed:** Providers can link automated deployment logic to their infrastructure resource descriptions.

## High-Level Requirements

-   **4.1:** Consult VM templates.
-   **4.2:** Consult deployment scripts.
-   **4.3:** Create new VM templates.

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/sa04-provider-manages-deployment-scripts](https://simpl-programme.ec.europa.eu/book-page/sa04-provider-manages-deployment-scripts)
