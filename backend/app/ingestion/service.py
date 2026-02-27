# app/ingestion/service.py

import os
from app.ingestion.loaders import load_document
from app.ingestion.chunker import chunk_documents
from app.ingestion.vectorstore import get_vectorstore

FAKE_USER_ID = 1  # temp

def ingest_file(file_path: str, chatbot_id: int):
    # 1. Load
    documents = load_document(file_path)

    # 2. Chunk
    chunks = chunk_documents(documents)

    # 3. Vector store
    vectordb = get_vectorstore(FAKE_USER_ID, chatbot_id)

    # 4. Store
    vectordb.add_documents(chunks)
    vectordb.persist()