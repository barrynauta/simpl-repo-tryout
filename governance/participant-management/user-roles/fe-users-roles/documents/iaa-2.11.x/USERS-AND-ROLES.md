# Table of contents
1. [Attribute list](#1-attribute-list)
2. [User list](#2-user-list)
3. [Filter users](#3-filter-users)
4. [New user](#4-new-user)
5. [User roles list](#5-user-roles-list)
6. [Role list](#6-role-list)
7. [Filter roles list](#7-filter-roles-list)
8. [Role detail](#8-role-detail)
9. [Filter role detail](#9-filter-role-detail)
10. [Appendix](#10-appendix)

### 1. Attribute list

Simpl-Open has a page dedicated to viewing identity attributes. The page can be accessed via the following link `<authority-frontend>/users-roles/identity-attributes-info`. A page will be displayed with a paginated table showing the list of attributes with various information. On the left, you can filter and search for a single or multiple attribute using the filters provided, which are name, code and date range.
A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.
(i.e., a user with the **T1UAR_M** role, such as the preconfigured user `m.f`)

![](./imgs/users-and-roles/attribute%20list.png)

### 2. User list

The user list page is accessible via the following link `<authority-frontend>/users-roles/users`. A page will be displayed with a paginated table showing the list of users with various information.
(i.e., a user with the **T1UAR_M** role, such as the preconfigured user `m.f`)

![](./imgs/users-and-roles/users%20list.png)

### 3. Filter users

The user list page can be filtered by using the filters provided. The filters are:
- First name
- Last name
- Email
- Username

a combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.

![](./imgs/users-and-roles/filters%20users%20list.png)

### 4. New user

To create a new user, use the appropriate button in the top right corner of the page (+ Create new user) or navigate to the following link `<authority-frontend>/users-roles/users/new-user`.
The screen that will be displayed is shown below. To create a new user, fill in all the required fields on the form.

The fields to be filled in are:

- Email address
- First name
- Last name
- Username
- Password
- Confirm password
- Role

(i.e., a user with the **T1UAR_M** role, such as the preconfigured user `m.f`)

![](./imgs/users-and-roles/new%20user.png)

### 5. User roles list

You can also find out which roles are associated with the user. From the table, you can use the button with the information icon User roles to display a window listing the associated roles.
There is no navigation to perform; the UI allows you to view the window. The user will have the necessary role to view the window as they can already see the table.

![](./imgs/users-and-roles/user%20detail%20roles%20list.png)

### 6. Role list

You can consult the list of roles via the link `<authority-frontend>/users-roles/roles`. A paginated table will show the list of roles with all the necessary information.
(i.e., a user with the **T1UAR_M** role, such as the preconfigured user `m.f`)

![](./imgs/users-and-roles/roles%20list.png)

### 7. Filter roles list

The role list page can be filtered by using the filters provided. The filters are:
- Name
- Description

A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.

(i.e., a user with the **T1UAR_M** role, such as the preconfigured user `m.f`)

![](./imgs/users-and-roles/filters%20role%20list.png)

### 8. Role detail

To view the details of a role, click on the eye icon in the table. A dedicated page will be displayed with the details of the role, this page is accessible via the following link `<authority-frontend>/users-roles/role/:roleId`.
A table of attributes will be displayed in the role details to show which ones are associated with that specific role.

> **⚠️** The attributes that can be assigned to a specific role are those marked as "Assignable." For more information, read the dedicated [section](./SECURITY-ATTIBUTE-PROVIDER.md#1-attribute-list).

(i.e., a user with the **T1UAR_M** role, such as the preconfigured user `m.f`)

![](./imgs/users-and-roles/role%20detail.png)

### 9. Filter role detail

The role detail page can be filtered by using the filters provided. The filters are:
- Name
- Description

A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.

(i.e., a user with the **T1UAR_M** role, such as the preconfigured user `m.f`)

![](./imgs/users-and-roles/filters%20role%20list.png)

### 10. Appendix

The following tables contain the default users available in a standard Simpl-Open installation.

#### Participants

| Email | Roles |
|-------|-------|
| a.w@email.com | ONBOARDER_M, T1UAR_M |
| t.w@email.com | T1UAR_M |
| m.b@email.com | CATALOG_R, SD_CONSUMER |
| j.r@email.com | CATALOG_R, SD_PUBLISHER |
| s.p@email.com | SERVICE_PROVIDER |

#### Authority

| Email | Roles |
|-------|-------|
| e.j@email.com | T2IAA_M |
| m.t@email.com | NOTARY |
| m.f@email.com | T1UAR_M |
| m.m@email.com | IATTR_M |
| s.d@email.com | - |

Notes:
- A dash ( - ) in the Roles column indicates that no specific role has been assigned yet.
- These accounts are intended for demonstration and testing purposes.
