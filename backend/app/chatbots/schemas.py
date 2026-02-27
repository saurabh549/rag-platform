# app/chatbots/schemas.py

from pydantic import BaseModel

class ChatbotCreate(BaseModel):
    name: str
    system_prompt: str

class ChatbotUpdate(BaseModel):
    name: str | None = None
    system_prompt: str | None = None

class ChatbotResponse(BaseModel):
    id: int
    name: str
    system_prompt: str

    class Config:
        from_attributes = True