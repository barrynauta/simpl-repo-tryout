# Onboard a Participant into the dataspace
This documentation outlines the process for onboarding participants — either consumers or providers — into the dataspace. Participants refer to corporations or other institutions, such as universities, that seek to engage with the dataspace. The onboarding of end users falls outside the scope of this documentation.

## Authority 

> **⚠️**  Note: This step is exclusively performed by a tier-2 manager of the authority and not by the participant.

Before onboarding a participant, a tier-2 manager (i.e., a user with the **T2IAA_M** role, such as the preconfigured user `e.j`) **MUST** create an onboarding procedure template for each participant type. This can be done on the following page: `<authority-frontend>/onboarding/administration/management/onboarding-procedures`

![](./imgs/onboard/0-onboarding-procedures.png)

## Participant

> **⚠️**  Prerequisite: onboarding procedure templates **MUST** exist. Participants cannot continue unless the tier-2 manager has defined onboarding procedure templates on the authority.

### Summary

To obtain tier-2 credentials from the authority, the participant must complete the following steps:

1. [Obtain tier-1 credential](#1-obtain-tier-1-credential)
2. [Submit the onboarding request](#2-submit-the-onboarding-request)
3. [The NOTARY reviews and approves the onboarding request](#3-the-notary-reviews-and-approves-the-onboarding-request)
4. [Generate the key pair](#4-generate-the-key-pair)
5. [Generate the Certificate Signing Request (CSR)](#5-generate-the-certificate-signing-request-csr)
6. [Upload the CSR to the authority website](#6-upload-the-csr-to-the-authority-website)
7. [Download the Credential from the authority website](#7-download-the-credential-from-the-authority-website)
8. [Upload the Credential to the Participant Agent](#8-upload-the-credential-to-the-participant-agent)


### 1. Obtain tier-1 credential
Register temporary tier-1 credentials for applicant into the public dataspace onboarding site. On the authority's frontend: `<authority-frontend>/onboarding/application/request`.
These credentials are used exclusively for the onboarding procedure and are not intended for logging into the components of the agent. For this purpose, the end user must be onboarded to the respective participant agent and assigned the appropriate roles.

<!-- ![](./imgs/onboard/1-application-info.png) -->
<!-- ![](./imgs/onboard/2-application-request.png)
<!-- ![](./imgs/onboard/3-application-request-dropdown.png) -->
![](./imgs/onboard/4-application-request-form.png)
<!-- ![](./imgs/onboard/5-application-request-password.png) -->

### 2. Submit the onboarding request
Applicant submits the onboarding request. On the authority's frontend: `<authority-frontend>/onboarding/application/additional-request`

<!-- ![](./imgs/onboard/6-application-request-login.png) -->
<!-- ![](./imgs/onboard/7-additional-request.png) -->
![](./imgs/onboard/8-additional-request-upload.png)
![](./imgs/onboard/9-submit.png)



### 3. The NOTARY reviews and approves the onboarding request
> **⚠️**  Note: This step is exclusively performed by a user with the **NOTARY** role (such as the preconfigured user `m.t`) of the authority and not by the participant.

The NOTARY to approve the participant application. On the authority's frontend: `<authority-frontend>/onboarding/administration`

![](./imgs/onboard/10-notary-1.png)
![](./imgs/onboard/11-notary-approve.png)
![](./imgs/onboard/12-notary-confirm.png)
<!-- ![](./imgs/onboard/13-notary-success-confirm.png) -->


### 4. Generate the key pair
Onboarding Manager (e.g., preconfigured user `a.w`) generates the key pair. On the participant's frontend: `<participant-frontend>/participant-utility/agent-configuration`


![](./imgs/onboard/14-agent-configuration-gen-key.png)
![](./imgs/onboard/15-agent-configuration-gen-key-name.png)
![](./imgs/onboard/16-agent-configuration-gen-key-success.png)


<!-- To invoke the API to generate a keypair and a csr in the participant, you need to obtain a JWT from Keycloak for a user with the **ONBOARDER_M** role. In this example, we use the preconfigured user `a.w`. Here is an example of how to obtain the token and call the APIs.

```bash
# Authentication flow - Direct Access Grants must be enbled for frontend-cli in Keycloak clients settings
# Example: <participant-tier-1-gateway> = t1.iaads-participant-01.dev.simpl-europe.eu
curl --location 'https://<participant-tier-1-gateway>.dev.simpl-europe.eu/auth/realms/participant/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=frontend-cli' \
--data-urlencode 'password=password' \
--data-urlencode 'username=a.w'
```

```bash
# Keypair Generation
# Example: <participant-tier-1-gateway> = t1.iaads-participant-01.dev.simpl-europe.eu
curl --location 'https://<participant-tier-1-gateway>.dev.simpl-europe.eu/private/auth-api/keypair/generate' \
-X POST \
--header 'Authorization: Bearer <PARTICIPANT JWT_TOKEN>' \
``` -->

### 5. Generate the Certificate Signing Request (CSR)

> **⚠️**  The common name in the CSR need to be the location of the TLS (Tier2) Gateway

Onboarding Manager (e.g., preconfigured user `a.w`) export the CSR. On the participant's frontend: `<participant-frontend>/participant-utility/agent-configuration`

<!-- 
```bash
# CSR Generation
# Example: <participant-tier-1-gateway> = t1.iaads-participant-01.dev.simpl-europe.eu
# Example: <participant-tier-2-gateway> = t2.iaads-participant-01.dev.simpl-europe.eu
curl --location 'https://<participant-tier-1-gateway>.dev.simpl-europe.eu/private/auth-api/csr/generate' \
-X POST \
--header 'Authorization: Bearer <PARTICIPANT JWT_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "commonName": "<participant-tier-2-gateway>",
  "organization": "Aruba",
  "organizationalUnit": "DevTeam",
  "country": "IT"
}' \
-o csr.pem
``` 
-->

![](./imgs/onboard/17-agent-configuration-export-csr.png)
![](./imgs/onboard/18-agent-configuration-export-csr-form.png)
![](./imgs/onboard/19-agent-configuration-export-csr-download.png)

### 6. Upload the CSR to the authority website

Applicant uploads the CSR to the public dataspace onboarding site. On the authority's frontend: `<authority-frontend>/onboarding/application/additional-request`

<!-- 
To invoke the APIs to create the credentials and download them from the governance authority, you need to obtain a JWT from Keycloak. Here is an example of how to obtain the token and call the APIs.

```bash
# Authentication flow - Direct Access Grants must be enbled for frontend-cli in Keycloak clients settings
# Example: <authority-tier-1-gateway> = t1.iaads-authority-01.dev.simpl-europe.eu
curl --location 'https://<authority-tier-1-gateway>/auth/realms/authority/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=frontend-cli' \
--data-urlencode 'username=<participant-username>' \
--data-urlencode 'password=<user-password>' 
```

```bash
# Get the onboarding-request-id the authority
# Example: <authority-tier-1-gateway> = t1.iaads-authority-01.dev.simpl-europe.eu
curl --location 'https://<authority-tier-1-gateway>/private/onboarding-api/onboarding-request?applicantEmail=<participant-email>' \
--header 'Authorization: Bearer <AUTHORITY JWT_TOKEN>'
```

```bash
# Upload the CSR on the authority
# Example: <authority-tier-1-gateway> = t1.iaads-authority-01.dev.simpl-europe.eu
curl --location 'https://<authority-tier-1-gateway>/private/identity-api/crs/<onboarding-request-id>' \
-X POST \
--header 'Authorization: Bearer <AUTHORITY JWT_TOKEN>'
-F csr = < path to csr.pem >
``` 
-->

![](./imgs/onboard/20-upload-csr.png)
![](./imgs/onboard/21-upload-csr-success.png)

### 7. Download the Credential from the authority website
Applicant download the Credential from the public dataspace onboarding site. On the authority's frontend at: `<authority-frontend>/onboarding/application/additional-request`

![](./imgs/onboard/22-download-credential.png)

### 8. Upload the Credential to the Participant Agent

Onboarding Manager (e.g., preconfigured user `a.w`) uploads the credential on the Participant Agent. Go to the participant's frontend at:  `<participant-frontend>/participant-utility/agent-configuration`.

![](./imgs/onboard/23-upload-credential.png)
![](./imgs/onboard/24-upload-credential-confirm.png)
![](./imgs/onboard/25-upload-credential-success.png)





