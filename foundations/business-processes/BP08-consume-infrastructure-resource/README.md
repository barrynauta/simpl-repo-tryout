<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP08 — Consumer consumes an infrastructure resource from a Provider</strong><br/>
</p>
</div>

# BP08 – Consumer consumes an infrastructure resource from a Provider

> **See also: [Dynamic view](./dynamic-view.md)** — sequence diagram showing how
> this business process executes at runtime, with links to each participating
> solution.

## Overview

This process enables a _Consumer_ with a usage contract to access infrastructure
resources from a _Provider_. The objective is to provide secure, transparent,
and contractually governed access to an infrastructure resource within a data
space, ensuring that both the Infrastructure _Provider_ and _Consumer_ have
clearly defined rights and obligations.

It includes the following main steps:

- **Request infrastructure resource** — the _Consumer_ requests the resource from the _Provider_.
- **Provision infrastructure resource** — the _Provider_ provisions and configures the resource in a dedicated environment.
- **Provide access to infrastructure resource** — the _Provider_ applies access controls and delivers credentials.

## Actors

- _Infrastructure Provider_
- _Consumer_

## Assumptions

- The Infrastructure _Provider_ has its services available and running.
- The _Consumer_ understands the available infrastructure resources and knows how to use them.

## Prerequisites

- **Data space is configured** — the _Governance Authority_ has configured the data space with vocabulary, schemas, and resource descriptions (BP02).
- **Both Consumer and Infrastructure Provider onboarded** (BP03A).
- **End-User authenticated & authorised** — the End-User is authenticated with the appropriate role and permissions (BP03B).
- **Resource description published in the catalogue** — the _Consumer_ has searched and found it (BP05B and BP06).

![BP08 figure 1](./media/BP08-figure-1.png)
*BP08 figure 1 — overview diagram*

![BP08 figure 2](./media/BP08-figure-2.png)
*BP08 figure 2 — detailed diagram*

## Process steps

### Trigger — infrastructure resource consumption

The _Consumer_ initiates the consumption process.

### BP08.01 Request infrastructure resource

The _Consumer_ requests the infrastructure resource from the Infrastructure
_Provider_.

### BP08.02 Provision infrastructure resource

The Infrastructure _Provider_ provisions and configures the infrastructure
resource for a dedicated environment specific for the _Consumer_.

### BP08.03 Post configuration

If the deployment script contains any part for the post-configuration process —
such as deployment of applications or loading datasets or images — the
Infrastructure _Provider_ performs the necessary actions in the
post-configuration phase.

### BP08.04 Provide access to the infrastructure resource

The _Provider_ configures and applies usage and access policies based on the
usage contract, and provides the _Consumer_ with the right access credentials.

### BP08.05 Access the infrastructure resource

The _Consumer_ consumes the resource until decommissioning.

### BP08.06 Remediate errors and notify Consumer

If during the provisioning or post-configuration process an error occurs, both
the _Consumer_ and the Infrastructure _Provider_ are informed through a
notification.

## High-level requirements

| ID | Title | Local copy |
|----|-------|------------|
| 8.1 | Requesting a resource (app/data/infrastructure). | [81-…](./81-requesting-resource-appdatainfrastructure.md) |
| 8.2 | Using infrastructure from a provider — Consumer Monitoring. | [82-…](./82-using-infrastructure-provider-consumer-monitoring.md) |
| 8.3 | Using infrastructure from a provider — Connectivity. | [83-…](./83-using-infrastructure-provider-connectivity.md) |
| 8.4 | Mechanisms to configure and provision infrastructure resources. | [84-…](./84-mechanisms-configure-and-provision-infrastructure-resources.md) |
| 8.5 | Using infrastructure from a provider — Credential management. | [85-…](./85-using-infrastructure-provider-credential-management.md) |
| 8.6 | Using infrastructure from a provider — IAM. | [86-…](./86-using-infrastructure-provider-iam.md) |
| 8.7 | Mechanisms to configure and provision VMs. | _no local file yet_ |
| 8.8 | Catalogue services. | [88-…](./88-catalogue-services.md) |

Detail pages on the public site:

- 8.1 → [81-requesting-resource-appdatainfrastructure](https://simpl-programme.ec.europa.eu/book-page/81-requesting-resource-appdatainfrastructure)
- 8.2 → [82-using-infrastructure-provider-consumer-monitoring](https://simpl-programme.ec.europa.eu/book-page/82-using-infrastructure-provider-consumer-monitoring)
- 8.3 → [83-using-infrastructure-provider-connectivity](https://simpl-programme.ec.europa.eu/book-page/83-using-infrastructure-provider-connectivity)
- 8.4 → [84-mechanisms-configure-and-provision-infrastructure-resources](https://simpl-programme.ec.europa.eu/book-page/84-mechanisms-configure-and-provision-infrastructure-resources)
- 8.5 → [85-using-infrastructure-provider-credential-management](https://simpl-programme.ec.europa.eu/book-page/85-using-infrastructure-provider-credential-management)
- 8.6 → [86-using-infrastructure-provider-iam](https://simpl-programme.ec.europa.eu/book-page/86-using-infrastructure-provider-iam)
- 8.7 → [8.5-mechanisms-configure-and-provision-vms](https://simpl-programme.ec.europa.eu/book-page/8.5-mechanisms-configure-and-provision-vms) *(note: source-site slug uses dotted "8.5" segment)*
- 8.8 → [88-catalogue-services](https://simpl-programme.ec.europa.eu/book-page/88-catalogue-services)

## Outcomes

- The _Consumer_ can consume the infrastructure resource based on the usage contract details, including the access policies and decommissioning terms and conditions.

## Source page metadata

- **Author:** Rick Marinus Johannes Santbergen
- **Published:** 23 June 2025
- **Status on source site:** Proposed
- **Snapshot taken:** 28 April 2026

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp08-consumer-consumes-infrastructure-resource-provider](https://simpl-programme.ec.europa.eu/book-page/bp08-consumer-consumes-infrastructure-resource-provider)

## Touches

- (auto-inferred — verify) [`../../../infrastructure/`](../../../infrastructure/README.md)
