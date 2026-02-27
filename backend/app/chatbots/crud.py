# app/chatbots/crud.py

from sqlalchemy.orm import Session
from app.db.models.chatbot import Chatbot
from app.chatbots.schemas import ChatbotCreate, ChatbotUpdate

FAKE_USER_ID = 1  # TEMP (will come from auth later)

def create_chatbot(db: Session, data: ChatbotCreate):
    chatbot = Chatbot(
        user_id=FAKE_USER_ID,
        name=data.name,
        system_prompt=data.system_prompt
    )
    db.add(chatbot)
    db.commit()
    db.refresh(chatbot)
    return chatbot

def get_chatbots(db: Session):
    return db.query(Chatbot).filter(Chatbot.user_id == FAKE_USER_ID).all()

def get_chatbot(db: Session, chatbot_id: int):
    return db.query(Chatbot).filter(
        Chatbot.id == chatbot_id,
        Chatbot.user_id == FAKE_USER_ID
    ).first()

def update_chatbot(db: Session, chatbot_id: int, data: ChatbotUpdate):
    chatbot = get_chatbot(db, chatbot_id)
    if not chatbot:
        return None

    if data.name is not None:
        chatbot.name = data.name
    if data.system_prompt is not None:
        chatbot.system_prompt = data.system_prompt

    db.commit()
    db.refresh(chatbot)
    return chatbot

def delete_chatbot(db: Session, chatbot_id: int):
    chatbot = get_chatbot(db, chatbot_id)
    if not chatbot:
        return None

    db.delete(chatbot)
    db.commit()
    return chatbot