#!/bin/bash

# Integriti Quick Test Script
# Tests the API endpoints to verify functionality

echo "🧪 Testing Integriti API Endpoints..."

API_BASE="http://localhost:8000"

# Test root endpoint
echo "📍 Testing root endpoint..."
curl -s "$API_BASE/" | python -m json.tool || echo "❌ Root endpoint failed"
echo ""

# Test health check
echo "🏥 Testing health endpoint..."
curl -s "$API_BASE/health" | python -m json.tool || echo "❌ Health check failed"
echo ""

# Test detection endpoint
echo "🔍 Testing detection endpoint..."
curl -s "$API_BASE/api/v1/detect?text=This%20is%20a%20test%20message%20generated%20by%20AI" | python -m json.tool || echo "❌ Detection endpoint failed"
echo ""

# Test attribution endpoint
echo "🕵️ Testing attribution endpoint..."
curl -s "$API_BASE/api/v1/attribution?content_id=test123" | python -m json.tool || echo "❌ Attribution endpoint failed"
echo ""

# Test intelligence endpoint
echo "🌐 Testing intelligence endpoint..."
curl -s "$API_BASE/api/v1/intelligence" | python -m json.tool || echo "❌ Intelligence endpoint failed"
echo ""

# Test analytics endpoint
echo "📊 Testing analytics endpoint..."
curl -s "$API_BASE/api/v1/analytics" | python -m json.tool || echo "❌ Analytics endpoint failed"
echo ""

echo "✅ API testing complete!"
