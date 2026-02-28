# app/rag/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.rag.schemas import QuestionRequest, AnswerResponse
from app.rag.service import ask_question
from app.db.models.chatbot import Chatbot
from app.db.deps import get_db

router = APIRouter(prefix="/rag", tags=["RAG"])

FAKE_USER_ID = 1

@router.post("/ask/{chatbot_id}", response_model=AnswerResponse)
def ask(
    chatbot_id: int,
    payload: QuestionRequest,
    db: Session = Depends(get_db)
):
    chatbot = db.query(Chatbot).filter(
        Chatbot.id == chatbot_id,
        Chatbot.user_id == FAKE_USER_ID
    ).first()

    if not chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found")

    answer = ask_question(chatbot_id, payload.question)
    return {"answer": answer}