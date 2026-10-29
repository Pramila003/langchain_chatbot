"""Connect to Qdrant and create a document retriever."""
from langchain_qdrant import QdrantVectorStore
from src.config import settings
from src.embeddings import embbedings

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embbedings,
    url=settings.qdrant_url,
    api_key=settings.qdrant_api_key,
    collection_name=settings.qdrant_collection,
)

retrive = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":4},
)