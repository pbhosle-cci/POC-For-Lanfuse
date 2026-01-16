# app/constants/prompt_constants.py

class PromptType:
    TEXT = "TEXT"
    CHAT = "CHAT"


class PromptRole:
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class LangfuseConfig:
    DEFAULT_LABELS = ["production"]
