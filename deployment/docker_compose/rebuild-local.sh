#!/bin/bash

# Rebuild script for local changes
# This script rebuilds only the services you'll be modifying (frontend and connectors)

set -e

echo "🔧 Rebuilding local services..."

# Function to rebuild a specific service
rebuild_service() {
    local service=$1
    echo "📦 Building $service..."
    docker-compose -f docker-compose.prod.yml build --no-cache $service
    echo "✅ $service build complete"
}

# Function to restart a service
restart_service() {
    local service=$1
    echo "🔄 Restarting $service..."
    docker-compose -f docker-compose.prod.yml up -d $service
    echo "✅ $service restarted"
}

# Parse command line arguments
case "${1:-all}" in
    "web"|"frontend")
        echo "🎨 Rebuilding frontend only..."
        rebuild_service web_server
        restart_service web_server
        ;;
    "api"|"backend"|"connectors")
        echo "🔌 Rebuilding backend services for connectors..."
        rebuild_service api_server
        rebuild_service background
        restart_service api_server
        restart_service background
        ;;
    "all")
        echo "🚀 Rebuilding all local services..."
        rebuild_service web_server
        rebuild_service api_server
        rebuild_service background
        
        echo "🔄 Restarting all services..."
        docker-compose -f docker-compose.prod.yml up -d web_server api_server background
        ;;
    *)
        echo "❌ Usage: $0 [web|api|all]"
        echo "  web/frontend   - Rebuild only frontend"
        echo "  api/backend/connectors - Rebuild only backend services"
        echo "  all            - Rebuild all local services (default)"
        exit 1
        ;;
esac

echo "🎉 Rebuild complete!"
echo "📡 Your changes are now live on seekdeeper.ai" 