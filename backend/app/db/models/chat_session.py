# app/db/models/chat_session.py

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from app.db.database import Base

class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    chatbot_id = Column(Integer, ForeignKey("chatbots.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)