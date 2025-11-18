"""
TTS Audio Processing API - Main Entry Point

Modularized production-grade application.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import get_settings
from core.dependencies import init_model_manager
from api.routes import router
from api.middleware import add_correlation_id_middleware, add_logging_middleware
from utils.logging_config import setup_logging
from utils.metrics import metrics_endpoint, update_model_metrics

# Initialize settings
settings = get_settings()

# Setup logging
setup_logging(level="INFO" if not settings.debug else "DEBUG")

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="Audio processing API with transcription, translation, and analysis capabilities",
    version="2.0.0",
    debug=settings.debug
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom middleware
add_correlation_id_middleware(app)
add_logging_middleware(app)

# Include API routes
app.include_router(router)

# Initialize models on startup
@app.on_event("startup")
async def startup_event():
    """Initialize models when the application starts."""
    import logging
    logger = logging.getLogger(__name__)
    logger.info("=" * 80)
    logger.info(f"Starting {settings.app_name}")
    logger.info("=" * 80)
    
    # Initialize model manager
    model_mgr = init_model_manager(settings)
    logger.info(f"Models initialized: {list(model_mgr.get_status().keys())}")
    
    logger.info("=" * 80)
    logger.info(f"Application ready! Running on http://{settings.host}:{settings.port}")
    logger.info(f"API docs available at http://{settings.host}:{settings.port}/docs")
    logger.info("=" * 80)


@app.get("/")
def root():
    """Root endpoint."""
    return {
        "message": "TTS Audio Processing API",
        "version": "2.0.0",
        "docs": "/docs",
        "health": "/health",
        "metrics": "/metrics"
    }


@app.get("/metrics")
def metrics():
    """Prometheus metrics endpoint."""
    from core.dependencies import get_model_manager
    model_mgr = get_model_manager()
    update_model_metrics(model_mgr)
    return metrics_endpoint()


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level="info" if not settings.debug else "debug"
    )
