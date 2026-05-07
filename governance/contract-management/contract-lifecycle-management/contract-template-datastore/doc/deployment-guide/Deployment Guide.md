# Deployment Guide

## Environment Requirements
- Infrastructure: server with Docker
- OS: Windows, Linux, macOS
- Permissions: administrator access for Docker

## Configuration
- No environment variables required for the basic version
- Files to be exposed should be placed in the `files` folder

## Deployment Procedure
1. Build the Docker image:
   ```sh
   docker build -t simpl-nginx .
   ```
2. Start the container:
   ```sh
   docker run -d -p 80:80 -v $(pwd)/files:/usr/share/nginx/html:ro simpl-nginx
   ```
   On Windows:
   ```bat
   docker run -d -p 80:80 -v %cd%\files:/usr/share/nginx/html:ro simpl-nginx
   ```

## Scaling and Monitoring
- To scale, start multiple containers and use a load balancer (e.g., nginx, traefik)
- Monitoring: check container status with `docker ps`

## Security
- Expose only the necessary port
- Protect access to sensitive files

## Rollback and Recovery
- In case of error, stop the container and restore the previous version
