# Workflow for Managing Identity Attributes

> **Note**: In the steps below, replace `<authority fe>` with the URL of your authority front-end and `<participant fe>` with the URL of your participant front-end.

Follow these steps to manage identity attributes, from creation to assignment to a local role:

1. **Create Identity Attributes**: Use the UI `<authority fe>/sap/identity-attributes` (log in with user `m.m`). Click on `+ New Attribute`, fill out the form, select `Assignable to roles`, and then click on `Save`.

![](./imgs/identity_attributes/1-a-create-attr.png)
![](./imgs/identity_attributes/1-b-create-attr.png)
![](./imgs/identity_attributes/1-c-create-attr.png)

2. **Assign/Unassign Identity Attributes to a Participant**: Use the participant management UI `<authority fe>/onboarding/administration/management/participant` (log in with user `m.m`). After selecting the participant, click on `+ Add Attribute`, choose the desired attribute, and then click `Save`.
    ![](./imgs/identity_attributes/2-b-select-participant.png)
    ![](./imgs/identity_attributes/2-b0-add-attr.png)
    ![](./imgs/identity_attributes/2-b1-add-attr.png)
    ![](./imgs/identity_attributes/2-b2-add-attr.png)

3. **Synchronize Identity Attributes**: Go to the participant utility echo page `<participant fe>/participant-utility/echo` (log in with user `a.w`).

![](./imgs/identity_attributes/3-echo.png)

4. **Verify Identity Attributes**: Check if the expected identity attributes are listed using the identity attributes info UI `<participant fe>/users-roles/identity-attributes-info` (log in with user `t.w`).


![](./imgs/identity_attributes/4-attr-list.png)

5. **Assign Identity Attributes to Roles**: Use the users-roles UI `<participant fe>/users-roles/roles` (log in with user `t.w`). Click on the selected role, assign the desired attributes, and then click `Save`.

![](./imgs/identity_attributes/5-a-assign-to-role.png)
![](./imgs/identity_attributes/5-b-assign-to-role.png)
![](./imgs/identity_attributes/5-c-assign-to-role.png)

