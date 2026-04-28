<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Data</a><br/>
        <a href="../README.md">Capability: Data Processing</a><br/>
            <strong>Service: Anonymisation and Pseudonymisation</strong><br/>
</p>
</div>

# Anonymisation and Pseudonymisation

Helps Participants — both Providers and Consumers — protect personal data, business-critical information, confidential datasets, and other sensitive records by applying a range of data-protection techniques. **Pseudonymisation** is reversible (the original data can be recovered from a separately stored key); **anonymisation** is irreversible.

The service is realised as two Dagster code-locations that are integrated as optional modules into the **Data Orchestration** runtime (the Dagster-based orchestration platform) on a Participant Agent. They run as part of the standard data-orchestration flow but conceptually belong to the Data Processing capability — the architecture spec lists "Anonymisation and pseudonymisation" as a service of the Data Processing capability and notes that the anonymisation services are "added to the ACV Static — Data Orchestration Service" deployment view.

## Solutions

- [dataframe-level-anonymisation/](dataframe-level-anonymisation/README.md) — anonymisation (k-anonymity, l-diversity, t-closeness) on pandas DataFrames; irreversible.
- [field-level-pseudo-anonymisation/](field-level-pseudo-anonymisation/README.md) — column-wise pseudonymisation on structured data and PII pseudonymisation on unstructured text; reversible (paired depseudonymisation jobs).

## Realised by

The runtime that hosts these code-locations is the [Orchestration Platform](../../supporting-data-services/data-orchestration/orchestration-platform/README.md) under `supporting-data-services/data-orchestration/`. CI/CD packages each code-location as a container image, the orchestration platform loads them as user code, and the Dagster scheduler executes their jobs and ops as part of broader Provider/Consumer data pipelines.

## Participates in

- [SA02 Data processing services used by a Participant](../../../foundations/business-processes/SA02-data-processing-services/README.md) — Pseudonymisation and anonymisation services for participants. Both sub-processes (*2.1 pseudonymise a dataset*, *2.2 anonymise a dataset*) are realised here.
