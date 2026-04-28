<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a> &nbsp;»&nbsp;
<a href="../README.md">signer-service</a> &nbsp;»&nbsp;
<strong>API specifications</strong>
</p>
</div>

# API specifications — signer-service

Specifications imported verbatim from the source repository, with rendered HTML viewers (ReDoc for OpenAPI, AsyncAPI Standalone for AsyncAPI). Last imported and rendered: **2026-04-28**.

| File | Rendered | Kind | Title | Version | Size |
|------|----------|------|-------|---------|------|
| [`openapi3-v1.yaml`](openapi3-v1.yaml) | [📖 view](openapi3-v1.html) | openapi | Signing service | `1.1` | 15 KB |

## Viewing the rendered docs

The HTML viewers fetch the YAML at runtime, which browsers block under `file://`. Serve the catalogue over HTTP — from the repo root:

```
python3 -m http.server 8000
```

Then open the rendered HTML file under `http://localhost:8000/...`. When the catalogue is published (e.g. GitLab Pages), the rendered HTML works without any local server.

## Notes

- These specs are imported from the implementation repos under `code.europa.eu/simpl/simpl-open/development/...`. The source-of-truth path is recorded in the parent solution's `README.md` under "Source code".
- Tier 1 vs Tier 2 spec variants reflect the IAA two-tier architecture: Tier 1 specs cover human/end-user APIs reached through the Tier 1 gateway; Tier 2 specs cover agent-to-agent APIs reached through the Tier 2 gateway under mTLS.
- AsyncAPI specs describe Kafka topic schemas (publishers / subscribers / message payloads) used by event-driven flows.

## Bird's-eye view

For an index over **every** API spec across the whole catalogue, organised by dimension, by kind, and by tier, see [foundations/api-catalogue.md](../../../../foundations/api-catalogue.md).
