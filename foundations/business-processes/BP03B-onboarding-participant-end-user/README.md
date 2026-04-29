<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Foundations</a><br/>
        <a href="../README.md">Business Processes</a><br/>
            <strong>BP03B — Onboarding of a new data space Participant End-User</strong><br/>
</p>
</div>

# BP03B – Onboarding of a new data space – Participant End-User

> **See also: [Dynamic view](./dynamic-view.md)** — sequence diagram showing how
> this business process executes at runtime, with links to each participating
> solution.

## Overview

This business process covers configuration of the User and Roles module of
Simpl-Open. It includes the following main steps:

- **Configure roles** that should be available in the Participant's Simpl-Open Agent.
- **Configure Identity Provider Federation** between external Identity Providers (e.g. the organisation's private IdP or a third-party IdP like eIDAS or EU Login) and the Simpl-Open Identity Provider, if needed.
- **Manage end users** available in the Participant's Simpl-Open Agent.

## Actors

The actor involved in this business process is referred to as the _Participant_,
and can correspond to an End-User or Representative of the:

- _Consumer_
- _Provider_
- _Governance Authority_

## Assumptions

- The _Participant_ has installed the Simpl-Open agent, and default users and roles are available for usage.

## Prerequisites

- **Governance Authority configured and ready for operations** — the _Governance Authority_ has defined the onboarding procedure and identity attributes relevant for the data space (BP02).
- **Participant onboarded** — the _Participant_ onboarding has been completed and the _Participant_ is fully onboarded (BP03A).

![BP03B figure 1](./media/BP03B-figure-1.png)
*BP03B figure 1 — high-level diagram*

![BP03B figure 2](./media/BP03B-figure-2.png)
*BP03B figure 2 — detailed-level diagram*

## Process steps

### Trigger — Participant configuration

The _Participant_ initiates the configuration of the agent.

### BP03B.01 Configure roles

The _Participant_'s Tier 1 User Roles Manager configures the roles to be used by
the participant agent. As part of the process, they map all the relevant Identity
Attributes assigned to the participant by the _Governance Authority_ to their
respective user roles. Features include role creation, role update, and role
cancellation.

### BP03B.02 Configure identity provider federation

The _Participant_'s Tier 1 User Roles Manager configures the federation between
an external Identity Provider and the Simpl-Open Identity Provider. This step is
optional and only configured if the organisation chooses to use external IdPs.

### BP03B.03 Manage end user

The _Participant_'s Tier 1 User Roles Manager manages the users of the
_Participant_'s Simpl-Open Agent. Features include user account creation, update,
cancellation, and inactivation.

## High-level requirements

| ID | Title | Local copy |
|----|-------|------------|
| 3B.1 | Access control — end users to agent (Simpl shall support Role-based Access Control). | [3b1-…](./3b1-access-control-end-users-agent.md) |
| 3B.2 | Access control — roles management (Simpl shall support the management of end users). | [3b2-…](./3b2-access-control-roles-management.md) |
| 3B.3 | Manage users and permissions (Simpl shall provide support to the new participant for the registration). | [3b3-…](./3b3-manage-users-and-permissions.md) |
| 3B.4 | Federated authentication (Simpl shall support authentication systems coming from trusted service providers). | [3b4-…](./3b4-federated-authentication.md) |

Detail pages for HLRs on the public site (note: source-site swaps 3B.1 ↔ 3B.2 slugs):

- 3B.1 → [https://simpl-programme.ec.europa.eu/book-page/3b2-access-control-end-users-agent](https://simpl-programme.ec.europa.eu/book-page/3b2-access-control-end-users-agent)
- 3B.2 → [https://simpl-programme.ec.europa.eu/book-page/3b1-access-control-roles-management](https://simpl-programme.ec.europa.eu/book-page/3b1-access-control-roles-management)
- 3B.3 → [https://simpl-programme.ec.europa.eu/book-page/3b3-onboarding-new-data-space-participant-participant-actions](https://simpl-programme.ec.europa.eu/book-page/3b3-onboarding-new-data-space-participant-participant-actions)
- 3B.4 → [https://simpl-programme.ec.europa.eu/book-page/3b4-federated-authentication](https://simpl-programme.ec.europa.eu/book-page/3b4-federated-authentication)

## Outcomes

- **Participant's User and Roles configured** — the _Participant_'s Agent User and Roles module is configured, and Tier 1 users can start logging in.

## Source page metadata

- **Author:** Rick Marinus Johannes Santbergen
- **Published:** 15 December 2025
- **Status on source site:** Proposed
- **Snapshot taken:** 28 April 2026

## Canonical source

[https://simpl-programme.ec.europa.eu/book-page/bp03b-onboarding-new-data-space-participant-end-user](https://simpl-programme.ec.europa.eu/book-page/bp03b-onboarding-new-data-space-participant-end-user)

## Touches

- (auto-inferred — verify) [`../../../governance/`](../../../governance/README.md)
