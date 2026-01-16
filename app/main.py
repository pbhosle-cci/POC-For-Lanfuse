from fastapi import FastAPI
from app.routers import prompt_test

app = FastAPI(title="Langfuse Prompt Management POC")

app.include_router(prompt_test.router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
