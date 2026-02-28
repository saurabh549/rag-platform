# app/rag/prompt.py

RAG_PROMPT_TEMPLATE = """
You are a helpful assistant.

Answer the question strictly using the context below.
If the answer is not present in the context, say:
"I don't have that information."

Context:
{context}

Question:
{question}

Answer:
"""