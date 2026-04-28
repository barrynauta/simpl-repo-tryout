<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a> &nbsp;»&nbsp;
<a href="../README.md">sd-tooling</a> &nbsp;»&nbsp;
<strong>API specifications</strong>
</p>
</div>

# API specifications — sd-tooling

Specifications imported verbatim from the source repository. Last imported: 2026-04-28.

| File | Kind | Title | Version | Size |
|------|------|-------|---------|------|
| [`openapi-sdtooling-tier1-v1.yaml`](openapi-sdtooling-tier1-v1.yaml) | openapi | SD Tooling API | `1.0` | 64 KB |
| [`openapi-sdtooling-tier1-v2.yaml`](openapi-sdtooling-tier1-v2.yaml) | openapi | SD Tooling API | `1.0` | 23 KB |
| [`openapi-sdtooling-tier1-v3.yaml`](openapi-sdtooling-tier1-v3.yaml) | openapi | SD Tooling API | `1.0` | 8 KB |

## How to view these specs

- **OpenAPI**: paste the YAML into [editor.swagger.io](https://editor.swagger.io/) for an interactive view.
- **AsyncAPI**: paste into [studio.asyncapi.com](https://studio.asyncapi.com/) for diagram + message browser.
- **Locally with Redoc**: `npx redoc-cli serve <file>.yaml`.

## Notes

- These are imported from the implementation repos under `code.europa.eu/simpl/simpl-open/development/...`. The source-of-truth path is recorded in the parent solution's `README.md` under "Source code".
- Tier 1 vs Tier 2 spec variants reflect the IAA two-tier architecture: Tier 1 specs cover human/end-user APIs reached through the Tier 1 gateway; Tier 2 specs cover agent-to-agent APIs reached through the Tier 2 gateway under mTLS.
- AsyncAPI specs describe Kafka topic schemas (publishers / subscribers / message payloads) used by event-driven flows.
