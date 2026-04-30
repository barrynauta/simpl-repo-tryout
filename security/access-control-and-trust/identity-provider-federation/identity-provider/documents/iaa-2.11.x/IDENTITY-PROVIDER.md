# Table of contents
1. [Participant list](#1-participant-list)
2. [Filter participant list](#2-filter-participant-list)
3. [Auto renewal settings](#3-auto-renewal-settings)
4. [Participant detail - identity attribute](#4-participant-detail---identity-attribute)
5. [Participant detail - Edit and add attribute](#5-participant-detail---edit-and-add-attribute)
6. [Attribute list](#6-attribute-list)
7. [Filter attribute list](#7-filter-attribute-list)
8. [Participant detail - credentials](#8-participant-detail---credentials)
9. [Participant detail - Filter credentials](#9-participant-detail---filter-credentials)
10. [Suspend ad reactivation credential](#10-suspend-and-reactivation-credential)
11. [Revoke credential](#11-revoke-credential)
12. [Renew credential](#12-renew-credential)
13. [Participant detail - Auto renewal settings](#13-participant-detail---auto-renewal-settings)

### 1. Participant list

In Simpl-Open, you can view participants for your dataspace. The page can be accessed via the following link `<authority-frontend>/identity-priover/participants`. A page will be displayed with a paginated table showing the list of participant with various information.
From the participant table, you can view [details](#4-participant-detail---identity-attribute) using the eye icon, [revoke](#11-revoke-credential) access using the trash can icon, or [suspend ad reactivation](#10-suspend-and-reactivation-credential) participant credentials using the closed or open padlock icon.
(i.e., a user with the **IATTR_M** role, such as the preconfigured user `m.m`)

![](./imgs/identity-provider/participant%20list.png)

### 2. Filter participant list

On the left, you can filter and search for a single or multiple participant/s using the filters provided, which are Organization name and Onboarding date range.
A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.

![](./imgs/identity-provider/filter%20participant%20list.png)

### 3. Auto renewal settings

From the participant list page, you can set or change the auto-renewal value.
Clicking on the button (Auto renewal settings) located at the top right will display a window where you can change the auto-renewal value expressed in days. You can enter a value between 0 and 1830.
There is no specific link, as the user accesses the feature directly from the participants page and has the role to do so.

![](./imgs/identity-provider/auto%20renewal%20settins.png)

### 4. Participant detail - identity attribute

Clicking on the eye icon will display the participant details. The page can be accessed via the following link `<authority-frontend>/identity-priover/participant/:participantId`.
The header with the various features is located at the top right of the page:
- [Revoke](#11-revoke-credential) credentials
- [Renew](#12-renew-credential) credentials
- [Suspend ad reactivation](#10-suspend-and-reactivation-credential)
- Download CSR (Click on the button at the top right of the page. The download will start automatically)
- Upload csr (Click on the button at the top right of the page. Select the file to upload)

In addition to the features listed in the page header, there are sections for [identity attribute](#6-attribute-list), [credentials](#8-participant-detail---credentials), and [auto renewal](#13-participant-detail---auto-renewal-settings) settings.

(i.e., a user with the **IATTR_M** role, such as the preconfigured user `m.m`)

![](./imgs/identity-provider/participant%20detail%20identity%20attribute.png)

### 5. Participant detail - Edit and add attribute

To manage the identity attributes related to the participant, select the tab labeled (Identity attribute) to view those associated with the participant being displayed. From the table, you can delete an identity attribute using the trash can icon. To make changes visible only after changing the status that allows modification using the button (Modify attributes).
In the attribute modification state, in addition to removing assigned attributes, one or more attributes can be added to the participant. This feature is available via the (Add attribute) button, which is only visible after entering edit mode.
All changes are temporary, whether they involve deletion or addition, and the user must confirm whether to save or cancel them.
There is no specific link, as the user accesses the feature directly from the participants page and has the role to do so.

![](./imgs/identity-provider/participant%20detail%20edit%20and%20add%20attribute.png)

### 6. Attribute list

From the identity attributes page, you can view all the necessary information and select the ones that need to be assigned to the participant using the checkboxes. The table shows paginated information, and the search filters are on the left.
The page can be accessed via the following link `<authority-frontend>/identity-priover/participant/:participantId/attributes`.

(i.e., a user with the **IATTR_M** role, such as the preconfigured user `m.m`)

![](./imgs/identity-provider/attribute%20list.png)

### 7. Filter attribute list

On the left, you can filter and search for a single or multiple attribute/s using the filters provided, which are attribute name and attribute code.
A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.

The page can be accessed via the following link `<authority-frontend>/identity-priover/participant/:participantId/attributes`.

(i.e., a user with the **IATTR_M** role, such as the preconfigured user `m.m`)
![](./imgs/identity-provider/filter%20attribute%20list.png)

### 8. Participant detail - credentials

From the participant details page, you can access the subsection via the tab (credentials).
In addition to all the necessary information about each credential, the credential table shows which credentials are active, highlighted with a badge (ACTIVE).
From the table, you can download (down arrow icon), revoke (trash can icon), [suspend](#10-suspend-and-reactivation-credential) (closed padlock icon), or [reactivate](#10-suspend-and-reactivation-credential) (open padlock icon) the credential.
There is no specific link, as the user accesses the feature directly from the participants page and has the role to do so.

![](./imgs/identity-provider/participant%20detail%20credential.png)

### 9. Participant detail - Filter credentials

On the left, you can filter and search for a single or multiple credential/s using the filters provided, which are credential status, issuance date range, expiration date range.
A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.
There is no specific link, as the user accesses the feature directly from the participants page and has the role to do so.

![](./imgs/identity-provider/participant%20detail%20filter%20credential.png)

### 10. Suspend and reactivation credential

To suspend credentials, you can either use the action from the table shown on the participants page ([see this section](#1-participant-list)) or click on the button (Suspend credentials) on the details page. To confirm the operation, click OK in the warning window or cancel.

![](./imgs/identity-provider/suspend%20credential.png)

To reactivate credentials, you can either use the action from the table shown on the participants page ([see this section](#1-participant-list))  or click on the button (Reactivate credentials) on the details page. To confirm the operation, click OK in the warning window or cancel.

![](./imgs/identity-provider/reactivation%20credential.png)

### 11. Revoke credential

To revoke a credential, use the Revoke credential button accessible from the participant's detail page. A warning window will open when you click the button. To continue, press OK; otherwise, cancel.

![](./imgs/identity-provider/revoke%20credential.png)

Revoke access from a table.
It is also possible to revoke credentials without viewing the participant's details, simply by clicking on the trash can icon on the participants page. A warning window will appear on the screen. Select OK to continue with the operation or cancel.

![](./imgs/identity-provider/revoke%20access%20from%20table.png)

### 12. Renew credential

To renew your credentials, go to the participant details page and click on the appropriate button (Renew credential). A window will appear on the screen. Select OK to confirm the operation or cancel.
![](./imgs/identity-provider/renew%20credential.png)

### 13. Participant detail - Auto renewal settings

Auto-renewal can be managed for each participant. Select the tab labeled “Auto-renewal settings” to access the configurator.
You can enable or disable automatic renewal using the toggle (Auto renewal enabled). When this is active, you can decide whether to use the default value for that participant or configure a custom one. By moving the second toggle (Use default settings), you tell the system to use the preconfigured setting. Conversely, by disabling the second toggle, you must enter a number of days between 0 and 1830. To confirm, click on the save button; otherwise, you can reset to the initial settings.

![](./imgs/identity-provider/participant%20detail%20auto%20renewal%20settings.png)