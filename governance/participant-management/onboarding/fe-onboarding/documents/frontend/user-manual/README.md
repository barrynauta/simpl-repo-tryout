# Table of contents
1. [Welcome page](#1-welcome-page)
2. [Create onboarding request page](#2-create-onboarding-request-page)
3. [Onboarding request status](#3-onboarding-request-status)
4. [Onboarding request file management](#4-onboarding-request-file-management)
  1. [eIDAS Documents](#41-eidas-documents)
5. [Submit onboarding request](#5-submit-onboarding-request)
6. [Onboarding application instruction](#6-onboarding-application-instruction)


### 1. Welcome page

The Simpl-Open welcome page helps you understand the first steps you need to take to register in a dataspace. It provides instructions to register to a new datapsace with the available identity providers.

The page can be accessed via the following link `<authority-frontend>/onboarding/application/info`.

This page is public and can be accessed by anyone without any specific role.

Clicking on the button (Access the onboarding portal) will redirect you to the Keycloak page where you can register to start the onboarding process or log in to resume an existing one.

![](./imgs/onboarding/onboarding-applicant/welcome%20page.png)

### 2. Create onboarding request page

The page can be accessed, after signing up or logging in with any of the available identity providers, via the following link `<authority-frontend>/onboarding/application/create-onboarding-request`.
To register and start the onboarding process in the dataspace, please fill in all the required fields in the form.
Some fields are automatically filled in based on the information provided by the chosen identity provider and cannot be changed.

![](./imgs/onboarding/onboarding-applicant/registration%20page%20new.png)

### 3. Onboarding request status

The Onboarding request status page can only be accessed after registering and creating a user account. On this page, you can check the status of your onboarding request and see which documents need to be uploaded and/or have already been uploaded.
If there are comments left by other users, these will be visible at the bottom of the page just above the text box that allows you to leave a comment. To send a comment, fill in the box and send it using the button (Post comment).
At the top right, there is a button that allows you to submit your request once it has been completed correctly.

The page can be accessed via the following link `<authority-frontend>/onboarding/application/additional-request`.

![](./imgs/onboarding/onboarding-applicant/onboarding%20request%20status.png)

### 4. Onboarding request file management

To continue or complete the onboarding process, you must upload the required documents. On the onboarding request page, you can upload, download, or remove files to attach to the request for each document.

The page can be accessed via the following link `<authority-frontend>/onboarding/application/additional-request`.

(i.e., a user with the **APPLICANT** role, use the user you registered in 2. [step two](#2-create-onboarding-request-page)
)

![](./imgs/onboarding/onboarding-applicant/onboarding%20request%20file%20management.png)

### 4.1 eIDAS Documents

Onboarding request can have at most one eIDAS document to be uploaded.

Uploading an eIDAS document is different from uploading a normal document.

To upload the eIDAS document, you must click on the button (Retrieve my eIDAS Data).

![](./imgs/onboarding/onboarding-applicant/eidas%20fetch.png)

After clicking on the button, you can view the fetched data from your eIDAS identity by clicking on the button (View my eIDAS Data).

![](./imgs/onboarding/onboarding-applicant/eidas%20view.png)

### 5. Submit onboarding request

Once everything has been uploaded and filled in correctly, the onboarding request can be sent. On the APPLICANT's onboarding request page, the button (Submit application request) is visible at the top right. Clicking on the button will display a warning message. Click submit to continue or cancel.

![](./imgs/onboarding/onboarding-applicant/Submit%20onboarding%20request.png)

### 6. Onboarding application instruction

You may see a banner that helps the applicant fill out the onboarding request. It can be a simple message or a list of instructions to keep in view and follow.

![](./imgs/onboarding/onboarding-applicant/application%20instruction.png)
