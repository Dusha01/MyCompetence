import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")

    cors_origins: list = ["http://localhost:5173", "http://127.0.0.1:5173", "https://dushafullstack.ru"]

    app_host: str = "127.0.0.1"
    app_port: int = 8000
    app_debug: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()