---
id: simpl:notification-service
type: solution
name: Notification Service
owner:
  team: team:contract-billing
dimension: dim:administration
capability: cap:notification-and-messaging
business-service: svc:notification
status: built
release: r3.0
since: r3.0
deprecated-in: null
replaced-by: null
aliases: []
participates-in:
  - bp:BP03C
realises:
  - cap:notification-and-messaging
covers-nfrs: []
provenance:
  source: built
  upstream: null
  repos:
    - code.europa.eu/simpl/simpl-open/development/contract-billing/notification-service
  licence: EUPL-1.2
---

<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../../README.md">🏠 Home</a><br/>
    <a href="../../../README.md">Dimension: Administration</a><br/>
        <a href="../../README.md">Capability: Notification And Messaging</a><br/>
            <a href="../README.md">Service: Notification</a><br/>
                <strong>Solution: Notification Service</strong><br/>
</p>
</div>

# Notification Service

Sends notifications (email and other channels) to data space participants in response to significant events in the Simpl-Open platform, such as new schema publications or contract events. Implements an asynchronous Kafka-based API using AsyncAPI v3.0.0; other services publish EmailNotification messages to the `notifications` Kafka topic, which this service consumes and delivers.

Capability-map placement: `administration / notification-and-messaging / notification / notification-service`. This solution implements the **Notification** business service.

Provenance: built by Simpl. Source repository: `contract-billing/notification-service`. Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [doc/api.md](doc/api.md) — Notification Service API overview.
- [LICENSE](LICENSE) — EUPL 1.2.

## Participates in

- [BP03C End User Role Request](../../../../foundations/business-processes/BP03C-end-user-role-request/dynamic-view.md)

## Source code

- `code.europa.eu/simpl/simpl-open/development/contract-billing/notification-service`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
