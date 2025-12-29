# Docker Quick Start Guide

**Purpose:** Essential Docker commands and patterns for Stratega operations
**Focus:** Running and debugging n8n and other services

---

## Core Concepts

```
Image   = Blueprint (immutable template)
Container = Running instance of an image
Volume  = Persistent storage (survives container restart)
Network = How containers communicate
```

---

## Essential Commands

### Container Management

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Start a container
docker start container_name

# Stop a container
docker stop container_name

# Restart a container
docker restart container_name

# Remove a container (must be stopped)
docker rm container_name

# Force remove (even if running)
docker rm -f container_name
```

### Viewing Logs

```bash
# View logs
docker logs container_name

# Follow logs (live)
docker logs -f container_name

# Last 100 lines
docker logs --tail 100 container_name

# With timestamps
docker logs -t container_name

# Logs since specific time
docker logs --since 1h container_name
```

### Execute Commands in Container

```bash
# Interactive shell
docker exec -it container_name sh
docker exec -it container_name bash

# Run single command
docker exec container_name ls /home/node
docker exec container_name cat /home/node/.n8n/config

# As specific user
docker exec -u root container_name command
```

### Images

```bash
# List images
docker images

# Pull latest image
docker pull n8nio/n8n:latest

# Remove image
docker rmi image_name
```

---

## Docker Compose

### Basic Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# Restart all services
docker-compose restart

# Restart specific service
docker-compose restart n8n

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f n8n

# Rebuild after changes
docker-compose up -d --build

# Pull latest images and restart
docker-compose pull && docker-compose up -d
```

### docker-compose.yml Anatomy

```yaml
# Your n8n compose file explained
services:
  n8n:
    image: n8nio/n8n:latest          # Image to use
    container_name: n8n-production   # Name for the container
    restart: unless-stopped          # Auto-restart policy
    ports:
      - "5678:5678"                   # Host:Container port mapping
    environment:
      # Configuration via environment variables
      N8N_HOST: "n8n.pickeat.cc"
      N8N_PROTOCOL: "https"
      N8N_PORT: "5678"
    volumes:
      # Persistent storage
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:                          # Named volume definition
```

---

## Debugging Workflows

### Container Won't Start

```bash
# 1. Check logs for errors
docker logs n8n-production

# 2. Check container status
docker ps -a | grep n8n

# 3. Try starting manually with verbose output
docker-compose up (without -d)

# 4. Check resource usage
docker stats
```

### Application Errors

```bash
# 1. Enter container
docker exec -it n8n-production sh

# 2. Check n8n files
ls -la /home/node/.n8n/

# 3. Check config
cat /home/node/.n8n/config

# 4. Check permissions
ls -la /home/node/
```

### Network Issues

```bash
# List networks
docker network ls

# Inspect network
docker network inspect bridge

# Check container network
docker inspect n8n-production | grep -A 20 "Networks"
```

### Disk Space Issues

```bash
# Check disk usage
docker system df

# Clean up unused resources
docker system prune

# Clean up everything (careful!)
docker system prune -a --volumes
```

---

## Common n8n Operations

### Backup n8n Data

```bash
# Create backup directory
mkdir -p ~/backups/n8n

# Copy volume data (while running)
docker cp n8n-production:/home/node/.n8n ~/backups/n8n/$(date +%Y%m%d)

# Or stop, backup, start
docker-compose stop
cp -r /var/lib/docker/volumes/n8n_data/_data ~/backups/n8n/$(date +%Y%m%d)
docker-compose start
```

### Restore n8n Data

```bash
# Stop n8n
docker-compose stop

# Copy backup to volume
docker cp ~/backups/n8n/20241126/. n8n-production:/home/node/.n8n/

# Start n8n
docker-compose start
```

### Update n8n

```bash
# Navigate to compose directory
cd ~/n8n-compose

# Pull latest image
docker-compose pull

# Recreate container with new image
docker-compose up -d

# Verify version
docker exec n8n-production n8n --version
```

### Export Workflows

```bash
# Export all workflows to file
docker exec n8n-production n8n export:workflow --all > workflows_backup.json

# Export specific workflow
docker exec n8n-production n8n export:workflow --id="workflow_id" > workflow.json
```

### Import Workflows

```bash
# Import workflow from file
docker cp workflow.json n8n-production:/tmp/
docker exec n8n-production n8n import:workflow --input=/tmp/workflow.json
```

---

## Environment Variables

### View Container Environment

```bash
# See all env vars
docker exec n8n-production env

# Check specific variable
docker exec n8n-production printenv N8N_HOST
```

### Modify Environment

Edit `docker-compose.yml`:

```yaml
environment:
  NEW_VARIABLE: "value"
```

Then restart:

```bash
docker-compose up -d
```

---

## Volume Management

### List Volumes

```bash
docker volume ls
```

### Inspect Volume

```bash
docker volume inspect n8n_data
```

### Backup Volume

```bash
# Create tarball
docker run --rm -v n8n_data:/data -v $(pwd):/backup alpine tar czf /backup/n8n_backup.tar.gz /data
```

### Restore Volume

```bash
# Restore from tarball
docker run --rm -v n8n_data:/data -v $(pwd):/backup alpine tar xzf /backup/n8n_backup.tar.gz -C /
```

---

## Health Monitoring Script

```bash
#!/bin/bash
# save as check_n8n.sh

CONTAINER="n8n-production"

if docker ps | grep -q $CONTAINER; then
    echo "✅ $CONTAINER is running"

    # Check n8n health endpoint
    if curl -s http://localhost:5678/healthz > /dev/null; then
        echo "✅ n8n health check passed"
    else
        echo "❌ n8n health check failed"
    fi
else
    echo "❌ $CONTAINER is not running"
    echo "Starting container..."
    docker start $CONTAINER
fi
```

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Start | `docker-compose up -d` |
| Stop | `docker-compose down` |
| Restart | `docker-compose restart` |
| Logs | `docker-compose logs -f` |
| Shell | `docker exec -it n8n-production sh` |
| Status | `docker ps` |
| Update | `docker-compose pull && docker-compose up -d` |
| Backup | `docker cp n8n-production:/home/node/.n8n ~/backup/` |

---

## Troubleshooting Checklist

### n8n Not Accessible

1. [ ] Is container running? `docker ps`
2. [ ] Check logs for errors: `docker logs n8n-production`
3. [ ] Is port exposed? `docker port n8n-production`
4. [ ] Is firewall blocking? Check ufw/iptables
5. [ ] Is reverse proxy working? Check Cloudflare tunnel

### Workflows Not Running

1. [ ] Check n8n logs: `docker logs -f n8n-production`
2. [ ] Check workflow execution history in n8n UI
3. [ ] Check credentials are valid
4. [ ] Check webhook URLs are correct
5. [ ] Check external service status

### Data Lost After Restart

1. [ ] Volume mounted correctly? Check docker-compose.yml
2. [ ] Volume exists? `docker volume ls`
3. [ ] Permissions issue? Check with `docker exec -it container ls -la /home/node/.n8n`

---

*Quick Reference v1.0 - Essential Docker for Stratega operations*
