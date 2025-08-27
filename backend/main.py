from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn

from settings import settings  # Импортируем экземпляр settings
from src.api.endpoints.forms import router as forms_router

app = FastAPI(
    title="Contact Form API",
    description="API для обработки контактных форм с отправкой в Telegram",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forms_router)

@app.get("/")
async def root():
    return {"message": "Contact Form API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.on_event("startup")
async def startup_event():
    logging.info("Starting up Contact Form API...")

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Shutting down Contact Form API...")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_debug
    )