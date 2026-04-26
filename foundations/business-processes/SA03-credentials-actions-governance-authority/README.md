<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>SA03 — Credentials Actions Governance Authority</strong><br/>
</p>
</div>

# SA03 - Credentials actions by the Governance Authority

> **See also: [Dynamic view](./dynamic-view.md)** — sequence diagram
> showing how this business process executes at runtime, with links
> to each participating solution.

## Overview

The  Governance Authority  is responsible for managing  Participant  credentials within the data space. One of their operational tasks is to manage the credential lifecycle, ensuring that access rights remain aligned with regulatory and operational requirements (defined in Business Process 1 - Define the data space governance ) . To enable the tracing of the actions of the  Governance Authority  representative performing them, the concept of "mandates" is introduced: these serve as the official approval that a specific credentials action can be taken by a  Governance Authority  representative who has the specific role required for performing this action. The entire process for obtaining these mandates shall be supported by, for example, the use of a ticketing system, but every  Governance Authority  is free to manage the workflow based on the rules they define internally. Before the execution of any credential action (like revocation or suspension), careful consideration should be given to analysing the potential impact on ongoing agent-to-agent interactions within the data space, which varies depending on how the  Governance Authority  manages these decision workflows (e.g., via ticketing system, paperwork, or other mechanisms). The outcome of these workflows is considered, in the scope of this business process, as an external decision procedure. Once the mandate is defined and received, the possible actions related to credentials are: Revoking The credentials of the selected  Participant  are revoked so that their actions inside the data space are blocked. Once the  Participant  credentials are revoked, the  Participant  can no longer operate within the data space. This means that any data exchange, service consumption, or any other interaction requiring authentication within the data space will be blocked. The  Participant  will remain in this non-operational state until the credentials are re-activated, or renewed if they would expire in the meantime. Suspending The credentials of the selected  Participant  are on hold so that their actions requiring authentication are temporarily blocked. Once the  Participant  credentials are suspended, the  Participant  can temporarily not operate within the data space. The  Participant  will remain in this non-operational state until the credentials are re-activated, or renewed if they would expired in the meantime. Re-activating Suspended credentials of the selected  Participant  are restored to full functionality, allowing the  Participant  to operate in the data space with the same access rights and capabilities they had prior to the suspension. Once the  Participant  credentials are re-activated, the  Participant  can start to operate within the data space, functioning like before the suspension of the credentials. Renewing The credentials of the selected  Participant  are issued by the  Governance Authority  so that a  Participant  representative can take and upload them into the  Participant  agent. Once the  Governance Authority  renews a  Participant's  credentials, the  Participant  whose credentials are renewed can manually upload the new credentials into their agent. If the  Governance Authority  configures an automatic renewal process for a  Participant , the upload process is performed automatically by the  Participant's  agent. Editing a Participant's identity attributes assignment The identity attributes assigned to a  Participant  are updated to reflect changes in their permissions or status within the data space. Once the  Governance Authority  updates a  Participant's  identity attributes, the new assignment takes effect, influencing the  Participant's  access rights and interactions within the data space.

## Actors

The actors involved in this process are: Governance Authority  representatives with the role required to manage the credentials. Participant  representative with the role to administer agent-to-agent communication configurations.

## Assumptions

The following assumptions are made: The  Governance Authority  has defined the rules describing how the mandates trigger the process actions. The  Governance Authority  has defined the role that enables performing credential actions, and the role is assigned to a  Governance Authority  representative. The role of accessing  Participant  management functionalities is assigned to a  Governance Authority  representative. The  Participant  whose credentials are the target of an action has been onboarded and, depending on the mandate, meets one of the following conditions: Holds valid credentials, allowing for credential suspension. Holds credentials that are valid, suspended, or revoked, allowing for credential renewal. Holds suspended credentials, allowing for credential re-activation. Holds credentials that are not yet revoked, allowing for credential revocation. There is a formal mandate (the result of a decision-making process managed and defined by the  Governance Authority  outside of this process) to proceed with a particular action: a mandate to revoke a  Participant's  credentials will enable the revocation subprocess (SA03.01). a mandate to suspend a  Participant's  credentials will enable the suspension subprocess (SA03.02). a mandate to re-activate a  Participant's  credentials will enable the re-activation subprocess (SA03.03). a mandate to edit a  Participant's  assigned identity attributes will enable the edit of identity attributes subprocess (SA03.04). a mandate to renew a  Participant's  credentials will enable the credentials renewal subprocess (SA03.05).

## Prerequisites

The following prerequisites must be fulfilled: Data space is configured:  The Simpl-Open agent is installed and the Governance Authority is ready for operations (Business Process 2). The communication security settings are configured and the Governance Authority ID/Trust is configured (e.g. ensuring tier2 communication security and identity management between  Participants ) (BP02.01 - Configure ID/Trust security solution). Provider onboarded:  One ore more  Providers  must be successfully onboarded (Business Processes 3A).

## Details

The following shows the detailed business process diagram and gives the step descriptions.

Trigger Credential operation   change

The  Governance Authority  representative initiates the specific action for which a mandate was received.

SA03.01 Revoke the credential of a Participant

The  Governance Authority  representative identifies the  Participant  whose credentials must be revoked and then revokes them so that their future actions using these credentials inside the data space are permanently blocked.

SA03.02 Suspend the credential of a Participant

The  Governance Authority  representative identifies the  Participant  whose credentials must be suspended and then suspends them so that their future actions inside the data space are temporarily blocked.

SA03.03 Re-activate the credential of a Participant

The  Governance Authority  representative identifies the  Participant  whose credentials must be re-activated and then re-activate them so that their future actions inside the data space are restored as they were before the suspension.

SA03.04 Edit assigned identity attributes of a Participant

The  Governance Authority  representative identifies the  Participant  whose identity attributes have to be edited and then edit them so that the new assignment will take effect.

SA03.05 Renew the credential of a Participant

The  Governance Authority  representative identifies the  Participant  whose credentials must be renewed and then issues new credentials for the  Participant  and makes it available to the  Participant  to be installed.

SA03.06 Upload a new credential

The  Participant  whose credentials are renewed uploads the issued credentials so that their future actions that require authentication inside the data space continue.

Outcomes

## Sub-processes

- [3.1 - Participant management](./31-participant-management.md)

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/sa03-credentials-actions-governance-authority](https://simpl-programme.ec.europa.eu/book-page/sa03-credentials-actions-governance-authority)

## Touches

- (auto-inferred — verify) [`../../../governance/`](../../../governance/README.md)
