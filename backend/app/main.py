from fastapi import FastAPI
from app.config import LLM_MODEL
from app.chatbots.routes import router as chatbot_router
from app.ingestion.routes import router as ingestion_router
from app.rag.routes import router as rag_router

app = FastAPI(title="RAG Platform Backend")

app.include_router(chatbot_router)
app.include_router(ingestion_router)
app.include_router(rag_router)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "llm_model": LLM_MODEL
    }