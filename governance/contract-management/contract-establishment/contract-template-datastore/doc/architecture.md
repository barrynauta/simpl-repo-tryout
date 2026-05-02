Source: FTA spec, §4.3.1 (ACV Static — Contract Template Datastore Service), §6.1.2 (TCV Static — Contract Template Datastore Service). PSO mapping spreadsheet: `contract-template-datastore` is **planned** (no dedicated source repo); `contract-template-datastore-temporary` is the **interim** workaround backed by `data1/simpl-files`.

# Contract Template Datastore — architecture

> **Status: planned (target) + interim (live).** The dedicated datastore has no source repo yet. SD Tooling currently reads contract templates from the generic file store `data1/simpl-files`; the PSO mapping explicitly labels this as "Workaround to make the SD Tooling work while waiting for the real contract template datastore." Treat all design content below as pre-implementation.

## Business view

The Contract Template Datastore stores contract templates to ensure consistent application of contract terms, which are later accessible to consumers during resource negotiation and access stages.

This is a thin planned component. Its primary consumer is the SD Tooling, which uses contract templates when providers define self-descriptions for their resources (via the Contract Template Editor sub-component).

Capability-map placement: Governance dimension → Contract management capability → Contract establishment business service.

Note from step 2 component inventory: the spec has very little detail on this component; it may be deployable as a sub-component of the Contract Manager. This documentation retains it as a separate solution folder per the step 3 mapping decision.

## Data view

- The Contract Template Datastore contains templates of contracts used as blueprints for resource negotiation.
- Technology (target): File System (§6.1.2 TCV) — likely a CSI-backed persistent volume in Kubernetes.
- **Interim**: today, contract templates live alongside other generic files in `data1/simpl-files` (a Helm-chart store). When the dedicated datastore lands, the templates will move; the SD Tooling integration point is the `Contract Template Editor`, which currently reads/writes through the same path.

## Application view

### Internal decomposition

The Contract Template Datastore is a simple storage component. No further decomposition is described in the architecture spec.

### Key integrations

- [SD Tooling](../../../../../data/semantics-and-vocabulary/schema-management/sd-tooling-api/README.md) — the Contract Template Editor (sub-component of SD Tooling) creates and stores contract templates in the Contract Template Datastore.
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
