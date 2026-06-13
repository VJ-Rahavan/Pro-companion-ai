from config import settings
from .base import BaseAIProvider
from .groq_provider import GroqProvider
from .gemini_provider import GeminiProvider


def get_provider() -> BaseAIProvider:
    """Returns the active AI provider based on the AI_PROVIDER env var."""
    if settings.ai_provider == "gemini":
        return GeminiProvider()
    return GroqProvider()
