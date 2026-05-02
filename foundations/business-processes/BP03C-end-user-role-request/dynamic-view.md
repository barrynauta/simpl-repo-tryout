---
id: bp:BP03C:dynamic-view
type: dynamic-view
name: BP03C - End-User Role Request – Dynamic view
of: bp:BP03C
since: r3.0
---

# BP03C Dynamic View

## Source

> **See also: [Business process overview](./README.md)** — narrative
> description of this business process, including actors, prerequisites,
> outcomes, and the full hierarchy of sub-processes.

Extracted from functional-and-technical-architecture-specifications.md, section 4.2.2.

---

## Trace

End users who have logged in but have not yet been assigned a role cannot operate their agent. This process (Individual User Onboarding) allows end users to request roles directly rather than waiting for an administrator to assign them.

**Step 1 — Role Request Submission**

After logging into the participant agent, the end user creates a role request specifying the desired role or set of roles. Once submitted, the system notifies Simpl-Open administrators that a new request is pending review.

**Step 2 — Role Request Review**

An administrator reviews all pending role requests. They can either approve the request — assigning one or more roles to the requester — or reject it, in which case no roles are assigned. After the decision, the system sends a notification to the end user confirming whether their request was approved or rejected.

![BP03C sequence diagram](./media/BP03C-sequence.png)
*Figure: Sequence of interactions for an end-user role request and administrator review.*

---

## Participants

- [fe-users-roles/](../../../governance/participant-management/user-roles/fe-users-roles/README.md) — Users & Roles (receives role requests; enables administrator review and approval/rejection)
- [notification-service/](../../../administration/notification-and-messaging/notification/notification-service/README.md) — Notification Service (notifies administrator of new request; notifies end user of decision)
