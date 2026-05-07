# Upgrade Guide

## Version Compatibility
- This guide covers upgrades between major and minor versions of the project.

## Backup
- Before upgrading, back up the `files` folder and any custom configurations.

## Upgrade Procedure
1. Stop the existing nginx container:
   ```sh
   docker stop <container-id>
   docker rm <container-id>
   ```
2. Update the code:
   ```sh
   git pull origin <branch>
   ```
3. Rebuild and restart the container:
   ```sh
   docker build -t simpl-nginx .
   docker run -d -p 80:80 -v $(pwd)/files:/usr/share/nginx/html:ro simpl-nginx
   ```

## Breaking Changes
- Change the `service.port` in **values.yaml** to update both internal and external service ports. If not set, the default value is **80**.

## Rollback
- If issues occur, restore the backup and restart the previous container version.
