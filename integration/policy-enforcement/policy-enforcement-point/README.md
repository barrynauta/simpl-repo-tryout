<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Integration</a><br/>
        <a href="../README.md">Capability: Policy enforcement</a><br/>
            <strong>Service: Policy enforcement point</strong><br/>
</p>
</div>

# Policy enforcement point

Runtime enforcement of access and usage policies during data-space interactions. Today the only realised solution is the Policy Engine embedded inside the Eclipse Dataspace Connector; it evaluates ODRL policies attached to contracts during contract negotiation and transfer. Future work may add a standalone PEP separate from the connector.

## Solutions


## Source

Cross-cuts FTA §6.4.3 (Policies) and §4.3.1 (ACV Static — Connector). See [governance/policy-management/policy-administration-point/detailed-spec.md](../../../governance/policy-management/policy-administration-point/detailed-spec.md) for the policy-expression model administered by the PAP and enforced by this PEP.
