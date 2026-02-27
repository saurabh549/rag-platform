from fastapi import FastAPI
from app.config import LLM_MODEL

app = FastAPI(title="RAG Platform Backend")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "llm_model": LLM_MODEL
    }