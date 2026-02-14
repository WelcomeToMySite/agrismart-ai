"""
AgriSmart AI - Backend API
Main FastAPI application entry point
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="AgriSmart AI API",
    description="Intelligent Farming Assistant for Rural India",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class HealthResponse(BaseModel):
    status: str
    message: str
    version: str


class DiseaseDetectionRequest(BaseModel):
    image_base64: str
    crop_type: str
    location: dict


class DiseaseDetectionResponse(BaseModel):
    disease_name: str
    confidence: float
    treatment: str
    severity: str


# Health check endpoint
@app.get("/", response_model=HealthResponse)
async def root():
    """
    Health check endpoint
    """
    return HealthResponse(
        status="healthy",
        message="AgriSmart AI API is running",
        version="1.0.0"
    )


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Detailed health check
    """
    return HealthResponse(
        status="healthy",
        message="All systems operational",
        version="1.0.0"
    )


# Disease detection endpoint (placeholder)
@app.post("/api/v1/detect-disease", response_model=DiseaseDetectionResponse)
async def detect_disease(request: DiseaseDetectionRequest):
    """
    Detect crop disease from image
    
    Args:
        request: DiseaseDetectionRequest with image and metadata
        
    Returns:
        DiseaseDetectionResponse with diagnosis
    """
    # TODO: Implement ML model inference
    # This is a placeholder response
    return DiseaseDetectionResponse(
        disease_name="Leaf Blight",
        confidence=0.92,
        treatment="Apply fungicide spray. Remove infected leaves.",
        severity="moderate"
    )


# Weather endpoint (placeholder)
@app.get("/api/v1/weather/{location}")
async def get_weather(location: str):
    """
    Get weather forecast for location
    """
    # TODO: Integrate with weather API
    return {
        "location": location,
        "temperature": 28,
        "humidity": 65,
        "forecast": "Partly cloudy"
    }


# Market prices endpoint (placeholder)
@app.get("/api/v1/market-prices")
async def get_market_prices(crop: str = "rice", location: str = "delhi"):
    """
    Get current market prices
    """
    # TODO: Integrate with market data API
    return {
        "crop": crop,
        "location": location,
        "price": 2500,
        "unit": "per quintal",
        "trend": "stable"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
