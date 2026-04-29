<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../README.md">🏠 Home</a><br/>
    <a href="../README.md">Dimension: Administration</a><br/>
        <strong>Capability: Observability</strong><br/>
</p>
</div>

# Observability

Provides visibility into the health, performance, and behaviour of all Simpl-Open application components on a node. Covers logging, dashboarding, QoS metrics and alerts, performance monitoring, application tracing, health checking, and reporting.

## Business services

- [Dashboarding](dashboarding/README.md) — primary placement for the Monitoring Service, which cross-cuts multiple observability business services.
- [Logging](logging/README.md) — centralised log collection and search. _(Realised by ELK stack + Filebeat.)_
- [Performance monitoring](performance-monitoring/README.md) — runtime metrics, traces, and health signals. _(Realised by Metricbeat + Heartbeat + custom Application Tracing; Prometheus on roadmap.)_
- [QoS metrics and alerts](qos-metrics-and-alerts/README.md) — threshold-based alerting on QoS metrics. _(Realised by Alert Manager.)_
- [Reporting](reporting/README.md) — audit and operational reports synthesised from observability data. _(Realised by a custom Reporting Application.)_

## Cross-cut references

- [business-logging.md](business-logging.md) — business-level logging and monitoring (audit and traceability layer for the Governance Authority and participant audits), extracted from FTA §6.5.6.
