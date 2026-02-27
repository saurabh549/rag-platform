# app/chatbots/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.chatbots import crud, schemas
from app.db.deps import get_db

router = APIRouter(prefix="/chatbots", tags=["Chatbots"])

@router.post("", response_model=schemas.ChatbotResponse)
def create_chatbot(
    payload: schemas.ChatbotCreate,
    db: Session = Depends(get_db)
):
    return crud.create_chatbot(db, payload)

@router.get("", response_model=list[schemas.ChatbotResponse])
def list_chatbots(db: Session = Depends(get_db)):
    return crud.get_chatbots(db)

@router.get("/{chatbot_id}", response_model=schemas.ChatbotResponse)
def get_chatbot(chatbot_id: int, db: Session = Depends(get_db)):
    chatbot = crud.get_chatbot(db, chatbot_id)
    if not chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found")
    return chatbot

@router.put("/{chatbot_id}", response_model=schemas.ChatbotResponse)
def update_chatbot(
    chatbot_id: int,
    payload: schemas.ChatbotUpdate,
    db: Session = Depends(get_db)
):
    chatbot = crud.update_chatbot(db, chatbot_id, payload)
    if not chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found")
    return chatbot

@router.delete("/{chatbot_id}")
def delete_chatbot(chatbot_id: int, db: Session = Depends(get_db)):
    chatbot = crud.delete_chatbot(db, chatbot_id)
    if not chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found")
    return {"message": "Chatbot deleted successfully"}