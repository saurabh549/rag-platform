# app/rag/service.py

from langchain_community.llms import Ollama
from app.config import LLM_MODEL
from app.rag.prompt import RAG_PROMPT_TEMPLATE
from app.rag.retriever import retrieve_context

llm = Ollama(model=LLM_MODEL)

def ask_question(chatbot_id: int, question: str):
    context = retrieve_context(chatbot_id, question)

    prompt = RAG_PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    answer = llm.invoke(prompt)
    return answer
