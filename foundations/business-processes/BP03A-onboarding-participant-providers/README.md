# BP03A – Onboarding of a new data space Participant - Providers (data - application - infrastructure) & Consumers

## Overview

This business process covers the onboarding process for a new Applicant . Both Providers and Consumers can apply to a data space and will be referred to as (data space) Applicants from here on.  It includes the following main steps: Prepare & submit onboarding request : The Applicant submits the onboarding requests to the Governance Authority for review. Review onboarding request: The Governance Authority verifies the Applicant ’s onboarding request against a predefined set of criteria and the alignment with the data space objectives. Generate public/private keypair: The Applicant deploys and configures the Simpl-Open agent and uses the agent to generate a public/private key pair to enable encrypted communications and data integrity within the data space. Create & sign security credentials: The Governance Authority creates and signs digital security credentials (e.g., x.509 certificates) that incorporate the Applicant’s public key. These credentials serve as proof of identity and are validated through the issuance of certifications by the Governance Authority . The certifications ensure that the credentials are securely linked to the correct entity. Store & install security credentials: The Applicant  stores and installs the signed identity security credentials in its Simpl-Open Agent.

## Actors

The following actors are involved: Governance Authority Applicant

## Assumptions

The following assumptions are made: Data space Applicants are assumed to be an organisation and not an individual person. The person/people acting on behalf of the Applicant , applying to the data space are assumed to be a member of the Applicant organisation's directory. Data space specifications: The document(s) describing the data space’s objectives, candidature criteria and requirements applicable to an organisation for onboarding are developed and available to a potential A pplicant (e.g., website publication).

## Prerequisites

The following prerequisites must be fulfilled: Data space is configured:   The   Governance Authority   has defined the onboarding procedure and identity attributes relevant for the data space (Business Process 2).

![BP03A figure 1](./media/BP03A-figure-1.png)
*BP03A figure 1*

![BP03A figure 2](./media/BP03A-figure-2.png)
*BP03A figure 2*

## Details

### Trigger onboarding of a new data space Participant

The  Participant initiates the preparation and submission of the onboarding request.

### BP03A.01 Prepare & submit onboarding request

The Applicant prepares a comprehensive application to participate to the data space, by gathering the required information based on the documentation made available by the Governance Authority (see prerequisite  1). After the preparation of the onboarding request, the  Applicant   fills in the forms and provides any other documents that may be mandatory (following the rules that are defined by the Governance Authority ) to the Governance Authority  for review.

### BP03A.02 Review onboarding request

After receiving the onboarding request, the Governance Authority starts the review process. It verifies the Applicant ’s onboarding request against a predefined set of criteria and the alignment with the data space objectives (see prerequisite 1). T he review process of the onboarding request can be either manually or automatically done by the Governance Authority . As an outcome of this step: The Governance Authority can approve the onboarding request. If the request is approved, the process continues to the identification of identity attributes in  step BP03A.03 . The Governance Authority reject the onboarding request. If the request is rejected, the process notifies the Applicant  about the rejection in step BP03A.11 . In case deficiencies are found, the Applicant  shall also have the possibility to address them and start over the process from  Step BP3A.01 .

### BP03A.03 Identify identity attributes

As part of the approval process the Governance Authority  identifies the relevant identity attributes of the Applicant  that will be used for authentication of the  Applicant .

### BP03A.04 Agent deployment

If the application is approved, the Applicant   downloads the minimal set of modules from Simpl-Open that are required to have an operative Simpl - Open . The Applicant  then deploys and configures the Simpl-Open modules on the Applicant 's infrastructure to establish the necessary environment for participating within the data space.

### BP03A.05 Generate public/private keypair

The Applicant 's agent generates a public/private key pair to enable encrypted communications and data integrity within the data space. The private key is securely stored in the Simpl-Open agent. The Applicant  shares the public key with the Governance Authority to request signed security credentials.

### BP03A.06 Create & sign security credentials

The Governance Authority creates and signs digital security credentials ( e.g., x.509 certificates) that incorporate the Applicant’s public key. These credentials serve as proof of identity and are validated through the issuance of certifications by the Governance Authority . The certifications ensure that the credentials are securely linked to the correct entity.

### BP03A.07 Provide the security credentials

The Governance Authority provides the signed security credentials to the Applicant . The security credentials are essential to ensure secure operations within the data space.

### BP03A.08 Store & install security credentials

The Applicant  stores and installs the signed identity security credentials in its Simpl-Open Agent.

### BP03A.09 Notification of successful onboarding

The  Applicant is notified that they are now fully onboarded to the data space and from now on are a  Participant.

### BP03A.10 Notify onboarding request rejected

The  Applicant is notified that their onboarding request has been rejected.

## Sub-processes

- [3A.1 - Onboarding of a new data space participant - registration of onboarding request](./3A1-onboarding-new-data-space-participant-registration-onboarding-request.md)
- [3A.2 - Onboarding of a new data space participant - review of the onboarding request](./3A2-onboarding-new-data-space-participant-review-onboarding-request.md)
- [3A.3 - Onboarding of a new data space participant - attribute placement during onboarding](./3A3-onboarding-new-data-space-participant-attribute-placement-during-onboarding.md)
- [3A.4 - Onboarding of a new data space participant - finalizing onboarding](./3A4-onboarding-new-data-space-participant-finalizing-onboarding.md)

## Outcomes

Participant onboarded:  The Participant onboarding has been completed and the Participant is fully onboarded. Participant onboarding rejected:  The Participant onboarding has been rejected and cannot join the data space.## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/3a-onboarding-new-dataspace-participant-providers-data-application-infrastructure](https://simpl-programme.ec.europa.eu/book-page/3a-onboarding-new-dataspace-participant-providers-data-application-infrastructure)

## Touches

- (auto-inferred — verify) [`../../../governance/`](../../../governance/README.md)
