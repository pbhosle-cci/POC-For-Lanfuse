from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import get_prompt, create_prompt
from pydantic import BaseModel, Field
from typing import Literal
from app.constants import (
    PromptType
)
router = APIRouter()

class CompanyRequest(BaseModel):
    prompt_name: str


class PromptCreateRequest(BaseModel):
    name: str
    type: Literal[PromptType.CHAT, PromptType.TEXT]
    ai_prompt: str
    prompt: str
    user_role: str
    ai_role: str


@router.post("/get_prompt")
def GetPrompt(req: CompanyRequest):
    result = get_prompt(req.prompt_name)
    return {
        "data": result
    }


@router.post("/create_prompt")
def GenPrompt(body: PromptCreateRequest):
    result = create_prompt(body)
    return {
        "classification": result
    }

