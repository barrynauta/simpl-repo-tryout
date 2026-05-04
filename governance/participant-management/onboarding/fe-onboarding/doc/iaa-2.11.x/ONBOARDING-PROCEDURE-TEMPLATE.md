# Table of contents

1. [Define Onboarding procedure template](#1-define-Onboarding-procedure-template)
   1. [Edit an onboarding procedure template](#11-edit-onboarding-procedure-template)
2. [Onboarding procedure template - documents](#2-onboarding-procedure-template---documents)
   1. [Manage documents](#21-manage-documents)
   2. [Manage MIME types for documents](#22-manage-mime-types-for-documents)
3. [Onboarding procedure template validation rules](#3-onboarding-procedure-template-validation-rules)
   1. [Add a Rule](#31-add-a-rule)
   2. [Edit Rules](#32-edit-existing-rules)
      1. [Delete an existing rule](#321-delete-an-existing-rule)
      2. [Disable an existing rule](#322-disable-an-existing-rule)
   3. [Composite Rules](#33-composite-rules)
4. [Onboarding procedure template - identity attributes](#4-onboarding-procedure-template---identity-attributes)
   1. [Onboarding procedure template - edit identity attribute](#41-onboarding-procedure-template---edit-identity-attributes)
   2. [Onboarding procedure template - add identity attribute](#42-onboarding-procedure-template---add-identity-attributes)
   3. [Onboarding procedure template - filter identity attribute](#43-onboarding-procedure-template---filter-identity-attributes)

## 1. Define onboarding procedure template

Onboarding procedure templates act as blueprints for creating onboarding procedures for individual applicants.

You can create and manage these templates by navigating to the following link: `<authority-frontend>/onboarding/administration/management/onboarding-procedures` logging in as a user with the T2IAA_M role, such as the preconfigured user e.j@email.com.

To create a new onboarding procedure template, choose a Participant Type from the tab and click the (Define onboarding procedure template) button.

![](./imgs/onboarding/onboarding-procedure-template/define%20onboarding%20procedure%20template.png)
![](./imgs/onboarding/onboarding-procedure-template/define%20onboarding%20procedure%20template%202.png)

### 1.1 Edit onboarding procedure template

To edit an existing onboarding procedure template, click on the (Edit Template) button.

After editing the template, click on the (Save Changes) button.

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20edit.png)

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20edit%202.png)



## 2. Onboarding procedure template - documents
The documents section allows you to manage the documents that will be required for the onboarding procedures.

The documents section is available by navigating to the following link: `<authority-frontend>/onboarding/administration/management/onboarding-procedures` logging in as a user with the T2IAA_M role, such as the preconfigured user e.j@email.com.

### 2.1 manage documents
To manage documents, click on the (Edit Documents) button.
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20document.png)
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20add%20document.png)

To add your first document, click on the (Add Document) button.

The mandatory checkbox field lets you select the document as mandatory, preventing the onboarding procedure from being submitted without it.

Be aware! The rule configuration is not saved until the (Save Changes) button is clicked.
If you attempt to navigate to another section or switch to a different Participant Type, you will be notified that the configuration has not been saved.

### 2.2 Manage MIME types for documents
The MIME type drop-down list allows you to select the supported MIME type for your document. Currently, only 'application/pdf' is supported.
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20new%20document.png)


## 3. Onboarding procedure template validation rules
Validation rules are a key part of the onboarding procedure templates. They help to automatically validate documents and reduce manual effort during onboarding request review.

Onboarding procedure template validation rules can be accessed via the following link `<authority-frontend>/onboarding/administration/management/onboarding-procedures` logging in as a user with the T2IAA_M role, such as the preconfigured user e.j@email.com) 

There are three types of rules:
1. **Presence check rules**: Used to verify the presence of a document.
2. **Content check rules**: Used to validate the content of a document using external services.
3. **Composite rules**: A special type of rule that enables the logical combination (AND | OR) of the two previous types.

Rules can be:
- **Enabled**: The rule will be used in every onboarding procedure that will be created using this template.
- **Required**: The onboarding procedure will be rejected if the rule is not satisfied.
- **Autoapproved**: If the rule evaluates to true, the onboarding procedure will be automatically approved.

The composite rules **strategy** can be configured in two ways:

- **All must be valid**: Corresponds to the logical AND operator. The rule is satisfied only if **all its child rules are valid**.
- **At least one**: Corresponds to the logical OR operator. The rule is satisfied if **at least one of its child rules is valid**.

Rule can be managed from the **Rules** tab of the onboarding procedure template, clicking the (Edit rules) button.

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20edit%20rules.png)

### 3.1 Add a rule
To add a rule, click the (Add Rule) button and select the corresponding rule type.

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20add%20rule.png)
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20chose%20rule.png)

Rule data consistency is evaluated in real time, so if necessary data is missing, or there is a logical error, the rule will be marked as invalid, highlighted in red in the tree view, and the field-related error message will be shown. The save changes button will be disabled too.
Once the user has filled all the required fields, the user can click on the (Save Changes) button to save the rules' configuration.

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20add%20rule%20errors.png)

Be aware! The rule configuration is not saved until the (Save Changes) button is clicked.
If you attempt to navigate to another section or switch to a different Participant Type, you will be notified that the configuration has not been saved.

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20add%20rule%20unsaved.png)


### 3.2 Edit existing rules

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20edit%20existing%20rules.png)

To edit existing rules, click on the (Edit rules) button.

To simplify the management of existing rules, you can hide disabled rules using the Hide Disabled toggle, which also displays the total number of disabled rules in the current configuration.

As with rule creation, saving is only possible when the entire rule tree is valid.

### 3.2.1 Delete an existing rule

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20delete%20existing%20rules.png)
A rule can be deleted by clicking the (trash icon button) on the right side of the rule’s header.

However, deleting a rule **is not always possible**. A rule can only be deleted only if **it has never been included in an already generated onboarding procedure**.

If the rule cannot be deleted, the user will be notified with a message and can still disable the rule to prevent it from being used in future onboarding procedures.

### 3.2.2 Disable an existing rule

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20disable%20existing%20rules.png)
It is always possible to disable an existing rule by unchecking the (Enabled flag) from the rule itself.

However, the rule will be disabled only in future onboarding procedures created from the selected template. Therefore, the change is **not retroactive**.


### 3.3 Composite rules

Composite rules are valid when:
- They have at least two child rules
- Each of the child rules is valid

Each composite rule can have at most one other composite rule as a child, which must also comply with the rules stated above.

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20composite%20rules.png)

It is possible to add child rules to a composite rule using the (Add Child Rule) button located at the bottom-right of the interface.

To facilitate navigation between nested rules, you can click the home icon next to a child rule’s name to automatically select its parent rule in the tree.

As with content check and presence check rules, the configuration can only be saved when all rules have been properly completed.

![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20composite%20rules%202.png)





## 4. Onboarding procedure template - identity attributes
The identity attributes section allows you to manage the identity attributes that will be assigned by default to new onboarding procedures.
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20identity%20attribute.png)

### 4.1 Onboarding procedure template - edit identity attributes
To manage identity attributes, click on the (Edit attributes) button.
This action will show the (add attributes) button and eventually add the action column to the table, making it possible to remove existing attributes.
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20edit%20identity%20attribute.png)

### 4.2 Onboarding procedure template - add identity attributes
Clicking on the (Add attribute) button will open a modal that allows the user to add new identity attributes that are not already present in the list.

To save the changes, click on the (Ok) button.
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20add%20identity%20attribute.png)

### 4.3 Onboarding procedure template - filter identity attributes
Clicking on the caret icon next to the (Filters) title will open a section that allows the user to filter the list of identity attributes.

Clicking on the (Apply) button will apply the selected filters and display the list of identity attributes that match the criteria.

Clicking on the (Reset) button will reset the filters and display the paginated list of all identity attributes.
![](./imgs/onboarding/onboarding-procedure-template/onboarding%20procedure%20template%20filter%20identity%20attribute.png)