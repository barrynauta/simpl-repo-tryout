# Table of contents
1. [Attribute list](#1-attribute-list)
2. [Filter attribute list](#2-filter-attribute-list)
3. [New attribute](#3-new-attribute)
4. [Edit attribute](#4-edit-attribute)
5. [Delete attribute](#5-delete-attribute)

### 1. Attribute list

Simp-Open enables comprehensive management of identity attributes that can be used in your data space.
The page dedicated to viewing and managing identity attributes can be accessed via the link `<authority-frontend>/sap/identity-attributes`.
The button for [create](#3-new-attribute) a new attribute is located at the top right.

You can view all attribute information in a paginated table. Each row will display the information. You can [Edit](#4-edit-attribute) or [Delete](#5-delete-attribute) the attribute.

(i.e., a user with the **IATTR_M** role, such as the preconfigured user `m.m`)

> **⚠️** Identity attributes are the most powerful and versatile tool at the disposal of the Dataspace Governance Authority to "design" the governance and the rules in the interactions between Dataspace participants. Some attributes are built in Simpl-Open (Built-in = true) and cannot be modified/removed. Built-in identity attributes will be available by default in every Simpl-Open dataspace and cannot be modified by the Governance Authority. The Governance Authority can add custom (not built-in) identity attributes based on specific needs.

> **⚠️** Assignable: if true means that any governance of a Participant that receives this identity attribute can assign it to any Tier 1 roles to then give it to its end users, if false means that this identity attribute is Participant wide and is to be considered as assigned to all the end users of the participant.
> 
![](./imgs/security-attribute-provider/attribute%20list.png)

### 2. Filter attribute list

The attribute page can be filtered by using the filters provided. The filters are:

- Name
- Code
- Built in

A combination of these filters will help you search more accurately for what you are looking for. To start the search, use the APPLY button, while, to clear the filters you have entered, use the RESET button.

![](./imgs/security-attribute-provider/filters%20attribute%20list.png)

### 3. New attribute

To create a new attribute, click the New attribute button at the top right.
The page dedicated to creating a new attribute can be accessed via the link `<authority-frontend>/sap/identity-attributes/new`.
Complete the form and click the SAVE button or CANCEL button to close the form.

(i.e., a user with the **IATTR_M** role, such as the preconfigured user `m.m`)

![](./imgs/security-attribute-provider/new%20attribute.png)

### 4. Edit attribute

Changing attributes is a table feature. Clicking on the pen icon transforms the table row into a row form. Change the fields and confirm with the check mark icon or cancel the changes with the x icon.
In this case, you are already authenticated with a user who can perform these operations because you are already viewing the table.

![](./imgs/security-attribute-provider/edit%20attribute.png)

### 5. Delete attribute

You can delete an attribute from the trash can icon available in the table. A confirmation message will appear on the screen, and you can confirm or cancel the operation.
In this case, you are already authenticated with a user who can perform these operations because you are already viewing the table.

![](./imgs/security-attribute-provider/delete%20attribute.png)
