# Local Development Workflow

This setup ensures that your frontend changes and connector additions are always built from your local source code, rather than using pre-built Docker images.

## Configuration Changes

The following services now build from local source:
- **web_server** - Frontend changes (React/Next.js)
- **api_server** - Backend/connector changes
- **background** - Background processing/connector changes

## Quick Rebuild Script

Use the `rebuild-local.sh` script for efficient rebuilds:

```bash
# Rebuild only frontend (fastest)
./rebuild-local.sh web

# Rebuild only backend/connectors
./rebuild-local.sh api

# Rebuild everything (slower but complete)
./rebuild-local.sh all
```

## Typical Development Workflow

### For Frontend Changes:
1. Make changes to files in `onyx/web/`
2. Run: `./rebuild-local.sh web`
3. Changes are live on seekdeeper.ai

### For Connector Changes:
1. Make changes to files in `onyx/backend/`
2. Run: `./rebuild-local.sh api`
3. Changes are live on seekdeeper.ai

### For Major Changes:
1. Make your changes
2. Run: `./rebuild-local.sh all`
3. Changes are live on seekdeeper.ai

## Manual Commands

If you prefer manual control:

```bash
# Build specific service
docker-compose -f docker-compose.prod.yml build --no-cache web_server

# Restart specific service
docker-compose -f docker-compose.prod.yml up -d web_server

# View logs
docker-compose -f docker-compose.prod.yml logs -f web_server
```

## Benefits of This Setup

✅ **Always uses your local code** - No accidentally using old Docker Hub images
✅ **Faster iteration** - Only rebuild what you changed
✅ **Production deployment** - Your changes go live immediately
✅ **Reliable builds** - No caching issues with external images

## Services That Still Use Pre-built Images

These services continue to use stable pre-built images (you typically won't modify these):
- `relational_db` (PostgreSQL)
- `index` (Vespa search)
- `nginx` (Reverse proxy)
- `cache` (Redis)
- `minio` (Object storage)
- `certbot` (SSL certificates)
- `inference_model_server` (ML models)
- `indexing_model_server` (ML models)

## Troubleshooting

If you run into issues:
1. Check logs: `docker-compose -f docker-compose.prod.yml logs -f SERVICE_NAME`
2. Rebuild from scratch: `./rebuild-local.sh all`
3. Check container status: `docker-compose -f docker-compose.prod.yml ps` 