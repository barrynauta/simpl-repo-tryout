# Notification Service

Sends notifications (email and other channels) to data space participants in response to significant events in the Simpl-Open platform, such as new schema publications or contract events. Implements an asynchronous Kafka-based API using AsyncAPI v3.0.0; other services publish EmailNotification messages to the `notifications` Kafka topic, which this service consumes and delivers.

Capability-map placement: `administration / notification-and-messaging / notification / notification-service`. This solution implements the **Notification** business service.

Provenance: built by Simpl. Source repository: `contract-billing/notification-service`. Licence: EUPL 1.2.

## Contents

- [doc/architecture.md](doc/architecture.md) — six-view architecture document.
- [doc/api.md](doc/api.md) — Notification Service API overview.
- [LICENSE](LICENSE) — EUPL 1.2.

## Source code

- `code.europa.eu/simpl/simpl-open/development/contract-billing/notification-service`

## Roadmap

Roadmap items live in the Simpl Notion "Roadmap items overview" page. Not duplicated here.
