#!/bin/bash
# Snake and CogWheel - Easy Startup Script

set -e

echo "🐍⚙️  Snake and CogWheel - Ansible Playbook Runner"
echo "=================================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed"
    echo "Please install Docker first:"
    echo "  Ubuntu/Debian: sudo apt-get install docker.io docker-compose"
    echo "  RHEL/CentOS:   sudo yum install docker docker-compose"
    echo "  macOS:         brew install docker docker-compose"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Error: Docker is not running"
    echo "Please start Docker:"
    echo "  Linux: sudo systemctl start docker"
    echo "  macOS/Windows: Start Docker Desktop"
    exit 1
fi

echo "✅ Docker is installed and running"
echo ""

# Check if docker-compose is available
if command -v docker-compose &> /dev/null; then
    echo "🚀 Starting Snake and CogWheel with docker-compose..."
    docker-compose up -d
else
    echo "🚀 Starting Snake and CogWheel with docker..."
    
    # Build the image if it doesn't exist
    if ! docker images | grep -q snake-cogwheel; then
        echo "📦 Building Docker image (first time only)..."
        docker build -t snake-cogwheel .
    fi
    
    # Stop and remove existing container if it exists
    if docker ps -a | grep -q snake-cogwheel; then
        echo "🧹 Removing old container..."
        docker stop snake-cogwheel 2>/dev/null || true
        docker rm snake-cogwheel 2>/dev/null || true
    fi
    
    # Run the container
    docker run -d -p 5000:5000 --name snake-cogwheel snake-cogwheel
fi

echo ""
echo "✅ Snake and CogWheel is now running!"
echo ""
echo "🌐 Access the application:"
echo "   http://localhost:5000"
echo ""
echo "📋 Useful commands:"
echo "   View logs:    docker logs -f snake-cogwheel"
echo "   Stop app:     docker stop snake-cogwheel"
echo "   Restart app:  docker restart snake-cogwheel"
echo ""
echo "Press Ctrl+C to view logs (app will keep running)"
echo ""

# Wait a moment for container to start
sleep 2

# Show logs
docker logs -f snake-cogwheel

