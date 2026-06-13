from pydantic import BaseModel
from typing import Literal, List


class SolutionRequest(BaseModel):
    problem_title: str
    pattern: str
    difficulty: Literal["easy", "med", "hard"]


class RelatedProblem(BaseModel):
    title: str
    pattern: str
    why: str


class SolutionResponse(BaseModel):
    approach: str
    solution_code: str
    time_complexity: str
    space_complexity: str
    related_problems: List[RelatedProblem]


class HintRequest(BaseModel):
    problem_title: str
    pattern: str
    hint_level: Literal[1, 2, 3]


class HintResponse(BaseModel):
    hint: str
    hint_level: int
