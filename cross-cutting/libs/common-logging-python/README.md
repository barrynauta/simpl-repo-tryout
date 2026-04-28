<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Libs</a><br/>
            <strong>Common Logging (Python)</strong><br/>
</p>
</div>

# Common Logging (Python)

Python implementation of the [`common-logging-java`](../common-logging-java/README.md) library — same log format and field set so both Java and Python services produce a consistent stream into the [Monitoring Service](../../../administration/observability/dashboarding/monitoring-service/README.md).

## Key features

- Structured log messages with business-operation tracking.
- HTTP request/response logging details.
- Custom fields for extensibility.
- Message-type enumeration: `REQUEST`, `REQUEST_ACK`, `RESPONSE`, `RESPONSE_ACK`.

## Used by

- The Dagster code-locations under [Anonymisation and Pseudonymisation](../../../data/data-processing/anonymisation-and-pseudonymisation/README.md) and [Asset Orchestrator](../../../data/supporting-data-services/data-orchestration/asset-orchestrator/README.md) callers — anywhere Python services need to feed the same Elastic stream as the Java services.

Provenance: built by Simpl. Source repository: `contract-billing/common_logging_python`. Owner: Monitoring team. Licence: EUPL 1.2.

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/contract-billing/common_logging_python>
