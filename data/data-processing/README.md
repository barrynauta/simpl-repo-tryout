<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Dimension: Data</a><br/>
        <strong>Capability: Data processing</strong><br/>
</p>
</div>

# Data processing

Provides the means to transform, aggregate, anonymise, and visualise datasets across multiple sources.

## Business services

- [Anonymisation and pseudonymisation](anonymisation-and-pseudonymisation/README.md) — applies masking, pseudonymisation, and irreversible anonymisation patterns to protect personal and sensitive data. Realised by two Dagster code-locations integrated into the Data Orchestration runtime.
- [Data analytics](data-analytics/README.md) — batch and interactive analytics for descriptive, diagnostic, and predictive insights. _(Roadmap: Apache Spark, Apache Jupyter)_
- [Data visualisation](data-visualisation/README.md) — charts and exploratory views to communicate insights and monitor KPIs.

## Notes

The **Anonymisation and pseudonymisation** service is conceptually a Data Processing service per the functional and technical architecture, but it is physically deployed as Dagster code-locations on top of the [Orchestration Platform](../supporting-data-services/data-orchestration/orchestration-platform/README.md). Cross-references run between this capability and `supporting-data-services/data-orchestration/` accordingly.
