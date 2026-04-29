<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP09A — Consumer consumes a data resource from a Provider</strong><br/>
</p>
</div>

# BP09A – Consumer consumes a data resource from a Provider

> **See also: [Dynamic view](./dynamic-view.md)** — sequence diagram showing how
> this business process executes at runtime, with links to each participating
> solution.

## Overview

This business process covers the situation where a _Consumer_ has a usage
contract for a certain data resource and seeks to consume that data resource
from a _Data Provider_. The aim is to facilitate secure, transparent, and
contractually governed access to a data resource within a data space, ensuring
that both _Data Providers_ and _Consumers_ have clearly defined rights and
obligations.

The process involves two basic actions:

1. _Data Providers_ grant _Consumers_ access using various methods (direct download, file transfer, etc.).
2. _Consumers_ request and access the data resource through established channels.

## Actors

- _Data Provider_
- _Consumer_

## Assumptions

None listed.

## Prerequisites

- **Dataspace is configured** — the _Governance Authority_ has configured the catalogue with the corresponding vocabulary and schemas (BP02).
- **Consumer / Data Provider onboarded** — both parties have completed onboarding (BP03A).
- **End-User authenticated & authorised** — the End-User has the appropriate role and permissions (BP03B).
- **Resource description present in the data space catalogue** — published (BP05B) and previously searched (BP06).
- **Usage contract established** — the _Consumer_'s access is governed by contractual terms (BP07).

![BP09A figure 1](./media/BP09A-figure-1.png)
*BP09A figure 1 — overview diagram*

![BP09A figure 2](./media/BP09A-figure-2.png)
*BP09A figure 2 — detailed business process diagram*

## Process steps

### Trigger — data resource consumption

The _Consumer_ initiates consumption of a data resource from a _Data Provider_.

### BP09A.01 Request data resource

The _Consumer_ initiates the process by requesting a specific data resource from
the _Data Provider_. This request is based on the information found in the data
space catalogue, which was previously searched and identified by the _Consumer_.

### BP09A.02 Provide access to the data resource

The _Data Provider_ provides the data resource via various means (e.g. direct
download link, file transfer via various existing technologies, etc.), as
indicated on the resource description published in the data space catalogue and
in the usage contract; accordingly, the data resource can be accessed or
downloaded.

### BP09A.03 Access the data resource

The _Consumer_ consumes the data resource via the channel indicated on the
resource description.

## High-level requirements

| ID | Title | Local copy |
|----|-------|------------|
| 9A.1 | A Consumer requests a data resource. | [9a1-…](./9a1-consumer-requests-data-resource.md) |
| 9A.2 | Enable and enforce usage policies — Enforcement. | _no local file yet_ |
| 9A.3 | Subscription to a dataset/application/infrastructure — Penalties. | [9a3-…](./9a3-subscription-datasetapplicationinfrastructure-penalties.md) |
| 9A.4 | Subscription to a dataset/application/infrastructure — Consumer. | [9a4-…](./9a4-subscription-datasetapplicationinfrastructure-consumer.md) |
| 9A.5 | Support for (near) real-time data within / across data spaces. | [9a5-…](./9a5-support-nearreal-time-data-withinacross-data-spaces.md) |
| 9A.6 | Subscription to a data/application/infrastructure — Provider. | [9a6-…](./9a6-subscription-dataapplicationinfrastructure-provider.md) |
| 9A.7 | A Provider provides access to a data resource. | [9a7-…](./9a7-provider-provides-access-data-resource.md) |

Detail pages on the public site:

- 9A.1 → [9a1-consumer-requests-data-resource](https://simpl-programme.ec.europa.eu/book-page/9a1-consumer-requests-data-resource)
- 9A.2 → [9a2-enable-and-enforce-usage-policies-enforcement](https://simpl-programme.ec.europa.eu/book-page/9a2-enable-and-enforce-usage-policies-enforcement)
- 9A.3 → [9a3-subscription-datasetapplicationinfrastructure-penalties](https://simpl-programme.ec.europa.eu/book-page/9a3-subscription-datasetapplicationinfrastructure-penalties)
- 9A.4 → [9a4-subscription-datasetapplicationinfrastructure-consumer](https://simpl-programme.ec.europa.eu/book-page/9a4-subscription-datasetapplicationinfrastructure-consumer)
- 9A.5 → [9a5-support-nearreal-time-data-withinacross-data-spaces](https://simpl-programme.ec.europa.eu/book-page/9a5-support-nearreal-time-data-withinacross-data-spaces)
- 9A.6 → [9a6-subscription-dataapplicationinfrastructure-provider](https://simpl-programme.ec.europa.eu/book-page/9a6-subscription-dataapplicationinfrastructure-provider)
- 9A.7 → [9a7-provider-provides-access-data-resource](https://simpl-programme.ec.europa.eu/book-page/9a7-provider-provides-access-data-resource)

## Source page metadata

- **Author:** Johan van Wyk
- **Published:** 23 June 2025
- **Status on source site:** Proposed
- **Snapshot taken:** 28 April 2026

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp09a-consumer-consumes-data-resource-provider](https://simpl-programme.ec.europa.eu/book-page/bp09a-consumer-consumes-data-resource-provider)

## Touches

- (auto-inferred — verify) [`../../../data/`](../../../data/README.md)
