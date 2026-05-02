<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../README.md">🏠 Home</a><br/>
    <a href="README.md">Foundations</a><br/>
        <strong>User interfaces</strong><br/>
</p>
</div>

# User interfaces

Inventory and behavioural specification of the front-end applications shipped with Simpl-Open: the Catalogue Client Application, Contract Template Editor, Policy Creator, Dagit, Kibana, Grafana, and the microfrontend framework that hosts them. Each UI here is also documented in its solution folder; this page is the cross-cut so a reader looking for "all the UIs" finds them in one place.

## Source

Extracted verbatim from `Functional-and-Technical-Architecture-Specifications.md`, section **4.5.2 User Interfaces** (lines 6114–6359 of the source, dated 2026-04-20). Upstream link: [FTA spec §4.5.2](https://code.europa.eu/simpl/simpl-open/architecture/-/blob/master/functional_and_technical_architecture_specifications/Functional-and-Technical-Architecture-Specifications.md?ref_type=heads#452-user-interfaces).

---

####  4.5.2. <a name='UserInterfaces'></a>User Interfaces

The Simpl-Open UX/UI Style Guide can be found in the Simpl Contributions
Code of Conduct & Guidelines.

<table>
<thead>
<tr class="header">
<th><strong>#</strong></th>
<th><strong>Component</strong></th>
<th><strong>Domain</strong></th>
<th><strong>Description</strong></th>
<th><strong>Functionalities</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A</td>
<td>User &amp; Roles</td>
<td>Domain 1</td>
<td>IAA frontend that allows to manage participant local users, assign roles to user and assign identity attributes to roles.</td>
<td><ul>
<li><p>Create and manage end users</p></li>
<li><p>Create and manage roles</p></li>
<li><p>Assign roles to end users</p></li>
<li><p>Assign identity attributes to roles</p></li>
<li><p>List the local copy of identity attributes of the Data Space.</p></li>
<li><p>Create and manage role requests</p></li>
<li><p>Approve or reject role requests</p></li>
</ul></td>
</tr>
<tr class="even">
<td>B</td>
<td>Onboarding</td>
<td>Domain 1</td>
<td>IAA frontend that allows Participant and Governance Authority representatives to manage the onboarding requests of new participants in the Governance Authority agent.</td>
<td><ul>
<li><p>Onboarding</p>
<ul>
<li><p>Governance Authority Representative</p>
<ul>
<li><p>Manage onboarding procedure templates along with document templates;</p></li>
<li><p>Approve or reject an onboarding request;</p></li>
<li><p>Request new documents on an open onboarding request;</p></li>
<li><p>Add comments to an Onboarding Request.</p></li>
</ul></li>
<li><p>Participant Representative</p>
<ul>
<li><p>Creating temporary credentials for a dataspace applicant;</p></li>
<li><p>Open a new onboarding request;</p></li>
<li><p>Add comments to an onboarding request;</p></li>
<li><p>Upload documents along with an onboarding request;</p></li>
<li><p>Submit an onboarding request for review;</p></li>
<li><p>Upload a participant public key;</p></li>
<li><p>Download participant credentials.</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr class="odd">
<td>C</td>
<td>Security Attributes Provider</td>
<td>Domain 1</td>
<td>IAA frontend component that allows a Governance Authority representative to manage the security attributes of a data space.</td>
<td><ul>
<li><p>Create identity attributes for the Data Space;</p></li>
<li><p>Assign identity attributes to a participant type (Consumer or Producer);</p></li>
<li><p>Unassign identity attributes to a participant type.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>D</td>
<td>Identity Provider</td>
<td>Domain 1</td>
<td>Allows the Governance Authority representative to manage participants and their credentials.</td>
<td><ul>
<li><p>Participant Management</p>
<ul>
<li><p>Governance Authority Representative </p>
<ul>
<li><p>manage onboarded participants</p></li>
<li><p>manage onboarded participants' credentials</p></li>
<li><p>renew participant credentials</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr class="odd">
<td>E</td>
<td>Domain 1</td>
<td>IAA frontend that allows the management of credentials Participant Agent. It allows a Participant Representative to generate Keypairs and install credentials to complete the onboarding process.</td>
<td><ul>
<li><p>Create a Keypair;</p></li>
<li><p>Request credential renewal</p></li>
<li><p>Manage keypairs</p></li>
<li><p>Upload a locally generated Keypair;</p></li>
<li><p>Upload the credential provided by the Governance Authority at the end of the onboarding process</p></li>
</ul></td>
</tr>
<tr class="even">
<td>F</td>
<td>Catalogue Client Application</td>
<td>Domain 2</td>
<td>The Catalogue Client Application is the primary interface through which users interact with the Catalogue. It presents search fields and options to users, which in case of advanced search are defined by the schema. </td>
<td><p><strong>Quick Search:</strong></p>
<p>put a number of search terms into the bar</p>
<p><img src="./media/image72.png" /></p>
<p>click on "Search" to receive the results</p>
<p><img src="./media/image73.png" /></p>
<p><strong>Advanced Search</strong></p>
<p>Select the Schema to search for</p>
<p><img src="./media/image73.png" /></p>
<p>Fill out the properties that you want to search on</p>
<p><img src="./media/image74.png" /></p>
<p>Click on "Search" to receive the results</p>
<p><img src="./media/image75.png" /></p>
<p><strong>Data Consumption</strong></p>
<p>Search for a valid document (see above)</p>
<p><img src="./media/image76.png" /></p>
<p>Click on the "More details" button to enable the "Request resource" button</p>
<p>Click on the "Request resource" button</p>
<p>A contract offer will appear after a short loading period</p>
<p><img src="./media/image77.png" /></p>
<p>Clicking "Decline" will close the modal</p>
<p>Clicking "Accept" will start the contract negotiation and will redirect to the contract negotiation status page</p>
<p><img src="./media/image78.png" /></p>
<p>The page refreshes every 3 seconds automatically to retrieve a new status until the status is "FINALIZED". It stops auto-refresh after that. You can also manually refresh the page to refresh the status.</p>
<p>When the status is "FINALIZED" the "Start Transfer" button will appear.</p>
<p>Clicking "Start transfer" will open a modal and it'll display the required data destination fields depending on resource type. For data offerings, this form will pop-up:</p>
<p><img src="./media/image79.png" /></p>
<p>Fill out the fields one-by-one, then scroll down to the bottom of the form and click the "Start Transfer" button:</p>
<p><img src="./media/image80.png" /></p>
<p>You'll be redirected to the transfer process status page:</p>
<p><img src="./media/image81.png" /></p>
<p>The page refreshes every 3 seconds automatically until the "DEPROVISIONED" or "TERMINATED" state is reached. The page can also be manually refreshed.</p></td>
</tr>
<tr class="odd">
<td>G</td>
<td>SD Tooling</td>
<td>Domain 2</td>
<td>Frontend with the forms for the provider to create Self-Descriptions. Written in Angular and NodeJS. The result is a SD in the form of a JSON-LD document that can be uploaded to the catalogue.</td>
<td><p>Select Schema for the SD to create<img src="./media/image82.png" /></p>
<p>Fill out the generated form with all mandatory properties</p>
<p><img src="./media/image83.png" /></p>
<p>Publish the SD to the catalogue on the Governance Authority</p>
<p><img src="./media/image84.png" /></p></td>
</tr>
<tr class="even">
<td>H</td>
<td>Schema Management UI</td>
<td>Domain 2</td>
<td>N/A - not part of the current release.</td>
<td></td>
</tr>
<tr class="odd">
<td>I</td>
<td>Vocabulary Management UI</td>
<td>Domain 2</td>
<td>N/A - not part of the current release.</td>
<td></td>
</tr>
<tr class="even">
<td>J</td>
<td>Infrastructure Deployment Script Management UI</td>
<td>Domain 2</td>
<td>User Interface for adding and removing (invalidating) the Deployment Scripts, that can provision infrastructure resources and/or deploy applications.  The UI also allows the addition of Post-Configuration script associated with a Deployment Script.</td>
<td><ul>
<li><p>List Deployment Scripts, by accessing the "Deployment Scripts" menu<br />
<img src="./media/image85.png" /></p></li>
<li><p>Add/Upload a Deployment Script, by clicking the "+ Add Script +" button<img src="./media/image86.png" /></p></li>
<li><p>Deployment Script details, by clicking the "Properties" icon</p></li>
</ul>
<blockquote>
<p><img src="./media/image87.png" /></p>
<p><img src="./media/image88.png" /></p>
</blockquote>
<ul>
<li><p>Download Script, by clicking the "Download" icon<br />
<img src="./media/image89.png" /></p></li>
<li><p>Inactivate a Deployment Script, by clicking the "Trash" icon<br />
<img src="./media/image90.png" /></p></li>
<li><p>Adding a Post Configuration, by clicking on "Add Config File" button</p></li>
</ul>
<blockquote>
<p><img src="./media/image91.png" /></p>
</blockquote>
<ul>
<li><p>List of Decommissioned resources, by accessing the "Contracts" menu</p></li>
</ul>
<blockquote>
<p><img src="./media/image92.png" /></p>
</blockquote>
<ul>
<li><p>Decommissioning a cloud resource, by clicking the "Decommission" button</p></li>
</ul>
<blockquote>
<p><img src="./media/image93.png" /></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>K</td>
<td>Orchestration Management UI</td>
<td>Domain 2</td>
<td>UI layer from dagster, allows you to manage the workflow</td>
<td><ul>
<li><p>list workflows</p></li>
<li><p>see contained services</p></li>
<li><p>configure workflow for run</p></li>
<li><p>manual start a workflow run</p></li>
<li><p>see previous runs with status</p></li>
<li><p>monitor execution and logs</p></li>
</ul></td>
</tr>
<tr class="even">
<td>L</td>
<td>Infrastructure Deployment Script Management UI</td>
<td>Domain 2</td>
<td>User Interface for managing templates for deployment scripts. A template is defined for a specific cloud environment and a specific deployment script is generated from such a template.</td>
<td><ul>
<li><p>Configure the Cloud Environment</p></li>
</ul>
<ul>
<li><p>Register Extra Configurations (Optional)</p>
<ul>
<li><p>Define configurations for the provisioned VM</p></li>
</ul></li>
</ul>
<p> </p>
<ul>
<li><ul>
<li><p>Define security policies for the provisioned VM</p></li>
</ul></li>
</ul>
<ul>
<li><ul>
<li><p>Define additional packages that will be installed on the provisioned VM</p></li>
</ul></li>
</ul>
<ul>
<li><p>Create the VM Template (OVH, IONOS)</p></li>
</ul></td>
</tr>
</tbody>
</table>

