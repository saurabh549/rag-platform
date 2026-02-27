# app/ingestion/routes.py

import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ingestion.service import ingest_file
from app.db.models.chatbot import Chatbot
from app.db.deps import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter(prefix="/ingestion", tags=["Ingestion"])

FAKE_USER_ID = 1

@router.post("/upload/{chatbot_id}")
def upload_document(
    chatbot_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    chatbot = db.query(Chatbot).filter(
        Chatbot.id == chatbot_id,
        Chatbot.user_id == FAKE_USER_ID
    ).first()

    if not chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found")

    upload_dir = f"uploads/user_{FAKE_USER_ID}/chatbot_{chatbot_id}"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    ingest_file(file_path, chatbot_id)

    return {"message": "File uploaded and ingested successfully"}