from openai import OpenAI
from app.config import langfuse
import os
from dotenv import load_dotenv
from langfuse import get_client

from app.constants import (
    Status,
    ErrorMessages,
    PromptType,
    LangfuseConfig
)

load_dotenv()

langfuse = get_client()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_prompt(prompt_name: str):
    prompt = langfuse.get_prompt(prompt_name)
    compiled_prompt = prompt.compile(
        prompt_name=prompt_name
    )
    response = {'compiled_prompt': compiled_prompt,
                'status': Status.SUCCESS}
    return response

def create_prompt(data):
    if data.type.upper() == PromptType.TEXT:
        # Create a text prompt
        try:
            langfuse.create_prompt(
                name=data.name,
                type=data.type,
                prompt=data.prompt,
                labels=LangfuseConfig.DEFAULT_LABELS
                )
            return {
            "status": Status.SUCCESS,
            "prompt_name": data.name
            }
        except Exception as e:
            print("Langfuse error:", str(e))
            return {
                "status": Status.FAILED,
                "error": str(e)
            }
    elif data.type.upper() == PromptType.CHAT:
        try:
            langfuse.create_prompt(
                name=data.name,
                type= data.type,
                prompt=[
                    {"role": data.ai_role, "content": data.ai_prompt},
                    {"role": data.user_role, "content": data.prompt},
                ],
                labels= LangfuseConfig.DEFAULT_LABELS
            )
            return {
                "status": Status.SUCCESS,
                "prompt_name": data.name
            }
        except Exception as e:
            print("Langfuse error:", str(e))
            return {
                "status": Status.FAILED,
                "error": str(e)
            }

    return {'error': ErrorMessages.INVALID_PROMPT_TYPE,
            'status': Status.FAILED}
