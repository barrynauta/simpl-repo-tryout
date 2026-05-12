1. [Request list](#1-request-list)
2. [Filter request list](#2-filter-request-list)
3. [Onboarding detail](#3-onboarding-detail)
4. [Onboarding detail - request revision](#4-onboarding-detail---request-revision)
5. [Onboarding detail - reject request](#5-onboarding-detail---reject-request)
6. [Onboarding detail - approve request](#6-onboarding-detail---approve-request)
7. [Onboarding detail recap](#7-onboarding-detail-recap)
8. [Onboarding detail - documents](#8-onboarding-detail---documents)
9. [Onboarding detail - addition document not uploaded](#9-onboarding-detail---addition-document-not-uploaded)
10. [Request new document](#10-request-new-document)
11. [Onboarding detail - comments](#11-onboarding-detail---comments)
12. [Onboarding detail - identity attribute](#12-onboarding-detail---identity-attribute)
13. [Onboarding detail - identity attribute - add attribute](#13-onboarding-detail---identity-attribute---add-attribute)
14. [Onboarding detail - identity attribute - Filter add attribute](#14-onboarding-detail---identity-attribute---Filter-add-attribute)

### 1. Request list

In Simpl-Open, the notary can access and view the list of onboarding requests made by the various APPLICANTS. The page has a paginated table showing the list of requests with key information such as:
- Request status
- Request email
- Participant type
- Request date
- Last update

The page can be accessed via the following link `<authority-frontend>/onboarding/administration`.
(i.e., a user with the **NOTARY** role, such as the preconfigured user `m.t`)

![](./imgs/onboarding/onboarding-notary/request%20list.png)

### 2. Filter request list

Search filters are available on the left side of the onboarding requests page. The filters are:
- Status
- Email

A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.

The page can be accessed via the following link `<authority-frontend>/onboarding/administration`.
(i.e., a user with the **NOTARY** role, such as the preconfigured user `m.t`)

![](./imgs/onboarding/onboarding-notary/filter%20request%20list.png)

### 3. Onboarding detail

To fully manage an onboarding request, you can view the details page. You can access the page by clicking on the eye icon in the list of requests.
The details page contains information about the status, the applicant's email address, the date of the request, and the date of the last modification.
At the top right are the main features for [request revision](#4-onboarding-detail---request-revision) of the onboarding request, its [reject request](#5-onboarding-detail---reject-request)
or [approve request](#6-onboarding-detail---approve-request).

The page also features sections grouped into tabs:
- [Recap](#7-onboarding-detail-recap)
- [Documents](#8-onboarding-detail---documents)
- [Comments](#11-onboarding-detail---comments)
- [Identity attribute](#12-onboarding-detail---identity-attribute)

The page can be accessed via the following link `<authority-frontend>/onboarding/administration/:requestId`.
(i.e., a user with the **NOTARY** role, such as the preconfigured user `m.t`)

![](./imgs/onboarding/onboarding-notary/onboarding%20detail.png)

### 4. Onboarding detail - request revision

During the onboarding process, the notary may request additional documents to be uploaded by the applicant. This can be done by [adding](#10-request-new-document) additional documents.
After adding documents, the notary must be able to communicate and confirm the changes made to the specific request to the applicant. To complete the operation, the notary can use the button located at the top right of the page (Request revision). A window will appear on the screen; press the submit button to continue or cancel.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20request%20revision.png)

### 5. Onboarding detail - reject request

To reject an onboarding request, the notary can use the button located at the top right of the page (Reject). A window will appear on the screen; Compile the Reject cause and press the submit button to continue or cancel.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20reject%20request.png)

### 6. Onboarding detail - approve request

If all the information is correct and the applicant has uploaded and completed their application correctly, the notary can approve the application. To do this, click on the button at the top right (Approve). A window will appear on the screen with a notification showing the identity attributes selected for this applicant. To continue with the operation, click on the approve button, otherwise cancel.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20approve%20request.png)

### 7. Onboarding detail recap

On the details page, the recap section helps the notary get a quick overview of the latest developments for a specific onboarding request.
It is possible to view the attached documents and how many there are, whether there are any failed rules for document control, the last comment left, the list of identity attributes, and those selected for that participant.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20recap.png)
![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20recap%202.png)

### 8. Onboarding detail - documents

The documents section shows the list of documents attached or requested to the onboarding request.
From this specific section, the notary can better manage documents by downloading and viewing them, reading information messages for documents not yet uploaded by the applicant, or adding others to the onboarding request.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20documents.png)

### 9. Onboarding detail - addition document not uploaded

When a new document has been requested and a revision request has been sent, the applicant must upload the requested document. The notary can view a specific message below the document that says "The applicant has not yet uploaded any files. Check back again later"
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20additional%20document%20not%20uploaded.png)

### 10. Request new document

To request and add a new document to the onboarding request, use the button in the Documents section located at the top right. A window will appear on the screen. Fill in the document name and mime type fields, which are mandatory, and confirm with OK or cancel.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/request%20new%20document.png)

### 11. Onboarding detail - comments

In Simpl-Open, messages left in the onboarding request can be exchanged as comments. These are useful for the applicant and the notary to exchange information or clarify certain aspects during the onboarding phase. In the Comments section available on the onboarding request details page, you can view comments in chronological order and a text box with a button to send a new reply comment.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20comments.png)
![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20comments%202.png)

### 12. Onboarding detail - identity attribute

Identity attribute management is available from the Identity attribute section on the onboarding request details page. You can view the attributes selected for the participant and, if necessary, add or delete those assigned. Deletion is only available if you enter edit mode using the Edit attribute button and then the trash can icon. When you click, a window will appear with a deletion warning. Confirm or cancel the operation.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20identity%20attribute.png)
![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20identity%20attribute%202.png)
![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20identity%20attribute%203.png)

### 13. Onboarding detail - identity attribute - add attribute
![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20identity%20attribute%20add%20attribute.png)

To assign new identity attributes to the participant, click on the button (Edit attribute) and then (Add attribute). A window with the list of attributes will be displayed. You can select the ones to assign and confirm by clicking OK or cancel.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

### 14. Onboarding detail - identity attribute - Filter add attribute

Filters are available to search for one or more attributes. The filter are:
- Name
- code

A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.
There are no specific links to view the window, as this feature is available from the onboarding request details page.

![](./imgs/onboarding/onboarding-notary/onboarding%20detail%20identity%20attribute%20filter%20add%20attribute.png)
