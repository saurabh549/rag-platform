# app/rag/retriever.py

from app.ingestion.vectorstore import get_vectorstore

FAKE_USER_ID = 1

def retrieve_context(chatbot_id: int, query: str, k: int = 4):
    vectordb = get_vectorstore(FAKE_USER_ID, chatbot_id)
    docs = vectordb.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in docs)