# Upgrade Guide

## Purpose
This guide helps to upgrade the `asset-orchestrator` service from one version to another, ensuring a smooth transition with minimal downtime and data integrity.

---

## Pre-Upgrade Checklist

Before starting the upgrade process:

- [ ] Review the release notes for the target version
- [ ] Backup the database (see Backup section below)
- [ ] Test the upgrade in a staging/development environment
- [ ] Verify all dependencies are compatible (Dagster, PostgreSQL, Vault)
- [ ] Schedule a maintenance window for production upgrades
- [ ] Notify stakeholders about the planned upgrade
- [ ] Ensure rollback plan is in place

---

## Breaking Changes

### Version 1.0.0 → 2.0.0 (Future)
- No breaking changes planned for initial releases
- Any future breaking changes will be documented here

### Version 0.x → 1.0.0
- Initial stable release
- Database schema migrations handled automatically by Flyway
- No manual migration steps required

---

## Backup Procedures

### 1. Database Backup

**PostgreSQL Backup:**
```bash
# Full database backup
pg_dump -h <DB_HOST> \
        -U <DB_USER> \
        -d orchestration_platform \
        -n asset-orchestrator \
        -F c \
        -f asset-orchestrator-backup-$(date +%Y%m%d-%H%M%S).dump

# SQL format backup (human-readable)
pg_dump -h <DB_HOST> \
        -U <DB_USER> \
        -d orchestration_platform \
        -n asset-orchestrator \
        --clean --if-exists \
        > asset-orchestrator-backup-$(date +%Y%m%d-%H%M%S).sql
```

**Kubernetes PostgreSQL Backup:**
```bash
# Backup from Kubernetes pod
kubectl exec -n common pg-cluster-0 -- \
  pg_dump -U postgres \
          -d orchestration_platform \
          -n asset-orchestrator \
          > asset-orchestrator-backup.sql
```

### 2. Configuration Backup

```bash
# Backup Helm values
helm get values asset-orchestrator -n dataorchestrator > values-backup.yaml

# Backup Kubernetes resources
kubectl get deployment asset-orchestrator -n dataorchestrator -o yaml > deployment-backup.yaml
kubectl get service asset-orchestrator -n dataorchestrator -o yaml > service-backup.yaml
kubectl get configmap -n dataorchestrator -l app=asset-orchestrator -o yaml > configmap-backup.yaml
```

### 3. Vault Secrets Backup

```bash
# Export Vault secrets (requires appropriate permissions)
vault kv get -format=json asset-orchestrator/database > vault-database-backup.json
vault kv get -format=json asset-orchestrator/otel > vault-otel-backup.json
```

---

## Upgrade Process

### A. Docker Upgrade

1. **Stop the running container:**
   ```bash
   docker stop asset-orchestrator
   docker rm asset-orchestrator
   ```

2. **Pull the new image:**
   ```bash
   docker pull <registry>/asset-orchestrator:<new-version>
   ```

3. **Run the new version:**
   ```bash
   docker run -d \
     --name asset-orchestrator \
     -p 8080:8080 \
     -e DB_HOST=postgres \
     -e DB_PORT=5432 \
     -e DB_NAME=orchestration_platform \
     -e DB_USER=postgres \
     -e DB_PWD=<password> \
     -e DAGSTER_GRAPHQL_URL=http://dagster:3000/dagster/graphql \
     <registry>/asset-orchestrator:<new-version>
   ```

4. **Verify the upgrade:**
   ```bash
   docker logs -f asset-orchestrator
   curl http://localhost:8080/actuator/health
   ```

### B. Kubernetes Upgrade (Helm)

1. **Update Helm repository:**
   ```bash
   helm repo update
   ```

2. **Review the changes:**
   ```bash
   helm diff upgrade asset-orchestrator <chart-path> \
     -n dataorchestrator \
     -f values.yaml
   ```

3. **Perform the upgrade:**
   ```bash
   helm upgrade asset-orchestrator <chart-path> \
     -n dataorchestrator \
     -f values.yaml \
     --atomic \
     --timeout 5m
   ```

   > **Note**: The `--atomic` flag ensures automatic rollback on failure.

4. **Monitor the upgrade:**
   ```bash
   # Watch pod status
   kubectl get pods -n dataorchestrator -l app.kubernetes.io/name=asset-orchestrator -w
   
   # Check rollout status
   kubectl rollout status deployment/asset-orchestrator -n dataorchestrator
   
   # View logs
   kubectl logs -n dataorchestrator -l app.kubernetes.io/name=asset-orchestrator -f
   ```

5. **Verify the upgrade:**
   ```bash
   # Check health
   kubectl exec -n dataorchestrator deployment/asset-orchestrator -- \
     curl http://localhost:8080/actuator/health
   
   # Check version
   kubectl get deployment asset-orchestrator -n dataorchestrator -o jsonpath='{.spec.template.spec.containers[0].image}'
   ```

### C. Kubernetes Upgrade (kubectl)

1. **Update the image tag:**
   ```bash
   kubectl set image deployment/asset-orchestrator \
     asset-orchestrator=<registry>/asset-orchestrator:<new-version> \
     -n dataorchestrator
   ```

2. **Monitor the rollout:**
   ```bash
   kubectl rollout status deployment/asset-orchestrator -n dataorchestrator
   ```

### D. ArgoCD Upgrade

1. **Update the image tag in Git:**
   ```yaml
   # In values.yaml or deployment manifest
   image:
     repository: <registry>/asset-orchestrator
     tag: "<new-version>"
   ```

2. **Commit and push:**
   ```bash
   git add values.yaml
   git commit -m "chore: upgrade asset-orchestrator to <new-version>"
   git push
   ```

3. **Sync in ArgoCD:**
   ```bash
   # Manual sync via CLI
   argocd app sync asset-orchestrator
   
   # Or enable auto-sync in ArgoCD UI
   ```

4. **Monitor in ArgoCD UI:**
   - Navigate to the application
   - Watch the sync progress
   - Verify health status

---

## Database Migration

Database migrations are handled automatically by Flyway on application startup.

### Manual Migration Verification

1. **Check current schema version:**
   ```sql
   SELECT installed_rank, version, description, success 
   FROM "asset-orchestrator".flyway_schema_history 
   ORDER BY installed_rank DESC;
   ```

2. **Review pending migrations:**
   ```bash
   # In the application logs, look for:
   # "Migrating schema `asset-orchestrator` to version X.Y.Z"
   ```

3. **Manually apply migrations (if needed):**
   ```bash
   # This should rarely be necessary as Flyway runs automatically
   mvn flyway:migrate -Dflyway.url=jdbc:postgresql://<host>:5432/orchestration_platform \
                      -Dflyway.user=<username> \
                      -Dflyway.password=<password> \
                      -Dflyway.schemas=asset-orchestrator
   ```

---

## Post-Upgrade Verification

### 1. Health Checks

```bash
# Liveness
curl http://<service-url>/actuator/health/liveness

# Readiness
curl http://<service-url>/actuator/health/readiness

# Full health
curl http://<service-url>/actuator/health
```

Expected response:
```json
{
  "status": "UP",
  "components": {
    "db": {"status": "UP"},
    "diskSpace": {"status": "UP"},
    "ping": {"status": "UP"}
  }
}
```

### 2. API Functionality Tests

```bash
# Test catalog asset creation
curl -X POST http://<service-url>/v1/catalog-assets \
  -H "Content-Type: application/json" \
  -d '{"originalId": "upgrade-test-001"}'

# Test catalog asset retrieval
curl http://<service-url>/v1/catalog-assets

# Test Dagster integration
curl -X POST http://<service-url>/v1/dagster/validate-job-config \
  -H "Content-Type: application/json" \
  -d '{
    "repositoryName": "test",
    "codeLocation": "test",
    "jobName": "test",
    "configYaml": "ops:\n  test_op:\n    config:\n      value: 1"
  }'
```

### 3. Integration Tests

```bash
# Run integration test suite
mvn verify -Pintegration-tests

# Or using kubectl for in-cluster tests
kubectl run test-pod --rm -i --tty \
  --image=curlimages/curl \
  --restart=Never \
  -- curl http://asset-orchestrator.dataorchestrator.svc.cluster.local:8080/actuator/health
```

### 4. Monitoring Checks

- **Logs**: Review application logs for errors or warnings
  ```bash
  kubectl logs -n dataorchestrator -l app=asset-orchestrator --tail=100
  ```

- **Metrics**: Check Prometheus/Grafana dashboards
  - JVM heap usage
  - HTTP request rates
  - Database connection pool
  - API response times

- **Traces**: Verify OpenTelemetry traces in your observability platform

---

## Rollback Instructions

### A. Helm Rollback

```bash
# List release history
helm history asset-orchestrator -n dataorchestrator

# Rollback to previous version
helm rollback asset-orchestrator -n dataorchestrator

# Rollback to specific revision
helm rollback asset-orchestrator <revision-number> -n dataorchestrator

# Verify rollback
kubectl get pods -n dataorchestrator -l app=asset-orchestrator
```

### B. Kubectl Rollback

```bash
# Undo deployment
kubectl rollout undo deployment/asset-orchestrator -n dataorchestrator

# Rollback to specific revision
kubectl rollout undo deployment/asset-orchestrator \
  --to-revision=<revision-number> \
  -n dataorchestrator

# Check rollout status
kubectl rollout status deployment/asset-orchestrator -n dataorchestrator
```

### C. Database Rollback

If database migration causes issues:

```bash
# Restore from backup
psql -h <DB_HOST> \
     -U <DB_USER> \
     -d orchestration_platform \
     < asset-orchestrator-backup.sql

# Or using pg_restore for custom format
pg_restore -h <DB_HOST> \
           -U <DB_USER> \
           -d orchestration_platform \
           -n asset-orchestrator \
           --clean --if-exists \
           asset-orchestrator-backup.dump
```

### D. ArgoCD Rollback

```bash
# Via CLI
argocd app rollback asset-orchestrator <revision-number>

# Or revert Git commit
git revert <commit-hash>
git push
argocd app sync asset-orchestrator
```

---

## Migration Scripts

### Version-Specific Migrations

#### Version 1.0.0
- **Database Migrations**: Automatically applied by Flyway
  - `V1__init_db.sql`: Initial schema creation
  - Tables: `catalog_asset`, `dagster_workflow`, `workflow_catalog_asset`, `workflow_catalog_asset_run`
- **Configuration Changes**: None
- **Manual Steps**: None required

#### Future Versions
- Migration scripts will be documented here as they are released
- Flyway automatically applies all pending migrations in order

### Custom Migration Scripts

If manual data migration is required:

```sql
-- Example: Migrate data from old structure to new (if applicable)
-- This is a template and should be customized based on actual migration needs

BEGIN;

-- Backup existing data
CREATE TEMP TABLE catalog_asset_backup AS 
SELECT * FROM "asset-orchestrator".catalog_asset;

-- Perform migration
-- (Migration logic here)

-- Verify migration
-- (Verification queries here)

COMMIT;
```

---

## Known Issues and Workarounds

### Issue: Flyway Migration Timeout

**Symptom**: Application fails to start with Flyway timeout error

**Workaround**:
```yaml
# Increase timeout in values.yaml
env:
  - name: SPRING_FLYWAY_CONNECT_RETRIES
    value: "10"
  - name: SPRING_FLYWAY_CONNECT_RETRIES_INTERVAL
    value: "30"
```

### Issue: Vault Authentication Failure After Upgrade

**Symptom**: Pod cannot authenticate with Vault

**Workaround**:
1. Verify ServiceAccount exists: `kubectl get sa asset-orchestrator -n dataorchestrator`
2. Check Vault role: `vault read auth/kubernetes/role/asset-orchestrator`
3. Restart the pod: `kubectl delete pod -n dataorchestrator -l app=asset-orchestrator`

### Issue: Database Connection Pool Exhausted

**Symptom**: `HikariPool-1 - Connection is not available` errors

**Workaround**:
```yaml
# Increase pool size in values.yaml
env:
  - name: SPRING_DATASOURCE_HIKARI_MAXIMUM_POOL_SIZE
    value: "20"
  - name: SPRING_DATASOURCE_HIKARI_MINIMUM_IDLE
    value: "10"
```

---

## Additional Recommendations

### Pre-Production Checklist

- [ ] Test upgrade in development environment
- [ ] Test upgrade in staging environment with production-like data
- [ ] Perform load testing after upgrade in staging
- [ ] Verify all integrations (Dagster, Vault, OpenTelemetry)
- [ ] Review and update monitoring alerts
- [ ] Prepare communication plan for stakeholders

### Best Practices

1. **Blue-Green Deployment**: Consider running both old and new versions temporarily
2. **Canary Releases**: Gradually roll out to a subset of pods
3. **Feature Flags**: Use feature toggles for risky changes
4. **Observability**: Ensure comprehensive logging and monitoring
5. **Documentation**: Update runbooks with new version specifics

### Maintenance Window Planning

Recommended maintenance window duration:
- **Development**: 15-30 minutes
- **Staging**: 30-45 minutes
- **Production**: 1-2 hours (including buffer for issues)

Typical upgrade timeline:
1. Pre-upgrade checks: 10 minutes
2. Backup: 5-10 minutes
3. Upgrade execution: 5-10 minutes
4. Post-upgrade verification: 15-20 minutes
5. Monitoring period: 30-60 minutes

---

## Support and Escalation

If you encounter issues during the upgrade:

1. **Check application logs**:
   ```bash
   kubectl logs -n dataorchestrator -l app=asset-orchestrator --tail=200
   ```

2. **Review database logs**:
   ```bash
   kubectl logs -n common pg-cluster-0 --tail=100
   ```

3. **Check Vault status**:
   ```bash
   vault status
   kubectl logs -n default vault-0
   ```

4. **Contact support**:
   - Email: simpl-support@ec.europa.eu
   - Slack: #asset-orchestrator-support
   - Create issue: https://code.europa.eu/simpl/data-orchestrator/asset-orchestrator/issues

5. **Emergency rollback**: Follow rollback instructions above

---

## Version History

| Version | Release Date | Key Changes | Breaking Changes |
|---------|--------------|-------------|------------------|
| 1.0.0   | 2025-12-01   | Initial release | None |
| 0.9.0   | 2025-11-15   | Beta release | None |

---

## References

- [Release Notes](../release-notes/)
- [Deployment Guide](../deployment-guide/deployment-guide.md)
- [Installation Guide](../installation-guide/installation-guide.md)
- [Helm Documentation](https://helm.sh/docs/)
- [Flyway Documentation](https://flywaydb.org/documentation/)
- [Kubernetes Rolling Update Documentation](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
