<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Data</a><br/>
        <a href="../../README.md">Capability: Data Processing</a><br/>
            <a href="../README.md">Service: Anonymisation and Pseudonymisation</a><br/>
                <strong>Solution: Dataframe-Level Anonymisation</strong><br/>
</p>
</div>

# Dataframe-Level Anonymisation

Privacy-preserving transformations applied at the dataset (DataFrame) level. Implements **k-anonymity**, **l-diversity**, and **t-closeness** to ensure that sensitive attributes cannot be used to re-identify individuals within structured tabular data. Anonymisation is irreversible: there is no de-anonymisation counterpart.

Capability-map placement: `data / data-processing / anonymisation-and-pseudonymisation / dataframe-level-anonymisation`. This solution implements the **Anonymisation and pseudonymisation** business service (anonymisation half).

Provenance: built by Simpl. Packaged as a Dagster code-location and deployed into the main Dagster environment via CI/CD; participates in the Data Orchestration runtime as an optional module on Provider and Consumer Agents. Source repository: `code.europa.eu/simpl/simpl-open/development/data-services/dataframe-level-anonymisation`. Licence: EUPL 1.2.

## Key features

- Implements core anonymisation algorithms (k-anonymity, l-diversity, t-closeness) over structured and semi-structured datasets loaded as pandas DataFrames.
- Modular Dagster ops and jobs — reusable and composable inside data-orchestration workflows.
- Integrates with the main Dagster deployment as a code-location delivered through the Simpl-Open CI/CD pipeline.
- Built-in error handling, validation, and logging for traceability and audit of anonymisation jobs.
- Reads from and writes back to the configured object storage bound to the Agent.

## Participates in

- [SA02 Data processing services used by a Participant](../../../../foundations/business-processes/SA02-data-processing-services/README.md) — sub-process *2.2 Participant anonymises a dataset*.

## Source code

- Simpl repo: <https://code.europa.eu/simpl/simpl-open/development/data-services/dataframe-level-anonymisation>

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
