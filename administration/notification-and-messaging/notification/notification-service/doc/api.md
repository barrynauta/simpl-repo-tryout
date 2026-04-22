# Notification Service — API

The Notification Service implements an AsyncAPI v3.0.0 contract for its Kafka-based interface.

**Channel**: `notifications` (Kafka topic)

**Operation**: `SendNotification` — any Simpl-Open service publishes an `EmailNotification` message to this channel.

**Message schema** (`EmailNotification`):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `channel` | string (enum: `email`) | Yes | Notification channel type |
| `message` | string | Yes | Body of the message |
| `to` | string | Yes | Recipient email address |
| `cc` | array of string | No | CC email addresses |
| `subject` | string | Yes | Message subject |

Full AsyncAPI specification: `notification-service/docs/asyncApi/asyncapi.yaml` in the source repository.
