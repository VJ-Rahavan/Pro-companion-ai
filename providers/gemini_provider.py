import google.generativeai as genai
from .base import BaseAIProvider
from config import settings


class GeminiProvider(BaseAIProvider):
    def __init__(self):
        genai.configure(api_key=settings.gemini_api_key)
        self._model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        combined = f"{system_prompt}\n\n{user_prompt}"
        response = await self._model.generate_content_async(combined)
        return response.text or ""
