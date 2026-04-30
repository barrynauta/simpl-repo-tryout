<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Dimension: Integration</a><br/>
        <strong>Capability: Data sharing</strong><br/>
</p>
</div>

# Data sharing

Allows participants to exchange data with others through interoperable interfaces.

> **Implementation note.** Today, **all** data transfers run through the [Connector](../resource-sharing/resource-sharing-runtime/connector/README.md)'s Data Plane — there are no separate solution folders under this capability yet. The capability-map split into bulk / streaming / simple is forward-looking architecture; in current Simpl-Open the Connector's six Simpl extensions cover the implemented part. Per MAPPING.md the planned target solutions live at `bulk-data-transfer/{edc-s3-extension,minio}/` and `simple-data-transfer/edelivery/`, but no folders have been created since their source repos are stubs (`gaia-x-edc/edc-minio-s3`, `gaia-x-edc/edelivery`) and MinIO has no Simpl-side fork.

## Business services

- **Bulk data transfer** — moves large datasets reliably with checkpointing, integrity checks, and resume support.
  - **Implemented today** inside the [Connector](../resource-sharing/resource-sharing-runtime/connector/README.md) via its **MinIO S3 Object Storage Extension** (the connector's primary data-plane sink). MinIO itself is consumed as upstream OSS — no Simpl fork. PSO mapping target paths: `bulk-data-transfer/edc-s3-extension/` and `bulk-data-transfer/minio/` *(folders not yet created — placeholder source repos)*.
- **Simple data transfer** — provides lightweight pull or push exchanges for small files and APIs.
  - **Roadmap item** (FTA §6.3.1 Technology Roadmap). Designated implementation: **eDelivery**. The hook exists in the Connector source today (one of its six Simpl extensions: *"triggers eDelivery transfer"*); the eDelivery service itself (`gaia-x-edc/edelivery`) is a stub repo. PSO mapping target path: `simple-data-transfer/edelivery/` *(folder not yet created — source is a stub)*.
- [Data streaming](data-streaming/README.md) — publishes and subscribes to real-time event flows with ordering, retention, and replay.
  - **Not yet implemented.** No designated solution in the FTA spec or PSO mapping; pending future architecture work.
