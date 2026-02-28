# app/rag/schemas.py

from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str