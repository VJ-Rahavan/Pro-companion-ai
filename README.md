# Pro Companion — AI Service

FastAPI service that generates DSA solutions and hints.
Standalone repo — switch between Groq and Gemini via a single env var.

## Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI + uvicorn |
| AI (default) | Groq — llama-3.1-70b-versatile |
| AI (alt) | Google Gemini — gemini-1.5-flash |
| Validation | Pydantic v2 |
| Config | pydantic-settings |

## Prerequisites

- Python 3.11+

## Local setup

### 1. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate     # macOS / Linux
# .venv\Scripts\activate      # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create environment file

```bash
cp .env.example .env
```

Fill in `.env`:

| Variable | Description |
|----------|-------------|
| `AI_PROVIDER` | `groq` or `gemini` |
| `GROQ_API_KEY` | From [console.groq.com](https://console.groq.com) |
| `GEMINI_API_KEY` | From [aistudio.google.com](https://aistudio.google.com) |
| `PORT` | Port to run on (default: `8000`) |

### 4. Start the service

```bash
python main.py
```

Runs on `http://localhost:8000`.
Interactive API docs at `http://localhost:8000/docs`.

## Switching providers

Change `AI_PROVIDER` in `.env` and restart — no code change needed:

```
AI_PROVIDER=groq     # uses llama-3.1-70b-versatile
AI_PROVIDER=gemini   # uses gemini-1.5-flash
```

## Project architecture

```
ai-service/
├── main.py                 # FastAPI app — CORS, router registration, /health
├── config.py               # pydantic-settings — reads .env
├── schemas.py              # Pydantic request/response models
├── providers/
│   ├── __init__.py         # get_provider() factory — reads AI_PROVIDER at call time
│   ├── base.py             # abstract BaseAIProvider interface
│   ├── groq_provider.py    # Groq SDK implementation
│   └── gemini_provider.py  # Google Generative AI SDK implementation
└── routers/
    └── solution.py         # POST /generate-solution
```

## How provider switching works

```
.env: AI_PROVIDER=groq
         │
         ▼
   get_provider()           ← called per request
         │
   ┌─────┴─────┐
   ▼           ▼
GroqProvider  GeminiProvider
   │           │
   └─────┬─────┘
         ▼
  BaseAIProvider.generate()
         │
         ▼
  JSON response → POST /generate-solution
```

## Endpoints

### `POST /generate-solution`

Request:
```json
{
  "problem_title": "Trapping rain water",
  "pattern": "two pointers",
  "difficulty": "hard"
}
```

Response: `approach`, `solution_code`, `time_complexity`, `space_complexity`, `related_problems[]`

### `GET /health`

```json
{ "ok": true, "provider": "groq" }
```

## Related repos

| Repo | What |
|------|------|
| `Pro-companion-service` | Express + PostgreSQL + TypeORM backend |
| `Pro-companion-frontend` | Turborepo — React web + Expo mobile |
