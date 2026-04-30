---
id: sa:SA03:dynamic-view
type: dynamic-view
name: SA03 - Credentials actions by the Governance Authority – Dynamic view
of: sa:SA03
since: r3.0
---

# SA03 Dynamic View

## Source

> **See also: [Business process overview](./README.md)** — narrative
> description of this business process, including actors, prerequisites,
> outcomes, and the full hierarchy of sub-processes.

Extracted from functional-and-technical-architecture-specifications.md, section 4.2.2.

---

## Trace

After a participant has been onboarded (BP03A), the Governance Authority is responsible for managing the full lifecycle of that participant's credentials. The Identity Provider component within the Governance Authority handles all subsequent credential actions. The following actions are covered by this scenario architecture.

**Revoke a credential**

The Governance Authority permanently revokes a participant's Tier 2 identity credential. Once revoked, the credential cannot be used or reinstated.

**Suspend a credential**

The Governance Authority temporarily suspends credentials, preventing their use without permanently revoking them.

**Reactivate a credential**

Previously suspended credentials are restored once the underlying issue has been resolved, allowing the participant to resume operating in the data space.

**Renew a credential**

Credentials approaching expiry can be renewed in two ways: (a) manually, where the participant submits a Credential Renewal Request and the Governance Authority processes it; or (b) automatically, where a participant configured for auto-renewal has their credential extended without manual intervention.

**Edit Identity Attributes**

The Governance Authority updates the identity attributes assigned to a participant as required (for example, changing a participant's role in the data space).

![SA03 sequence diagram](./media/SA03-sequence.jpeg)
*Figure: Components involved in credential lifecycle actions by the Governance Authority.*

---

## Participants

- [identity-provider/](../../../security/access-control-and-trust/identity-provider-federation/identity-provider/README.md) — Identity Provider (executes all credential lifecycle actions: revocation, suspension, reactivation, renewal)
- [security-attributes-provider/](../../../security/access-control-and-trust/security-attribute-provider-federation/security-attributes-provider/README.md) — Security Attributes Provider (stores updated identity attributes when edited)
