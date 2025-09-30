"""
Integriti Main Application Entry Point
AI-Driven National Security Defense Platform
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
import uvicorn
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    logger.info("🚀 Integriti Platform Starting...")
    logger.info("🔒 Initializing Security Modules...")
    logger.info("🤖 Loading AI Detection Models...")
    logger.info("🌐 Connecting to Graph Database...")
    logger.info("📊 Setting up Analytics Pipeline...")
    
    yield
    
    # Shutdown
    logger.info("🛑 Integriti Platform Shutting Down...")


# Create FastAPI application
app = FastAPI(
    title="Integriti - AI National Security Defense Platform",
    description="""
    **Integriti** is a comprehensive AI-driven platform designed to detect, analyze, 
    and mitigate the misuse of Large Language Models (LLMs) in hostile information operations.
    
    ## Core Capabilities
    
    * **🔍 Real-Time Detection** - AI-generated content detection with >90% accuracy
    * **🕵️ Attribution & Forensics** - Trace content to source models and operators  
    * **🌐 Graph Intelligence** - Map disinformation networks using Graph Neural Networks
    * **🤝 International Sharing** - Federated intelligence sharing protocols
    * **📊 Predictive Analytics** - Proactive threat anticipation and risk assessment
    * **🛡️ Privacy-Preserving** - Built-in privacy protection and compliance
    
    ## API Endpoints
    
    This API provides access to all core platform capabilities for authorized users.
    """,
    version="0.1.0",
    contact={
        "name": "Integriti Team",
        "email": "team@integriti.ai"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    lifespan=lifespan
)

# Add security middleware
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=["localhost", "127.0.0.1", "*.integriti.ai"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["System"])
async def root() -> Dict[str, Any]:
    """Platform status and information"""
    return {
        "platform": "Integriti",
        "version": "0.1.0",
        "status": "operational",
        "mission": "Defending Democracy Through Intelligent Detection",
        "capabilities": [
            "LLM Content Detection",
            "Attribution & Forensics", 
            "Graph-Based Intelligence",
            "International Sharing",
            "Predictive Analytics",
            "Privacy-Preserving Analytics"
        ]
    }


@app.get("/health", tags=["System"])
async def health_check() -> Dict[str, str]:
    """System health check"""
    return {
        "status": "healthy",
        "timestamp": "2025-09-30T12:00:00Z",
        "services": "operational"
    }


@app.get("/api/v1/detect", tags=["Detection"])
async def detect_content(text: str) -> Dict[str, Any]:
    """
    Detect if content is AI-generated
    
    **Early Development Version** - Returns mock responses for testing
    """
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text content required")
    
    # Mock response for development
    return {
        "text": text[:100] + "..." if len(text) > 100 else text,
        "ai_generated": True if len(text) > 50 else False,
        "confidence": 0.92,
        "model_family": "GPT-based" if "AI" in text else "Unknown",
        "analysis": {
            "stylometric_score": 0.87,
            "semantic_score": 0.94,
            "statistical_score": 0.89
        },
        "status": "development_mode"
    }


@app.get("/api/v1/attribution", tags=["Attribution"])
async def analyze_attribution(content_id: str) -> Dict[str, Any]:
    """
    Perform forensic attribution analysis
    
    **Early Development Version** - Returns mock responses for testing
    """
    if not content_id:
        raise HTTPException(status_code=400, detail="Content ID required")
    
    # Mock response for development
    return {
        "content_id": content_id,
        "attribution_confidence": 0.85,
        "likely_source": "Advanced LLM System",
        "watermark_detected": False,
        "fingerprint_match": "Partial",
        "threat_actor": "Unknown",
        "status": "development_mode"
    }


@app.get("/api/v1/intelligence", tags=["Intelligence"])
async def get_threat_intelligence() -> Dict[str, Any]:
    """
    Get current threat intelligence summary
    
    **Early Development Version** - Returns mock responses for testing
    """
    return {
        "active_campaigns": 15,
        "threat_level": "moderate",
        "new_actors_detected": 3,
        "platforms_monitored": 8,
        "detection_rate": "94.2%",
        "last_updated": "2025-09-30T12:00:00Z",
        "status": "development_mode"
    }


@app.get("/api/v1/analytics", tags=["Analytics"])
async def get_analytics_dashboard() -> Dict[str, Any]:
    """
    Get analytics dashboard data
    
    **Early Development Version** - Returns mock responses for testing
    """
    return {
        "daily_detections": 1247,
        "accuracy_rate": 94.2,
        "false_positive_rate": 1.8,
        "processing_latency_ms": 89,
        "active_threats": 23,
        "mitigated_threats": 187,
        "status": "development_mode"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
