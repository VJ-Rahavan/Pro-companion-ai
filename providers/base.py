from abc import ABC, abstractmethod


class BaseAIProvider(ABC):
    @abstractmethod
    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Send a chat completion request and return the raw text response."""
        ...
