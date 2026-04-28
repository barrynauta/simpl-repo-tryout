# Upgrade guide

## Upgrade to v2.9.x

No relevant changes are made on charts in this version, so it is enough to upgrade the version via helm upgrade.

## Upgrade to v2.8.x

No relevant changes are made on charts in this version, so it is enough to upgrade the version via helm upgrade:

```bash
helm upgrade identity-provider identity-provider-charts/identity-provider \
--version 2.8.0 \
--values values.yaml
```

## Upgrade up to version 2.7
For upgrades prior to version 2.7, please refer to the 'UPGRADING.md' file in the appropriate version of the 'version_docs' (https://code.europa.eu/simpl/simpl-open/development/iaa/documentation/-/tree/main/versioned_docs) folder within the central documentation repository.
