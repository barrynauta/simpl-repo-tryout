# Field-Level Pseudo-Anonymisation - Upgrade Guide

## Purpose

This guide describes the minimal steps required to upgrade this code location to a new release.

## Upgrade Process

1. **Read the release notes** for the code-location to review breaking changes and configuration updates.
2. **Build the new Docker image**, the CI/CD pipeline automatically builds and publishes the updated image when changes are pushed.
3. **Update the image tag** in the Dagster values.yaml file.
This triggers the Dagster deployment (via Helm/ArgoCD) to pull the new image and roll out the update.

Once the image tag is updated, the code location will be automatically redeployed.

## Rollback Instructions

If the upgrade fails or issues are detected:

1. **Restore the previous image tag** in the Dagster values.yaml file.
2. **Commit and push the change,** letting ArgoCD or Helm apply the previous version.
3. **Verify** that the code location is running correctly.

---

## Migration Scripts

- No migration scripts required for this release.

---

## Additional Recommendations

- Test the upgrade in a staging environment before production.
- Review logs after upgrade for errors or warnings.
