<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Dimension: Governance</a><br/>
        <a href="../README.md">Capability: Resource Management</a><br/>
            <a href="README.md">Service: Metadata Description</a><br/>
                <strong>Detailed technical specification</strong><br/>
</p>
</div>

# Detailed technical specification — Self-Descriptions

This page reproduces the Self-Descriptions section of the functional and technical architecture specification (FTA §6.4.2). It is the canonical reference for the structure, syntax, and validation rules of resource self-descriptions — the GX-Trustframework-derived ontology, the SHACL shapes used by the Federated Catalogue to validate submissions, the JSON-LD signing model, and the bridge between Self-Descriptions and the [contract](../../../contract-management/contract-establishment/README.md) and [policy](../../../policy-management/policy-administration-point/README.md) flows.

The components that implement this specification — [SD Manager, SD Tooling, Validation Backend](README.md) — sit under this service folder. The Gaia-X Trust Framework that this ontology derives from is referenced in [foundations/interoperability.md](../../../foundations/interoperability.md).

## Source

This content is extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **6.4.2 Self-Descriptions** (lines 12653–13556 of the source document, dated 2026-04-20).

Upstream link: [Functional and Technical Architecture Specifications](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#642-self-descriptions).

---

####  6.4.2. <a name='Self-Descriptions'></a>Self-Descriptions

The metadata will be described as self-descriptions. These are described
in this section.

In the sub-section Self-Description Tooling the tools to create
self-descriptions are introduced and the flow of the different steps to
be considered are visualised. The SD Schema Creator enables customised
schemas for each Data Space. In Schema Definition Properties the
proposed attributes any Simpl Data Space should utilise are enlisted.
The Validation of Syntax and schema can be looked up in SD Tooling
Syntax Validation & Schema Validation.

The structure of Self-Descriptions should be based on the [GAIA-X
Trustframework](https://gaia-x.gitlab.io/policy-rules-committee/trust-framework/trust_anchors/).
There are already Gaia-X powered Data Spaces providing such an SD. This
way the created SD can be easily reused and be enhanced by the special
requirements of each sectoral Data Space. 

**<span class="underline">Base Entities and their relationship due to
Gaia-X Trustframework</span>**

Note

Attributes marked in red color are planned, but not yet implemented.

**Data Offering:**

<table>
<thead>
<tr class="header">
<th><strong>Simpl Attribute</strong></th>
<th><strong>Entity</strong></th>
<th><strong>Attribute</strong></th>
<th><strong>Cardinality</strong></th>
<th><strong>Mandatory / Recommended</strong></th>
<th><strong>Data Type</strong></th>
<th><strong>Constraint</strong></th>
<th><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unique identifier</td>
<td>service-offering</td>
<td>id</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td></td>
<td>The id of the ServiceOffering. usually refering to a DID. Set automatically.</td>
</tr>
<tr class="even">
<td>Name</td>
<td>service-offering</td>
<td>name</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:maxLength 255</td>
<td>A human readable name of the service offering</td>
</tr>
<tr class="odd">
<td>Description</td>
<td>service-offering</td>
<td>description</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:maxLength 1000</td>
<td>a short description of the service offering</td>
</tr>
<tr class="even">
<td>Location of the dataset (e.g. URL, handle)</td>
<td>service-offering</td>
<td>serviceAccessPoint</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:anyURI</td>
<td>sh:pattern "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&amp;//=]*)"</td>
<td>a list of <a href="https://en.wikipedia.org/wiki/Service_Access_Point">Service Access Point</a> which can be an endpoint as a mean to access and interact with the resource</td>
</tr>
<tr class="odd">
<td>Keywords</td>
<td>service-offering</td>
<td>keywords</td>
<td>0..16</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:maxLength 50</td>
<td>list of keywords</td>
</tr>
<tr class="even">
<td>Language (of the metadata, like the title, description)</td>
<td>service-offering</td>
<td>inLanguage</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:languageIn ("bg" "hr" "cs" "da" "nl" "en" "et" "fi" "fr" "de" "el" "hu" "ga" "it" "lv" "lt" "mt" "pl" "pt" "ro" "sk"  "sl" "es" "sv")</td>
<td>The language of the content or performance or used in an action. Please use one of the language codes from the <a href="http://tools.ietf.org/html/bcp47">IETF BCP 47 standard</a>. See also <a href="https://schema.org/availableLanguage">availableLanguage</a>.</td>
</tr>
<tr class="odd">
<td>Version</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>xsd:string</td>
<td></td>
<td>The version of the self-description. Technical property, set automatically.</td>
</tr>
<tr class="even">
<td>Creation date</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>xsd:dateTimeStamp</td>
<td></td>
<td>The first onboarding date. Technical property, set automatically.</td>
</tr>
<tr class="odd">
<td>Last update date</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>xsd:dateTimeStamp</td>
<td></td>
<td> The last update date. Technical property, set automatically.</td>
</tr>
<tr class="even">
<td>SD Schema</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>xsd:string</td>
<td></td>
<td>Reference to the used Schema ID (and version). Technical property, set automatically.</td>
</tr>
<tr class="odd">
<td>Data Provider</td>
<td>provider-information</td>
<td>providedBy</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:maxLength 255</td>
<td>Reference to Participant SD. <strong>To be Set automatically.</strong></td>
</tr>
<tr class="even">
<td>Contact point (who to contact in case of questions/issues)</td>
<td>provider-information</td>
<td>contact</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:pattern "^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"</td>
<td>email adress of the contact point</td>
</tr>
<tr class="odd">
<td>License</td>
<td>offering-price</td>
<td>license</td>
<td>1..n</td>
<td>Mandatory</td>
<td>xsd:anyURI</td>
<td><p>sh:pattern "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&amp;//=]*)"</p>
<p>sh:maxLength 255</p></td>
<td>A list of <a href="https://github.com/spdx/license-list-data/tree/master/jsonld">SPDX</a> identifiers or URL to document</td>
</tr>
<tr class="even">
<td>Price Type</td>
<td></td>
<td>priceType</td>
<td></td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:in("free" "commercial")</td>
<td>Link to price in the future.</td>
</tr>
<tr class="odd">
<td>Price (free, under cost)</td>
<td>offering-price</td>
<td>price</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:decimal</td>
<td>sh:minInclusive 0</td>
<td></td>
</tr>
<tr class="even">
<td>Currency</td>
<td></td>
<td>currency</td>
<td></td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:in("BGN" "EUR" "CZK" "DKK" "HUF" "PLN" "RON" "SEK" )</td>
<td></td>
</tr>
<tr class="odd">
<td>Access policy (to define who can access the dataset)</td>
<td>service-policy</td>
<td>access-policy</td>
<td>0..n</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:pattern "[:,\{\}\[\]]|(\".*?\")|('.*?')|[-\w.]+"</td>
<td>a list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, …)</td>
</tr>
<tr class="even">
<td>Usage policy (to define how a dataset can be used)</td>
<td>service-policy</td>
<td>usage-policy</td>
<td>0..n</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:pattern "[:,\{\}\[\]]|(\".*?\")|('.*?')|[-\w.]+"</td>
<td>a list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, …)</td>
</tr>
<tr class="odd">
<td>Compliance: Indicates compliance with relevant data protection regulations and standards.</td>
<td>service-policy</td>
<td>dataProtectionRegime</td>
<td>0..n</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:pattern "[:,\{\}\[\]]|(\".*?\")|('.*?')|[-\w.]+"</td>
<td></td>
</tr>
<tr class="even">
<td>Provenance</td>
<td>dataset-properties</td>
<td>producedBy</td>
<td>1</td>
<td>Recommended</td>
<td>xsd:anyURI</td>
<td>sh:pattern "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&amp;//=]*)"</td>
<td>a resolvable link to the participant self-description legally enabling the data usage</td>
</tr>
<tr class="odd">
<td>Format under which the data is distributed (e.g. csv, xml, …)</td>
<td>dataset-properties</td>
<td>format</td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Schema of the dataset, depends on the type of data for JSON it would be JSON Schema Description that states what fields the data has and the types.</td>
<td>dataset-properties</td>
<td>openAPI</td>
<td>0..n</td>
<td>Recommended</td>
<td>xsd:anyURI</td>
<td>sh:pattern "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&amp;//=]*)"</td>
<td>URL of the <a href="https://github.com/OAI/OpenAPI-Specification/blob/3.1.0/versions/3.1.0.md">OpenAPI documentation</a></td>
</tr>
<tr class="odd">
<td>Additional Information about the dataset</td>
<td></td>
<td>additionalInfo</td>
<td></td>
<td></td>
<td>xsd:anyURI</td>
<td>sh:pattern "[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&amp;//=]*)"</td>
<td></td>
</tr>
<tr class="even">
<td>Related datasets</td>
<td>dataset-properties</td>
<td>relatedDatasets</td>
<td>0..n</td>
<td>Recommended</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Target users</td>
<td>dataset-properties</td>
<td>targetUsers</td>
<td>0..n</td>
<td>Recommended</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Data Quality (to include metrics such as completeness, accuracy, timeliness and other)</td>
<td>dataset-properties</td>
<td>dataQuality</td>
<td>0..n</td>
<td>Recommended</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Encryption: Describes the encryption algorithms and keys used to secure the data.</td>
<td>dataset-properties</td>
<td>encryption</td>
<td>0..1</td>
<td>Recommended</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Anonymisation/pseudonymisation: Indicates whether sensitive information has been anonymised or pseudonymised to protect privacy.</td>
<td>dataset-properties</td>
<td>anonymization</td>
<td>0..1</td>
<td>Recommended</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Contract template</td>
<td>contract-template</td>
<td>contractTemplate</td>
<td>1..n</td>
<td></td>
<td>xsd:string</td>
<td>sh:in ( "Contract Template 1" "Contract Template 2" "Contract Template 3" )</td>
<td>Refering to an SD of a Contract Template</td>
</tr>
</tbody>
</table>

**Infrastructure Offering:**

<table>
<thead>
<tr class="header">
<th><strong>Simpl Attribute</strong></th>
<th><strong>Entity</strong></th>
<th><strong>Attribute</strong></th>
<th><strong>Cardinality</strong></th>
<th><strong>Mandatory / Recommended</strong></th>
<th><strong>Data Type</strong></th>
<th><strong>Constraint</strong></th>
<th><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Resource Type</td>
<td>infrastructure-properties</td>
<td></td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:in("vm" "container" "block_storage" "object_storage" "relational_db" "document_db")</td>
<td></td>
</tr>
<tr class="even">
<td>Region and availability zone</td>
<td>infrastructure-properties</td>
<td></td>
<td>1..n</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:in("eu-west-1" "eu-west-2" "eu-west-3" "eu-central-1" "eu-north-1" "eu-south-1" "eu-south-2")</td>
<td></td>
</tr>
<tr class="odd">
<td>Size and capacity</td>
<td>infrastructure-properties</td>
<td></td>
<td>0..1</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:pattern "\d+(\.\d+)?\s?(B|KB|MB|GB|TB|PB|EB|ZB|YB)"</td>
<td></td>
</tr>
<tr class="even">
<td>Operating system and image</td>
<td>infrastructure-properties</td>
<td></td>
<td>0..1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Network configuration</td>
<td>infrastructure-properties</td>
<td></td>
<td>0..1</td>
<td>Recommended</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Security settings (access control, security groups/firewalls, encryption)</td>
<td>infrastructure-properties</td>
<td></td>
<td>0..1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Instance type</td>
<td>infrastructure-properties</td>
<td></td>
<td>0.1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Storage type</td>
<td>infrastructure-properties</td>
<td></td>
<td>0.1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Backup and redundancy</td>
<td>infrastructure-properties</td>
<td></td>
<td>0..1</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:in("full-backup" "incremental-backup" "differential-backup")</td>
<td></td>
</tr>
<tr class="even">
<td>Scalability options</td>
<td>infrastructure-properties</td>
<td></td>
<td>0..1</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:in("dynamic-scaling" "scheduled-scaling", "sharding")</td>
<td></td>
</tr>
<tr class="odd">
<td>Monitoring and logging</td>
<td>infrastructure-properties</td>
<td></td>
<td>0..1</td>
<td>Recommended</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Tags and metadata</td>
<td>infrastructure-properties</td>
<td>keywords</td>
<td>0..16</td>
<td>Recommended</td>
<td>xsd:string</td>
<td>sh:maxLength 50</td>
<td></td>
</tr>
<tr class="odd">
<td>External Url</td>
<td>infrastructure-properties</td>
<td></td>
<td>1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td>sh:maxLength 255</td>
<td></td>
</tr>
<tr class="even">
<td>Deployment script ID</td>
<td>infrastructure-properties</td>
<td></td>
<td>0.1</td>
<td>Mandatory</td>
<td>xsd:string</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**termsAndCondition structure (defined by Gaia-X Trustframework)**

<table>
<thead>
<tr class="header">
<th><strong>Attribute</strong></th>
<th><strong>Cardinality</strong></th>
<th><strong>DataType</strong></th>
<th><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>URL</td>
<td>1</td>
<td>xsd:string</td>
<td>a resolvable link to document</td>
</tr>
<tr class="even">
<td>hash</td>
<td>1</td>
<td>xsd:string</td>
<td>SHA256 of the above document</td>
</tr>
</tbody>
</table>

**dataAccountExport structure (defined by Gaia-X Trustframework)**

The purpose is to enable the participant ordering the service to assess
the feasibility to export its personal and non-personal data out of the
service.  
This export shall cover account data e.g., account holder’s billing
information, information on the PII held - but also data provided
previously to the service by the user.

<table>
<thead>
<tr class="header">
<th><strong>Attribute</strong></th>
<th><strong>Cardinality</strong></th>
<th><strong>DataType</strong></th>
<th><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>requestType</td>
<td>1</td>
<td>xsd:string</td>
<td>the mean to request data retrieval: API, email, webform,<br />
unregisteredLetter, registeredLetter, supportCenter</td>
</tr>
<tr class="even">
<td>accessType</td>
<td>1</td>
<td>xsd:string</td>
<td>type of data support: digital, physical</td>
</tr>
<tr class="odd">
<td>formatType</td>
<td>1</td>
<td>xsd:string</td>
<td>type of Media Types (formerly known as MIME types) as defined by the <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">IANA</a>.</td>
</tr>
</tbody>
</table>

#####  2.28.1. <a name='QualityRules'></a>Quality Rules

Currently, only *mandatory quality* *rules* are supported. A Quality
Score can only be calculated for recommended quality rules thus this
will also not be supported.

*Mandatory quality* *rules are always *enforced during the creation of a
Self-Description (SD) for an offering, to ensure the data quality of the
SD. A resource provider is not able to publish an SD that is not
complying with the mandatory quality rules.

###### Quality Rule Formalisation

Quality rules are defined in the schema of the self-description (which
are semantic RDF Graphs) and allow to express data types, constraints
and conditions on those RDF Graphs. Thus, SHACL (Shape Constraint
Language) Constraints are intended to be used as the formal notation to
express quality rules.

The quality rules that can be defined for an SD property can be based on
the data type and/or on a SHACL constraint. Example of Constraints:

-   Minimum or maximum length of a string value

-   Value Ranges for Numbers

-   Non-Negative Numbers

-   Regular Expressions (Patterns)

-   List of allowed values

-   Constraints based on other properties

**<span class="underline">Data Model (initial)</span>**

To define the quality rules, there are three basic entities:

-   Quality Rule: The (mandatory) quality rule. It is uniquely defined
    by an id and contains a textual description of the rule in clear
    text;

-   Rule Template: The template for the formal definition of the rule.
    It contains besides the ID a field with SHACL template that is
    parameterised. The number of parameters and their type is defined in
    a parameter\_schema, i.e., JSON Blob with the parameter and data
    types;

-   Quality Dimension: The quality dimension used to group the quality
    rule for instance FAIR as an example.

Each Quality Rule has exactly one Dimension and one Rule Template
associated. The template\_assoc also contains the concrete
parameterisation for the rule template.

<img src="./media/image161.png" />

**<span class="underline">Score Calculation</span>**

The score is calculated by dimension.

\\delta\_{r,s} = \\begin{cases}

1 & \\text{if the quality rule r is fulfilled for the self-description
s} \\\\

0 & \\text{else}

\\end{cases}

\\newline \\newline

\\text{score}(s, d) = \\frac{\\sum\_{r \\ in ~R\_d} \\delta\_{r,s} \*
w\_r}{\\sum\_{r \\ in ~{R}\_d} w\_r} \* 100

\\newline \\newline

s \\text{ is valid} \\Leftrightarrow \\forall d \\in D: \\text{score}(s,
d) \\geq \\text{min\_score}\_d

<img src="./media/image162.png" />

The kronecker-delta is 1 if the quality rule r is fulfilled for the
self-description s, else 0.

The score for a self-description s and quality dimension d is calculated
by the sum over all the Quality rules r for the Dimension d (R\_d)
multiplied by their weight w. This is then normalised by the sum of all
weights for the dimension. Because a value between 0-100 is desired
instead of between 0-1, it is multiplied by 100.

A self-description is valid exactly if, for all quality dimension the
score is greater than the specified threshold (min\_score). 

**<span class="underline">Calculation Process</span>**

The calculation of the score (and the validation of the rules) is done
during the publication of the self-description **s** in the query
mapper. First, all the active quality rules are retrieved from the
database (with the associated SHACL template). All the rules are looped
over and validated against the self-description **s.** The results are
added to the quality report for **s**. After all the rules are
processed, all the quality dimensions **d** are iterated over. For each
dimension the score is calculated.

Next, it is checked whether all the mandatory rules are fulfilled and if
the score for each dimension is above the defined threshold. If this is
not the case, the publication is aborted, and the quality report is
returned to the provider. Else, the publication continues, and the
quality report is returned to the provider.

<img src="./media/image163.png" />

#####  2.28.2. <a name='Self-DescriptionTooling'></a>Self-Description Tooling

The self-description tooling consists of four different components that
are all in their respective repositories:

1.  SD Schema Creator: [SD Schemas](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-schemas/sd-schemas)  
    This component creates the schemas that describe the form and
    content of the self-description. It is used by the Governance
    Authority to set the standard for the Self-Description. Technically
    it is done by a set of configuration files in the form of
    YAML-Documents. Those files are verified and transformed into an
    ontology and SHACL Constraints that are used by the other components
    to create the wizards. The component is written in Python, and at
    least the YAML configuration needs to be adjusted for Simpl-Open.

2.  SD Creation Wizard API: [SD Creation Wizard API](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-creation-wizard-api)  
    The main API project. Transform the SHACL-shapes from the SD
    Schema Creator into JSON forms that are used by the frontend to
    allow the provider to write new Self-Descriptions. 

3.  SD Creation Wizard Frontend: [SD Creation Wizard Frontend](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-creation-wizard-frontend)  
    Frontend with the forms for the provider to create
    Self-Descriptions. Written in Angular and NodeJS. The result is an
    SD in the form of a JSON-LD document that can be uploaded to the
    catalogue.

4.  SD Validation API: [SD Validation API](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-validation-api)  
    Validation of the Self-Description against SHACL files. Might be
    used for the Quality Rule Validation. Written in Java.

<img src="./media/image164.png" />

###### SD Schema Creator

**<span class="underline">Background</span>**

Self-Description in the context of DATA/APP are documents that describe
the service offering (either Data, Application, or Infrastructure). The
Schema of the Self-Description defines the format of the
Self-Description, i.e. it is a description about what are the fields for
the self-description, their data types and if they are mandatory or not.

**Component Self-Description Schema Creator**:

The Schema-Framework is a component that is able to generate the
self-description schemas from configuration files. The idea is that from
a simple configuration the schemas are generated and later used by the
provider to write the self-description.

It should include validation of the schema files (syntax and semantic).

The basis of the implementation is the repository from Gaia-X Context
[sd-schemas](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-schemas/sd-schemas/-/tree/main?ref_type=heads)

**<span class="underline">Context View</span>**

The main actor in the SD Schema Creator is the Data Governance
Authority. They can configure the schema by changing the yaml files that
define how the schemas for the different services should look like.

<img src="./media/image165.png" />

**<span class="underline">Component View</span>**

The input of the system is the SD Schema Configuration, the file uses
the LinkML data model and is serialised as a YAML document. After the
configuration is changed the process is triggered that first checks the
syntax and the semantic. After the validation the configuration files
are transformed into two different files that describe the semantic. One
is an ontology, i.e. a formal representation of the knowledge which is
used as a vocabulary for the SD Tool. The other are constraints in the
form of SHACL-Shapes that are used as a template to build the forms in
the SD Tool. Both semantic files are serialised as Turtle-files. 

<img src="./media/image166.png" />

***Syntax Validation***

For YAML files there exist currently no standard for schema validation.
To this end, the SD Schema Description is transformed into a JSON
Serialisation and a JSON-Schema Description is used for the syntax
validation. This JSON-Schema is written by the Data Governance
Authority.

<img src="./media/image167.png" />

***Semantic Validation***

The Semantic Validation uses a Python script which reads some
configuration and guidelines (for instance which fields are mandatory in
the schema).

<img src="./media/image168.png" />

**<span class="underline">Runtime View</span>**

For the current release, the system is simply deployed as a GitLab
repository. A GitLab CI Pipeline starts if the configuration is changed
by the data governance authority and generates new files. If the Data
Provider starts the SD Tool, the SD-Tool pulls from the repository the
current SHACL Constraints and Ontology.

<img src="./media/image169.png" />

##### SD Tooling Syntax Validation & Schema Validation

**<span class="underline">Vocabulary, Schema and
Self-Descriptions</span>**

<img src="./media/image170.png" />

The vocabulary is a formal description of an ontology, representing
knowledge and relationships between the terminologies, containing
inference and integrity rules for reasoning.

A schema is describing a data object with constraints on the content,
structure and meaning of a graph. These conditions may constrain the
number of values that a property may have, the type of values, numeric
ranges, string matching patterns or logical combinations of constraints.

The Self-Description is an instance of a schema object, meaning that
values are assigned to the properties.

**<span class="underline">Syntax Validation</span>**

**Syntax Validation** during the process of creating the SD comprises
the following:

-   Formatting: Check if the file is malformed (e.g. missing brackets
    etc.);

-   Data Types: Check for the correctly applied values according to data
    types. Allowed data Types according to
    [dataTypeAbbreviation.yaml](https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-schemas/sd-schemas/-/blob/main/single-point-of-truth/yaml/validation/trusted-cloud/dataTypeAbbreviation.yaml?ref_type=heads).

The syntax validation for data types in the SD Frontend is based on the
schema definition, which is the single point of truth. 

The Syntax validation on the provider node is based on the schemas that
are imposed by Simpl and are intended to guide the user to provide an
error free Self-Description.

The Syntax validation on the Governance Authority Node ensures that only
valid Self-Descriptions will be published to the catalogue.

**<span class="underline">Allowed Data Types</span>**

xsd:string: 'http://www.w3.org/2001/XMLSchema\#string'

xsd:boolean: 'http://www.w3.org/2001/XMLSchema\#boolean'

xsd:decimal: 'http://www.w3.org/2001/XMLSchema\#decimal'

xsd:float: 'http://www.w3.org/2001/XMLSchema\#float'

xsd:double: 'http://www.w3.org/2001/XMLSchema\#double'

xsd:duration: 'http://www.w3.org/2001/XMLSchema\#duration'

xsd:dateTime: 'http://www.w3.org/2001/XMLSchema\#dateTime'

xsd:time: 'http://www.w3.org/2001/XMLSchema\#time'

xsd:date: 'http://www.w3.org/2001/XMLSchema\#date'

xsd:gYearMonth: 'http://www.w3.org/2001/XMLSchema\#gYearMonth'

xsd:Day: 'http://www.w3.org/2001/XMLSchema\#Day'

xsd:hexBinary: 'http://www.w3.org/2001/XMLSchema\#hexBinary'

xsd:base64Binary: 'http://www.w3.org/2001/XMLSchema\#base64Binary'

xsd:anyURI: 'http://www.w3.org/2001/XMLSchema\#anyURI'

xsd:QName: 'http://www.w3.org/2001/XMLSchema\#QName'

xsd:NOTATION: 'http://www.w3.org/2001/XMLSchema\#NOTATION'

xsd:dateTimeStamp: 'http://www.w3.org/2001/XMLSchema\#dateTimeStamp'

xsd:enum: 'http://www.w3.org/2001/XMLSchema\#enum'

xsd:integer: 'http://www.w3.org/2001/XMLSchema\#integer'

xsd:address: 'http://www.w3.org/2001/XMLSchema\#address'

xsd:nonNegativeNumber:
'http://www.w3.org/2001/XMLSchema\#nonNegativeNumber'

did:example: 'https://www.w3.org/TR/did-core/\#example'

dct:location: 'http://dublincore.org/usage/terms/history/\#Location-001'

trusted-cloud:meaningfulString:
'class-placeholder-from-dataTypeAbbreviation.yaml'

**<span class="underline">Semantic Validation</span>**

**Semantic Validation** during the process of creating the SD comprises:

-   the verification of property patterns;

-   data ranges;

-   other constraints;

-   the cardinality of the properties;

-   the ontology/vocabulary compliance.

Examples:

-   Value Ranges;

-   Length;

-   Pattern;

-   Value Comparison;

-   Memberships;

-   Logical.

Constraints can be defined according to [Shapes Constraint
Language](https://www.w3.org/TR/shacl/#property-shapes)

