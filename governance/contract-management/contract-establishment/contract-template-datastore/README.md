<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Governance</a><br/>
        <a href="../../README.md">Capability: Contract Management</a><br/>
            <a href="../README.md">Service: Contract Establishment</a><br/>
                <strong>Solution: Contract Template Datastore</strong><br/>
</p>
</div>

# Contract Template Datastore

Stores contract templates to ensure consistent application of contract terms. Templates are accessible to consumers during resource negotiation and access stages.

Capability-map placement: `governance / contract-management / contract-establishment / contract-template-datastore`. This solution implements the **Contract establishment** business service (alongside the Contract Manager).

Provenance: planned — no dedicated source repository yet. **Interim implementation:** the SD Tooling currently reads templates from `data1/simpl-files`, a generic-file store re-used as a placeholder. The PSO mapping spreadsheet labels this app-service as `contract-template-datastore-temporary` and notes it as "Workaround to make the SD Tooling work while waiting for the real contract template datastore." Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [LICENSE](LICENSE) — EUPL 1.2.


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `installation-guide/` (1 file), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source code

- **Target (planned)**: dedicated repository — not yet existing.
- **Interim**: <https://code.europa.eu/simpl/simpl-open/development/data1/simpl-files> — generic file storage hosting contract templates until the dedicated datastore lands.

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here — see `references.md` once step 7 populates it.
