import json
from fastapi import APIRouter, HTTPException
from schemas import SolutionRequest, SolutionResponse, RelatedProblem
from providers import get_provider

router = APIRouter()

# System prompt instructs the model to return structured JSON only
SYSTEM_PROMPT = """You are an expert DSA interview coach. When given a problem, respond ONLY with a valid JSON object — no markdown, no explanation outside the JSON:
{
  "approach": "clear step-by-step explanation of the approach",
  "solution_code": "clean Python solution",
  "time_complexity": "O(...)",
  "space_complexity": "O(...)",
  "related_problems": [
    { "title": "Problem name", "pattern": "pattern name", "why": "one sentence on why it's related" },
    { "title": "...", "pattern": "...", "why": "..." },
    { "title": "...", "pattern": "...", "why": "..." }
  ]
}
Return exactly 3 related problems."""


@router.post("/generate-solution", response_model=SolutionResponse)
async def generate_solution(req: SolutionRequest):
    provider = get_provider()

    user_prompt = (
        f"Problem: {req.problem_title}\n"
        f"Pattern: {req.pattern}\n"
        f"Difficulty: {req.difficulty}\n\n"
        "Generate the solution."
    )

    raw = await provider.complete(SYSTEM_PROMPT, user_prompt)

    # Parse the JSON response from the model
    try:
        data = json.loads(raw)
        data["related_problems"] = [RelatedProblem(**p) for p in data.get("related_problems", [])]
        return SolutionResponse(**data)
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse AI response: {e}")
