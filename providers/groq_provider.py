from groq import AsyncGroq
from .base import BaseAIProvider
from config import settings


class GroqProvider(BaseAIProvider):
    def __init__(self):
        self._client = AsyncGroq(api_key=settings.groq_api_key)

    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        response = await self._client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
            max_tokens=2048,
        )
        return response.choices[0].message.content or ""
