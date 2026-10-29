# """Build the RAG prompt and Groq model chain."""

# from langchain_groq import ChatGroq
# from src.config import settings
# from src.vector_store import retrive
# from src.prompts import rag_prompt

# llm = ChatGroq(
#     model=settings.groq_model,
#     temperature=0,
# )

# def format_documents(document):
#     """turn retrive document from the qdrant into the readable format"""
    
#     formatted =[]
#     for index, documents in enumerate(document,start=1):
#         source = documents.metadata.get("sourve","unknown source0")
#         page = documents.metadata.get("page")
        
#         soource_label = source
#         if page is None:
#             soource_label+=f",page{page+1}"
#         formatted.append(
#             f"[documents {index}| source:{soource_label}]\n"
#         )
#         return "\n\n".join(formatted)
    
    
# def answer_document(question:str):
#     documents = retrive.invoke(question)
#     context = format_documents(documents)
    
#     message= rag_prompt.format_messages(
#         context=context,
#         question=question,
#     )
    
#     response = llm.invoke(message)
    
#     sources =[]
#     for document in documents:
#         source = document.metadata.get("source","unkown source")
#         page = document.metadata.get("page")
        
#         label = source if page is None else f"{source}, page {page + 1}"
#         if label not in sources:
#             sources.append(label)
            
#         return {
#             "answer": response.content,
#             "source": sources,
#         }



"""Build the RAG prompt and Groq model chain."""

from langchain_groq import ChatGroq
from src.config import settings
from src.vector_store import retrive
from src.prompts import rag_prompt

llm = ChatGroq(
    model=settings.groq_model,
    temperature=0,
)

def format_documents(documents):
    """Turn retrieved documents from Qdrant into a readable context string."""
    if not documents:
        return "No relevant documents found."

    formatted = []
    for index, doc in enumerate(documents, start=1):
        source = doc.metadata.get("source", "unknown source")
        page = doc.metadata.get("page")
        
        source_label = source
        if page is not None:
            source_label += f", page {page + 1}"
            
        # IMPORTANT: Include doc.page_content so the LLM can actually read the text!
        formatted.append(
            f"[Document {index} | Source: {source_label}]\n{doc.page_content}"
        )
    
    # Return outside the for loop
    return "\n\n".join(formatted)


def answer_document(question: str):
    documents = retrive.invoke(question)
    context = format_documents(documents)
    
    message = rag_prompt.format_messages(
        context=context,
        question=question,
    )
    
    response = llm.invoke(message)
    
    sources = []
    for doc in documents:
        source = doc.metadata.get("source", "unknown source")
        page = doc.metadata.get("page")
        
        label = source if page is None else f"{source}, page {page + 1}"
        if label not in sources:
            sources.append(label)
            
    # Return outside the for loop, and match 'sources' with chats.py
    return {
        "answer": response.content,
        "sources": sources,
    }