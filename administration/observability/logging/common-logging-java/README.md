<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Libs</a><br/>
            <strong>Common Logging (Java)</strong><br/>
</p>
</div>

# Common Logging (Java)

Structured-logging library used by Java services across Simpl-Open. Emits log lines in the format consumed by the [Monitoring Service](../../../administration/observability/dashboarding/monitoring-service/README.md) (ECK stack), with MDC propagation for correlation/tenant/participant IDs and message-type categorisation (REQUEST, REQUEST_ACK, RESPONSE, RESPONSE_ACK).

A format-compatible Python sibling exists at [`common-logging-python/`](../common-logging-python/README.md).

Provenance: built by Simpl. Source repository: `contract-billing/common_logging`. Owner: Monitoring team. Licence: EUPL 1.2.

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/contract-billing/common_logging>
