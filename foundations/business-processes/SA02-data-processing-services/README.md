<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>SA02 — Data processing services used by a Participant</strong><br/>
</p>
</div>

# SA02 – Data processing services used by a Participant

## Overview

This supporting activity serves solely as a functional container for a set of
data processing services offered through the Simpl platform. It is expected that
services will be incrementally added to the process to cover the full data
lifecycle — from preparation and transformation to analysis and beyond —
enabling both _Providers_ and _Consumers_ to interact with datasets in a
structured and governed manner. While this supporting activity does not aim to
define specific workflows, it is intended to present, at a high level, the
scope of the data processing services it refers to.

Simpl currently provides two data processing services used by _Participants_
(both _Provider_ and _Consumer_) according to their specific needs. Additional
services are planned for future introduction.

These services will be made available in the Simpl-Open agent. Some services
will be pre-installed (i.e. deployed together with the Simpl-Open agent),
others can be added by the participants or identified in the application
catalogue. Services expected to be relevant across multiple usage patterns will
be provided as pre-installed, whereas more specialised services will be
identified in the application catalogue.

This service supports _Participants_ (either _Provider_ or _Consumer_) in
protecting personal data, as well as business-critical information, confidential
datasets, and other sensitive records, by enabling the application of a range of
data protection techniques.

- **Pseudonymisation** allows for reversible transformations, making it possible to re-identify data subjects when justified, through the use of securely managed auxiliary information.
- **Anonymisation** ensures that data is irreversibly transformed in such a way that no direct or indirect link to the original data subjects remains.

## Actors

- _Participant_ (Provider and Consumer)

## Assumptions

- The pseudonymisation and anonymisation service allows users to balance data protection with data utility by selecting and applying the most appropriate techniques based on their operational needs.
- Users retain full responsibility for making informed decisions on the data to be processed and the techniques to be used, validating the effectiveness of the chosen methods, and managing any associated risks. The service provides support but does not replace expert judgment.

## Prerequisites

- **Participant onboarded** — the _Participant_ should have successfully completed the onboarding business process (BP03A).
- **End-User authenticated & authorised** — the End-User is authenticated and has the appropriate role and permissions to perform the steps in the process (BP03B).

![SA02 figure 1](./media/SA02-figure-1.png)
*SA02 figure 1 — overview diagram*

## Process steps

### Trigger — data processing services

The _Participant_ (either _Provider_ or _Consumer_) decides to use one of the
available data processing services offered by Simpl, based on their operational
needs.

### SA02.01 Data pseudonymisation

The _Participant_, after evaluating the dataset and the context of use, decides
to apply a pseudonymisation technique on the dataset. This technique can either
be configured by the _Participant_ at the moment of execution or applied based
on a previously defined configuration.

### SA02.02 Data anonymisation

The _Participant_, after evaluating the dataset and the context of use, decides
to apply an anonymisation technique on the dataset. This technique can either be
configured by the _Participant_ at the moment of execution or applied based on a
previously defined configuration.

## High-level requirements

| ID | Title | Local copy |
|----|-------|------------|
| 2.1 | Participant pseudonymises a dataset. | [21-…](./21-participant-pseudonymises-dataset.md) |
| 2.2 | Participant anonymises a dataset. | [22-…](./22-participant-anonymises-dataset.md) |

> **Note on numbering:** the source site uses bare `2.x` IDs (and `2x-…` slugs)
> for these HLRs, not `SA02.x`. Local files mirror that.

Detail pages on the public site:

- 2.1 → [21-participant-pseudonymises-dataset](https://simpl-programme.ec.europa.eu/book-page/21-participant-pseudonymises-dataset)
- 2.2 → [22-participant-anonymises-dataset](https://simpl-programme.ec.europa.eu/book-page/22-participant-anonymises-dataset)

## Outcomes

- The _Participant_ used the data pseudonymisation service.
- The _Participant_ used the data anonymisation service.

## Source page metadata

- **Author:** Annalie te Hofste
- **Published:** 19 December 2025
- **Status on source site:** Proposed
- **Snapshot taken:** 28 April 2026

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/sa02-data-processing-services-used-participant](https://simpl-programme.ec.europa.eu/book-page/sa02-data-processing-services-used-participant)

## Touches

- (auto-inferred — verify) [`../../../data/data-processing/`](../../../data/data-processing/README.md)
