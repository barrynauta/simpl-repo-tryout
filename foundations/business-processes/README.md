# Business Processes and Scenario Architectures

Simpl-Open business processes and supporting scenario architectures, documented from the public requirements catalogue at https://simpl-programme.ec.europa.eu/book-page/simpl-requirements.

Each file contains a summary in the author's own words, a canonical source link, any available diagrams, and auto-inferred cross-references to the capability map (verify before relying on them).

---

## Business Processes

<table>
<tr>
<td align="center" valign="top" width="200">
<a href="./BP01-define-dataspace-governance/">
<img src="./media/BP01-tile.png" width="180" /><br>
<b>BP01</b><br>
<sub>Define dataspace governance</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP02-configuration-governance-authority/">
<img src="./media/BP02-tile.png" width="180" /><br>
<b>BP02</b><br>
<sub>Configure data space</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP03A-onboarding-participant-providers/">
<img src="./media/BP03A-tile.png" width="180" /><br>
<b>BP03A</b><br>
<sub>Onboard providers &amp; consumers</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP03B-onboarding-participant-end-user/">
<img src="./media/BP03B-tile.png" width="180" /><br>
<b>BP03B</b><br>
<sub>Onboard end-users</sub>
</a>
</td>
</tr>
<tr>
<td align="center" valign="top" width="200">
<a href="./BP05B-provider-manages-resource-descriptions/">
<img src="./media/BP05B-tile.png" width="180" /><br>
<b>BP05B</b><br>
<sub>Manage resource descriptions</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP06-consumer-searches-resources/">
<img src="./media/BP06-tile.png" width="180" /><br>
<b>BP06</b><br>
<sub>Search resources</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP07-establish-usage-contract/">
<img src="./media/BP07-tile.png" width="180" /><br>
<b>BP07</b><br>
<sub>Establish usage contract</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP08-consume-infrastructure-resource/">
<img src="./media/BP08-tile.png" width="180" /><br>
<b>BP08</b><br>
<sub>Consume infrastructure resource</sub>
</a>
</td>
</tr>
<tr>
<td align="center" valign="top" width="200">
<a href="./BP09A-consume-data-resource/">
<img src="./media/BP09A-tile.png" width="180" /><br>
<b>BP09A</b><br>
<sub>Consume data resource</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP09B-consume-data-via-application/">
<img src="./media/BP09B-tile.png" width="180" /><br>
<b>BP09B</b><br>
<sub>Consume data via application</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP12B-single-node-logging-monitoring/">
<img src="./media/BP12B-tile.png" width="180" /><br>
<b>BP12B</b><br>
<sub>Single-node logging &amp; monitoring</sub>
</a>
</td>
<td align="center" valign="top" width="200">
<a href="./BP13-it-administration/">
<img src="./media/BP13-tile.png" width="180" /><br>
<b>BP13</b><br>
<sub>IT administration</sub>
</a>
</td>
</tr>
</table>

> **BP03C** (End-user role request) has no card image on the public index page and is omitted from the tile grid above.

---

## Solution Architectures

No card images exist on the public index page for the SA entries. Text-only links:

| ID | Name | Description |
|----|------|-------------|
| [SA01](./SA01-data-orchestration/) | Data orchestration | Design, execute, and monitor traceable multi-step data processing workflows |
| [SA02](./SA02-data-processing-services/) | Data processing services | Pseudonymisation and anonymisation services for participants |
| [SA03](./SA03-credentials-actions-governance-authority/) | Credentials actions | Governance Authority manages participant credentials: revocation, suspension, renewal |
| [SA04](./SA04-provider-manages-deployment-scripts/) | Deployment scripts | Infrastructure Providers create and manage VM templates and deployment scripts |

---

## Full list

### Business Processes

- [BP01](./BP01-define-dataspace-governance/) — Define dataspace governance
- [BP02](./BP02-configuration-governance-authority/) — Configuration of data space Governance Authority
- [BP03A](./BP03A-onboarding-participant-providers/) — Onboarding of a new data space participant (Providers and Consumers)
- [BP03B](./BP03B-onboarding-participant-end-user/) — Onboarding of a new data space participant end-user
- [BP03C](./BP03C-end-user-role-request/) — End-user role request
- [BP05B](./BP05B-provider-manages-resource-descriptions/) — Provider manages resource descriptions
- [BP06](./BP06-consumer-searches-resources/) — Consumer searches resources in data space catalogues
- [BP07](./BP07-establish-usage-contract/) — Consumer and Provider establish a usage contract
- [BP08](./BP08-consume-infrastructure-resource/) — Consumer consumes an infrastructure resource from a Provider
- [BP09A](./BP09A-consume-data-resource/) — Consumer consumes a data resource from a Provider
- [BP09B](./BP09B-consume-data-via-application/) — Consumer receives a data processing service on a data resource via an application
- [BP12B](./BP12B-single-node-logging-monitoring/) — Single node logging & monitoring
- [BP13](./BP13-it-administration/) — IT administration

### Solution Architectures

- [SA01](./SA01-data-orchestration/) — Data orchestration used by a Participant
- [SA02](./SA02-data-processing-services/) — Data processing services used by a Participant
- [SA03](./SA03-credentials-actions-governance-authority/) — Credentials actions by the Governance Authority
- [SA04](./SA04-provider-manages-deployment-scripts/) — Provider manages deployment scripts
