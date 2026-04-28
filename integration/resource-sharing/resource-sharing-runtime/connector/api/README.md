<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../../README.md">🏠 Home</a> &nbsp;»&nbsp;
<a href="../README.md">connector</a> &nbsp;»&nbsp;
<strong>API specifications</strong>
</p>
</div>

# API specifications — Connector

The Simpl Connector is a fork of the upstream **Eclipse Dataspace Connector (EDC)**. The API specifications it exposes are inherited from upstream and are not redefined in the Simpl repository.

## Three API surfaces (per upstream EDC)

| API | Purpose | Upstream documentation |
|-----|---------|------------------------|
| Management API | Asset / policy / contract registration; called by upper-layer Simpl components via the [EDC Connector Adapter](../../edc-connector-adapter/api/README.md) | [EDC Management API](https://eclipse-edc.github.io/Connector/openapi/management-api/) |
| Dataspace Protocol (DSP) API | Agent-to-agent contract negotiation per the IDSA DSP specification | [DSP specification](https://docs.internationaldataspaces.org/ids-knowledgebase/v/dataspace-protocol/) |
| Data Plane API | Data transfer execution (Consumer Pull, Provider Push) | [EDC Data Plane](https://eclipse-edc.github.io/Connector/openapi/data-plane-api/) |

For Simpl-specific extensions to these APIs (MinIO S3 Extension, Triggering Extension, eDelivery extension, Contract Management extensions), see the [connector architecture document](../doc/architecture.md).
