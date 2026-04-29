<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Governance</a><br/>
        <a href="../README.md">Capability: Policy Management</a><br/>
            <a href="README.md">Service: Policy Administration Point</a><br/>
                <strong>Detailed technical specification</strong><br/>
</p>
</div>

# Detailed technical specification — Policies

This page reproduces the Policies section of the functional and technical architecture specification (FTA §6.4.3). It is the canonical reference for the ODRL-based policy expression model, the policy templates and parameters that providers and the Governance Authority configure, and the contract-time and runtime enforcement points (the EDC policy engine and the Tier 2 ABAC gateway). Companion content lives under [integration/policy-enforcement](../../../../integration/policy-enforcement/README.md) for the runtime enforcement-point side.

The components that implement this specification — [Policy Creator, Policy Template Datastore, ODRL Policy Language](README.md) — sit under this service folder.

## Source

This content is extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **6.4.3 Policies** (lines 13557–14238 of the source document, dated 2026-04-20).

Upstream link: [Functional and Technical Architecture Specifications](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#643-policies).

---

####  6.4.3. <a name='Policies'></a>Policies

For this context, both access and usage policies for resources (Data,
Application, or Infrastructure) are defined.

The below definition of the Data Space Support Center is followed:

-   *Access Rules/Policy: define whether access to a resource is allowed
    or not.*

-   *Usage Rules/Policy: define how a resource might or may not be
    used.*

*Access control policies control the authorisation to access specific
data while the data rights owner retains direct control over the data.
Usage policies, including consent, regulate the permissible actions and
behaviours related to the utilisation of the accessed data, which means
keeping control of data even after the items have left the trust
boundaries of the data owner.* Policies can only be enforced when
technically feasible, otherwise only legal enforcement is possible

<https://dssc.eu/space/BVE/357075567/Access+%26+Usage+Policies+Enforcement#Data-Space-Registry>

Following this definition the access policies are checked before the
provider gives (at least partial) control over to the consumer. The
usage policies describe the behaviour after the consumer has access to
the resource (Data, Application or Infrastructure).

**<span class="underline">Policy Language</span>**

A formal and machine-readable way to express and enforce the policies is
needed. Open Digital Rights Language (ODRL) is intended to be used to
write both access and usage policies.
<https://www.w3.org/TR/odrl-model/>

The key components of ODRL are:

Here are the key components of an ODRL usage policy:

1.  **Asset**: The digital content or service to which the policy
    applies;

2.  **Permissions**: Actions that are allowed with respect to the asset
    (e.g., read, download);

3.  **Prohibitions**: Actions that are explicitly forbidden;

4.  **Constraints**: Conditions or limitations that must be met for the
    permissions to apply (e.g., time restrictions);

5.  **Duties**: Obligations that must be fulfilled by the user in order
    to exercise a permission (e.g., attribution, payment).

Different ways exist to serialise the ODRL expressions, and JSON-LD is
intended to be used for this part.

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "http://example.com/policy/123",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"permission": \[

{

"target": "http://example.com/asset/image123",

"action": "http://www.w3.org/ns/odrl/2/distribute",

"constraint": \[

{

"leftOperand": "http://www.w3.org/ns/odrl/2/purpose",

"operator": "http://www.w3.org/ns/odrl/2/eq",

"rightOperand": "http://www.example.com/vocab\#nonCommercial"

},

{

"leftOperand": "http://www.w3.org/ns/odrl/2/payAmount",

"operator": "http://www.w3.org/ns/odrl/2/eq",

"rightOperand": "0"

}

\],

"duty": \[

{

"action": "http://www.w3.org/ns/odrl/2/attribution"

}

\]

}

\],

"prohibition": \[

{

"target": "http://example.com/asset/image123",

"action": "http://www.w3.org/ns/odrl/2/modify"

}

\]

}

**<span class="underline">Access Policy</span>**

Here is an example of an access policy for a dataset provided by a data
provider. The policy will specify who can access the data, under which
conditions, and for how long.

Scenario:

-   The dataset contains research data that can be accessed by different
    roles:

    -   Researchers: Full access to the data for analysis;

    -   Students: Limited access to anonymised data for study purposes;

    -   External partners: Access to aggregated data for collaboration
        purposes.

-   The access is granted for a specific period;

-   The access is granted only for the geographic location of the EU.

Different datasets for the full data, anonymised data and aggregated
data are used.

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "http://example.com/policy/123",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"target": "http://example.com/dataset/research123",

"assigner": {

"uid": "http://example.com/provider/dataProvider001",

"role": "http://www.w3.org/ns/odrl/2/assigner"

},

"permission": \[

{

"assignee": {

"uid": "SECURITY\_ATTRIBUTE",

"role": "http://www.w3.org/ns/odrl/2/assignee"

},

"action": \[

{ "name": "http://www.w3.org/ns/odrl/2/read" }

\],

"target": "http://example.com/dataset/research123/aggregated",

"constraint": \[

{

"leftOperand": "http://www.w3.org/ns/odrl/2/dateTime",

"operator": "http://www.w3.org/ns/odrl/2/leq",

"rightOperand": "2024-12-31T23:59:59"

},

{

"leftOperand": "http://www.w3.org/ns/odrl/2/dateTime",

"operator": "http://www.w3.org/ns/odrl/2/geq",

"rightOperand": "2024-01-01T00:00:00"

},

{

"leftOperand": "http://www.w3.org/ns/odrl/2/spatial",

"operator": "http://www.w3.org/ns/odrl/2/eq",

"rightOperand": "http://www.geonames.org/external-partner-location"

}

\]

}

\]

}

**<span class="underline">Minimal Access Policy</span>**

For the the current release, access policies with limited expressive
power are planned to be supported. It is possible to define two
different actions

-   <http://www.w3.org/ns/odrl/2/>**read**: the attribute holder is able
    to search for the dataset/application/infrastructure;

-   <http://www.w3.org/ns/odrl/2/>**use**:  The attribute holder can
    consume the dataset/application/infrastructure.

while **use** implies **read**.

Date time constraints are planned to be supported for specifying when
the policy should be valid.

{RESSOURCE\_URI}, {POLICY\_URI}, {PROVIDER\_URI} are later automatically
replaced with the correct URI. {SECURITY\_ATTRIBUTE\_URI} need to be
specified but documentation with the available URI is provided, as well
as the action (read for searching and use for consumption, which implies
read)

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "{POLICY\_URI}",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"target": "{RESSOURCE\_URI}",

"assigner": {

"uid": "{PROVIDER\_URI}",

"role": "http://www.w3.org/ns/odrl/2/assigner"

},

"permission": \[

{

"assignee": {

"uid": "{SECURITY\_ATTRIBUTE\_URI}",

"role": "http://www.w3.org/ns/odrl/2/assignee"

},

"action": \[

{ "name": "http://www.w3.org/ns/odrl/2/{read/use}" }

\],

"target": "{RESSOURCE\_URI}",

"constraint": \[

{

"leftOperand": "http://www.w3.org/ns/odrl/2/dateTime",

"operator": "http://www.w3.org/ns/odrl/2/leq",

"rightOperand": "2024-12-31T23:59:59"

},

{

"leftOperand": "http://www.w3.org/ns/odrl/2/dateTime",

"operator": "http://www.w3.org/ns/odrl/2/geq",

"rightOperand": "2024-01-01T00:00:00"

}

\]

}

\]

}

1.  API to get all available attributes with description about the
    semantic. When will this be available, and can static get list so
    the development can start.

    1.  Prioritises before the MTLS;

    2.  Availability not clear;

    3.  Provide a static list.

2.  API to get the attributes of the searching consumer. For the use of
    filtering the results of the catalogue search:

    1.  over the public key;

    2.  from the JWT, attributes are in the payload.

3.  How to get Provider ID? While you use self-description? Is it
    somehow possible to get the ID of the provider from an API to add
    this information to the Self-description:

    1.  unique id of the agent is the public key, from the vault
        (HashiCorp/OCM) or the public endpoint;

    2.  self-description in long run of the participants.

4.  Map Policy to ABAC (who is doing it?):

    1.  ABAC only for first layer;

    2.  Second Layer with policy evaluation in EDC.

<img src="./media/image171.png" />

**<span class="underline">Usage Policy</span>**

The IDS Usage Control Language is based on
ODRL: <https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl>

The Usage Policy is part of the usage contract, as well as the
Self-Description. It contains permissions, prohibitions and obligations.

Usage Policy Examples:

***Allow the Usage of the Data***

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "http://example.com/policy/usage/UsagePolicy001",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"target": "http://example.com/dataset/TestData001",

"action": "http://www.w3.org/ns/odrl/2/use",

"assigner": {

"uid": "http://example.com/provider/dataProvider001",

"role": "http://www.w3.org/ns/odrl/2/assigner"

},

"permission": \[

{

"assignee": {

"uid": "http://example.com/roles/dataConsumer001",

"role": "http://www.w3.org/ns/odrl/2/assignee"

}

}

\]

}

***Use Data and Delete it After***

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "http://example.com/policy/usage/UsagePolicy001",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"target": "http://example.com/dataset/TestData001",

"action": "http://www.w3.org/ns/odrl/2/use",

"assigner": {

"uid": "http://example.com/provider/dataProvider001",

"role": "http://www.w3.org/ns/odrl/2/assigner"

},

"permission": \[

{

"assignee": {

"uid": "http://example.com/roles/consumer001",

"role": "http://www.w3.org/ns/odrl/2/assignee"

}

}

\],

"constraint": \[

{

"leftOperand": "http://www.w3.org/ns/odrl/2/deletion",

"operator": "http://www.w3.org/ns/odrl/2/eq",

"rightOperand": "after\_use"

}

\]

}

***Restricted Number of Usages***

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "http://example.com/policy/usage/UsagePolicy001",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"target": "http://example.com/dataset/TestData001",

"action": "http://www.w3.org/ns/odrl/2/use",

"assigner": {

"uid": "http://example.com/provider/dataProvider001",

"role": "http://www.w3.org/ns/odrl/2/assigner"

},

"permission": \[

{

"assignee": {

"uid": "http://example.com/roles/consumer001",

"role": "http://www.w3.org/ns/odrl/2/assignee"

}

}

\],

"constraint": \[

{

"leftOperand": "http://www.w3.org/ns/odrl/2/count",

"operator": "http://www.w3.org/ns/odrl/2/lteq",

"rightOperand": "10"

}

\]

}

***Duration-restricted Data Usage***

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "http://example.com/policy/usage/UsagePolicy001",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"target": "http://example.com/dataset/TestData001",

"action": "http://www.w3.org/ns/odrl/2/use",

"assigner": {

"uid": "http://example.com/provider/dataProvider001",

"role": "http://www.w3.org/ns/odrl/2/assigner"

},

"permission": \[

{

"assignee": {

"uid": "http://example.com/roles/consumer001",

"role": "http://www.w3.org/ns/odrl/2/assignee"

}

}

\],

"constraint": \[

{

"leftOperand": "http://www.w3.org/ns/odrl/2/dateTime",

"operator": "http://www.w3.org/ns/odrl/2/leq",

"rightOperand": "2024-12-31T23:59:59"

},

{

"leftOperand": "http://www.w3.org/ns/odrl/2/dateTime",

"operator": "http://www.w3.org/ns/odrl/2/geq",

"rightOperand": "2024-01-01T00:00:00"

}

\]

}

***Extended Scenario***

Another example of an extended usage policy for a dataset provided by a
data provider. The policy will specify how a resource can be used once
the access has been granted.

A dataset contains sensitive health research data. The data provider
wants to ensure that this data is used responsibly and in compliance
with specific guidelines. The usage policy specifies the following:

1.  The data can only be used for academic research purposes;

2.  The data cannot be shared with third parties;

3.  The data must be deleted after the research project is completed;

4.  The data usage is monitored, and any breach of the policy will
    result in revocation of access.

{

"@context": "http://www.w3.org/ns/odrl.jsonld",

"@type": "Policy",

"uid": "http://example.com/policy/usage/001",

"profile": "http://www.w3.org/ns/odrl/2/odrl.jsonld",

"target": "http://example.com/dataset/health\_research123",

"assigner": {

"uid": "http://example.com/provider/dataProvider001",

"role": "http://www.w3.org/ns/odrl/2/assigner"

},

"permission": \[

{

"assignee": {

"uid": "http://example.com/roles/researcher",

"role": "http://www.w3.org/ns/odrl/2/assignee"

},

"action": \[

{ "name": "http://www.w3.org/ns/odrl/2/use" }

\],

"constraint": \[

{

"leftOperand": "http://www.w3.org/ns/odrl/2/purpose",

"operator": "http://www.w3.org/ns/odrl/2/eq",

"rightOperand": "http://example.com/purpose/academic\_research"

},

{

"leftOperand": "http://www.w3.org/ns/odrl/2/deletion",

"operator": "http://www.w3.org/ns/odrl/2/eq",

"rightOperand": "after\_use"

}

\]

}

\]

}

**<span class="underline">Policy Enforcement</span>**

This section presents draft content for a capability falling behind the
scope of the current release and will be completed at a later time.

<img src="./media/image172.png" />

