from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    ai_provider: Literal["groq", "gemini"] = "groq"
    groq_api_key: str = ""
    gemini_api_key: str = ""
    port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
