<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Data Processing</a><br/>
            <a href="../README.md">Service: Anonymisation and Pseudonymisation</a><br/>
                <strong>Solution: Field-Level Pseudo-Anonymisation</strong><br/>
</p>
</div>

# Field-Level Pseudo-Anonymisation

Privacy-preserving transformations applied at the field (column) or PII-entity level. Supports **column-wise pseudonymisation** of structured data (CSV files / pandas DataFrames) and **PII detection and pseudonymisation** of unstructured text. Pseudonymisation is reversible — paired depseudonymisation jobs recover original values when the protected key material is available.

Capability-map placement: `data / data-processing / anonymisation-and-pseudonymisation / field-level-pseudo-anonymisation`. This solution implements the **Anonymisation and pseudonymisation** business service (pseudonymisation half).

Provenance: built by Simpl. Packaged as a Dagster code-location and deployed into the main Dagster environment; participates in the Data Orchestration runtime as an optional module on Provider and Consumer Agents. Source repository: `code.europa.eu/simpl/simpl-open/development/data-services/field-level-pseudo-anonymisation`. Licence: EUPL 1.2.

## Key features

- **Structured data**: column-wise pseudonymisation on pandas DataFrames with CSV in/out support.
- **Unstructured data**: PII detection and pseudonymisation using Scrubadub and spaCy across 18+ languages.
- **Multiple techniques**: hash, encrypt, redact, replace, and retain transformations.
- **Reversible operations**: depseudonymisation jobs recover encrypted data when keys are available.
- **HashiCorp Vault integration**: secure key management for reversible (encryption-based) transformations.
- **Dagster orchestration**: dual-output ops emitting both transformed data and run metrics, with comprehensive metadata for auditing.

## Participates in

- [SA02 Data processing services used by a Participant](../../../../foundations/business-processes/SA02-data-processing-services/README.md) — sub-process *2.1 Participant pseudonymises a dataset*.


## Documentation (imported from source)

[`documents/`](documents/) — user-facing documentation imported verbatim from the source repository: `deployment-guide/` (1 file), `installation-guide/` (1 file), `upgrade-guide/` (1 file), `user-manual/` (1 file).

## Source code

- Simpl repo: <https://code.europa.eu/simpl/simpl-open/development/data-services/field-level-pseudo-anonymisation>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
