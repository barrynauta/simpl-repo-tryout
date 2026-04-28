# Upgrade Guide

## Purpose
This guide helps to upgrade the `dagster` release from the previous one.


## Upgrade Process
1. **Read the release notes** for the target Dagster chart and code-location versions to review breaking changes and configuration updates.
2. **Backup critical components**, including:
    - Dagster PostgreSQL metadata database (if persistence is enabled).
    - Helm values files and any environment-specific configuration overrides.
3. **Update Helm dependencies** and pull the latest chart version:
   ```sh
   helm dependency update <chart-path>
   ```
4. **Upgrade the deployment** using Helm:
   ```sh
   helm upgrade dagster <chart-path> -f charts/values-<env>.yaml -n dagster
   ```
5. **Verify the rollout** to ensure all pods are updated successfully:
   ```sh
   kubectl rollout status deployment/dagster-webserver -n dagster
   kubectl rollout status deployment/dagster-daemon -n dagster
   ```
6. **Confirm code location images** are using the updated tags:
   ```sh
   kubectl get pods -n dagster
   ```
---

## Rollback Instructions
If the upgrade fails or issues are detected:
1. **Stop the service.**
2. **Install the previous version.**
3. **Restart the service.**
4. **Verify the application** is working as before.

---

## Migration Scripts
- no migration scripts required for this release.

---

## Additional Recommendations
- Test the upgrade in a staging environment before production.
- Review logs after upgrade for errors or warnings.
