<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../../README.md">🏠 Home</a> &nbsp;»&nbsp;
<a href="../README.md">schema-sync-adapter</a> &nbsp;»&nbsp;
<strong>API specifications</strong>
</p>
</div>

# API specifications — schema-sync-adapter

Specifications imported verbatim from the source repository. Last imported: 2026-04-28.

| File | Kind | Title | Version |
|------|------|-------|---------|
| [`openapi-schema-sync-adapter-v1.yaml`](openapi-schema-sync-adapter-v1.yaml) | openapi | Schema Sync Adapter — Tier 1 API | `1` |
| [`openapi-schema-sync-adapter-tier2-v1.yaml`](openapi-schema-sync-adapter-tier2-v1.yaml) | openapi | Schema Sync Adapter — Tier 2 API | `1` |

## How to view these specs

- **OpenAPI**: paste the YAML into [editor.swagger.io](https://editor.swagger.io/) for an interactive view.
- **Locally with Redoc**: `npx redoc-cli serve <file>.yaml`.

## Notes

- Imported from `code.europa.eu/simpl/simpl-open/development/data1/schema-sync-adapter`. The source-of-truth path is recorded in [CANONICAL.md](../CANONICAL.md).
- Tier 1 vs Tier 2 spec variants reflect the IAA two-tier architecture: Tier 1 specs cover human/end-user APIs reached through the Tier 1 gateway; Tier 2 specs cover agent-to-agent APIs reached through the Tier 2 gateway under mTLS.
