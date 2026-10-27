"""Load, split, embed, and store source documents."""

from langchain_qdrant import QdrantVectorStore
from src.config import settings
from src.embeddings import embbedings
from src.loaders import load_split_documnet

documents= load_split_documnet()

QdrantVectorStore.from_documents(
    documents=documents,
    embedding=embbedings,                    
    url=settings.qdrant_url,                 
    api_key=settings.qdrant_api_key,           
    collection_name=settings.qdrant_collection,
)


print(f"Indexed {len(documents)} chunks ")