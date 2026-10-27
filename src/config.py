"""Read application configuration from environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    groq_api_key=os.getenv("GROQ_API_KEY")
    groq_model=os.getenv("GROQ_MPODEL","openai/gpt-oss-120b")
    
    qdrant_api_key=os.getenv("QDRANT_API_KEY")
    qdrant_url=os.getenv("QDRANT_URL")
    qdrant_collection=os.getenv("QDRANT_COLLECTION","deterministic")
    
    embedding_model=os.getenv("EMBEDDING_MODEL","sentence-transformers/all-MiniLM-L6-v2")
    
    
settings= Settings()
