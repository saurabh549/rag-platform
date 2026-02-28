# app/ingestion/vectorstore.py

import os
from langchain_chroma import Chroma
# from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
from app.config import EMBEDDING_MODEL

def get_vectorstore(user_id: int, chatbot_id: int):
    path = f"vectorstore/user_{user_id}/chatbot_{chatbot_id}"
    os.makedirs(path, exist_ok=True)

    embedding = OllamaEmbeddings(model=EMBEDDING_MODEL)

    return Chroma(
        persist_directory=path,
        embedding_function=embedding
    )