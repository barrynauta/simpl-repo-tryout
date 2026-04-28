<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a> &nbsp;»&nbsp;
<a href="../README.md">tier-2-authentication-provider</a> &nbsp;»&nbsp;
<strong>API specifications</strong>
</p>
</div>

# API specifications — tier-2-authentication-provider

Specifications imported verbatim from the source repository. Last imported: 2026-04-28.

| File | Kind | Title | Version | Size |
|------|------|-------|---------|------|
| [`asyncapi-v1.yaml`](asyncapi-v1.yaml) | asyncapi | Authentication Provider Async API | `1.3.0` | 5 KB |
| [`authenticationprovider-tier1-v2.yaml`](authenticationprovider-tier1-v2.yaml) | openapi | Authentication Provider Tier 1 | `2.0.0` | 92 KB |
| [`authenticationprovider-tier2-v2.yaml`](authenticationprovider-tier2-v2.yaml) | openapi | Authentication Provider Tier 2 | `2.0.0` | 13 KB |
| [`authenticationprovider-v1.yaml`](authenticationprovider-v1.yaml) | openapi | Authentication Provider | `1.5.0` | 59 KB |

## How to view these specs

- **OpenAPI**: paste the YAML into [editor.swagger.io](https://editor.swagger.io/) for an interactive view.
- **AsyncAPI**: paste into [studio.asyncapi.com](https://studio.asyncapi.com/) for diagram + message browser.
- **Locally with Redoc**: `npx redoc-cli serve <file>.yaml`.

## Notes

- These are imported from the implementation repos under `code.europa.eu/simpl/simpl-open/development/...`. The source-of-truth path is recorded in the parent solution's `README.md` under "Source code".
- Tier 1 vs Tier 2 spec variants reflect the IAA two-tier architecture: Tier 1 specs cover human/end-user APIs reached through the Tier 1 gateway; Tier 2 specs cover agent-to-agent APIs reached through the Tier 2 gateway under mTLS.
- AsyncAPI specs describe Kafka topic schemas (publishers / subscribers / message payloads) used by event-driven flows.
