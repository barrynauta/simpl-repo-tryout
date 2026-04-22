Source: functional-and-technical-architecture-specifications.md, sections 4.3.1 (ACV Static — Contract Template Datastore Service), 6.1.2 (TCV Static — Contract Template Datastore Service).

# Contract Template Datastore — architecture

## Business view

The Contract Template Datastore stores contract templates to ensure consistent application of contract terms, which are later accessible to consumers during resource negotiation and access stages.

This is a thin planned component. Its primary consumer is the SD Tooling, which uses contract templates when providers define self-descriptions for their resources (via the Contract Template Editor sub-component).

Capability-map placement: Governance dimension → Contract management capability → Contract establishment business service.

Note from step 2 component inventory: the spec has very little detail on this component; it may be deployable as a sub-component of the Contract Manager. This documentation retains it as a separate solution folder per the step 3 mapping decision.

## Data view

- The Contract Template Datastore contains templates of contracts used as blueprints for resource negotiation.
- Technology: implemented as a File System (§6.1.2 TCV).

## Application view

### Internal decomposition

The Contract Template Datastore is a simple storage component. No further decomposition is described in the architecture spec.

### Key integrations

- [SD Tooling](../../../../resource-management/metadata-description/sd-tooling/doc/architecture.md) — the Contract Template Editor (sub-component of SD Tooling) creates and stores contract templates in the Contract Template Datastore.
- [Contract Manager](../../contract-manager/doc/architecture.md) — retrieves contract templates during contract establishment flows.

## Technical view

- The Contract Template Datastore component is implemented as a File System (§6.1.2 TCV Static).

Deployment: deployed in Participant Agents (provider side). Each provider agent hosts a Contract Template Datastore instance.

## Security view

- Access is restricted to authorised provider users via Tier 1/Tier 2 Gateway.
- Templates contain policy and contract terms; their integrity should be verified before use.

Threat model: Status: not yet documented.

Secrets management: Status: not yet documented.

## Testing

Strategy: Status: not yet documented.

PSO validation status: Status: not yet documented.

Requirements traceability: Status: not yet documented.
