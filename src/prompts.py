"""Define system and RAG prompts."""
from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful assistant answering questions about indexed documents.

Rules:
- Answer only using the supplied context.
- If the answer is not in the context, say:
  "I don't have enough information in the indexed documents."
- Do not invent facts.
- Keep the answer clear and concise.

Context:
{context}""",
        ),
        ("human", "{question}"),
    ]
)