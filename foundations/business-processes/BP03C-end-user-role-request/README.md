---
id: bp:BP03C
type: business-process
name: BP03C - End-User Role Request
since: r3.0
---

<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP03C — End User Role Request</strong><br/>
</p>
</div>

# BP03C - End-User Role Request

> **See also: [Dynamic view](./dynamic-view.md)** — sequence diagram
> showing how this business process executes at runtime, with links
> to each participating solution.

## Overview

This Business Process (BP) covers the procedure for requesting roles by End-Users of Simpl-Open.  This BP applies in the following situations: When a federated user logs in for the first time without any assigned roles, the only permitted action will be to request one or more roles When a local user identifies the need to request additional roles If a user is created with pre-assigned roles, or if federation is configured to automatically map organisational roles to Simpl roles, the user will be fully operational without the need to request a role through this BP. It includes the following main steps: Request role:  End-User creates and submits the role request to the Participant's Tier 1 User and Roles Manager Review role request:  Participant's Tier 1 User and Roles Manager reviews the submitted role request

## Actors

The actor involved in this business process is referred to as the Participant, and can correspond to an  End-User  or  Representative  of the: Consumer Provider Governance Authority

## Assumptions

The following assumptions are made: The  Participant  has installed the Simpl-Open agent, and default users and roles are available for usage.

## Prerequisites

The following prerequisites must be fulfilled: Governance Authority Agent configured and ready for operations:  The  Governance Authority  has defined the onboarding procedure and identity attributes relevant for the data space (Business Process 2). Participant's User and Roles configured:  The  Participant's Agent  has been configured, Participant's Agent User and Roles module is configured, and Tier 1 users can start logging in to perform operations within the Agent (Business Process 3B)

![BP03C figure 1](./media/BP03C-figure-1.png)
*BP03C figure 1*

![BP03C figure 2](./media/BP03C-figure-2.png)
*BP03C figure 2*

## Sub-processes

- [3C.1 - Access Control - End-Users Role Request](./3C1-access-control-end-users-role-request.md)

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp03c-end-user-role-request](https://simpl-programme.ec.europa.eu/book-page/bp03c-end-user-role-request)

## Touches

- (auto-inferred — verify) [`../../../governance/`](../../../governance/README.md)
