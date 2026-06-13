"""
Pro Companion — AI Service
FastAPI app that proxies requests to Groq or Gemini.
Switch providers by setting AI_PROVIDER=groq|gemini in .env
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import solution
from config import settings

app = FastAPI(title="Pro Companion AI Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # only the backend should call this
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(solution.router)


@app.get("/health")
def health():
    return {"ok": True, "provider": settings.ai_provider}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.port, reload=True)
