#!/bin/bash
# Snake and CogWheel - Stop Script

echo "🛑 Stopping Snake and CogWheel..."

if command -v docker-compose &> /dev/null && [ -f "docker-compose.yml" ]; then
    docker-compose down
else
    docker stop snake-cogwheel 2>/dev/null || true
    docker rm snake-cogwheel 2>/dev/null || true
fi

echo "✅ Snake and CogWheel has been stopped"

