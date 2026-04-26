---
id: svc:notification
type: business-service
name: Notification
dimension: dim:administration
capability: cap:notification-and-messaging
since: r3.0
---

<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Administration</a><br/>
        <a href="../README.md">Capability: Notification And Messaging</a><br/>
            <strong>Service: Notification</strong><br/>
</p>
</div>

# Notification

Delivers notifications (email and other channels) to data space participants. Subscribes to the `notifications` Kafka topic and dispatches messages published by other Simpl-Open services.

## Solutions

- [Notification Service](notification-service/README.md) — AsyncAPI v3.0.0 Kafka consumer that delivers email notifications.
