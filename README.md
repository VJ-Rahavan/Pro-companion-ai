# Pro Companion — AI Service

FastAPI service that generates DSA solutions and hints. Standalone — switch between Groq and Gemini via a single env var.

## Stack

- Python 3.11+ / FastAPI / uvicorn
- Groq (llama-3.1-70b) or Gemini (gemini-1.5-flash) — switchable

## Prerequisites

- Python 3.11+

## Setup

### 1. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
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

Change `AI_PROVIDER` in `.env` and restart:

```
AI_PROVIDER=groq     # uses llama-3.1-70b-versatile
AI_PROVIDER=gemini   # uses gemini-1.5-flash
```

## Project structure

```
ai-service/
├── providers/
│   ├── base.py           # abstract interface
│   ├── groq_provider.py
│   └── gemini_provider.py
├── routers/
│   └── solution.py       # POST /generate-solution
├── schemas.py            # Pydantic models
├── config.py             # env settings
└── main.py               # FastAPI entry point
```

## Endpoint

### `POST /generate-solution`

```json
{
  "problem_title": "Trapping rain water",
  "pattern": "two pointers",
  "difficulty": "hard"
}
```

Returns `approach`, `solution_code`, `time_complexity`, `space_complexity`, and 3 `related_problems`.

### `GET /health`

Returns `{ "ok": true, "provider": "groq" }`.
