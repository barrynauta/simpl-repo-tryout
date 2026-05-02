<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Administration</a><br/>
        <a href="../README.md">Capability: Notification and messaging</a><br/>
            <strong>Service: Messaging</strong><br/>
</p>
</div>

# Messaging

Asynchronous message-broker substrate that the rest of the platform publishes to and consumes from. Underpins the Notification service, the Contract Manager Orchestrator ↔ Backend split, and any other Kafka-coordinated flow.

## Solutions

- [kafka](kafka/README.md) — Helm chart deploying the shared Kafka cluster used pervasively across Simpl-Open.
