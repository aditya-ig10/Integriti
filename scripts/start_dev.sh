#!/bin/bash

# Integriti Development Server Startup Script
# This script starts the development environment

echo "🚀 Starting Integriti Development Environment..."

# Check if virtual environment exists
if [ ! -d "integriti_env" ]; then
    echo "❌ Virtual environment not found. Please run setup.sh first."
    exit 1
fi

# Activate virtual environment
source integriti_env/bin/activate

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "📋 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created. Please review and update as needed."
fi

# Start the API server
echo "🌐 Starting API server on http://localhost:8000"
echo "📚 API Documentation available at http://localhost:8000/docs"
echo "🔍 Alternative docs at http://localhost:8000/redoc"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
